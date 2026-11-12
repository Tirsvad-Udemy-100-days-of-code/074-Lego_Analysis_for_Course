[English](Step-8-Merge) · **Dansk** · [Bahasa Malaysia](Step-8-Merge-ms)

# Trin 8: Sammenfletning af DataFrames på en nøgle

**Spørgsmål:** Hvordan kombinerer vi antallet af sæt pr. tema med temanavnene?

![Trin 8: Sammenfletning af DataFrames på en nøgle](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-8-merge.png)

## Hvad koden gør

`set_theme_count` gør optællingerne af `theme_id` til en DataFrame med kolonnerne `id` og `set_count`. `merge_theme_names` kalder `pd.merge(set_theme_count, themes, on="id")`. Første række er **Star Wars med 753 sæt**, efterfulgt af Gear (656), Friends (398) og Ninjago (356).

## Hvad du lærte

- `.value_counts()` tæller sæt pr. tema-id.
- `pd.merge(left, right, on="id")` fletter to DataFrames sammen på et fælles kolonnenavn.
- En dictionary bygger en DataFrame; dens nøgler bliver til kolonnenavnene.

Forrige: [Trin 7: Temaer, primærnøgler og fremmednøgler](Step-7-Themes-and-Keys-da) · Næste: [Trin 9: Et søjlediagram over de 10 største temaer](Step-9-Bar-Chart-da)
