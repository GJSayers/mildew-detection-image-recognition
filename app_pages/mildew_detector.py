import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )


def mildew_detector_content():
    """
    Contents of Mildew Detector
    """
    st.write("### Mildew Detector")
    st.info(
        f"* The client is interested in conducting a study to visually differentiate a healthy"
        f"cherry leaf from one with powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
        )

    st.write(
        f"* You can download a set of healthy and uninfected cells for live prediction. "
        f"You can download the images from [here](https://www.kaggle.com/ccodeinstitute/cherry-leaves)"
        )

    st.write("---")

    images_buffer = st.file_uploader('Upload Cherry Leaf image samples. You may select more than one.',
                                        type='png',accept_multiple_files=True)
   
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf Sample Image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_prob, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_prob, pred_class)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)

