# ============================================================
# MEDIA PREPARATION CALCULATOR
# ============================================================

import streamlit as st

# Standard preparation (grams per litre)
MEDIA = {
    "LB Broth": 25,
    "Nutrient Broth": 13,
    "Tryptic Soy Broth (TSB)": 30,
    "Brain Heart Infusion (BHI) Broth": 37,
    "MRS Broth": 55,
    "Sabouraud Dextrose Broth": 30
}


def show():

    st.header("🧫 Media Preparation Calculator")

    st.write(
        "Calculate the amount of dehydrated culture media required."
    )

    st.divider()

    medium = st.selectbox(
        "Select Culture Medium",
        list(MEDIA.keys())
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
            "Volume (mL)",
            min_value=1.0,
            value=500.0
        )

        volume_l = volume / 1000

    else:

        volume = st.number_input(
            "Volume (L)",
            min_value=0.1,
            value=1.0
        )

        volume_l = volume

    st.divider()

    if st.button("Calculate Media", use_container_width=True):

        grams = MEDIA[medium] * volume_l

        st.success("Calculation Completed")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Selected Medium",
                medium
            )

        with col2:

            st.metric(
                "Required Powder",
                f"{grams:.2f} g"
            )

        st.divider()

        st.info(
            f"""
Preparation Instructions

• Weigh **{grams:.2f} g** of **{medium}**.

• Dissolve in distilled water.

• Adjust the volume to **{volume} {unit}**.

• Sterilize by autoclaving at **121°C for 15 minutes** unless the manufacturer specifies otherwise.

• Cool before use.
"""
        )