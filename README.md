# AIPY-ST1-ClothingStore

# Clothing Store Management System

A Python project developed for a business problem-solving class. The program simulates a clothing retail store and allows users to perform basic operations related to clothing exchanges, returns, discounts, price inquiries, and data analysis.

## Business Problem

Clothing store employees need a simple way to handle customer requests, calculate refunds and exchange price differences, provide accurate product prices, and inspect business data.

This project uses a predefined clothing catalog so that users select items by their product codes instead of entering prices manually.

It also includes a data analysis feature that allows users to import CSV and Excel files, prepare datasets, and explore their contents using Python and Pandas.

## Features

The program includes an interactive menu with the following options:

1. **Return an Item** — Calculates the refund amount based on the item's catalog price and the quantity returned.
2. **Exchange an Item** — Compares the total price of the original items with the replacement items and determines whether an additional payment or refund is required.
3. **Get a Discount** — Applies a predefined 10% discount and calculates the final price.
4. **Check Item Price** — Displays the price of a selected clothing item.
5. **View Clothing Catalog** — Displays all available items, their codes, and prices.
6. **Exit** — Closes the program.
7. **Analyze Data File** — Reads a CSV or Excel file, prepares the dataset, and displays descriptive information and statistics.

### Data Analysis Features

The data analysis functionality includes:

- **File Reading:** Imports CSV (`.csv`) and Excel (`.xlsx`) files into a Pandas DataFrame.
- **File Validation:** Checks whether the file format is supported and whether the file exists.
- **Data Cleaning:** Removes completely empty rows and duplicate records and trims extra spaces from text values.
- **Dataset Overview:** Displays the first five rows, number of rows and columns, and column names.
- **Missing Value Analysis:** Counts missing values in each column.
- **Numerical Statistics:** Displays descriptive statistics for numerical columns.
- **Categorical Analysis:** Displays the five most frequent values in each categorical column.
- **Record Conversion:** Converts the DataFrame into a list of dictionaries and displays the total number of records.

## Clothing Catalog

| Code | Item | Price |
|---:|---|---:|
| 1 | Basic T-Shirt | $19.90 |
| 2 | Premium T-Shirt | $29.90 |
| 3 | Jeans | $59.90 |
| 4 | Jacket | $89.90 |
| 5 | Hoodie | $49.90 |
| 6 | Dress | $69.90 |

Prices are fictional and used for demonstration purposes.

## Technologies

- **Python** — Main programming language.
- **Jupyter Notebook** — Development and execution environment.
- **Pandas** — DataFrame creation, file reading, data cleaning, and data analysis.
- **OpenPyXL** — Excel file support.
- **OS module** — File existence and extension checks.
- **Python dictionaries** — Store the clothing catalog.
- **Lists and list of dictionaries** — Organize and process data.
- **Functions, loops, conditionals, and exception handling** — Implement business operations and input validation.

## Requirements

The project requires Python and the following libraries:

- `pandas`
- `openpyxl`

Install the dependencies using:

```bash
pip install pandas openpyxl
```
## How to Run

1. Clone or download this repository.
2. Install the required dependencies.
3. Choose one of the following ways to run the project:

### Option 1 — Python Script

1. Open the project folder in VS Code or another Python-compatible editor.
2. Run `ClothingStoreMenu.py`.
3. Select an option by entering its number and follow the prompts.

### Option 2 — Jupyter Notebook

1. Open `Code.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab.
2. Run the notebook cells in order, starting with the clothing catalog and function definitions.
3. Run the main menu cell.
4. Select an option by entering its number and follow the prompts.

## How to Analyze a Data File

1. Place the CSV or XLSX file in the project directory.
2. Run the program and select Option 7 — Analyze Data File.
3. Enter the file name, including its extension (for example, `sales.csv`).
4. The application loads the file into a DataFrame, prepares the data, and displays the analysis results in the terminal.

### Supported File Formats

- `.csv`
- `.xlsx`

Files must be available in the directory from which the program is running, unless a valid file path is provided.

## Business Rules and Assumptions

- Product prices are predefined in the clothing catalog.
- Items are selected using their numeric product codes.
- The discount rate is fixed at 10%.
- Returns are assumed to be eligible for a full refund at the catalog price.
- Exchanges compare the catalog prices of the original and replacement items.
- The quantity must be greater than zero.
- The data analysis feature accepts CSV and XLSX files only.
- Completely empty rows and duplicate records are removed during data preparation.
- Leading and trailing spaces are removed from text values.
- The data analysis feature provides descriptive information and does not modify the original input file.
- The program is a classroom simulation and does not process real payments or store transaction records.

## Project Structure

The repository contains the following project files:

- `ClothingStoreMenu.py` — Python script containing the application logic and main menu.
- `Code.ipynb` — Jupyter Notebook version of the project.
- `sales.csv` — Example dataset for data analysis.
- `test_data.csv` — Dataset used to test file reading and data preparation.
- `README.md` — Project documentation.

## Error Handling and Validation

The application includes basic validation and error handling:

- Invalid menu selections are rejected.
- Non-numeric values are handled by the integer input validation function.
- Invalid product codes are rejected.
- Quantities must be greater than zero for business operations.
- Unsupported file extensions are rejected.
- Missing files generate an error message.
- File reading errors are handled without intentionally terminating the application.

## Data Analysis Output

When a valid file is loaded, the application displays:

1. Data preparation results, including the number of rows before and after cleaning.
2. The total number of records.
3. The first five rows of the cleaned dataset.
4. Dataset dimensions and column names.
5. Missing values per column.
6. Descriptive statistics for numerical columns.
7. The most frequent values in categorical columns.

## Project Goal

This project demonstrates how Python can be used to solve a basic retail business problem while introducing data preparation and exploratory data analysis using Pandas.
