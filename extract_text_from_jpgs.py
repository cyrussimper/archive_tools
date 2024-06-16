import os
import pytesseract
from PIL import Image
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ensure this path is correct

def pre_process_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply adaptive thresholding
    processed_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Denoise image
    processed_image = cv2.fastNlMeansDenoising(processed_image, h=30)
    return processed_image

def extract_text_from_jpgs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.endswith(".jpg"):
                jpg_path = os.path.join(root, file_name)
                try:
                    print(f"Processing: {jpg_path}")
                    processed_image = pre_process_image(jpg_path)
                    text = pytesseract.image_to_string(processed_image)
                    relative_path = os.path.relpath(root, input_folder)
                    output_subfolder = os.path.join(output_folder, relative_path)
                    if not os.path.exists(output_subfolder):
                        os.makedirs(output_subfolder)
                    base_name = os.path.splitext(file_name)[0]
                    txt_path = os.path.join(output_subfolder, f"{base_name}.txt")
                    with open(txt_path, "w") as text_file:
                        text_file.write(text)
                    print(f"Saved text to: {txt_path}")
                except Exception as e:
                    print(f"Failed to extract text from {jpg_path}: {e}")
                    continue

def select_folders():
    def browse_input():
        folder = filedialog.askdirectory(title="Select the Input Folder")
        input_folder.set(folder)
        print(f"Selected input folder: {folder}")

    def browse_output():
        folder = filedialog.askdirectory(title="Select the Output Folder")
        output_folder.set(folder)
        print(f"Selected output folder: {folder}")

    def start_extraction():
        if not input_folder.get() or not output_folder.get():
            messagebox.showwarning("Missing Information", "Please select both input and output folders.")
            return
        print(f"Starting text extraction from {input_folder.get()} to {output_folder.get()}")
        extract_text_from_jpgs(input_folder.get(), output_folder.get())
        messagebox.showinfo("Extraction Complete", "Text extraction from JPGs is complete.")

    root = tk.Tk()
    root.title("JPG to Text Extractor")

    input_folder = tk.StringVar()
    output_folder = tk.StringVar()

    tk.Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=input_folder, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=output_folder, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2, padx=10, pady=5)

    tk.Button(root, text="Start Extraction", command=start_extraction, bg='blue', fg='white').grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    print("Starting JPG to Text Extractor...")
    select_folders()


