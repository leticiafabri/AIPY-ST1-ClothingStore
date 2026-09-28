# AIPY-ST1-ClothingStore

# Clothing Store Management System

A simple Python project developed for a business problem-solving class. The program simulates a clothing retail store and helps users perform basic operations related to clothing exchanges, returns, discounts, and price inquiries.

## Business Problem

Clothing store employees need a simple way to handle customer requests, calculate refunds and exchange price differences, and provide accurate product prices.

This project uses a predefined clothing catalog so that users select items by their product codes instead of entering prices manually.

## Features

The program includes an interactive menu with the following options:

1. **Return an Item** — Calculates the refund amount based on the item's catalog price and the quantity returned.
2. **Exchange an Item** — Compares the total price of the original items with the replacement items and determines whether an additional payment or refund is required.
3. **Get a Discount** — Applies a predefined 10% discount and calculates the final price.
4. **Check Item Price** — Displays the price of a selected clothing item.
5. **View Clothing Catalog** — Displays all available items, their codes, and prices.
6. **Exit** — Closes the program.

The menu includes basic input validation for invalid menu selections. The catalog is displayed before users are asked to enter item codes.

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

- Python
- Jupyter Notebook
- Python dictionaries
- `input()` and `print()`
- Functions, loops, conditionals, and basic exception handling

## How to Run

1. Clone or download this repository.
2. Open the `.ipynb` notebook in Jupyter Notebook, JupyterLab, or Google Colab.
3. Run the notebook cells in order, starting with the clothing catalog and function definitions.
4. Run the main menu cell.
5. Select an option by entering its number and follow the prompts.

## Business Rules and Assumptions

- Product prices are predefined in the clothing catalog.
- Items are selected using their numeric product codes.
- The discount rate is fixed at 10%.
- Returns are assumed to be eligible for a full refund at the catalog price.
- Exchanges compare the catalog prices of the original and replacement items.
- The quantity must be greater than zero.
- The program is a classroom simulation and does not process real payments or store transaction records.

## Project Goal

The goal is to apply fundamental Python concepts to a practical business scenario by creating a small, interactive solution that performs calculations and displays clear results.

---

*Created as part of a class project on AI-assisted Python for business problem solving.*
