[English](Step-8-Merge) · [Dansk](Step-8-Merge-da) · **Bahasa Malaysia**

# Langkah 8: Menggabungkan DataFrame pada satu kunci

**Soalan:** Bagaimanakah kita menggabungkan bilangan set setiap tema dengan nama tema?

![Langkah 8: Menggabungkan DataFrame pada satu kunci](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-8-merge.png)

## Apa yang kod lakukan

`set_theme_count` menukar kiraan `theme_id` kepada DataFrame dengan lajur `id` dan `set_count`. `merge_theme_names` memanggil `pd.merge(set_theme_count, themes, on="id")`. Baris pertama ialah **Star Wars dengan 753 set**, diikuti Gear (656), Friends (398) dan Ninjago (356).

## Apa yang anda perolehi

- `.value_counts()` mengira set bagi setiap id tema.
- `pd.merge(left, right, on="id")` menggabungkan dua DataFrame pada nama lajur yang dikongsi.
- Kamus membina DataFrame; kuncinya menjadi nama lajur.

Sebelumnya: [Step-7-Themes-and-Keys](Step-7-Themes-and-Keys-ms) · Seterusnya: [Step-9-Bar-Chart](Step-9-Bar-Chart-ms)
