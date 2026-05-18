import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_data
from charts import generate_chart
from ml_model import train_model
from insights import generate_insights
from ui import apply_custom_ui
from utils import download_dataset

from dataset_history.history import (
    save_dataset,
    get_dataset_history
)

from forecasting import forecast_future_values
from chatbot import ask_data_question
from report_generator import generate_pdf_report
from anomaly_detection import detect_anomalies
from auth import create_user, login_user

# LOGIN SESSION
if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

# PAGE SETTINGS
st.set_page_config(
    page_title="AI Business Analytics Dashboard",
    layout="wide"
)

# APPLY UI
apply_custom_ui()

# SIDEBAR NAVIGATION
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "AI Insights",
        "Forecasting",
        "Chatbot",
        "Anomaly Detection",
        "Dataset History"
    ]
)
if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()

# AUTHENTICATION
if not st.session_state.logged_in:

    st.title("🔐 Login System")

    auth_mode = st.selectbox(
        "Select Option",
        ["Login", "Signup"]
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    # SIGNUP
    if auth_mode == "Signup":

        if st.button("Create Account"):

            create_user(
                username,
                password
            )

            st.success(
                "Account created successfully!"
            )

    # LOGIN
    else:

        if st.button("Login"):

            user = login_user(
                username,
                password
            )

            if user:

                st.session_state.logged_in = True

                st.success(
                    "Login successful!"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    st.stop()

# TITLE
st.title("AI Powered Business Analytics Dashboard")

st.markdown("---")

# FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# IF FILE UPLOADED
if uploaded_file is not None:

    # SAVE DATASET HISTORY
    save_dataset(uploaded_file)

    # LOAD DATA
    data = load_data(uploaded_file)

    # NUMERIC COLUMNS
    numeric_columns = list(
        data.select_dtypes(
            include=['number']
        ).columns
    )

    # CATEGORICAL COLUMNS
    categorical_columns = list(
        data.select_dtypes(
            include=['object', 'string']
        ).columns
    )

    # FILTERED DATA
    filtered_data = data.copy()

    # SIDEBAR FILTERS
    st.sidebar.header("Dataset Filters")

    # CATEGORICAL FILTERS
    for column in categorical_columns:

        unique_values = (
            data[column]
            .dropna()
            .unique()
        )

        selected_values = st.sidebar.multiselect(
            f"Filter {column}",
            unique_values,
            default=unique_values
        )

        filtered_data = filtered_data[
            filtered_data[column].isin(
                selected_values
            )
        ]

    # NUMERIC FILTERS
    for column in numeric_columns:

        min_value = float(
            data[column].min()
        )

        max_value = float(
            data[column].max()
        )

        selected_range = st.sidebar.slider(
            f"Filter {column}",
            min_value,
            max_value,
            (min_value, max_value)
        )

        filtered_data = filtered_data[
            (
                filtered_data[column]
                >= selected_range[0]
            )
            &
            (
                filtered_data[column]
                <= selected_range[1]
            )
        ]

    # CHART SETTINGS
    st.sidebar.header("Chart Settings")

    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        [
            "Bar Chart",
            "Line Chart",
            "Pie Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot"
        ]
    )

    x_axis = st.sidebar.selectbox(
        "Select X-Axis",
        options=list(filtered_data.columns)
    )

    y_axis = st.sidebar.selectbox(
        "Select Y-Axis",
        numeric_columns
    )

    # SIDEBAR HISTORY
    st.sidebar.markdown(
        "## 📂 Dataset History"
    )

    history_files = get_dataset_history()

    for file in history_files[:5]:
        st.sidebar.write(file)

    # DASHBOARD PAGE
    if page == "Dashboard":

        st.markdown(
            "## 📊 Dataset Preview"
        )

        st.write(filtered_data.head())

        st.markdown(
            "## 📈 Generated Chart"
        )

        fig = generate_chart(
            filtered_data,
            x_axis,
            y_axis,
            chart_type
        )

        st.pyplot(fig)

        st.markdown(
            "## 📌 Dataset KPIs"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            filtered_data.shape[0]
        )

        col2.metric(
            "Columns",
            filtered_data.shape[1]
        )

        avg_value = round(
            filtered_data[y_axis].mean(),
            2
        )

        col3.metric(
            "Average Value",
            avg_value
        )
        # DOWNLOAD SECTION
        st.markdown("---")

        st.subheader(
            "Download Filtered Dataset"
        )

        download_dataset(filtered_data)

        # GENERATE COMMON PDF REPORT
        st.markdown("---")

        st.markdown("## 📄 Generate Complete Analytics Report")

        # GENERATE COMMON INSIGHTS
        common_insights = generate_insights(
            filtered_data,
            x_axis,
            y_axis
        )

        # GENERATE COMMON FORECAST
        forecast_values = forecast_future_values(
            filtered_data,
            y_axis
        )

        if st.button("Generate Full PDF Report"):

            fig = generate_chart(
                filtered_data,
                x_axis,
                y_axis,
                chart_type
            )

            pdf_file = generate_pdf_report(
                filtered_data,
                common_insights,
                forecast_values,
                fig
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="Download Full Report",
                    data=file,
                    file_name="analytics_report.pdf",
                    mime="application/pdf"
                )


    # AI INSIGHTS PAGE
    elif page == "AI Insights":

        st.markdown(
            "## 🤖 AI Generated Insights"
        )

        insights = generate_insights(
            filtered_data,
            x_axis,
            y_axis
        )

        for insight in insights:
            st.write("•", insight)

        st.markdown("---")

        st.subheader(
            "AI Prediction Module"
        )

        input_column = st.selectbox(
            "Select Input Feature (X)",
            numeric_columns
        )

        target_column = st.selectbox(
            "Select Target Value (Y)",
            numeric_columns
        )

        if input_column != target_column:

            predictions, y_test, error = train_model(
                filtered_data,
                input_column,
                target_column
            )

            st.write(
                "Model trained successfully!"
            )

            st.write(
                "Mean Absolute Error:",
                round(error, 2)
            )

            fig2, ax2 = plt.subplots(
                figsize=(10, 5)
            )

            ax2.scatter(
                y_test,
                predictions
            )

            ax2.set_xlabel(
                "Actual Values"
            )

            ax2.set_ylabel(
                "Predicted Values"
            )

            ax2.set_title(
                "Actual vs Predicted"
            )

            st.pyplot(fig2)

        else:

            st.warning(
                "Please select different columns for X and Y."
            )

    # FORECASTING PAGE
    elif page == "Forecasting":

        st.markdown(
            "## 🔮 Future Forecasting"
        )

        forecast_column = st.selectbox(
            "Select Column for Forecasting",
            numeric_columns
        )

        forecast_values = forecast_future_values(
            filtered_data,
            forecast_column
        )

        st.write(
            "Next 10 Predicted Values:"
        )

        st.write(forecast_values)

        fig3, ax3 = plt.subplots(
            figsize=(10, 5)
        )

        ax3.plot(
            range(len(forecast_values)),
            forecast_values,
            marker='o'
        )

        ax3.set_title(
            f"Future Forecast for {forecast_column}"
        )

        ax3.set_xlabel(
            "Future Time"
        )

        ax3.set_ylabel(
            "Predicted Value"
        )

        st.pyplot(fig3)

    # CHATBOT PAGE
    elif page == "Chatbot":

        st.markdown(
            "## 🤖 Chat With Your Data"
        )

        user_question = st.text_input(
            "Ask a question about your dataset"
        )

        if user_question:

            answer = ask_data_question(
                filtered_data,
                user_question
            )

            st.success(answer)

    # ANOMALY DETECTION PAGE
    elif page == "Anomaly Detection":

        st.markdown(
            "## ⚠️ AI Anomaly Detection"
        )

        anomaly_column = st.selectbox(
            "Select Column for Detection",
            numeric_columns
        )

        anomalies = detect_anomalies(
            filtered_data,
            anomaly_column
        )

        st.write(
            f"Total Anomalies Found: {len(anomalies)}"
        )

        if len(anomalies) > 0:

            st.warning(
                "Anomalies Detected!"
            )

            st.write(anomalies)

        else:

            st.success(
                "No significant anomalies detected."
            )
        

    # DATASET HISTORY PAGE
    elif page == "Dataset History":

        st.markdown(
            "## 📂 Dataset History"
        )

        for file in history_files:
            st.write(file)

    
    

else:

    st.info(
        "Please upload a dataset to begin."
    )