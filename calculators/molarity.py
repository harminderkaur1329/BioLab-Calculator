# ============================================================
# MOLARITY CALCULATOR
# ============================================================

import streamlit as st


def show():

    st.header("🧪 Molarity Calculator")

    st.write(
        "Calculate the amount of solute required to prepare a solution of a desired molarity."
    )

    st.divider()

    molecular_weight = st.number_input(
        "Molecular Weight (g/mol)",
        min_value=0.0001,
        value=58.44,
        format="%.4f"
    )

    molarity = st.number_input(
        "Desired Molarity (M)",
        min_value=0.0001,
        value=1.0,
        format="%.4f"
    )

    unit = st.selectbox(
        "Volume Unit",
        ["mL", "L"]
    )

    if unit == "mL":
        volume = st.number_input(
            "Final Volume (mL)",
            min_value=1.0,
            value=1000.0
        )
        volume_l = volume / 1000

    else:
        volume = st.number_input(
            "Final Volume (L)",
            min_value=0.001,
            value=1.0
        )
        volume_l = volume

    st.divider()

    if st.button("Calculate Molarity", use_container_width=True):

        grams = molecular_weight * molarity * volume_l

        st.success("Calculation Completed")

        st.metric(
            "Required Solute",
            f"{grams:.4f} g"
        )

        st.info(
            f"Weigh **{grams:.4f} g** of solute and make the final volume up to **{volume} {unit}**."
        )

        