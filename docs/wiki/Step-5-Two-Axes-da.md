[English](Step-5-Two-Axes) · **Dansk** · [Bahasa Malaysia](Step-5-Two-Axes-ms)

# Trin 5: To akser i ét diagram

**Spørgsmål:** Hvordan kan sæt og temaer dele ét diagram, når deres skalaer er forskellige?

![Trin 5: To akser i ét diagram](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-5-two-axes.png)

## Hvad koden gør

`sets_and_themes_chart` opretter en akse, kalder `.twinx()` for at få en anden y-akse, der deler x-aksen, og farver hver kurve og dens akse, så læseren kan skelne dem fra hinanden. Temaerne går op til omkring 90 og sættene op til omkring 900.

## Hvad du lærte

- `ax1 = plt.gca()` og `ax2 = ax1.twinx()` opretter to akser, der deler x-aksen.
- Farver og mærkater gør to kurver til en læsbar fortælling.
- Hvis man plotter forskellige skalaer på samme akse, forsvinder den mindre dataserie.

Forrige: [Trin 4: Temaer pr. år med .agg()](Step-4-Themes-per-Year-da) · Næste: [Trin 6: Gennemsnitligt antal dele pr. sæt](Step-6-Parts-per-Set-da)
