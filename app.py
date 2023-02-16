import streamlit as st
from app_pages.dashboard import DashBoard

from app_pages.exec_summary import exec_summary_content
from app_pages.leaf_comparison import leaf_comparison_content
from app_pages.mildew_detector import mildew_detector_content
from app_pages.ml_metrics import ml_metrics_content
from app_pages.project_hypothesis import project_hypothesis_content

app = DashBoard(app_name="Mildew Detection in Cherry Leaves")

                
app.add_page("Executive Summary", exec_summary_content)
app.add_page("Leaf Comparison Vizualizer", leaf_comparison_content)
app.add_page("Mildew Detection", mildew_detector_content)
app.add_page("ML Metrics", ml_metrics_content)
app.add_page("Project Hypothesis", project_hypothesis_content)

app.run()
