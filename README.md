
# Multi-Purpose Document Processing Tools

This repository contains four Python scripts for document processing:

1. **JPG to Text Extractor**: Extracts text from JPG images using Tesseract OCR.
2. **DOCX Combiner**: Combines multiple `.docx` files into a single document while preserving formatting.
3. **JPG/PNG to TIFF Converter**: Converts JPG and PNG images to TIFF format.
4. **PDF to JPG Converter**: Converts PDF files to JPG images.

## Features

### JPG to Text Extractor

- **Image Preprocessing**: Adaptive thresholding and denoising using OpenCV.
- **Text Extraction**: Utilizes Tesseract OCR to extract text from processed images.
- **GUI Interface**: Easy folder selection for input and output directories.

### DOCX Combiner

- **Combines Multiple DOCX Files**: Merges multiple `.docx` files into a single document.
- **Preserves Formatting**: Retains the original formatting of paragraphs and tables from the source documents.
- **GUI for File Selection**: Utilizes a simple GUI for selecting the input files and output location.

### JPG/PNG to TIFF Converter

- **Image Conversion**: Converts JPG and PNG images to TIFF format.
- **GUI Interface**: Easy folder selection for input and output directories.

### PDF to JPG Converter

- **PDF to Image Conversion**: Converts PDF files to JPG images.
- **GUI Interface**: Easy folder selection for input and output directories.

## Requirements

- Python 3.x
- python-docx
- pytesseract
- OpenCV
- Pillow
- Tkinter

## Installation

1. **Install Python**: Ensure you have Python 3.x installed on your system.
2. **Install Required Python Packages**:
   ```bash
   pip install pytesseract pillow opencv-python-headless python-docx
   ```

3. **Install Tesseract OCR**: Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

## Configuration

Update the `tesseract_cmd` variable in the JPG to Text Extractor and PDF to JPG Converter scripts to match the installation path of Tesseract OCR on your system:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

### JPG to Text Extractor

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/document-processing-tools.git
   cd document-processing-tools
   ```

2. **Run the Script**:
   ```bash
   python jpg_to_text_extractor.py
   ```

   Replace `jpg_to_text_extractor.py` with the actual name of your script file.

3. **Select Folders**:
   - Use the GUI to select the input folder containing JPG images.
   - Select the output folder where extracted text files will be saved.

4. **Start Extraction**: Click the "Start Extraction" button in the GUI to begin the process.

### DOCX Combiner

1. **Run the Script**:
   ```bash
   python docx_combiner.py
   ```

   Replace `docx_combiner.py` with the actual name of your script file.

2. **Select Files**:
   - Use the GUI to select the `.docx` files you want to combine.
   - Select the location and name for the output file.

3. **Combine and Save**: The script will combine the selected `.docx` files into a single document and save it to the specified location.

### JPG/PNG to TIFF Converter

1. **Run the Script**:
   ```bash
   python jpg_png_to_tiff_converter.py
   ```

   Replace `jpg_png_to_tiff_converter.py` with the actual name of your script file.

2. **Select Folders**:
   - Use the GUI to select the input folder containing JPG and PNG images.
   - Select the output folder where the converted TIFF images will be saved.

3. **Start Conversion**: Click the "Start Conversion" button in the GUI to begin the process.

### PDF to JPG Converter

1. **Run the Script**:
   ```bash
   python pdf_to_jpg_gui.py
   ```

   Replace `pdf_to_jpg_gui.py` with the actual name of your script file.

2. **Select Folders**:
   - Use the GUI to select the input folder containing PDF files.
   - Select the output folder where the converted JPG images will be saved.

3. **Start Conversion**: Click the "Start Conversion" button in the GUI to begin the process.

## Script Details

### JPG to Text Extractor

#### `pre_process_image(image_path)`

Preprocesses the image to enhance OCR accuracy by applying adaptive thresholding and denoising.

#### `extract_text_from_jpgs(input_folder, output_folder)`

Processes each JPG image in the input folder, extracts text using Tesseract OCR, and saves the text to the output folder.

#### `select_folders()`

Launches a Tkinter-based GUI for selecting input and output folders and starting the text extraction process.

### DOCX Combiner

#### `select_files()`

Launches a file dialog to select multiple `.docx` files for combining.

#### `append_paragraphs(target_document, source_document)`

Appends paragraphs from the source document to the target document, preserving formatting.

#### `append_tables(target_document, source_document)`

Appends tables from the source document to the target document, preserving formatting.

#### `combine_docx_files(file_paths, output_path)`

Combines the selected `.docx` files into a single document and saves it to the specified output path.

#### `main()`

The main function that orchestrates file selection, combining, and saving the combined document.

### JPG/PNG to TIFF Converter

#### `convert_to_tiff(input_folder, output_folder)`

Converts JPG and PNG images in the input folder to TIFF format and saves them to the output folder.

#### `select_folders()`

Launches a Tkinter-based GUI for selecting input and output folders and starting the conversion process.

### PDF to JPG Converter

#### `pre_process_image(image_path)`

Preprocesses the image to enhance OCR accuracy by applying adaptive thresholding and denoising.

#### `extract_text_from_jpgs(input_folder, output_folder)`

Processes each JPG image in the input folder, extracts text using Tesseract OCR, and saves the text to the output folder.

#### `select_folders()`

Launches a Tkinter-based GUI for selecting input and output folders and starting the text extraction process.

## License

This project is licensed under the GNU General Public License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

