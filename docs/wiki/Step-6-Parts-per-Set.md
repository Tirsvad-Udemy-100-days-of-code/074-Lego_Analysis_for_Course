**English** · [Dansk](Step-6-Parts-per-Set-da) · [Bahasa Malaysia](Step-6-Parts-per-Set-ms)

# Step 6: Average parts per set

**Question:** Did LEGO sets grow in size and complexity?

![Step 6: Average parts per set](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-6-parts-per-set.png)

## What the code does

`parts_per_set` groups by `year` and averages `num_parts` with `.agg()`: about 12 parts in 1954 and about 222 in 2017. `parts_per_set_chart` draws a scatter plot, which shows an upward trend: recent sets have roughly twice the parts of sets from the 1960s.

## What you gained

- `.agg({"num_parts": "mean"})` together with `.groupby()`.
- A scatter plot (`.scatter()`) uses a dot per data point and shows trends.
- The same slicing trick removes the incomplete last two years.

Previous: [Step-5-Two-Axes](Step-5-Two-Axes) · Next: [Step-7-Themes-and-Keys](Step-7-Themes-and-Keys)
