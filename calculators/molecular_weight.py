# ============================================================
# MOLECULAR WEIGHT CALCULATOR
# ============================================================

import streamlit as st
from molmass import Formula


def show():

    st.header("⚗️ Molecular Weight Calculator")

    st.write(
        "Calculate the molecular weight of a chemical compound."
    )

    st.divider()

    formula = st.text_input(
        "Chemical Formula",
        placeholder="Examples: NaCl, H2SO4, C6H12O6, CaCl2"
    )

    st.divider()

    if st.button("Calculate Molecular Weight", use_container_width=True):

        if not formula.strip():

            st.warning("Please enter a chemical formula.")

        else:

            try:

                compound = Formula(formula)

                st.success("Calculation Completed")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Input Formula",
                        formula
                    )

                with col2:
                    st.metric(
                        "Molecular Weight",
                        f"{compound.mass:.4f} g/mol"
                    )

                st.divider()

                st.subheader("Compound Information")

                st.write(f"**Hill Formula:** {compound.formula}")

                st.write(f"**Average Molecular Mass:** {compound.mass:.4f} g/mol")

                st.info(
                    "The molecular weight is calculated using standard atomic masses from the molmass library."
                )

            except Exception as e:

                st.error("Invalid chemical formula.")

                st.code(str(e))