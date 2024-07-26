## PDF Field Extraction Script

This script extracts text from a PDF and parses fields and values based on the presence of a colon (":"). The fields and values are then printed to the console.

### Prerequisites

- Python 3.x
- `venv` for creating a virtual environment
- `PyMuPDF` library for PDF manipulation

### Setup

1. **Create a virtual environment:**
   ```sh
   python -m venv myvenv
   ```

2. **Activate the virtual environment:**

   - On Windows:
     ```sh
     myvenv\Scripts\activate
     ```

   - On macOS and Linux:
     ```sh
     source myvenv/bin/activate
     ```

3. **Install the required library:**
   ```sh
   pip install PyMuPDF
   ```

### Script Description

The script consists of three main functions:

1. **`extract_text_from_pdf(pdf_path)`**:
   - Opens the PDF file using `PyMuPDF`.
   - Extracts text from each page and concatenates it into a single string.
   - Returns the extracted text.

2. **`parse_fields_and_values(text)`**:
   - Splits the extracted text into lines.
   - Parses lines containing a colon (":") into field-value pairs.
   - Returns a dictionary of parsed fields and values.

3. **`main(pdf_path)`**:
   - Calls the `extract_text_from_pdf` function to get the text from the PDF.
   - Calls the `parse_fields_and_values` function to get the fields and values.
   - Prints each field and its corresponding value.

### Usage

1. **Edit the `pdf_path` variable in the script:**
   ```python
   pdf_path = "C:\\Users\\basil\\OneDrive\\Documentos\\test\\doc.pdf"
   ```

2. **Run the script:**
   ```sh
   python script_name.py
   ```

Replace `script_name.py` with the name of your script file. The script will print the fields and values extracted from the specified PDF.

### Example

Given a PDF with the following content:
```
Name: John Doe
Age: 30
Email: john.doe@example.com
```

The script will output:
```
Field: Name, Value: John Doe
Field: Age, Value: 30
Field: Email, Value: john.doe@example.com
```

### Notes

- Ensure the PDF file exists at the specified path.
- The script assumes fields and values are separated by a colon (":"). Adjust the parsing logic if your PDF format differs.

### Deactivation

To deactivate the virtual environment, simply run:
```sh
deactivate
```