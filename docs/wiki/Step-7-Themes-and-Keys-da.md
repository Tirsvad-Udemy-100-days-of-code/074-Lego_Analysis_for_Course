[English](Step-7-Themes-and-Keys) · **Dansk** · [Bahasa Malaysia](Step-7-Themes-and-Keys-ms)

# Trin 7: Temaer, primærnøgler og fremmednøgler

**Spørgsmål:** Hvilke temanavne hører til tema-id'erne, og hvordan er tabellerne forbundet?

![Trin 7: Temaer, primærnøgler og fremmednøgler](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-7-themes-and-keys.png)

## Hvad koden gør

`sets.csv` indeholder `theme_id` (en **fremmednøgle**); `themes.csv` indeholder det unikke `id` (**primærnøglen**) og temanavnet. `find_theme_ids(themes, "Star Wars")` finder fire id'er (18, 158, 209, 261), og `sets_for_theme_ids` viser de tilhørende sæt, for eksempel Star Wars-adventskalendrene, der deler ét tema.

## Hvad du lærte

- En relationel database er opdelt i tabeller, der er forbundet med nøgler.
- En primærnøgle er unik i sin egen tabel; en fremmednøgle peger på den fra en anden tabel.
- Ét navn (Star Wars) kan høre til flere id'er.

Forrige: [Trin 6: Gennemsnitligt antal dele pr. sæt](Step-6-Parts-per-Set-da) · Næste: [Trin 8: Sammenfletning af DataFrames på en nøgle](Step-8-Merge-da)
