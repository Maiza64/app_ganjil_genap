import streamlit as st

st.header('Define Number Type Apps', divider='rainbow')
st.write('ini adalah aplikasi untuk menentukan bilangan genap atau bilangan ganjil')
st.write('English or Spanish:snake:')

# Input for the first number
number1 = st.number_input("Insert the first number", value=0)
st.write("The first number is", number1)

# Determine if the first number is even or odd
if number1 % 2 == 0:
    st.write("The first number is even bilangan genap")
else:
    st.write("The first number is odd bilangan ganjil")

# Input for the second number
number2 = st.number_input("Insert the second number", value=0)
st.write("The second number is", number2)

# Determine if the second number is even or odd
if number2 % 2 == 0:
    st.write("The second number is even bilangan genap")
else:
    st.write("The second number is odd bilangan ganjil")

# Calculate the result of multiplication
result = number1 * number2
st.write("The result of multiplication is", result)

# Determine if the result is even or odd
if result % 2 == 0:
    st.write("The result is even bilangan genap")
else:
    st.write("The result is odd bilangan ganjil")
