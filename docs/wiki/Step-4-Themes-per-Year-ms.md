[English](Step-4-Themes-per-Year) · [Dansk](Step-4-Themes-per-Year-da) · **Bahasa Malaysia**

# Langkah 4: Tema setiap tahun dengan .agg()

**Soalan:** Berapa banyak tema berbeza yang dijual LEGO setiap tahun?

![Langkah 4: Tema setiap tahun dengan .agg()](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-4-themes-per-year.png)

## Apa yang kod lakukan

`themes_by_year` menjalankan `sets.groupby("year").agg({"theme_id": pd.Series.nunique})` dan menamakan semula lajur itu kepada `nr_themes`. Terdapat 2 tema pada 1949 dan 78 pada 2019; `themes_by_year_chart` hanya memplot tahun kalendar yang lengkap.

## Apa yang anda perolehi

- `.agg()` menerima kamus: kunci ialah lajur, nilai ialah operasi.
- `.rename(columns=...)` memberi lajur nama yang lebih baik.
- Bilangan tema meningkat sehingga pertengahan 1990-an, mendatar, dan meningkat semula pada awal 2010-an.

Sebelumnya: [Step-3-Sets-per-Year](Step-3-Sets-per-Year-ms) · Seterusnya: [Step-5-Two-Axes](Step-5-Two-Axes-ms)
