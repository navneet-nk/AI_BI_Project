import numpy as np

from sklearn.linear_model import LinearRegression

def forecast_future_values(data, target_column):

    # REMOVE NULL VALUES
    clean_data = data[target_column].dropna()

    # CREATE INDEX
    X = np.arange(len(clean_data)).reshape(-1, 1)

    y = clean_data.values

    # TRAIN MODEL
    model = LinearRegression()

    model.fit(X, y)

    # FUTURE INDEX
    future_days = 10

    future_X = np.arange(
        len(clean_data),
        len(clean_data) + future_days
    ).reshape(-1, 1)

    # PREDICT FUTURE
    predictions = model.predict(future_X)

    return predictions