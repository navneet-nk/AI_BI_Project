from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def train_model(data, input_column, target_column):

    # PREPARE DATA
    X = data[[input_column]]
    y = data[target_column]

    # SPLIT DATA
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # CREATE MODEL
    model = LinearRegression()

    # TRAIN MODEL
    model.fit(X_train, y_train)

    # PREDICTIONS
    predictions = model.predict(X_test)

    # CALCULATE ERROR
    error = mean_absolute_error(
        y_test,
        predictions
    )

    return predictions, y_test, error