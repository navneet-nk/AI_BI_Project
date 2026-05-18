def generate_insights(data, x_axis, y_axis):

    insights = []

    try:

        # HIGHEST VALUE
        max_row = data.loc[data[y_axis].idxmax()]

        insights.append(
            f"Highest {y_axis} is {max_row[y_axis]}"
        )

        insights.append(
            f"Top performing {x_axis} is {max_row[x_axis]}"
        )

        # AVERAGE VALUE
        avg_value = round(data[y_axis].mean(), 2)

        insights.append(
            f"Average {y_axis} is {avg_value}"
        )

        # LOWEST VALUE
        min_row = data.loc[data[y_axis].idxmin()]

        insights.append(
            f"Lowest {y_axis} is {min_row[y_axis]}"
        )

    except Exception as e:

        insights.append(
            f"Could not generate insights: {e}"
        )

    return insights