[English](Step-3-Sets-per-Year) · [Dansk](Step-3-Sets-per-Year-da) · **Bahasa Malaysia**

# Langkah 3: Set yang dikeluarkan setiap tahun

**Soalan:** Bagaimanakah bilangan set yang dikeluarkan berubah dari semasa ke semasa?

![Langkah 3: Set yang dikeluarkan setiap tahun](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-3-sets-per-year.png)

## Apa yang kod lakukan

`sets_by_year` mengumpulkan mengikut `year` dan mengira: 5 set pada 1949, 28 pada 1955 dan 840 pada 2019. Syot data ini diambil pada penghujung 2020, jadi `drop_incomplete_years` membuang dua baris terakhir (2020 dan 2021) sebelum `sets_by_year_chart` melukis carta garis.

## Apa yang anda perolehi

- `.groupby()` diikuti `.count()` mengagregat baris bagi setiap kumpulan.
- Mengiris DataFrame seperti senarai: `df[:-2]` membuang dua baris terakhir (pengirisan senarai Python dari Hari 21).
- Data yang tidak lengkap menghasilkan carta yang mengelirukan; potong data itu sebelum memplot.

Sebelumnya: [Step-2-Sets](Step-2-Sets-ms) · Seterusnya: [Step-4-Themes-per-Year](Step-4-Themes-per-Year-ms)
