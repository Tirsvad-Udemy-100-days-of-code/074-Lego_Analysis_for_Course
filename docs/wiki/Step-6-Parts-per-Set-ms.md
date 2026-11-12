[English](Step-6-Parts-per-Set) · [Dansk](Step-6-Parts-per-Set-da) · **Bahasa Malaysia**

# Langkah 6: Purata bahagian setiap set

**Soalan:** Adakah set LEGO bertambah besar dan kompleks?

![Langkah 6: Purata bahagian setiap set](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-6-parts-per-set.png)

## Apa yang kod lakukan

`parts_per_set` mengumpulkan mengikut `year` dan mengira purata `num_parts` dengan `.agg()`: kira-kira 12 bahagian pada 1954 dan kira-kira 222 pada 2017. `parts_per_set_chart` melukis carta serakan yang menunjukkan aliran menaik: set terkini mempunyai kira-kira dua kali ganda bahagian berbanding set dari tahun 1960-an.

## Apa yang anda perolehi

- `.agg({"num_parts": "mean"})` bersama `.groupby()`.
- Carta serakan (`.scatter()`) menggunakan satu titik bagi setiap titik data dan menunjukkan aliran.
- Helah pengirisan yang sama membuang dua tahun terakhir yang tidak lengkap.

Sebelumnya: [Step-5-Two-Axes](Step-5-Two-Axes-ms) · Seterusnya: [Step-7-Themes-and-Keys](Step-7-Themes-and-Keys-ms)
