import pandas as pd

# UBAH nama file jika berbeda
FILE = "TEMPLATE_PRODUK.xlsx"

xls = pd.ExcelFile(FILE)

print("\n=== DAFTAR SHEET ===")
print(xls.sheet_names)

print("\n=== STRUKTUR SETIAP SHEET ===")

for sheet in xls.sheet_names:
    print(f"\n--- Sheet: {sheet} ---")
    df = pd.read_excel(FILE, sheet_name=sheet, dtype=str)
    print(df.head(10))      # tampilkan 10 baris pertama
    print("Kolom:", df.columns.tolist())
    print("-" * 60)
