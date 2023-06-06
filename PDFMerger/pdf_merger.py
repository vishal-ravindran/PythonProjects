import PyPDF2
import sys
import os

data_folder = r'C:\Users\Visha\OneDrive\Desktop\Temp Folder\Python Projects\PythonProjects\PDFMerger\samplePDF'
target_folder = r'C:\Users\Visha\OneDrive\Desktop\Temp Folder\Python Projects\PythonProjects\PDFMerger\CombinedPDFs'

merged = PyPDF2.PdfMerger()

for file in os.listdir(data_folder):
    if file.endswith(".pdf"):
        file_path = os.path.join(data_folder, file)
        with open(file_path, 'rb') as pdf_file:
            merged.append(pdf_file)

output_path = os.path.join(target_folder, 'combined.pdf')
with open(output_path, 'wb') as output_file:
    merged.write(output_file)
