**English** · [Dansk](Step-1-Colours-da) · [Bahasa Malaysia](Step-1-Colours-ms)

# Step 1: Exploring the brick colours

**Question:** How many colours does LEGO make, and how many are transparent?

![Step 1: Exploring the brick colours](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-1-colours.png)

## What the code does

`count_unique_colours` uses `.nunique()` on the `name` column: **135** colours. `transparent_counts_groupby` (`.groupby("is_trans").count()`) and `transparent_counts_value_counts` (`.value_counts()`) give the same answer in two ways: **107** opaque and **28** transparent colours.

## What you gained

- Reading a CSV with `pd.read_csv` and looking at it with `.head()`.
- `.nunique()` counts distinct values.
- The same question can be answered with `.groupby().count()` or `.value_counts()`; `.value_counts()` is the shortcut for counting categories.

Previous: [Getting-Started](Getting-Started) · Next: [Step-2-Sets](Step-2-Sets)
