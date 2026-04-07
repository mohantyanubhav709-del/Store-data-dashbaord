import pandas as pd

df = pd.read_csv("store.csv", encoding='latin1')

new_markdown_cell = {
 "cell_type": "markdown",
 "metadata": {},
 "source": [
  "## Data Cleaning\n",
  "We will perform the following data cleaning steps:\n",
  "1. Convert `Order Date` and `Ship Date` into datetime formats.\n",
  "2. Fill missing values in `Product Base Margin` with the column average.\n",
  "3. Drop the redundant `Row ID` column.\n",
  "4. Drop any duplicate rows."
 ]
}

new_code_cell = {
 "cell_type": "code",
 "execution_count": None,
 "metadata": {},
 "outputs": [],
 "source": [
  "# 1. Convert Dates\n",
  "df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, format='mixed')\n",
  "df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, format='mixed')\n",
  "\n",
  "# 2. Handle Missing values\n",
  "df['Product Base Margin'] = df['Product Base Margin'].fillna(df['Product Base Margin'].mean())\n",
  "\n",
  "# 3. Drop Redundant col\n",
  "if 'Row ID' in df.columns:\n",
  "    df.drop('Row ID', axis=1, inplace=True)\n",
  "\n",
  "# 4. Check for duplicates\n",
  "df.drop_duplicates(inplace=True)\n",
  "\n",
  "print('Data has been cleaned!')\n",
  "display(df.info())"
 ]
}

nb['cells'].append(new_markdown_cell)
nb['cells'].append(new_code_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
