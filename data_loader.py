# data_loader.py
import pandas as pd
import os

FOLDER_PATH = r"C:\Users\97250\OneDrive\Desktop\python\Dataset\NBA.Data\csv"

def load_all_nba_data(folder_path=FOLDER_PATH):
    """
    Loads all NBA CSV files from a folder and combines them into a single DataFrame.
    """
    all_dfs = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path)
                df.columns = [col.strip() for col in df.columns]
                if 'date' in df.columns:
                    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
                df['source_file'] = file_name
                all_dfs.append(df)
                print(f" Loaded {file_name}")
            except Exception as e:
                print(f" Failed to load {file_name}: {e}")

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        print(" All NBA data loaded and combined!")
        return combined_df
    else:
        print(" No CSV files loaded.")
        return None
