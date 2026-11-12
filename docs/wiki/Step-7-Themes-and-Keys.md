**English** · [Dansk](Step-7-Themes-and-Keys-da) · [Bahasa Malaysia](Step-7-Themes-and-Keys-ms)

# Step 7: Themes, primary keys and foreign keys

**Question:** Which theme names belong to the theme ids, and how are the tables linked?

![Step 7: Themes, primary keys and foreign keys](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-7-themes-and-keys.png)

## What the code does

`sets.csv` holds `theme_id` (a **foreign key**); `themes.csv` holds the unique `id` (the **primary key**) and the theme name. `find_theme_ids(themes, "Star Wars")` finds four ids (18, 158, 209, 261) and `sets_for_theme_ids` lists the matching sets, for example the Star Wars Advent Calendars that share one theme.

## What you gained

- A relational database is split into tables linked by keys.
- A primary key is unique in its own table; a foreign key points to it from another table.
- One name (Star Wars) can belong to several ids.

Previous: [Step-6-Parts-per-Set](Step-6-Parts-per-Set) · Next: [Step-8-Merge](Step-8-Merge)
