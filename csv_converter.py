import pandas as pd

# Read the Excel file
excel_file = pd.read_excel('game.xlsx')

# Convert to CSV
csv_file = 'game.csv'
excel_file.to_csv(csv_file, index=False, encoding='utf-8')

print(f"Excel file '{excel_file}' has been converted to CSV successfully!")
