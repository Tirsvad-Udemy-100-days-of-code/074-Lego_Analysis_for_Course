**English** · [Dansk](Step-4-Themes-per-Year-da) · [Bahasa Malaysia](Step-4-Themes-per-Year-ms)

# Step 4: Themes per year with .agg()

**Question:** How many different themes did LEGO sell each year?

![Step 4: Themes per year with .agg()](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-4-themes-per-year.png)

## What the code does

`themes_by_year` runs `sets.groupby("year").agg({"theme_id": pd.Series.nunique})` and renames the column to `nr_themes`. There were 2 themes in 1949 and 78 in 2019; `themes_by_year_chart` plots the full calendar years only.

## What you gained

- `.agg()` takes a dictionary: the key is the column, the value is the operation.
- `.rename(columns=...)` gives a column a better name.
- The number of themes grew until the mid-1990s, stalled, and grew again in the early 2010s.

Previous: [Step-3-Sets-per-Year](Step-3-Sets-per-Year) · Next: [Step-5-Two-Axes](Step-5-Two-Axes)
