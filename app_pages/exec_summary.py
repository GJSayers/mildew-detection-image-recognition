import streamlit as st


def exec_summary_content():
    """Contents of Exec Summary"""
    st.write("### Executive Summary")
    st.info(
        f"* Powdery Mildew is a disease infecting herbaceous and woody plants, and can result "
        f"in a low fruit yield in the case of Cherry Trees.\n"
        f"* The current process is manual verification if a given cherry tree contains powdery"
        f"mildew.\n" 
        f"* An employee spends around 30 minutes in each tree, taking a few samples of"
        f"tree leaves and verifying visually if the leaf tree is healthy or has powdery" f"mildew.\n"
        f"* According to the [Conneticut Portal](https://portal.ct.gov/CAES/Fact-Sheets/Plant-Pathology/Powdery-Mildew): Powdery mildews are easily recognized by "
        f"the white, powdery growth of the fungus on infected portions of the plant host. \n"
        f"* The powdery appearance results from the superficial growth of the fungus as" f"thread-like strands (hyphae) over the plant surface and the production of chains of"
        f"spores (conidia). Colonies vary in appearance from fluffy and white to sparse and gray."
    )