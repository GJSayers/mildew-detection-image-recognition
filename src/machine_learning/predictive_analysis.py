import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_prob, pred_class):
    """
    Plot prediction probability results
    """

    prob_by_class= pd.DataFrame(
            data=[0,0],
            index={'Powdery Mildew': 0, 'Healthy': 1}.keys(),
            columns=['Probability']
        )
    prob_by_class.loc[pred_class] = pred_prob
    for x in prob_by_class.index.to_list():
        if x not in pred_class: prob_by_class.loc[x] = 1 - pred_prob
    prob_by_class = prob_per_class.round(3)
    prob_by_class['Diagnostic'] = prob_by_class.index
    
    fig = px.bar(
            prob_by_class,
            x = 'Diagnostic',
            y = prob_by_class['Probability'],
            range_y=[0,1],
            width=500, height=400,template='seaborn')
    st.plotly_chart(fig)



def resize_input_image(img, version):  
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    new_image = np.expand_dims(img_resized, axis=0)/255

    return new_image


def load_model_and_predict(new_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/mildew_detection_model.h5")

    pred_prob = model.predict(new_image)[0,0]

    target_map = {v: k for k, v in {'Powdery Mildew': 0, 'Healthy': 1}.items()}
    pred_class =  target_map[pred_prob > 0.5]  
    if pred_class == target_map[0]: pred_prob = 1 - pred_prob


    st.write(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}** with malaria.")
    
    return pred_prob, pred_class