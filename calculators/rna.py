# ============================================================
# RNA CONCENTRATION CALCULATOR
# ============================================================

import streamlit as st


def show():

    st.header("🧬 RNA Concentration Calculator")

    st.write(
        "Calculate RNA concentration using NanoDrop or spectrophotometer readings."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        a260 = st.number_input(
            "A260 Absorbance",
            min_value=0.000,
            value=1.000,
            format="%.3f"
        )

    with col2:

        dilution = st.number_input(
            "Dilution Factor",
            min_value=1,
            value=1
        )

    st.divider()

    if st.button("Calculate RNA Concentration", use_container_width=True):

        concentration = a260 * 40 * dilution

        st.success("Calculation Completed")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "RNA Concentration",
                f"{concentration:.2f} ng/µL"
            )

        with c2:

            st.metric(
                "Equivalent",
                f"{concentration:.2f} µg/mL"
            )

        st.divider()

        st.info(
            f"""
Formula Used

RNA Concentration = A260 × 40 × Dilution Factor

= {a260:.3f} × 40 × {dilution}

= **{concentration:.2f} ng/µL**
"""
        )

        if concentration < 20:
            st.warning("Low RNA concentration.")

        elif concentration < 100:
            st.success("Suitable RNA concentration for downstream applications.")

        else:
            st.success("High RNA concentration.")