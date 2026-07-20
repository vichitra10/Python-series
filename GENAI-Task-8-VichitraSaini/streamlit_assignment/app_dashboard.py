## Mini Dashboard
import streamlit as st
st.title("Dashboard")
st.write("Simple Sales Dashboard")
months = st.selectbox("Selects Month",["Januarary","February","March","April"])
sales = {"Januarary":1200, "February":1500, "March":900, "April": 2000}
 
## Display selected month's sales

st.metric("Sales" , sales[months]) 

## Display Bar Chart
st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))
