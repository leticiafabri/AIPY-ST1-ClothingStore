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
