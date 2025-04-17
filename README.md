Pricing Engine Solution
Overview
This project implements a pricing engine that adjusts product prices based on inventory levels and sales performance, following the specified rules for the Thrd Coding Challenge.
Project Structure
pricing_engine/
├── data/
│   ├── products.csv        # Input: Product catalog
│   └── sales.csv          # Input: Sales data
├── output/
│   └── updated_prices.csv  # Output: Updated prices
├── pricing_engine.py      # Main Python script
├── README.md              # Project documentation
└── requirements.txt       # Dependencies

Setup Instructions

Clone the Repository:
git clone <repository-url>
cd pricing_engine


Create Virtual Environment (Optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Place Input Files:

Ensure products.csv and sales.csv are in the data/ directory.
The provided CSV files are already included in the data/ directory.


Run the Script:
python pricing_engine.py


Check Output:

The output file updated_prices.csv will be generated in the output/ directory.



Dependencies

Python 3.8+
pandas

Implementation Details

File Loading: Uses pandas to read CSV files with validation for required columns.
Pricing Rules: Applied in specified order (Low Stock, Dead Stock, Overstocked, Minimum Profit).
Output: Generates updated_prices.csv with columns sku, old_price (USD), new_price (USD).
Error Handling: Includes checks for file existence and column validation.
Rounding: All prices are rounded to 2 decimal places as specified.

Assumptions

Input CSV files are well-formed and contain the specified columns.
Prices are in USD (unit explicitly mentioned in output).
Missing sales data for a product implies zero sales (handled by filling NaN with 0).

Example Output
Based on the provided input files:
sku,old_price (USD),new_price (USD)
A123,649.99,600.0
B456,699.0,803.85
C789,999.0,899.1

Running in VS Code

Open the project folder in VS Code.
Ensure Python extension is installed.
Select the Python interpreter (from virtual environment if created).
Right-click pricing_engine.py and select "Run Python File in Terminal".
View the output in the output/updated_prices.csv file.

Submission

Zip the entire pricing_engine/ folder.
Submit via the provided Google Form link before the deadline (19th Apr, 2025, 11:55 PM).

Contact
For any clarification, please reach out via the challenge submission platform.
