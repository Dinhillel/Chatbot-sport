import os

FILE_PATH = r"C:\Users\97250\OneDrive\Desktop\python\src\Data\csv\nba"
if os.path.exists(FILE_PATH):
    print("File exists")
else:
    print("File does not exist")