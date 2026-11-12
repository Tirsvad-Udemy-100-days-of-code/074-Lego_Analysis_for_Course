[English](Step-2-Sets) · **Dansk** · [Bahasa Malaysia](Step-2-Sets-ms)

# Trin 2: De ældste og de største sæt

**Spørgsmål:** Hvornår udkom de første sæt, hvor mange var der, og hvilket sæt har flest dele?

![Trin 2: De ældste og de største sæt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-2-sets.png)

## Hvad koden gør

`first_release_year` sorterer efter `year` og finder **1949**. `count_sets_in_year(sets, 1949)` filtrerer med `sets["year"] == 1949` og finder **5** sæt. `largest_sets` sorterer efter `num_parts` i faldende rækkefølge: **The Ultimate Battle for Chima** (9.987 dele) kommer først, derefter UCS Millennium Falcon (7.541 dele).

## Hvad du lærte

- `.sort_values()` sorterer som standard stigende; `ascending=False` vender rækkefølgen.
- Filtrering af en DataFrame med en betingelse (`df[df["year"] == 1949]`).
- Det første svar kan være overraskende: den største æske indeholdt under 10.000 dele.

Forrige: [Trin 1: Udforskning af klodsernes farver](Step-1-Colours-da) · Næste: [Trin 3: Udgivne sæt pr. år](Step-3-Sets-per-Year-da)
