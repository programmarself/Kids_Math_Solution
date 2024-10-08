import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 36px;
        color: #2C3E50;
        text-align: center;
        font-weight: bold;
        padding: 10px;
    }
    .section-header {
        font-size: 24px;
        color: #34495E;
        text-align: center;
        padding: 5px;
    }
    .instructions {
        font-size: 16px;
        color: #2980B9;
        text-align: left;
        padding: 5px;
    }
    .footer {
        font-size: 12px;
        text-align: center;
        color: #BDC3C7;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page layout
st.markdown("<div class='main-header'>Kids Math Solution</div>", unsafe_allow_html=True)
st.write("Welcome to the Kids Math Solution! Choose an activity and start learning.")

# Sidebar or main prompt for options
options = ["Tables", "Forward Counting", "Backward Counting"]
pro = st.sidebar.selectbox("Choose Activity", options)

# Information box to guide user
st.info("This app helps kids practice basic math operations like multiplication tables, forward counting, and backward counting.")

# Option 1: Tables
if pro == "Tables":
    st.markdown("<div class='section-header'>Tables Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='instructions'>Enter a number to generate its multiplication table.</div>", unsafe_allow_html=True)
    
    table_of = st.number_input("Enter Table Number", min_value=1, step=1)
    start_from = st.number_input("Enter Start Number", min_value=1, step=1)
    end_from = st.number_input("Enter End Number", min_value=1, step=1)
    
    if st.button("Generate Table"):
        st.write(f"### Table of {table_of}")
        table_result = ""
        for i in range(start_from, end_from + 1):
            table_result += f"{table_of} x {i} = {table_of * i}\n"
        st.text(table_result)

# Option 2: Forward Counting
elif pro == "Forward Counting":
    st.markdown("<div class='section-header'>Forward Counting</div>", unsafe_allow_html=True)
    st.markdown("<div class='instructions'>Enter the start and end numbers for forward counting.</div>", unsafe_allow_html=True)
    
    f_start_count = st.number_input("Enter Start Number:", min_value=1, step=1)
    f_end_count = st.number_input("Enter End Number:", min_value=f_start_count, step=1)
    
    if st.button("Generate Forward Counting"):
        st.write(f"### Forward Counting from {f_start_count} to {f_end_count}")
        count_result = ""
        for i in range(f_start_count, f_end_count + 1):
            count_result += f"{i} "
        st.text(count_result)

# Option 3: Backward Counting
elif pro == "Backward Counting":
    st.markdown("<div class='section-header'>Backward Counting</div>", unsafe_allow_html=True)
    st.markdown("<div class='instructions'>Enter the start and end numbers for backward counting.</div>", unsafe_allow_html=True)
    
    start_counting = st.number_input("Enter Start Number:", min_value=1, step=1)
    end_counting = st.number_input("Enter End Number:", min_value=1, step=1)
    
    if start_counting >= end_counting and st.button("Generate Backward Counting"):
        st.write(f"### Backward Counting from {start_counting} to {end_counting}")
        count_result = ""
        for i in range(start_counting, end_counting - 1, -1):
            count_result += f"{i} "
        st.text(count_result)
    else:
        st.warning("Start number should be greater than or equal to the end number.")

# Footer for branding
st.markdown("<div class='footer'>Developed by: Your Name | Kids Math Solution © 2024</div>", unsafe_allow_html=True)
