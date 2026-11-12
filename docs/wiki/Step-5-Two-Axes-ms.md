[English](Step-5-Two-Axes) · [Dansk](Step-5-Two-Axes-da) · **Bahasa Malaysia**

# Langkah 5: Dua paksi dalam satu carta

**Soalan:** Bagaimanakah set dan tema boleh berkongsi satu carta apabila skalanya berbeza?

![Langkah 5: Dua paksi dalam satu carta](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-5-two-axes.png)

## Apa yang kod lakukan

`sets_and_themes_chart` mencipta satu paksi, memanggil `.twinx()` untuk mendapatkan paksi y kedua yang berkongsi paksi x, dan mewarnakan setiap garis serta paksinya supaya pembaca dapat membezakannya. Tema mencapai sekitar 90 dan set sekitar 900.

## Apa yang anda perolehi

- `ax1 = plt.gca()` dan `ax2 = ax1.twinx()` mencipta dua paksi yang berkongsi paksi x.
- Warna dan label menjadikan dua garis sebagai cerita yang mudah dibaca.
- Memplot skala yang berbeza pada satu paksi menyembunyikan siri yang lebih kecil.

Sebelumnya: [Step-4-Themes-per-Year](Step-4-Themes-per-Year-ms) · Seterusnya: [Step-6-Parts-per-Set](Step-6-Parts-per-Set-ms)
