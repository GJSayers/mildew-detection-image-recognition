import streamlit as st


def project_hypothesis_content():
    """Contents of Project Hypothesis"""
    st.write("### Project Hypothesis")
    st.info(
        "1. We suggest that images of Cherry leaves with powdery mildew will have enough differences compared to those without the disease in order to train the model with an image dataset. \n"
        "2. A company analysis showed that it takes 30 minutes to evaluate a Cherry tree manually for signs of powdery Mildew. We propose that using image recognition will produce a vast time-benefit for the company and ensure that the detection of mildew is scalable. \n"
        "3. Since the sample dataset provided contains images classified into infected vs uninfected, we suggest that binary classification will be the best way to determine the difference between infected and uninftected leaves."
    )