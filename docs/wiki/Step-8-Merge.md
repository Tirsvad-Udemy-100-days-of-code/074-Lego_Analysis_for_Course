**English** · [Dansk](Step-8-Merge-da) · [Bahasa Malaysia](Step-8-Merge-ms)

# Step 8: Merging DataFrames on a key

**Question:** How do we combine the number of sets per theme with the theme names?

![Step 8: Merging DataFrames on a key](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-8-merge.png)

## What the code does

`set_theme_count` turns the `theme_id` counts into a DataFrame with the columns `id` and `set_count`. `merge_theme_names` calls `pd.merge(set_theme_count, themes, on="id")`. The first row is **Star Wars with 753 sets**, followed by Gear (656), Friends (398) and Ninjago (356).

## What you gained

- `.value_counts()` counts sets per theme id.
- `pd.merge(left, right, on="id")` joins two DataFrames on a shared column name.
- A dictionary builds a DataFrame; its keys become the column names.

Previous: [Step-7-Themes-and-Keys](Step-7-Themes-and-Keys) · Next: [Step-9-Bar-Chart](Step-9-Bar-Chart)
