# ============================================================
# DNA DILUTION CALCULATOR
# ============================================================

import streamlit as st


def show():

    st.header("🧬 DNA Dilution Calculator")

    st.write(
        "Calculate the amount of stock DNA and nuclease-free water required."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        stock = st.number_input(
            "Stock DNA Concentration (ng/µL)",
            min_value=0.01,
            value=100.0,
            step=1.0
        )

        desired = st.number_input(
            "Desired DNA Concentration (ng/µL)",
            min_value=0.01,
            value=20.0,
            step=1.0
        )

    with col2:

        final_volume = st.number_input(
            "Final Volume (µL)",
            min_value=1.0,
            value=50.0,
            step=1.0
        )

    st.divider()

    if st.button("Calculate DNA Dilution", use_container_width=True):

        if desired >= stock:

            st.error(
                "Desired concentration must be less than the stock concentration."
            )

        else:

            stock_volume = (desired * final_volume) / stock

            water = final_volume - stock_volume

            st.success("Calculation Completed")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Stock DNA Required",
                    f"{stock_volume:.2f} µL"
                )

            with c2:

                st.metric(
                    "Water Required",
                    f"{water:.2f} µL"
                )

            st.divider()

            st.info(
                f"""
Preparation Instructions

• Pipette **{stock_volume:.2f} µL** of stock DNA.

• Add **{water:.2f} µL** of nuclease-free water.

• Final volume = **{final_volume:.2f} µL**

• Final concentration = **{desired:.2f} ng/µL**
"""
            )