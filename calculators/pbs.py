# ============================================================
# PBS PREPARATION CALCULATOR
# ============================================================

import streamlit as st


def show():

    st.header("🧂 PBS Preparation Calculator")

    st.write(
        "Calculate the amount of chemicals required to prepare Phosphate Buffered Saline (PBS)."
    )

    st.divider()

    strength = st.selectbox(
        "PBS Strength",
        [
            "1X PBS",
            "10X PBS"
        ]
    )

    unit = st.selectbox(
        "Volume Unit",
        [
            "mL",
            "L"
        ]
    )

    if unit == "mL":

        volume = st.number_input(
            "Final Volume (mL)",
            min_value=1.0,
            value=500.0
        )

        volume_l = volume / 1000

    else:

        volume = st.number_input(
            "Final Volume (L)",
            min_value=0.1,
            value=1.0
        )

        volume_l = volume

    st.divider()

    if st.button("Calculate PBS", use_container_width=True):

        if strength == "1X PBS":

            nacl = 8.00 * volume_l
            kcl = 0.20 * volume_l
            na2hpo4 = 1.44 * volume_l
            kh2po4 = 0.24 * volume_l

        else:

            nacl = 80.00 * volume_l
            kcl = 2.00 * volume_l
            na2hpo4 = 14.40 * volume_l
            kh2po4 = 2.40 * volume_l

        st.success("PBS Recipe")

        col1, col2 = st.columns(2)

        with col1:

            st.metric("NaCl", f"{nacl:.2f} g")
            st.metric("KCl", f"{kcl:.2f} g")

        with col2:

            st.metric("Na₂HPO₄", f"{na2hpo4:.2f} g")
            st.metric("KH₂PO₄", f"{kh2po4:.2f} g")

        st.divider()

        st.info(
            f"""
Preparation Instructions

• Dissolve all salts in approximately 80% of the final volume of distilled water.

• Adjust the pH to **7.4**.

• Add distilled water to reach the final volume (**{volume} {unit}**).

• Sterilize by autoclaving or membrane filtration if required.
"""
        )