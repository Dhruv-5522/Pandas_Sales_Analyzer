# Pandas Analyzer & Data Visualization Tool

This is a comprehensive Sales Data Analysis and Visualization tool built using Python. The entire project is developed using Object-Oriented Programming (OOP) principles, where all core functionalities are cleanly encapsulated within the `SalesDataAnalyzer` class. 

I have created a fully interactive, menu-driven console interface that allows users to seamlessly load datasets, process data, and generate insightful plots on the fly.

---

## 🚀 Key Features Implemented

1. **Data Loading & Exploration:** Built-in exception handling to load any standard `.csv` dataset. Users can quickly inspect the data structure using options like `head()`, `tail()`, `info()`, and check data types or column names.
2. **Missing Data Cleaning:** Features a dedicated sub-menu to detect empty rows or missing values. Users can choose to either drop those rows or fill them using column mean values.
3. **NumPy Array Operations:** Converts specific DataFrame columns into NumPy arrays to demonstrate core concepts like indexing, slicing, and element-wise mathematical operations.
4. **Data Manipulation:** Implements advanced Pandas functionalities including data splitting (groupby), search/filter mechanisms, total aggregations, and customized pivot tables.
5. **Statistical Analysis:** Automatically generates comprehensive descriptive statistics (`describe()`) alongside manual calculations for Standard Deviation and Variance.
6. **Dynamic Visualization:** An interactive visualization sub-menu powered by Matplotlib and Seaborn. Users can type in custom X and Y axis column names to generate Bar plots, Line plots, Scatter plots, Pie charts, and Histograms.
7. **Save Feature:** Includes functionality to save the most recently generated plot directly to the local folder with a custom filename.

---

## 🛠️ Tech Stack Used

* **Language:** Python 3
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, OS

---

## 💻 How to Run the Project

1. Clone or download this project folder.
2. Place your dataset file (e.g., `supermarket_sales.csv`) inside the same directory.
3. Open your terminal in VS Code and run the following command:

```bash
python main2.py# Pandas_Sales_Analyzer
