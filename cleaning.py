
import pandas as pd

# 1. Membaca data mentah hasil crawling
df = pd.read_csv("hasil_scraping.csv")

print("Jumlah data awal:", len(df))

# 2. Menghapus baris yang tidak memiliki ID atau teks
df = df.dropna(subset=["id", "teks"])

# 3. Membersihkan spasi berlebih pada teks
df["teks"] = (
    df["teks"]
    .astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

# 4. Menghapus teks yang kosong
df = df[df["teks"] != ""]

# 5. Menghapus duplikasi berdasarkan ID
df = df.drop_duplicates(subset=["id"], keep="first")

# 6. Menghapus teks yang sama persis setelah dirapikan
df["teks_pembanding"] = df["teks"].str.casefold()
df = df.drop_duplicates(
    subset=["teks_pembanding"],
    keep="first"
)
df = df.drop(columns=["teks_pembanding"])

# 7. Menyeragamkan format tanggal
df["tanggal"] = pd.to_datetime(
    df["tanggal"],
    errors="coerce",
    utc=True
)

# 8. Menyimpan hasil cleaning
df.to_csv(
    "hasil_cleaning.csv",
    index=False,
    encoding="utf-8-sig"
)

# 9. Menampilkan ringkasan
print("\n=== HASIL DATA CLEANING ===")
print("Jumlah data setelah cleaning:", len(df))
print("Data kosong:")
print(df.isna().sum())
print("File tersimpan: hasil_cleaning.csv")
