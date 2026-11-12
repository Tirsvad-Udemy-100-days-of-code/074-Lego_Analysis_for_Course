**English** · [Dansk](Step-3-Sets-per-Year-da) · [Bahasa Malaysia](Step-3-Sets-per-Year-ms)

# Step 3: Sets released per year

**Question:** How did the number of released sets change over time?

![Step 3: Sets released per year](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-3-sets-per-year.png)

## What the code does

`sets_by_year` groups by `year` and counts: 5 sets in 1949, 28 in 1955 and 840 in 2019. The snapshot is from late 2020, so `drop_incomplete_years` removes the last two rows (2020 and 2021) before `sets_by_year_chart` draws the line chart.

## What you gained

- `.groupby()` followed by `.count()` aggregates rows per group.
- Slicing a DataFrame like a list: `df[:-2]` drops the last two rows (Python list slicing from Day 21).
- Incomplete data gives a misleading chart; cut it before plotting.

Previous: [Step-2-Sets](Step-2-Sets) · Next: [Step-4-Themes-per-Year](Step-4-Themes-per-Year)
