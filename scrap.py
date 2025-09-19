import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import re

data = {
    'Tahun': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Indeks': [3.47, None, 3.46, 3.49, None, None, 3.78],
    'Sumber': [
        "Kemenkominfo 2018",
        "Tidak tersedia (resmi tidak dipublikasikan)",
        "Kemenkominfo & Katadata 2020",
        "Kemenkominfo & Katadata 2021",
        "Katadata (akan dicoba scraping)",
        "Tidak tersedia (resmi tidak dipublikasikan)",
        "Laporan Kinerja Pemerintah 2024"
    ],
    'Link': [
        "https://kominfo.go.id/",
        "",
        "https://katadata.co.id/",
        "https://katadata.co.id/",
        "https://katadata.co.id/digital/berita/6385980a3c2e1/indeks-literasi-digital-indonesia-naik-jadi-3-54-di-2022",
        "",
        "https://kinerja.go.id/"
    ]
}

url = data['Link'][4]
scraped_value_2022 = None

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_body = soup.find('div', class_='prose')
        if article_body:
            text = article_body.get_text()
            match = re.search(r'(\d+[.,]\d+)', text)
            if match:
                scraped_value_2022 = float(match.group(1).replace(',', '.'))
except Exception as e:
    print("Scraping gagal:", e)

if scraped_value_2022:
    data['Indeks'][4] = scraped_value_2022
    data['Sumber'][4] = "Katadata (scraping sukses)"

df = pd.DataFrame(data)
df['Indeks_interpolasi'] = df['Indeks'].interpolate()

sns.set_style("whitegrid")

plt.figure(figsize=(12, 7))
bar_plot = sns.barplot(x='Tahun', y='Indeks', data=df, palette='viridis')
for index, row in df.iterrows():
    if pd.notnull(row['Indeks']):
        bar_plot.text(index, row['Indeks'] + 0.03, f"{row['Indeks']:.2f}",
                      color='black', ha="center", fontsize=12)
plt.title('Indeks Literasi Digital (ILD) Indonesia (2018-2024)', fontsize=16)
plt.ylabel('Skor Indeks (Skala 1-5)')
plt.xlabel('Tahun')
plt.ylim(0, 5)
plt.savefig('grafik_batang_literasi_digital.png')
plt.close()

plt.figure(figsize=(12, 7))
sns.lineplot(x='Tahun', y='Indeks', data=df, marker='o', linestyle='--', label='Data Asli')
sns.lineplot(x='Tahun', y='Indeks_interpolasi', data=df, marker='o', color='red', label='Estimasi Tren')
plt.title('Tren Pertumbuhan Literasi Digital Indonesia (2018-2024)', fontsize=16)
plt.ylabel('Skor Indeks (Skala 1-5)')
plt.xlabel('Tahun')
plt.ylim(3, 4.5)
plt.legend()
plt.grid(True)
plt.savefig('grafik_garis_literasi_digital.png')
plt.close()

df['Visualisasi'] = "grafik_batang_literasi_digital.png; grafik_garis_literasi_digital.png"

with open("indeks_literasi_digital.csv", "w", encoding="utf-8") as f:
    f.write("Judul: Indeks Literasi Digital Indonesia 2018-2024\n")
    f.write("Keterangan: Data gabungan dari Kemenkominfo, Katadata, dan Laporan Kinerja Pemerintah\n\n")
    df.to_csv(f, index=False)

print("✅ CSV lengkap berhasil dibuat: indeks_literasi_digital.csv")
