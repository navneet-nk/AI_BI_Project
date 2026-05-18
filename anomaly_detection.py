import numpy as np

def detect_anomalies(data, column):

    # REMOVE NULL VALUES
    clean_data = data[column].dropna()

    # MEAN
    mean = clean_data.mean()

    # STANDARD DEVIATION
    std = clean_data.std()

    anomalies = []

    # CHECK EACH VALUE
    for value in clean_data:

        z_score = (
            value - mean
        ) / std

        # ANOMALY CONDITION
        if abs(z_score) > 3:

            anomalies.append(value)

    return anomalies