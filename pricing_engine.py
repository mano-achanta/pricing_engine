import pandas as pd
import os

def load_csv_files(products_path, sales_path):
    """Load and validate products and sales CSV files."""
    try:
        products_df = pd.read_csv(products_path)
        sales_df = pd.read_csv(sales_path)
        
        # Validate required columns
        required_product_cols = ['sku', 'name', 'current_price', 'cost_price', 'stock']
        required_sales_cols = ['sku', 'quantity_sold']
        
        if not all(col in products_df.columns for col in required_product_cols):
            raise ValueError("Missing required columns in products.csv")
        if not all(col in sales_df.columns for col in required_sales_cols):
            raise ValueError("Missing required columns in sales.csv")
            
        return products_df, sales_df
    except Exception as e:
        print(f"Error loading CSV files: {str(e)}")
        raise

def apply_pricing_rules(products_df, sales_df):
    """Apply pricing rules to compute new prices."""
    # Merge dataframes to get all relevant info
    merged_df = products_df.merge(sales_df, on='sku', how='left')
    # Fill NaN quantity_sold with 0 for products with no sales
    merged_df['quantity_sold'] = merged_df['quantity_sold'].fillna(0)
    
    # Initialize new_price column with current_price
    merged_df['new_price'] = merged_df['current_price']
    
    for index, row in merged_df.iterrows():
        current_price = row['current_price']
        stock = row['stock']
        quantity_sold = row['quantity_sold']
        cost_price = row['cost_price']
        
        # Rule 1: Low Stock, High Demand
        if stock < 20 and quantity_sold > 30:
            merged_df.at[index, 'new_price'] = current_price * 1.15
        # Rule 2: Dead Stock
        elif stock > 200 and quantity_sold == 0:
            merged_df.at[index, 'new_price'] = current_price * 0.7
        # Rule 3: Overstocked Inventory
        elif stock > 100 and quantity_sold < 20:
            merged_df.at[index, 'new_price'] = current_price * 0.9
            
        # Rule 4: Minimum Profit Constraint
        min_price = cost_price * 1.2
        if merged_df.at[index, 'new_price'] < min_price:
            merged_df.at[index, 'new_price'] = min_price
            
        # Round to 2 decimal places
        merged_df.at[index, 'new_price'] = round(merged_df.at[index, 'new_price'], 2)
    
    return merged_df

def generate_output_csv(merged_df, output_path):
    """Generate output CSV with required columns and units."""
    output_df = merged_df[['sku', 'current_price', 'new_price']].copy()
    output_df.columns = ['sku', 'old_price (USD)', 'new_price (USD)']
    output_df.to_csv(output_path, index=False)
    print(f"Output CSV generated at: {output_path}")

def main():
    # Define file paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    products_path = os.path.join(base_dir, 'data', 'products.csv')
    sales_path = os.path.join(base_dir, 'data', 'sales.csv')
    output_path = os.path.join(base_dir, 'output', 'updated_prices.csv')
    
    # Ensure output directory exists
    os.makedirs(os.path.join(base_dir, 'output'), exist_ok=True)
    
    # Load data
    products_df, sales_df = load_csv_files(products_path, sales_path)
    
    # Apply pricing rules
    result_df = apply_pricing_rules(products_df, sales_df)
    
    # Generate output
    generate_output_csv(result_df, output_path)

if __name__ == "__main__":
    main()