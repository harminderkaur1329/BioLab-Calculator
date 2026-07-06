# ============================================================
# PCR MASTER MIX CALCULATOR
# ============================================================

import streamlit as st
import pandas as pd


def show():

    st.header("🧬 PCR Master Mix Calculator")

    st.write(
        "Calculate reagent volumes required for preparing a PCR Master Mix."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        reactions = st.number_input(
            "Number of Reactions",
            min_value=1,
            value=10
        )

        reaction_volume = st.selectbox(
            "Reaction Volume (µL)",
            [10, 20, 25, 50]
        )

        template = st.number_input(
            "Template DNA / reaction (µL)",
            min_value=0.0,
            value=1.0,
            step=0.1
        )

    with col2:

        buffer = st.number_input(
            "10X Buffer / reaction (µL)",
            value=2.5,
            step=0.1
        )

        dntp = st.number_input(
            "dNTP Mix / reaction (µL)",
            value=0.5,
            step=0.1
        )

        forward = st.number_input(
            "Forward Primer / reaction (µL)",
            value=0.5,
            step=0.1
        )

        reverse = st.number_input(
            "Reverse Primer / reaction (µL)",
            value=0.5,
            step=0.1
        )

        taq = st.number_input(
            "Taq Polymerase / reaction (µL)",
            value=0.2,
            step=0.1
        )

    extra = st.checkbox(
        "Include 10% Extra Master Mix",
        value=True
    )

    st.divider()

    if st.button("Calculate PCR Mix", use_container_width=True):

        total_reactions = reactions * 1.1 if extra else reactions

        water = (
            reaction_volume
            - (
                buffer
                + dntp
                + forward
                + reverse
                + taq
                + template
            )
        )

        reagents = {
            "Reagent": [
                "Nuclease-Free Water",
                "10X Buffer",
                "dNTP Mix",
                "Forward Primer",
                "Reverse Primer",
                "Taq Polymerase",
                "Template DNA"
            ],

            "Volume / Reaction (µL)": [
                water,
                buffer,
                dntp,
                forward,
                reverse,
                taq,
                template
            ],

            "Total Volume (µL)": [
                water * total_reactions,
                buffer * total_reactions,
                dntp * total_reactions,
                forward * total_reactions,
                reverse * total_reactions,
                taq * total_reactions,
                template * reactions
            ]
        }

        df = pd.DataFrame(reagents)

        st.success("PCR Master Mix")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.metric(
            "Total Master Mix",
            f"{reaction_volume * total_reactions:.1f} µL"
        )

        st.info(
            "Prepare the master mix without template DNA if your laboratory protocol requires adding DNA separately."
        )