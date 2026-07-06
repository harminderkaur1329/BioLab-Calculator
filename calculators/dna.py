# ============================================================
# DNA CONCENTRATION CALCULATOR
# ============================================================

import streamlit as st


def show():

    st.header("🧬 DNA Concentration Calculator")

    st.write(
        "Calculate DNA concentration using NanoDrop or spectrophotometer readings."
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

    if st.button("Calculate DNA Concentration", use_container_width=True):

        concentration = a260 * 50 * dilution

        st.success("Calculation Completed")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "DNA Concentration",
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

DNA Concentration = A260 × 50 × Dilution Factor

= {a260:.3f} × 50 × {dilution}

= **{concentration:.2f} ng/µL**
"""
        )

        if concentration < 20:

            st.warning("Low DNA concentration.")

        elif concentration < 100:

            st.success("Suitable DNA concentration for many PCR applications.")

        else:

            st.success("High DNA concentration.")