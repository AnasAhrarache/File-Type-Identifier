# File Type Identifier

## Project Overview

The File Type Identifier is a Python tool that detects the actual type of a file by analyzing its **magic bytes** (file signature) rather than relying on file extensions.
This approach improves security by detecting disguised or malicious files that have misleading extensions.

### Features

* Detects common file types such as JPEG, PNG, PDF, ZIP, and more.
* Supports analyzing single files or entire folders.
* Optionally compares detected file type with file extension to flag inconsistencies.
* Modular and expandable design for adding new file types easily.

---

## Project Structure

```
file_type_identifier/
│
├── main.py             # Entry point: handles user input and runs detection
├── file_reader.py      # Functions to open files and read bytes
├── magic_dict.py       # Dictionary of magic numbers and corresponding file types
├── detector.py         # Core logic to match bytes against magic numbers
├── utils.py            # Optional helpers: logging, extension comparison, reporting
└── README.md           # Project explanation and instructions
```

---

## Prerequisites

* Python 3.8+
* No external libraries required for basic functionality. (Optional: `python-magic` for extended detection)

---

## How to Run

1. Clone the repository:

```bash
git clone <repository_url>
cd file_type_identifier
```

2. Run the program:

```bash
python main.py
```

3. Input the path to a file or folder when prompted:

```
Enter file or folder path to analyze: /path/to/your/files
```

4. Output will display detected file types and optionally flag mismatched extensions:

```
example.jpg: Detected type -> JPEG
Warning: Extension 'png' does not match detected type 'JPEG'
```

---

## How It Works

1. Reads the first N bytes of the file (usually 4–8 bytes).
2. Compares the bytes against a predefined dictionary of **magic numbers**.
3. Returns the detected file type or 'Unknown' if no match is found.
4. Optional: compares detected type with the file extension for verification.

---

## Adding New File Types

1. Open `magic_dict.py`.
2. Add a new entry with the magic bytes as the key and file type as the value:

```python
MAGIC_NUMBERS[b'\x42\x4D'] = 'BMP'
```

3. Save and run `main.py` again.

---

## Testing

* Place test files with known file types in the `tests/` folder.
* Use `tests/test_cases.py` to run automated checks with `pytest` or `unittest`.

---

## Future Enhancements

* Detect nested file types (e.g., ZIP inside DOCX).
* Advanced verification by reading deeper into the file structure.
* GUI or web interface for easier use.
* Integration with security tools to flag suspicious files.

---

## License

This project is open-source and free to use, modify, and distribute.

---

## Author

Anas Ah
