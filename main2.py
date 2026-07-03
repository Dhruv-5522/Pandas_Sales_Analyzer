import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        self.current_figure = None 
        print("[System] SalesDataAnalyzer Instance Created.")

    def __del__(self):
        print("[System] SalesDataAnalyzer Instance Destroyed.")

    def load_data(self, file_path):
        try:
            if not os.path.exists(file_path):
                print(f"Error: File not found at path '{file_path}'")
                return False
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading file: {e}")
            return False

    def explore_data(self):
        if self.data is None:
            print("Please load the dataset first (Option 1).")
            return
        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to main menu")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    print("\n--- First 5 Rows ---")
                    print(self.data.head())
                elif choice == 2:
                    print("\n--- Last 5 Rows ---")
                    print(self.data.tail())
                elif choice == 3:
                    print("\n--- Column Names ---")
                    print(list(self.data.columns))
                elif choice == 4:
                    print("\n--- Data Types ---")
                    print(self.data.dtypes)
                elif choice == 5:
                    print("\n--- Basic Info ---")
                    print(self.data.info())
                elif choice == 6:
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

    def clean_data(self):
        if self.data is None:
            print("Please load the dataset first (Option 1).")
            return
        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to main menu")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    missing_rows = self.data[self.data.isnull().any(axis=1)]
                    if missing_rows.empty:
                        print("\nNo missing values found in the dataset!")
                    else:
                        print("\n--- Rows with Missing Values ---")
                        print(missing_rows)
                elif choice == 2:
                    numeric_cols = self.data.select_dtypes(include=[np.number]).columns
                    self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
                    print("Missing values filled with column mean successfully!")
                elif choice == 3:
                    self.data.dropna(inplace=True)
                    print("Rows with missing values dropped successfully!")
                elif choice == 4:
                    val = input("Enter the specific value to replace missing data: ")
                    self.data.fillna(val, inplace=True)
                    print(f"Missing values replaced with '{val}' successfully!")
                elif choice == 5:
                    break
            except ValueError:
                print("Please enter a valid number.")

    def mathematical_operations(self):
        if self.data is None:
            print("Please load the dataset first (Option 1).")
            return
        print("\n== Perform DataFrame & Array Operations ==")
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            print("No numeric columns available.")
            return
        print(f"Available numeric columns: {list(numeric_cols)}")
        col_name = input("Select a column to convert to NumPy array: ")
        if col_name not in self.data.columns:
            print("Invalid column name.")
            return
        arr = self.data[col_name].to_numpy()
        print(f"\nNumPy Array Created! First 3 elements: {arr[:3]}")
        print("Array multiplied by 2:", arr * 2)

    def split_data(self):
        if self.data is None: return
        # તમારા ડેટામાં 'branch' અથવા 'city' કોલમ છે તેનાથી સ્પ્લિટ થશે
        col = 'branch' if 'branch' in self.data.columns else self.data.columns[1]
        print(f"\n--- Splitting Data by '{col}' ---")
        for name, group in self.data.groupby(col):
            print(f"Group {name}: {len(group)} rows")

    def search_sort_filter(self):
        if self.data is None: return
        # તમારા ડેટામાં 'revenue' કોલમ છે, તેના પર ફિલ્ટર લાગશે
        if 'revenue' in self.data.columns:
            print("\n--- Filtering Data (Revenue > 500) ---")
            print(self.data[self.data['revenue'] > 500].head())

    def aggregate_functions(self):
        if self.data is None: return
        if 'branch' in self.data.columns and 'revenue' in self.data.columns:
            print("\n--- Aggregation: Total Revenue by Branch ---")
            print(self.data.groupby('branch')['revenue'].sum().reset_index())

    def statistical_analysis(self):
        if self.data is None:
            print("Please load the dataset first (Option 1).")
            return
        print("\n== Generate Descriptive Statistics ==")
        print(self.data.describe())
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("\n--- Standard Deviation ---")
            print(self.data[numeric_cols].std())
            print("\n--- Variance ---")
            print(self.data[numeric_cols].var())

    def create_pivot_table(self):
        if self.data is None: return
        if 'branch' in self.data.columns and 'customer_type' in self.data.columns and 'revenue' in self.data.columns:
            print("\n--- Pivot Table (Total Revenue) ---")
            print(self.data.pivot_table(values='revenue', index='branch', columns='customer_type', aggfunc='sum'))

    def visualize_data(self):
        if self.data is None:
            print("Please load the dataset first (Option 1).")
            return
        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart\n5. Histogram\n6. Stack Plot\n7. Back")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 7: break
                
                x_col = input("Enter x-axis column name: ")
                if x_col not in self.data.columns:
                    print("Column doesn't exist.")
                    continue

                plt.close('all')
                fig, ax = plt.subplots(figsize=(8, 5))
                self.current_figure = fig

                if choice in [1, 2, 3]:
                    y_col = input("Enter y-axis column name: ")
                    if y_col not in self.data.columns: continue
                    
                    if choice == 1:
                        sns.barplot(data=self.data, x=x_col, y=y_col, ax=ax)
                    elif choice == 2:
                        sns.lineplot(data=self.data, x=x_col, y=y_col, ax=ax)
                    elif choice == 3:
                        sns.scatterplot(data=self.data, x=x_col, y=y_col, ax=ax)
                elif choice == 4:
                    counts = self.data[x_col].value_counts()
                    ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
                elif choice == 5:
                    sns.histplot(data=self.data, x=x_col, ax=ax, kde=True)
                elif choice == 6:
                    print("Stack plot requires structured sequence data. Showing hist instead.")
                    sns.histplot(data=self.data, x=x_col, ax=ax)

                plt.show()
                print("Plot displayed successfully!")
            except Exception as e:
                print(f"Error: {e}")

    def save_visualization(self):
        if self.current_figure is None:
            print("No plot to save!")
            return
        file_name = input("Enter file name (e.g., plot.png): ")
        self.current_figure.savefig(file_name, bbox_inches='tight')
        print(f"Saved successfully as {file_name}!")

def main():
    analyzer = SalesDataAnalyzer()
    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset\n2. Explore Data\n3. Perform DataFrame Operations\n4. Handle Missing Data")
        print("5. Generate Descriptive Statistics\n6. Data Visualization\n7. Save Visualization\n8. Exit")
        print("===========================================================")
        choice = input("Enter your choice: ")
        if choice == '1':
            path = input("Enter CSV path: ")
            analyzer.load_data(path)
        elif choice == '2': analyzer.explore_data()
        elif choice == '3':
            analyzer.mathematical_operations()
            analyzer.split_data()
            analyzer.search_sort_filter()
            analyzer.aggregate_functions()
            analyzer.create_pivot_table()
        elif choice == '4': analyzer.clean_data()
        elif choice == '5': analyzer.statistical_analysis()
        elif choice == '6': analyzer.visualize_data()
        elif choice == '7': analyzer.save_visualization()
        elif choice == '8':
            print("\nExiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()