## Simple Price Calculator App
import streamlit as st
st.title('Price Calculator')
price = st.number_input("Enter Product Price", min_value=1) ## Product Price Input

## Discount Slider
discount = st.slider("Select Discount (%)", 0,50)
# st.button('Calculate')

## Button
if st.button("Calculate"):
    ## Calculate Discount Amount

    discount_price = price * discount/100
    final_price = price - discount_price

    st.success(f"Final Price: ₹{final_price:.2f}")

    table_data = [
        ["Item", "Value"],
        ["Original Price", price],
        ["Discount (%)", f"{discount}%"],
        ["Final Price", final_price]
    ]
    st.table(table_data)