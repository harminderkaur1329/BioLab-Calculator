# ============================================================
# UNIT CONVERTER
# ============================================================

import streamlit as st


def show():

    st.header("📏 Laboratory Unit Converter")

    st.write(
        "Convert commonly used laboratory units."
    )

    st.divider()

    category = st.selectbox(
        "Select Category",
        [
            "Volume",
            "Mass",
            "Temperature",
            "Length",
            "Time",
            "Concentration"
        ]
    )

    # =========================================================
    # VOLUME
    # =========================================================

    if category == "Volume":

        units = {
            "µL": 0.001,
            "mL": 1,
            "L": 1000
        }

    # =========================================================
    # MASS
    # =========================================================

    elif category == "Mass":

        units = {
            "µg": 0.001,
            "mg": 1,
            "g": 1000,
            "kg": 1000000
        }

    # =========================================================
    # LENGTH
    # =========================================================

    elif category == "Length":

        units = {
            "mm": 0.1,
            "cm": 1,
            "m": 100
        }

    # =========================================================
    # TIME
    # =========================================================

    elif category == "Time":

        units = {
            "Second": 1,
            "Minute": 60,
            "Hour": 3600
        }

    # =========================================================
    # CONCENTRATION
    # =========================================================

    elif category == "Concentration":

        units = {
            "mg/mL": 1,
            "µg/mL": 0.001,
            "g/L": 1
        }

    # =========================================================
    # TEMPERATURE
    # =========================================================

    if category == "Temperature":

        value = st.number_input(
            "Enter Value",
            value=25.0
        )

        from_unit = st.selectbox(
            "From",
            ["°C", "°F", "K"]
        )

        to_unit = st.selectbox(
            "To",
            ["°C", "°F", "K"]
        )

        if st.button("Convert", use_container_width=True):

            if from_unit == to_unit:
                result = value

            elif from_unit == "°C" and to_unit == "°F":
                result = value * 9 / 5 + 32

            elif from_unit == "°F" and to_unit == "°C":
                result = (value - 32) * 5 / 9

            elif from_unit == "°C" and to_unit == "K":
                result = value + 273.15

            elif from_unit == "K" and to_unit == "°C":
                result = value - 273.15

            elif from_unit == "°F" and to_unit == "K":
                result = (value - 32) * 5 / 9 + 273.15

            else:
                result = (value - 273.15) * 9 / 5 + 32

            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

    else:

        value = st.number_input(
            "Enter Value",
            value=1.0
        )

        from_unit = st.selectbox(
            "From Unit",
            list(units.keys())
        )

        to_unit = st.selectbox(
            "To Unit",
            list(units.keys())
        )

        if st.button("Convert", use_container_width=True):

            base = value * units[from_unit]

            result = base / units[to_unit]

            st.success(
                f"{value} {from_unit} = {result:.4f} {to_unit}"
            )