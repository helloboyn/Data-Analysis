import pandas as pd

def remove_duplicates(input_file, output_file, column_name):
    try:
        # Read the Excel file
        data = pd.read_excel(input_file)

        # Print the column names for debugging
        print("Column names in the file:", data.columns)

        # Remove duplicate rows based on the specified column
        data_cleaned = data.drop_duplicates(subset=column_name, keep='first')

        # Save the cleaned data to a new Excel file
        data_cleaned.to_excel(output_file, index=False)

        print(f"Duplicates removed based on column '{column_name}'. Cleaned file saved as '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input and output file names
    input_file = "dupli.xlsx"
    output_file = "clean-out.xlsx"

    # Column to check for duplicates
    column_to_check = "Hindi"  # Ensure this matches exactly with the column name

    # Call the function
    remove_duplicates(input_file, output_file, column_to_check)
