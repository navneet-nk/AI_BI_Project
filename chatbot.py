def ask_data_question(data, question):

    question = question.lower()

    # COLUMN NAMES
    columns = data.columns

    # HIGHEST VALUE
    if "highest" in question or "maximum" in question:

        for column in columns:

            if column.lower() in question:

                if data[column].dtype != 'object':

                    max_value = data[column].max()

                    return f"Highest {column} is {max_value}"

    # LOWEST VALUE
    elif "lowest" in question or "minimum" in question:

        for column in columns:

            if column.lower() in question:

                if data[column].dtype != 'object':

                    min_value = data[column].min()

                    return f"Lowest {column} is {min_value}"

    # AVERAGE VALUE
    elif "average" in question or "mean" in question:

        for column in columns:

            if column.lower() in question:

                if data[column].dtype != 'object':

                    avg_value = round(
                        data[column].mean(),
                        2
                    )

                    return f"Average {column} is {avg_value}"

    # TOTAL VALUE
    elif "total" in question or "sum" in question:

        for column in columns:

            if column.lower() in question:

                if data[column].dtype != 'object':

                    total_value = data[column].sum()

                    return f"Total {column} is {total_value}"

    return "Sorry, I could not understand the question."