[English](Step-6-Parts-per-Set) · **Dansk** · [Bahasa Malaysia](Step-6-Parts-per-Set-ms)

# Trin 6: Gennemsnitligt antal dele pr. sæt

**Spørgsmål:** Blev LEGO-sættene større og mere komplekse?

![Trin 6: Gennemsnitligt antal dele pr. sæt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-6-parts-per-set.png)

## Hvad koden gør

`parts_per_set` grupperer efter `year` og beregner gennemsnittet af `num_parts` med `.agg()`: omkring 12 dele i 1954 og omkring 222 i 2017. `parts_per_set_chart` tegner et spredningsdiagram, som viser en stigende tendens: nyere sæt har cirka dobbelt så mange dele som sæt fra 1960'erne.

## Hvad du lærte

- `.agg({"num_parts": "mean"})` sammen med `.groupby()`.
- Et spredningsdiagram (`.scatter()`) bruger en prik pr. datapunkt og viser tendenser.
- Det samme udsnitstrick fjerner de to sidste, ufuldstændige år.

Forrige: [Trin 5: To akser i ét diagram](Step-5-Two-Axes-da) · Næste: [Trin 7: Temaer, primærnøgler og fremmednøgler](Step-7-Themes-and-Keys-da)
