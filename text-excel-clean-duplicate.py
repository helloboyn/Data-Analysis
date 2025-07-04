# Let clean bitext pair!
import pandas as pd
import re
from tqdm import tqdm
from openpyxl.utils.exceptions import IllegalCharacterError

# Clean function to remove illegal characters
def clean_text(text):
    if isinstance(text, str):
        # Remove illegal characters that Excel can't handle
        return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', text)
    return text

# File paths
source_path = 'source_path.txt'
target_path = 'source_path.txt'

# Read lines
with open(source_path, 'r', encoding='utf-8') as f:
    source_lines = [clean_text(line.strip()) for line in f]

with open(target_path, 'r', encoding='utf-8') as f:
    target_lines = [clean_text(line.strip()) for line in f]

# Check alignment
assert len(source_lines) == len(target_lines), "❌ Files are not aligned!"

# Create DataFrame
df = pd.DataFrame({'Source': source_lines, 'Target': target_lines})

# Excel row limit
max_rows = 1000000
total_parts = (len(df) + max_rows - 1) // max_rows

# Save in chunks with progress bar
for i in tqdm(range(0, len(df), max_rows), desc="💾 Saving Excel parts", unit="part", total=total_parts):
    df_part = df.iloc[i:i+max_rows]

    # Extra safety: clean entire DataFrame again before saving
    df_part = df_part.applymap(clean_text)

    # Save to Excel
    df_part.to_excel(f'un-dupli-bitext-part{i//max_rows + 1}.xlsx', index=False)

print("✅ All Excel files saved successfully.")

#make with love helloboyn



