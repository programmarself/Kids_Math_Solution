import streamlit as st

st.title("Kids Math Solution")

# Main prompt for user to select an option
options = ["Tables", "Forward Counting", "Backward Counting"]
pro = st.selectbox("WHAT WOULD YOU LIKE TO ATTEMPT?", options)

# Option 1: Tables
if pro == "Tables":
    table_of = st.number_input("Enter Table Number", min_value=1, step=1)
    start_from = st.number_input("Enter Start Number", min_value=1, step=1)
    end_from = st.number_input("Enter End Number", min_value=1, step=1)

    if st.button("Generate Table"):
        st.write(f"### Table of {table_of}")
        for i in range(start_from, end_from + 1):
            st.write(f"{table_of} x {i} = {table_of * i}")

# Option 2: Forward Counting
elif pro == "Forward Counting":
    f_start_count = st.number_input("Enter Start Number:", min_value=1, step=1)
    f_end_count = st.number_input("Enter End Number:", min_value=f_start_count, step=1)

    if st.button("Generate Forward Counting"):
        st.write(f"### Forward Counting from {f_start_count} to {f_end_count}")
        for i in range(f_start_count, f_end_count + 1):
            st.write(i, end=" ")

# Option 3: Backward Counting
elif pro == "Backward Counting":
    start_counting = st.number_input("Enter Start Number:", min_value=1, step=1)
    end_counting = st.number_input("Enter End Number:", min_value=1, step=1)

    if start_counting >= end_counting and st.button("Generate Backward Counting"):
        st.write(f"### Backward Counting from {start_counting} to {end_counting}")
        for i in range(start_counting, end_counting - 1, -1):
            st.write(i, end=" ")
    else:
        st.write("Start number should be greater than or equal to the end number.")
