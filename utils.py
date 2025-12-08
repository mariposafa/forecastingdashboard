import pandas as pd

def load_multisheet_excel(file):
    xls = pd.ExcelFile(file)
    all_data = []

    for sheet in xls.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)

        # Set pasangan kolom Mei-Juni-Juli sesuai template
        pairs = [
            ("Date_Mei", "Prod_Mei"),
            ("Date_Juni", "Prod_Juni"),
            ("Date_Juli", "Prod_Juli")
        ]

        ts_list = []

        for date_col, prod_col in pairs:
            # Skip kalau kolom tidak ada
            if date_col not in df.columns or prod_col not in df.columns:
                continue

            # Ambil dua kolom dan rename jadi standar
            temp = df[[date_col, prod_col]].rename(
                columns={
                    date_col: "tanggal",
                    prod_col: "permintaan"
                }
            )

            # Konversi tipe
            temp["tanggal"] = pd.to_datetime(temp["tanggal"], errors="coerce")
            temp["permintaan"] = pd.to_numeric(temp["permintaan"], errors="coerce")

            # Buang baris kosong
            temp = temp.dropna(subset=["tanggal", "permintaan"])

            ts_list.append(temp)

        # Gabungkan: Mei → Juni → Juli
        merged = pd.concat(ts_list, ignore_index=True)

        # Urutkan berdasarkan tanggal (sangat penting)
        merged = merged.sort_values("tanggal")

        # Tambah kolom nama produk
        merged["produk"] = sheet

        all_data.append(merged)

    # Gabungkan semua sheet
    result = pd.concat(all_data, ignore_index=True)
    result = result.sort_values(["produk", "tanggal"])

    return result
