[English](Step-3-Sets-per-Year) · **Dansk** · [Bahasa Malaysia](Step-3-Sets-per-Year-ms)

# Trin 3: Udgivne sæt pr. år

**Spørgsmål:** Hvordan ændrede antallet af udgivne sæt sig over tid?

![Trin 3: Udgivne sæt pr. år](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-3-sets-per-year.png)

## Hvad koden gør

`sets_by_year` grupperer efter `year` og tæller: 5 sæt i 1949, 28 i 1955 og 840 i 2019. Datasættet er et øjebliksbillede fra slutningen af 2020, så `drop_incomplete_years` fjerner de to sidste rækker (2020 og 2021), før `sets_by_year_chart` tegner kurvediagrammet.

## Hvad du lærte

- `.groupby()` efterfulgt af `.count()` aggregerer rækker pr. gruppe.
- At udsnitte en DataFrame som en liste: `df[:-2]` fjerner de sidste to rækker (Python-listeudsnit fra dag 21).
- Ufuldstændige data giver et misvisende diagram; skær dem væk, før du plotter.

Forrige: [Trin 2: De ældste og de største sæt](Step-2-Sets-da) · Næste: [Trin 4: Temaer pr. år med .agg()](Step-4-Themes-per-Year-da)
