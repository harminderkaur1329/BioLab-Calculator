# ============================================================
# SERIAL DILUTION CALCULATOR
# ============================================================

import streamlit as st
import pandas as pd


def show():

    st.header("🧪 Serial Dilution Calculator")

    st.write(
        "Generate a serial dilution protocol."
    )

    st.divider()

    dilution = st.selectbox(
        "Dilution Factor",
        [
            "1:10",
            "1:100",
            "1:1000"
        ]
    )

    tubes = st.number_input(
        "Number of Tubes",
        min_value=1,
        max_value=20,
        value=5
    )

    transfer = st.number_input(
        "Transfer Volume (µL)",
        min_value=1,
        value=100
    )

    st.divider()

    if st.button("Generate Dilution Table", use_container_width=True):

        if dilution == "1:10":
            diluent = transfer * 9
            factor = 10

        elif dilution == "1:100":
            diluent = transfer * 99
            factor = 100

        else:
            diluent = transfer * 999
            factor = 1000

        data = []

        cumulative = 1

        for i in range(1, tubes + 1):

            cumulative *= factor

            data.append(
                {
                    "Tube": i,
                    "Transfer (µL)": transfer,
                    "Diluent (µL)": diluent,
                    "Final Dilution": f"1:{cumulative}"
                }
            )

        df = pd.DataFrame(data)

        st.success("Serial Dilution Table")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            f"Add **{diluent} µL** diluent into each tube. "
            f"Transfer **{transfer} µL** sequentially from one tube to the next."
        )