
## 📁 Project Structure

```
pricing_engine/
├── data/
│   ├── products.csv        # Input: Product catalog
│   └── sales.csv           # Input: Sales data
├── output/
│   └── updated_prices.csv  # Output: Updated prices
├── pricing_engine.py       # Main Python script
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd pricing_engine
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Place Input Files

Ensure `products.csv` and `sales.csv` are located inside the `data/` directory.  
➡️ These files are already provided in the project.

---

## 🚀 Run the Script

```bash
python pricing_engine.py
```

---

## 📦 Check Output

After running the script, the updated prices will be saved in:
```
output/updated_prices.csv
```

---

## 🧩 Dependencies

- Python 3.8+
- pandas

---

## 🛠 Implementation Details

- **File Loading**: Uses `pandas` to read CSV files with validation for required columns.
- **Pricing Rules**:
  - Low Stock
  - Dead Stock
  - Overstocked
  - Minimum Profit
- **Output**: CSV file with columns `sku`, `old_price (USD)`, and `new_price (USD)`.
- **Error Handling**: File and column checks are included.
- **Rounding**: Prices are rounded to 2 decimal places.

---

## 📌 Assumptions

- Input CSVs are well-formed and contain required fields.
- All prices are in **USD** (explicitly stated in output).
- Products with missing sales data are assumed to have **zero sales**.

---

## 📋 Example Output

Sample output in `updated_prices.csv`:

```
sku,old_price (USD),new_price (USD)
A123,649.99,600.0
B456,699.0,803.85
C789,999.0,899.1
```

---

## 🖥 Running in VS Code

1. Open the folder in VS Code.
2. Ensure the **Python extension** is installed.
3. Select the appropriate **Python interpreter**.
4. Right-click `pricing_engine.py` and choose **"Run Python File in Terminal"**.
5. Check the output file: `output/updated_prices.csv`.

---
