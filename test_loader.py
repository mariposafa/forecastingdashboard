from utils import load_multisheet_excel

df = load_multisheet_excel("TEMPLATE_PRODUK.xlsx")

print("\n=== 20 data pertama Corn DDGS ===")
print(df[df["produk"] == "Corn DDGS"].head(20))

print("\n=== Jumlah data Corn DDGS ===")
print(len(df[df["produk"]=="Corn DDGS"]))
