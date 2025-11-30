import os 
from file_reader import read_file_bytes
from detector import detect_file_type
from utils import compare_extension_and_type


def analyze_file(file_path):
    file_bytes = read_file_bytes(file_path)
    detected_type = detect_file_type(file_bytes)
    print(f"{file_path}: Detected type -> {detected_type}")
    compare_extension_and_type(file_path, detected_type)

def analyze_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            analyze_file(file_path)


path = input("Enter file or folder path to analyze: ").strip()
if os.path.isfile(path):
    analyze_file(path)
elif os.path.isdir(path):
    analyze_folder(path)
else:
    print("Invalid input")
