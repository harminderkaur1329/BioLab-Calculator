import streamlit as st

def show():
    st.header("🧪 Normality Calculator")

    st.write(
        "Calculate the amount of solute required to prepare a solution of a desired normality."
    )

    equivalent_weight = st.number_input(
        "Equivalent Weight (g/eq)",
        min_value=0.0001,
        value=49.04,
        format="%.4f"
    )

    normality = st.number_input(
        "Desired Normality (N)",
        min_value=0.0001,
        value=1.0,
        format="%.4f"
    )

    volume = st.number_input(
        "Final Volume (L)",
        min_value=0.0001,
        value=1.0,
        format="%.4f"
    )

    if st.button("Calculate Normality", use_container_width=True):

        grams = equivalent_weight * normality * volume

        st.success(f"Required Solute = **{grams:.4f} g**")

        st.info(
            f"Prepare {volume:.2f} L of a {normality:.2f} N solution "
            f"using {grams:.4f} g of solute."
        )