**English** · [Dansk](Step-2-Sets-da) · [Bahasa Malaysia](Step-2-Sets-ms)

# Step 2: The oldest and the largest sets

**Question:** When were the first sets released, how many were there, and which set has the most parts?

![Step 2: The oldest and the largest sets](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-2-sets.png)

## What the code does

`first_release_year` sorts by `year` and finds **1949**. `count_sets_in_year(sets, 1949)` filters with `sets["year"] == 1949` and finds **5** sets. `largest_sets` sorts by `num_parts` in descending order: **The Ultimate Battle for Chima** (9,987 parts) comes first, then the UCS Millennium Falcon (7,541 parts).

## What you gained

- `.sort_values()` sorts ascending by default; `ascending=False` reverses it.
- Filtering a DataFrame with a condition (`df[df["year"] == 1949]`).
- The first answer can be surprising: the largest box held under 10,000 parts.

Previous: [Step-1-Colours](Step-1-Colours) · Next: [Step-3-Sets-per-Year](Step-3-Sets-per-Year)
