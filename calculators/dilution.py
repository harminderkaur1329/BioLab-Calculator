# ============================================================
# Dilution Calculator
# Formula: C1V1 = C2V2
# ============================================================

import streamlit as st


def show():

    st.header("💧 Dilution Calculator")

    st.write(
        "Calculate the amount of stock solution and diluent required."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        c1 = st.number_input(
            "Stock Concentration (C₁)",
            min_value=0.0001,
            value=5.0,
            format="%.4f"
        )

        c2 = st.number_input(
            "Desired Concentration (C₂)",
            min_value=0.0001,
            value=1.0,
            format="%.4f"
        )

    with col2:

        v2 = st.number_input(
            "Final Volume (mL)",
            min_value=0.1,
            value=100.0,
            format="%.2f"
        )

    st.divider()

    if st.button("Calculate Dilution", use_container_width=True):

        if c2 >= c1:

            st.error(
                "Desired concentration must be less than stock concentration."
            )

        else:

            v1 = (c2 * v2) / c1

            diluent = v2 - v1

            st.success("Calculation Completed")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Stock Solution Required",
                    f"{v1:.2f} mL"
                )

            with col2:
                st.metric(
                    "Diluent Required",
                    f"{diluent:.2f} mL"
                )

            st.info(
                f"Mix **{v1:.2f} mL** of stock solution with "
                f"**{diluent:.2f} mL** of diluent "
                f"to prepare **{v2:.2f} mL** solution."
            )