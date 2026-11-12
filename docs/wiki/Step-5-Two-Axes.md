**English** · [Dansk](Step-5-Two-Axes-da) · [Bahasa Malaysia](Step-5-Two-Axes-ms)

# Step 5: Two axes in one chart

**Question:** How can sets and themes share one chart when their scales differ?

![Step 5: Two axes in one chart](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/raw/branch/main/docs/images/step-5-two-axes.png)

## What the code does

`sets_and_themes_chart` creates an axis, calls `.twinx()` to get a second y axis that shares the x axis, and colours each line and its axis so the reader can tell them apart. The themes range up to about 90 and the sets up to about 900.

## What you gained

- `ax1 = plt.gca()` and `ax2 = ax1.twinx()` create two axes that share the x axis.
- Colour and labels turn two lines into a readable story.
- Plotting different scales on one axis hides the smaller series.

Previous: [Step-4-Themes-per-Year](Step-4-Themes-per-Year) · Next: [Step-6-Parts-per-Set](Step-6-Parts-per-Set)
