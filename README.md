# Chat2Viz

Chat2Viz is a Streamlit application that allows users to upload a CSV file containing sales data, filter the data by typing a query with a month, and visualize key performance indicators (KPIs) and bar charts for products and sales.

## Features

- Upload a CSV file containing sales data.
- Extract the month from a user-typed query using regular expressions.
- Filter the sales data by month based on the query.
- Display KPIs for transactions, products, and total sales.
- Visualize the quantity ordered and sales for each product in bar charts.

## Requirements

- Python 3.6 or higher
- Streamlit
- Pandas
- Matplotlib

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/chat2viz.git
    cd chat2viz
    ```

2. Install the required packages:

    ```bash
    pip install streamlit pandas matplotlib
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Upload a CSV file containing sales data. The file should have the following columns:
    - `Order Date`: The date of the order.
    - `Order ID`: The unique identifier for the order.
    - `Product`: The name of the product.
    - `Quantity Ordered`: The quantity of the product ordered.
    - `Total`: The total sales amount.

3. Type a query in the input box to filter the data by month (e.g., "sales in January"). If no query is typed, all months will be selected by default.

4. View the KPIs for transactions, products, and total sales.

5. Visualize the quantity ordered and sales for each product in bar charts.

