# Web Scraping Opini Pengguna X tentang PPh Pasal 22 Marketplace

## Deskripsi Proyek

Proyek ini dibuat untuk tugas mata kuliah SOSMED dengan tujuan mengumpulkan data post dari platform X yang berkaitan dengan kebijakan PPh Pasal 22 bagi penjual marketplace menggunakan Python.

Pengambilan data dilakukan melalui layanan TwitterAPIs dengan pendekatan API-based crawling, pencarian berbasis kata kunci (*keyword-based search*), dan pagination menggunakan cursor.

## Kata Kunci

- PPh Pasal 22
- Pajak marketplace
- Pajak seller
- Pajak penjual online

## Teknik yang Digunakan

1. API-based crawling untuk mengambil data melalui API.
2. Keyword-based search untuk mencari post sesuai topik penelitian.
3. Pagination untuk mengambil hasil dari halaman berikutnya.
4. Deduplication untuk mengurangi data post yang berulang.
5. Data cleaning untuk merapikan teks, memeriksa data kosong, menghapus duplikasi, dan menyeragamkan format tanggal.

## Teknologi

- Python
- Requests
- Pandas
- Python-dotenv
- TwitterAPIs

## Cara Menjalankan

1. Unduh atau clone repository ini.
2. Instal library yang diperlukan dengan perintah `pip install -r requirements.txt`.
3. Buat file `.env` di folder proyek.
4. Tambahkan API key milik sendiri ke file `.env` dengan format `TWITTERAPIS_KEY=API_KEY_MILIK_KAMU`.
5. Jalankan crawling dengan `python scraper.py`.
6. Jalankan pembersihan data dengan `python cleaning.py`.

## Hasil Pengumpulan Data

Proses crawling menghasilkan 639 post unik dari 38 panggilan API. Setelah proses data cleaning, tersisa 632 post.

Data hasil cleaning disimpan secara lokal dalam file `hasil_cleaning.csv` dan tidak disertakan dalam repository publik ini.

## Catatan

Jumlah dan isi data yang diperoleh dapat berubah bergantung pada hasil pencarian API, kata kunci, serta data yang tersedia pada saat pengambilan. API key harus dijaga kerahasiaannya dan tidak boleh dipublikasikan.

Proyek ini berfokus pada crawling dan data cleaning, belum mencakup analisis sentimen.
