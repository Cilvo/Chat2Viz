import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

st.set_page_config(layout="wide")
st.title('Chat2Viz')

def check_sequence(sentence, sequence):
    pattern = re.escape(sequence)  # Escape special characters in the sequence
    match = re.search(pattern, sentence)
    
    if match:
        return True
    else:
        return False
    
def extract_month_with_regex(sentence):
        if check_sequence(sentence, 'sale'):
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            pattern = r'\b(?:' + '|'.join(months) + r')\b'
            
            match = re.search(pattern, sentence, re.IGNORECASE)
            if match:
                return match.group(0)
            else:
                return None

file = st.file_uploader(label = 'Upload the file', type = 'csv')

if file:
    
    #"---"
    df = pd.read_csv(file)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    # Extract the month from each datetime value
    df['month'] = df['Order Date'].dt.strftime('%B')

    # Get the list of unique months
    list_of_months = [month for month in df['month'].unique()]
    

    text = st.text_input(label = 'Type the query ')
    if text:
        month_text = extract_month_with_regex(text)
        if month_text:
            df = df[df['month'] == month_text]
            st.write(f"Sales of {month_text}")
            month_selected = st.sidebar.multiselect(label = 'Months', options= list_of_months , default= [month_text])
    
    else:
        
        month_selected = st.sidebar.multiselect(label = 'Months', options= list_of_months , default= list_of_months)
    df = df[df['month'].isin(month_selected)]
  
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label = 'Transactions', value = str(round(df['Order ID'].nunique()/1000, 2))+'K')
    kpi2.metric(label = 'Product', value = df['Product'].nunique())
    kpi3.metric(label = 'Total Sales', value = str(round(df['Total'].sum()/1000000, 2))+'M')

    plt1, plt2 = st.columns(2)

    with plt1:
        grouped_product = df.groupby('Product')['Quantity Ordered'].sum()
        plt.bar(grouped_product.index, grouped_product.values)
        plt.xlabel('Product')
        plt.ylabel('Quantity Ordered')
        plt.ylim([0, 35000])
        plt.xticks(rotation= 90)
        st.pyplot(plt)

    with plt2:
        grouped_sales = df.groupby('Product')['Total'].sum()
        plt.bar(grouped_sales.index, grouped_sales.values)
        plt.xlabel('Product')
        plt.ylabel('Sales')
        plt.xticks(rotation= 90)
        plt.ylim([0, 9e6])
        st.pyplot(plt)

    # st.sidebar.multiselect(label = 'Columns', options= df.columns.tolist() , default= df.columns.tolist())

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

st.set_page_config(layout="wide")
st.title('Chat2Viz')

def check_sequence(sentence, sequence):
    pattern = re.escape(sequence)  # Escape special characters in the sequence
    match = re.search(pattern, sentence)
    
    if match:
        return True
    else:
        return False
    
def extract_month_with_regex(sentence):
        if check_sequence(sentence, 'sale'):
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            pattern = r'\b(?:' + '|'.join(months) + r')\b'
            
            match = re.search(pattern, sentence, re.IGNORECASE)
            if match:
                return match.group(0)
            else:
                return None

file = st.file_uploader(label = 'Upload the file', type = 'csv')

if file:
    
    #"---"
    df = pd.read_csv(file)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    # Extract the month from each datetime value
    df['month'] = df['Order Date'].dt.strftime('%B')

    # Get the list of unique months
    list_of_months = [month for month in df['month'].unique()]
    

    text = st.text_input(label = 'Type the query ')
    if text:
        month_text = extract_month_with_regex(text)
        if month_text:
            df = df[df['month'] == month_text]
            st.write(f"Sales of {month_text}")
            month_selected = st.sidebar.multiselect(label = 'Months', options= list_of_months , default= [month_text])
    
    else:
        
        month_selected = st.sidebar.multiselect(label = 'Months', options= list_of_months , default= list_of_months)
    df = df[df['month'].isin(month_selected)]
  
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label = 'Transactions', value = str(round(df['Order ID'].nunique()/1000, 2))+'K')
    kpi2.metric(label = 'Product', value = df['Product'].nunique())
    kpi3.metric(label = 'Total Sales', value = str(round(df['Total'].sum()/1000000, 2))+'M')

    plt1, plt2 = st.columns(2)

    with plt1:
        grouped_product = df.groupby('Product')['Quantity Ordered'].sum()
        plt.bar(grouped_product.index, grouped_product.values)
        plt.xlabel('Product')
        plt.ylabel('Quantity Ordered')
        plt.ylim([0, 35000])
        plt.xticks(rotation= 90)
        st.pyplot(plt)

    with plt2:
        grouped_sales = df.groupby('Product')['Total'].sum()
        plt.bar(grouped_sales.index, grouped_sales.values)
        plt.xlabel('Product')
        plt.ylabel('Sales')
        plt.xticks(rotation= 90)
        plt.ylim([0, 9e6])
        st.pyplot(plt)

    # st.sidebar.multiselect(label = 'Columns', options= df.columns.tolist() , default= df.columns.tolist())

