import pandas as pd

def load_data(uploaded_file):

    # CSV FILE
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)

    # EXCEL FILE
    else:
        data = pd.read_excel(uploaded_file)

    return data