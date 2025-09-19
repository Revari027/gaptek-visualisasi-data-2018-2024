# 📊 Indeks Literasi Digital Indonesia (2018-2024)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-yellow?logo=html5)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 Deskripsi
Proyek ini mengumpulkan, mengolah, dan memvisualisasikan **Indeks Literasi Digital (ILD) Indonesia** dari tahun 2018 hingga 2024.  
Data bersumber dari:
- **Kemenkominfo**
- **Katadata**
- **Laporan Kinerja Pemerintah**

Selain data manual, proyek ini juga menambahkan **web scraping otomatis** untuk melengkapi data yang belum tersedia.

---

## ✨ Fitur Utama
- 🔎 **Web Scraping** dari Katadata untuk memperbarui data tahun 2022.  
- 📑 **CSV Output** dengan metadata (judul, keterangan, sumber, link).  
- 📊 **Visualisasi Data** berupa:
  - Grafik Batang (Bar Chart)
  - Grafik Garis (Line Chart dengan interpolasi tren).  
- 📂 Semua grafik otomatis disimpan sebagai file `.png` agar mudah dipakai dalam laporan.

---

## 📂 Struktur File

.
├── indeks_literasi_digital.py # Script utama (Python)
├── indeks_literasi_digital.csv # Output data dalam format CSV
├── grafik_batang_literasi_digital.png # Visualisasi grafik batang
├── grafik_garis_literasi_digital.png # Visualisasi grafik garis
├── requirements.txt # Daftar dependencies Python
└── README.md # Dokumentasi proyek


---

## 🚀 Cara Menjalankan
### 1️⃣ Clone repository
```bash
git clone https://github.com/username/indeks-literasi-digital.git
cd indeks-literasi-digital 
```
```bash
2️⃣ Install dependencies

pip install -r requirements.txt
```
```bash
3️⃣ Jalankan script

python indeks_literasi_digital.py
```


4️⃣ Lihat hasil

    CSV output: indeks_literasi_digital.csv

    Grafik batang: grafik_batang_literasi_digital.png

    Grafik garis: grafik_garis_literasi_digital.png

```bash
📊 Contoh Output
📑 Cuplikan Data (CSV)
Tahun	Indeks	Sumber	Link	Indeks_interpolasi	Visualisasi
2018	3.47	Kemenkominfo 2018	https://kominfo.go.id/
3.470	grafik_batang_literasi_digital.png; grafik_garis_literasi_digital.png
2020	3.46	Kemenkominfo & Katadata 2020	https://katadata.co.id/
3.460	grafik_batang_literasi_digital.png; grafik_garis_literasi_digital.png
2021	3.49	Kemenkominfo & Katadata 2021	https://katadata.co.id/
3.490	grafik_batang_literasi_digital.png; grafik_garis_literasi_digital.png
2022	3.54	Katadata (scraping sukses)	https://katadata.co.id/digital/berita/6385980a3c2e1/
...	3.540	grafik_batang_literasi_digital.png; grafik_garis_literasi_digital.png
📊 Grafik Batang

Grafik Batang Literasi Digital
📈 Grafik Garis

Grafik Garis Literasi Digital
```

🛠️ Dependencies

Semua pustaka sudah tersedia dalam requirements.txt:

    pandas

    matplotlib

    seaborn

    requests

    beautifulsoup4

Opsional:

    lxml (parser HTML lebih cepat)

📌 Catatan

    Beberapa data resmi tidak dipublikasikan sehingga diisi None dan dilengkapi dengan interpolasi tren.

    Scraping bisa gagal jika struktur website berubah, pastikan selector BeautifulSoup diperbarui sesuai kondisi terbaru.

📬 Kontribusi

🤝 Pull Request sangat terbuka!
Jika ada tambahan data, sumber resmi baru, atau ide visualisasi yang lebih menarik, silakan kontribusi.
👨‍💻 Author

    Revario Sayiddina Al Habsy
    📍 Jakarta, Indonesia
    🚀 Frontend Engineer & Data Enthusiast


---

Mau aku bikinin juga **preview badge** (misalnya `open in Colab` atau `run with Binder`) biar orang bisa langsung coba script ini tanpa setup manual?

