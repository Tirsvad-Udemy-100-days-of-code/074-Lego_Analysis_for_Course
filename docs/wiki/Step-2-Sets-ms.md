[English](Step-2-Sets) · [Dansk](Step-2-Sets-da) · **Bahasa Malaysia**

# Langkah 2: Set tertua dan terbesar

**Soalan:** Bilakah set pertama dikeluarkan, berapa banyak set ketika itu, dan set manakah yang mempunyai bahagian paling banyak?

![Langkah 2: Set tertua dan terbesar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-2-sets.png)

## Apa yang kod lakukan

`first_release_year` mengisih mengikut `year` dan mendapati **1949**. `count_sets_in_year(sets, 1949)` menapis dengan `sets["year"] == 1949` dan mendapati **5** set. `largest_sets` mengisih mengikut `num_parts` secara menurun: **The Ultimate Battle for Chima** (9,987 bahagian) di tempat pertama, diikuti UCS Millennium Falcon (7,541 bahagian).

## Apa yang anda perolehi

- `.sort_values()` mengisih secara menaik secara lalai; `ascending=False` membalikkannya.
- Menapis DataFrame dengan satu syarat (`df[df["year"] == 1949]`).
- Jawapan pertama mungkin mengejutkan: kotak terbesar mengandungi kurang daripada 10,000 bahagian.

Sebelumnya: [Step-1-Colours](Step-1-Colours-ms) · Seterusnya: [Step-3-Sets-per-Year](Step-3-Sets-per-Year-ms)
