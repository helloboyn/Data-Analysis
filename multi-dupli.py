import pandas as pd

def remove_duplicates_from_sheets(input_file, output_file, column_name):
    try:
        # Read all sheets into a dictionary of DataFrames
        sheets = pd.read_excel(input_file, sheet_name=None)

        # Dictionary to store cleaned DataFrames
        cleaned_sheets = {}

        # Iterate through each sheet
        for sheet_name, data in sheets.items():
            print(f"Processing sheet: {sheet_name}")

            # Check if the column exists in the current sheet
            if column_name in data.columns:
                # Remove duplicate rows based on the specified column
                cleaned_data = data.drop_duplicates(subset=column_name, keep='first')
                print(f"Duplicates removed from sheet '{sheet_name}' based on column '{column_name}'.")
            else:
                # If column doesn't exist, keep the sheet as is
                cleaned_data = data
                print(f"Column '{column_name}' not found in sheet '{sheet_name}', skipping duplicate removal.")

            # Add the cleaned DataFrame to the dictionary
            cleaned_sheets[sheet_name] = cleaned_data

        # Write the cleaned DataFrames to a new Excel file
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for sheet_name, cleaned_data in cleaned_sheets.items():
                cleaned_data.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"Cleaned file saved as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input and output file names
    input_file = "Clean-NCERT.xlsx"  # Original file with all sheets
    output_file = "Clean-NCERT-Out.xlsx"  # File to save cleaned data

    # Column to check for duplicates
    column_to_check = "Hindi"  # Ensure this matches exactly with the column name

    # Call the function
    remove_duplicates_from_sheets(input_file, output_file, column_to_check)
