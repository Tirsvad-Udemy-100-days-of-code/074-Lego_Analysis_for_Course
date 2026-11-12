[English](Step-1-Colours) · [Dansk](Step-1-Colours-da) · **Bahasa Malaysia**

# Langkah 1: Meneroka warna bata

**Soalan:** Berapa banyak warna yang dihasilkan LEGO, dan berapa yang lut sinar?

![Langkah 1: Meneroka warna bata](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-1-colours.png)

## Apa yang kod lakukan

`count_unique_colours` menggunakan `.nunique()` pada lajur `name`: **135** warna. `transparent_counts_groupby` (`.groupby("is_trans").count()`) dan `transparent_counts_value_counts` (`.value_counts()`) memberikan jawapan yang sama dengan dua cara: **107** warna legap dan **28** warna lut sinar.

## Apa yang anda perolehi

- Membaca CSV dengan `pd.read_csv` dan melihatnya dengan `.head()`.
- `.nunique()` mengira nilai yang berbeza.
- Soalan yang sama boleh dijawab dengan `.groupby().count()` atau `.value_counts()`; `.value_counts()` ialah jalan pintas untuk mengira kategori.

Sebelumnya: [Getting-Started](Getting-Started-ms) · Seterusnya: [Step-2-Sets](Step-2-Sets-ms)
