import numpy as np
import pandas as pd
import streamlit as st

if st.toggle("Show data"):
    num_rows = st.number_input("Num rows", 0, 500000, 100000, 1000)
    # create a random dataframe
    df = pd.DataFrame(
        np.random.randn(num_rows, 20), columns=("col %d" % i for i in range(20))
    )
    st.dataframe(df)


@st.experimental_dialog("Simple Dialog")
def simple_dialog():
    st.write("Hello again!")
    st.text_input("Enter something!", key="dialog2-input")

    if st.button("Submit"):
        st.rerun()


if st.button("Open Dialog"):
    simple_dialog()

st.write(st.session_state.get("dialog2-input"))
