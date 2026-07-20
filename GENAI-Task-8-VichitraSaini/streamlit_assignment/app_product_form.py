## Product Form 
import streamlit as st
st.title('Mini SideBar Project')

product_name =  st.sidebar.text_input('Product Name')
category = st.sidebar.selectbox('Select Categroy', ["Electronics","Clothing","Books","Groceries","Sports"])

price = st.sidebar.number_input("Enter Product Price",min_value=1)


## Sidebar Button
if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully !")
    st.write("## Product Details")
    st.write(f"Product Name: {product_name}")
    st.write(f"Product Category: {category}")
    st.write(f"Product Price:  {price}")