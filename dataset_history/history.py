import os
import shutil
from datetime import datetime

HISTORY_FOLDER = "dataset_history"

# CREATE FOLDER IF NOT EXISTS
os.makedirs(HISTORY_FOLDER, exist_ok=True)

def save_dataset(uploaded_file):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"{timestamp}_{uploaded_file.name}"

    save_path = os.path.join(
        HISTORY_FOLDER,
        filename
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

def get_dataset_history():

    files = os.listdir(HISTORY_FOLDER)

    files.sort(reverse=True)

    return files