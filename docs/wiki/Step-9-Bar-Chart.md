**English** · [Dansk](Step-9-Bar-Chart-da) · [Bahasa Malaysia](Step-9-Bar-Chart-ms)

# Step 9: A bar chart of the top 10 themes

**Question:** Which themes have the most sets?

![Step 9: A bar chart of the top 10 themes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-9-bar-chart.png)

## What the code does

`top_themes` keeps the first ten rows of the merged table and `top_themes_bar_chart` draws a bar chart with a larger figure (14 by 8), a 45 degree rotation of the theme names, larger fonts and axis labels. Star Wars, Town and Ninjago look like LEGO; Gear, Key Chain and Books show that LEGO sells much more than bricks.

## What you gained

- `.bar()` draws a bar chart from names and values.
- Figure size, rotated tick labels and axis labels make a chart readable.
- Slicing with `[:10]` keeps the top rows.

Previous: [Step-8-Merge](Step-8-Merge) · Next: [Summary](Summary)
