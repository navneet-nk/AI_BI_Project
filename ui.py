import streamlit as st

def apply_custom_ui():

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #06111f 0%,
            #0b1220 100%
        );
        color: #e6eaf1;
        font-family: "Segoe UI", sans-serif;
    }

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #06111f 0%,
            #0b1220 100%
        ) !important;

        border-right: 1px solid #1f2a3d;
    }

    section[data-testid="stSidebar"] * {
        color: #e6eaf1 !important;
    }

    h1 {

        color: #ffffff !important;

        text-align: center;

        font-size: 52px !important;

        font-weight: 800;

        margin-bottom: 10px;

        letter-spacing: 1px;
    }

    h2, h3 {

        color: #ffffff !important;

        font-weight: 700;
    }

    hr {

        border: 1px solid #1e293b;

        margin-top: 20px;

        margin-bottom: 20px;
    }

    div[data-testid="metric-container"] {

        background: linear-gradient(
            135deg,
            #162033,
            #1f2a44
        );

        border: 1px solid #334155;

        border-radius: 16px;

        padding: 18px;

        box-shadow: 0px 8px 20px rgba(
            0,
            0,
            0,
            0.25
        );

        transition: 0.2s ease-in-out;
    }

    div[data-testid="metric-container"]:hover {

        transform: translateY(-4px);

        border-color: #3b82f6;
    }

    .stButton > button {

        background: #2563eb;

        color: white;

        border: none;

        border-radius: 10px;

        padding: 10px 20px;

        font-weight: 600;

        transition: 0.2s ease;
    }

    .stButton > button:hover {

        background: #3b82f6;

        transform: translateY(-2px);
    }

    .stDownloadButton > button {

        background: #16a34a;

        color: white;

        border: none;

        border-radius: 10px;

        padding: 10px 20px;

        font-weight: 600;

        transition: 0.2s ease;
    }

    .stDownloadButton > button:hover {

        background: #22c55e;

        transform: translateY(-2px);
    }

    .stSelectbox > div > div {

        background-color: #111b33;

        border: 1px solid #334155;

        border-radius: 10px;

        color: #ffffff;
    }

    .stTextInput > div > div > input {

        background-color: #111b33;

        color: #e6eaf1;

        border: 1px solid #334155;

        border-radius: 10px;

        padding: 8px 12px;
    }

    .stSlider > div > div > div > div {

        background: #2563eb;
    }

    .stDataFrame {

        border-radius: 12px;

        overflow: hidden;

        border: 1px solid #334155;
    }

    .stDataFrame td {

        background-color: #0f172a;

        color: #e6edf3;
    }

    .stDataFrame tbody tr:hover {

        background-color: #1e293b !important;
    }

    ::-webkit-scrollbar {

        width: 8px;
    }

    ::-webkit-scrollbar-thumb {

        background: #334155;

        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {

        background: #475569;
    }

    </style>
    """, unsafe_allow_html=True)