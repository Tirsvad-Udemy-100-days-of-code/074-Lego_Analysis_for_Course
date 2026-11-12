[English](Step-4-Themes-per-Year) · **Dansk** · [Bahasa Malaysia](Step-4-Themes-per-Year-ms)

# Trin 4: Temaer pr. år med .agg()

**Spørgsmål:** Hvor mange forskellige temaer solgte LEGO hvert år?

![Trin 4: Temaer pr. år med .agg()](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-4-themes-per-year.png)

## Hvad koden gør

`themes_by_year` kører `sets.groupby("year").agg({"theme_id": pd.Series.nunique})` og omdøber kolonnen til `nr_themes`. Der var 2 temaer i 1949 og 78 i 2019; `themes_by_year_chart` plotter kun de hele kalenderår.

## Hvad du lærte

- `.agg()` tager en dictionary: nøglen er kolonnen, værdien er operationen.
- `.rename(columns=...)` giver en kolonne et bedre navn.
- Antallet af temaer voksede indtil midten af 1990'erne, stagnerede og voksede igen i begyndelsen af 2010'erne.

Forrige: [Trin 3: Udgivne sæt pr. år](Step-3-Sets-per-Year-da) · Næste: [Trin 5: To akser i ét diagram](Step-5-Two-Axes-da)
