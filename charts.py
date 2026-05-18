import matplotlib.pyplot as plt
import pandas as pd

def generate_chart(data, x_axis, y_axis, chart_type):

    fig, ax = plt.subplots(figsize=(10, 5))

    # HANDLE DUPLICATE COLUMNS
    data = data.loc[:, ~data.columns.duplicated()]

    # ENSURE SERIES
    x_data = data[x_axis]
    y_data = data[y_axis]

    # IF MULTIPLE COLUMNS RETURNED
    if isinstance(y_data, pd.DataFrame):
        y_data = y_data.iloc[:, 0]

    # CATEGORICAL DATA
    if data[x_axis].dtype == 'object':

        grouped_data = data.groupby(x_axis)[y_axis].sum()

        if chart_type == "Bar Chart":
            ax.bar(grouped_data.index, grouped_data.values)

        elif chart_type == "Line Chart":
            ax.plot(grouped_data.index, grouped_data.values)

        elif chart_type == "Pie Chart":
            ax.pie(
                grouped_data.values,
                labels=grouped_data.index,
                autopct='%1.1f%%'
            )

    # NUMERIC DATA
    else:

        plot_data = data[[x_axis, y_axis]].head(20)

        # REMOVE DUPLICATES AGAIN
        plot_data = plot_data.loc[
            :,
            ~plot_data.columns.duplicated()
        ]

        y_values = plot_data[y_axis]

        # SAFETY CHECK
        if isinstance(y_values, pd.DataFrame):
            y_values = y_values.iloc[:, 0]

        if chart_type == "Bar Chart":

            ax.bar(
                range(len(plot_data)),
                y_values
            )

        elif chart_type == "Line Chart":

            ax.plot(
                range(len(plot_data)),
                y_values
            )

        elif chart_type == "Pie Chart":

            pie_data = y_values.head(5)

            ax.pie(
                pie_data,
                autopct='%1.1f%%'
            )
        elif chart_type == "Scatter Plot":

            ax.scatter(
                plot_data[x_axis],
                y_values
            )
        elif chart_type == "Histogram":

            ax.hist(
                y_values,
                bins=10
            )
        elif chart_type == "Box Plot":

            ax.boxplot(y_values)

    ax.set_title(f"{y_axis} by {x_axis}")

    return fig