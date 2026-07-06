# ============================================================
# AGAR PREPARATION CALCULATOR
# ============================================================

import streamlit as st

# Standard preparation (grams per litre)
AGAR_MEDIA = {
    "Nutrient Agar": 28,
    "LB Agar": 40,
    "MacConkey Agar": 52,
    "Mueller-Hinton Agar": 38,
    "Sabouraud Dextrose Agar": 65,
    "Blood Agar Base": 40,
    "Brain Heart Infusion Agar": 52
}


def show():

    st.header("🧫 Agar Preparation Calculator")

    st.write(
        "Calculate the amount of dehydrated agar medium required."
    )

    st.divider()

    medium = st.selectbox(
        "Select Agar Medium",
        list(AGAR_MEDIA.keys())
    )

    unit = st.selectbox(
        "Volume Unit",
        ["mL", "L"]
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

    if st.button("Calculate Agar", use_container_width=True):

        grams = AGAR_MEDIA[medium] * volume_l

        st.success("Calculation Completed")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Medium",
                medium
            )

        with col2:
            st.metric(
                "Required Powder",
                f"{grams:.2f} g"
            )

        st.info(
            f"Weigh **{grams:.2f} g** of **{medium}** "
            f"and prepare the final volume to **{volume} {unit}**."
        )

        st.warning(
            "After dissolving the medium, sterilize by autoclaving at "
            "121°C for 15 minutes unless otherwise specified by the manufacturer."
        )