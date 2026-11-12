[English](Step-1-Colours) · **Dansk** · [Bahasa Malaysia](Step-1-Colours-ms)

# Trin 1: Udforskning af klodsernes farver

**Spørgsmål:** Hvor mange farver laver LEGO, og hvor mange er gennemsigtige?

![Trin 1: Udforskning af klodsernes farver](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-1-colours.png)

## Hvad koden gør

`count_unique_colours` bruger `.nunique()` på kolonnen `name`: **135** farver. `transparent_counts_groupby` (`.groupby("is_trans").count()`) og `transparent_counts_value_counts` (`.value_counts()`) giver samme svar på to måder: **107** uigennemsigtige og **28** gennemsigtige farver.

## Hvad du lærte

- At læse en CSV-fil med `pd.read_csv` og se på den med `.head()`.
- `.nunique()` tæller forskellige værdier.
- Det samme spørgsmål kan besvares med `.groupby().count()` eller `.value_counts()`; `.value_counts()` er genvejen til at tælle kategorier.

Forrige: [Kom godt i gang](Getting-Started-da) · Næste: [Trin 2: De ældste og de største sæt](Step-2-Sets-da)
