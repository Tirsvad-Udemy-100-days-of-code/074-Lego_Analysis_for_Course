[English](Step-7-Themes-and-Keys) · [Dansk](Step-7-Themes-and-Keys-da) · **Bahasa Malaysia**

# Langkah 7: Tema, kunci utama dan kunci asing

**Soalan:** Nama tema manakah yang dimiliki oleh id tema, dan bagaimanakah jadual dihubungkan?

![Langkah 7: Tema, kunci utama dan kunci asing](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-7-themes-and-keys.png)

## Apa yang kod lakukan

`sets.csv` mengandungi `theme_id` (**kunci asing**); `themes.csv` mengandungi `id` yang unik (**kunci utama**) dan nama tema. `find_theme_ids(themes, "Star Wars")` menemui empat id (18, 158, 209, 261) dan `sets_for_theme_ids` menyenaraikan set yang sepadan, contohnya Kalendar Advent Star Wars yang berkongsi satu tema.

## Apa yang anda perolehi

- Pangkalan data hubungan dipecahkan kepada jadual yang dihubungkan oleh kunci.
- Kunci utama adalah unik dalam jadualnya sendiri; kunci asing menunjuk kepadanya dari jadual lain.
- Satu nama (Star Wars) boleh dimiliki oleh beberapa id.

Sebelumnya: [Step-6-Parts-per-Set](Step-6-Parts-per-Set-ms) · Seterusnya: [Step-8-Merge](Step-8-Merge-ms)
