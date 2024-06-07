import os
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_pdfs_to_jpgs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.endswith(".pdf"):
                pdf_path = os.path.join(root, file_name)
                try:
                    print(f"Processing: {pdf_path}")
                    pdf_document = fitz.open(pdf_path)
                    for page_num in range(len(pdf_document)):
                        page = pdf_document.load_page(page_num)
                        pix = page.get_pixmap()
                        relative_path = os.path.relpath(root, input_folder)
                        output_subfolder = os.path.join(output_folder, relative_path)
                        if not os.path.exists(output_subfolder):
                            os.makedirs(output_subfolder)
                        base_name = os.path.splitext(file_name)[0]
                        jpg_path = os.path.join(output_subfolder, f"{base_name}_page_{page_num + 1}.jpg")
                        print(f"Saving: {jpg_path}")
                        pix.save(jpg_path)
                except Exception as e:
                    print(f"Failed to convert {pdf_path}: {e}")
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

    def start_conversion():
        if not input_folder.get() or not output_folder.get():
            messagebox.showwarning("Missing Information", "Please select both input and output folders.")
            return
        print(f"Starting conversion from {input_folder.get()} to {output_folder.get()}")
        convert_pdfs_to_jpgs(input_folder.get(), output_folder.get())
        messagebox.showinfo("Conversion Complete", "PDF to JPG conversion is complete.")

    root = tk.Tk()
    root.title("PDF to JPG Converter")

    input_folder = tk.StringVar()
    output_folder = tk.StringVar()

    tk.Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=input_folder, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=output_folder, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2, padx=10, pady=5)

    tk.Button(root, text="Start Conversion", command=start_conversion, bg='blue', fg='white').grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    print("Starting PDF to JPG Converter...")
    select_folders()
