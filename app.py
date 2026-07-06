# ============================================================
# IMPORT LIBRARIES
# ============================================================

import streamlit as st

from calculators import (
    molarity,
    normality,
    dilution,
    pbs,
    agar,
    media,
    pcr,
    dna,
    rna,
    dna_dilution,
    serial_dilution,
    unit_converter,
    molecular_weight
)

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="BioLab Calculator",
    page_icon="🧪",
    layout="wide"
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧪 BioLab Calculator")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🧪 Solution Preparation",
        "💧 Dilution",
        "🧬 Molecular Biology",
        "📏 Unit Converter",
        "⚗️ Molecular Weight",
        "ℹ️ About"
    ]
)

# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.title("🧪 BioLab Calculator")

    st.markdown("""
### Welcome!

BioLab Calculator is an all-in-one laboratory toolkit designed for biotechnology students, researchers, microbiologists, molecular biologists, and laboratory professionals.

Use the navigation menu on the left to access different laboratory calculators.
""")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Calculators", "12+")
    c2.metric("Categories", "6")
    c3.metric("Modules", "9")
    c4.metric("Version", "1.0")
    

    st.divider()

    st.subheader("Available Modules")

    

    col1, col2 = st.columns(2)

    with col1:

        st.success("🧪 Solution Preparation")

        st.write("""
- Molarity
- Normality
- PBS Preparation
- Agar Preparation
- Media Preparation
""")

        st.success("💧 Dilution")

        st.write("""
- Dilution Calculator
- Serial Dilution
""")

    with col2:

        st.success("🧬 Molecular Biology")

        st.write("""
- PCR Master Mix
- DNA Concentration
- RNA Concentration
- DNA Dilution
""")

        st.success("⚗️ Chemistry")

        st.write("""
- Molecular Weight Calculator
""")
        
    st.divider()

    st.subheader("🚀 Quick Access")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🧪 Solution Preparation", use_container_width=True):
            st.info("👈 Open '🧪 Solution Preparation' from the sidebar.")

    with col2:
        if st.button("💧 Dilution", use_container_width=True):
            st.info("👈 Open '💧 Dilution' from the sidebar.")

    with col3:
        if st.button("🧬 Molecular Biology", use_container_width=True):
            st.info("👈 Open '🧬 Molecular Biology' from the sidebar.")

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("📏 Unit Converter", use_container_width=True):
            st.info("👈 Open '📏 Unit Converter' from the sidebar.")

    with col5:
        if st.button("⚗️ Molecular Weight", use_container_width=True):
            st.info("👈 Open '⚗️ Molecular Weight' from the sidebar.")

    with col6:
        if st.button("ℹ️ About", use_container_width=True):
            st.info("👈 Open 'ℹ️ About' from the sidebar.")


    st.divider()

    st.info(
        "💡 Tip: Use the navigation menu in the left sidebar to access each calculator."
    )

# ============================================================
# SOLUTION PREPARATION
# ============================================================

elif page == "🧪 Solution Preparation":

    st.title("🧪 Solution Preparation")

    option = st.selectbox(
        "Choose Calculator",
        [
            "Molarity Calculator",
            "Normality Calculator",
            "PBS Preparation",
            "Agar Preparation",
            "Media Preparation"
        ]
    )

    if option == "Molarity Calculator":
        molarity.show()

    elif option == "Normality Calculator":
        normality.show()

    elif option == "PBS Preparation":
        pbs.show()

    elif option == "Agar Preparation":
        agar.show()

    elif option == "Media Preparation":
        media.show()

# ============================================================
# DILUTION
# ============================================================

elif page == "💧 Dilution":

    dilution.show()

# ============================================================
# MOLECULAR BIOLOGY
# ============================================================

elif page == "🧬 Molecular Biology":

    st.title("🧬 Molecular Biology")

    option = st.selectbox(
        "Choose Calculator",
        [
            "PCR Master Mix",
            "DNA Concentration",
            "RNA Concentration",
            "DNA Dilution",
            "Serial Dilution"
        ]
    )

    if option == "PCR Master Mix":
        pcr.show()

    elif option == "DNA Concentration":
        dna.show()

    elif option == "RNA Concentration":
        rna.show()

    elif option == "DNA Dilution":
        dna_dilution.show()

    elif option == "Serial Dilution":
        serial_dilution.show()

# ============================================================
# UNIT CONVERTER
# ============================================================

elif page == "📏 Unit Converter":

    unit_converter.show()

# ============================================================
# MOLECULAR WEIGHT
# ============================================================

elif page == "⚗️ Molecular Weight":

    molecular_weight.show()

# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About BioLab Calculator")

    st.markdown("""
### 🧬 BioLab Calculator

BioLab Calculator is an all-in-one laboratory toolkit developed for biotechnology students, researchers, microbiologists, molecular biologists, and laboratory professionals.

It provides reliable scientific calculators for solution preparation, molecular biology, laboratory unit conversions, and chemical calculations through a simple and interactive interface.
""")

    st.divider()

    st.subheader("✨ Features")

    st.markdown("""
- 🧪 Solution Preparation Calculators
- 💧 Dilution Calculator
- 🧬 PCR Master Mix Calculator
- 🧬 DNA Concentration Calculator
- 🧬 RNA Concentration Calculator
- 🧬 DNA Dilution Calculator
- 🧬 Serial Dilution Calculator
- 📏 Laboratory Unit Converter
- ⚗️ Molecular Weight Calculator
""")

    st.divider()

    st.subheader("🛠 Technologies Used")

    st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 📊 Pandas
- ⚗️ Molmass
""")

    st.divider()

    st.subheader("👩‍💻 Developer")

    st.markdown("""
**Name:** Harminder Kaur

**Project:** BioLab Calculator

**Version:** 1.0

**License:** MIT License
""")

    st.divider()

    st.info(
        "This application is intended for educational and research purposes. Always verify laboratory calculations before experimental use."
    )