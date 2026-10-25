# from langchain_community.document_loaders import  CSVLoader

# loader = CSVLoader(file_path='BankwiseMessageId_File_Data.csv')

# data = loader.load()

# print(data[0])

# print(len(data))

from pathlib import Path
from langchain_community.document_loaders import CSVLoader

# Get the folder containing CSV_loader.py
folder = Path(__file__).resolve().parent

# Build the CSV file path
file_path = folder / "BankwiseMessageId_File_Data.csv"

print("CSV path:", file_path)
print("File exists:", file_path.exists())

loader = CSVLoader(file_path=str(file_path), encoding="utf-8")

data = loader.load()

print(data[2])

print(len(data))




































