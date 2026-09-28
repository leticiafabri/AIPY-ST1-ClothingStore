import pandas as pd
import openpyxl
import os


# CLOTHING STORE CATALOG

clothing_catalog = {
    1: {"name": "Basic T-Shirt", "price": 19.90},
    2: {"name": "Premium T-Shirt", "price": 29.90},
    3: {"name": "Jeans", "price": 59.90},
    4: {"name": "Jacket", "price": 89.90},
    5: {"name": "Hoodie", "price": 49.90},
    6: {"name": "Dress", "price": 69.90}
}

# FUNCTION: VIEW CLOTHING CATALOG

def view_catalog():
    print("\n--- CLOTHING STORE CATALOG ---")

    for code, item in clothing_catalog.items():
        print(f"{code} - {item['name']}: ${item['price']:.2f}")


# FUNCTION: DISPLAY ITEM OPTIONS

def display_item_options():
    print("\n--- AVAILABLE CLOTHING ITEMS ---")

    for code, item in clothing_catalog.items():
        print(f"{code} - {item['name']}")

# FUNCTION: CHECK PRICE

def check_price():
    print("\n--- CHECK ITEM PRICE ---")
    
    display_item_options()
    code = int(input("Enter the item code: "))

    if code in clothing_catalog:
        item = clothing_catalog[code]

        print(f"Item: {item['name']}")
        print(f"Price: ${item['price']:.2f}")
    else:
        print("Invalid item code. Please try again.")



# FUNCTION: GET DISCOUNT

def get_discount():
    print("\n--- GET DISCOUNT ---")

    display_item_options()
    code = int(input("Enter the item code: "))

    if code in clothing_catalog:
        quantity = int(input("Enter the quantity: "))

        if quantity > 0:
            item = clothing_catalog[code]
            price = item["price"]
            discount_rate = 0.10

            original_total = price * quantity
            discount_amount = original_total * discount_rate
            final_total = original_total - discount_amount

            print(f"Item: {item['name']}")
            print(f"Quantity: {quantity}")
            print(f"Original total: ${original_total:.2f}")
            print(f"Discount: ${discount_amount:.2f}")
            print(f"Final price: ${final_total:.2f}")
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Invalid item code. Please try again.")
        
        

# FUNCTION: RETURN ITEM

def return_item():
    print("\n--- RETURN ITEM ---")

    display_item_options()
    code = int(input("Enter the item code: "))

    if code in clothing_catalog:
        quantity = int(input("Enter the quantity to return: "))

        if quantity > 0:
            item = clothing_catalog[code]
            refund_amount = item["price"] * quantity

            print(f"Item: {item['name']}")
            print(f"Quantity returned: {quantity}")
            print(f"Refund amount: ${refund_amount:.2f}")
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Invalid item code. Please try again.")
        
        

# FUNCTION: EXCHANGE ITEM

def exchange_item():
    print("\n--- EXCHANGE ITEM ---")

    display_item_options()
    original_code = int(input("Enter the original item code: "))
    replacement_code = int(input("Enter the replacement item code: "))

    if original_code in clothing_catalog and replacement_code in clothing_catalog:
        quantity = int(input("Enter the quantity to exchange: "))

        if quantity > 0:
            original_item = clothing_catalog[original_code]
            replacement_item = clothing_catalog[replacement_code]

            original_total = original_item["price"] * quantity
            replacement_total = replacement_item["price"] * quantity

            difference = replacement_total - original_total

            print(f"Original item: {original_item['name']}")
            print(f"Replacement item: {replacement_item['name']}")
            print(f"Quantity: {quantity}")
            print(f"Original total: ${original_total:.2f}")
            print(f"Replacement total: ${replacement_total:.2f}")

            if difference > 0:
                print(f"Additional payment required: ${difference:.2f}")
            elif difference < 0:
                print(f"Refund amount: ${abs(difference):.2f}")
            else:
                print("No additional payment or refund is required.")
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Invalid item code. Please try again.")
 
 
# FUNCTION: READ DATA FILE       
def read_data_file(file_name):
    try:
        if not os.path.exists(file_name):
            print("Error: File not found.")
            return None

        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension == ".csv":
            df = pd.read_csv(file_name)

        elif file_extension == ".xlsx":
            df = pd.read_excel(file_name)

        else:
            print("Error: Please use a CSV or XLSX file.")
            return None

        print("File successfully loaded!")
        return df

    except Exception as e:
        print(f"Error reading file: {e}")
        return None 
    
          
def analyze_data_file():
    file_name = input("Enter the file name (e.g., sales.csv): ")

    df = read_data_file(file_name)

    if df is None:
        return

    print("\n--- DATA ANALYSIS ---")

    # Display the first five rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Display the number of rows and columns
    print("\nDataset dimensions:")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # Display column names and data types
    print("\nColumn information:")
    print(df.dtypes)

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Display statistics for numeric columns
    print("\nNumerical statistics:")
    print(df.describe())

    # Display the most frequent values in categorical columns
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:
        print(f"\nMost frequent values in '{column}':")
        print(df[column].value_counts().head(5))
        
# MAIN MENU

while True:
    print("\n===== CLOTHING STORE MENU =====")
    print("1 - Return an Item")
    print("2 - Exchange an Item")
    print("3 - Get a Discount")
    print("4 - Check Item Price")
    print("5 - View Clothing Catalog")
    print("6 - Exit")
    print("7. Analyze Sales Data")

    try:
        choice = int(input("Select an option (1-7): "))

        if choice == 1:
            return_item()

        elif choice == 2:
            exchange_item()

        elif choice == 3:
            get_discount()

        elif choice == 4:
            check_price()

        elif choice == 5:
            view_catalog()

        elif choice == 6:
            print("Thank you for visiting our Clothing Store!")
            break
        
        elif choice == 7:
            analyze_data_file()

        else:
            print("Invalid option. Please select a number between 1 and 6.")

    except ValueError:
        print("Invalid input. Please enter a number.")