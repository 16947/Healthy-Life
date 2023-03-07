import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts

from streamlit.server.server import Server
# from streamlit.script_run_context import get_script_run_ctx as get_report_ctx
from streamlit.scriptrunner import get_script_run_ctx as get_report_ctx

import graphviz
import pydeck as pdk
import altair as alt
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from pyecharts.charts import *
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

from PIL import Image
from io import BytesIO


def main():
    st.set_page_config(page_title="七里香还是稻香",page_icon=":rainbow:",layout="wide",initial_sidebar_state="auto")
    st.title('七里香还是稻香:heart:')
    st.markdown('<br>',unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True)
    charts_mapping={
        'Line':'line_chart','Bar':'bar_chart','Area':'area_chart','Hist':'pyplot','Altair':'altair_chart',
        'Map':'map','Distplot':'plotly_chart','Pdk':'pydeck_chart','Graphviz':'graphviz_chart','PyEchart':''
    }
    if 'first_visit' not in st.session_state:
        st.session_state.first_visit=True
    else:
        st.session_state.first_visit=False
    # 初始化全局配置
    if st.session_state.first_visit:
        # 在这里可以定义任意多个全局变量，方便程序进行调用
        st.session_state.date_time=datetime.datetime.now() + datetime.timedelta(hours=8) # Streamlit Cloud的时区是UTC，加8小时即北京时间
        st.session_state.random_chart_index=random.choice(range(len(charts_mapping)))
        st.session_state.my_random=MyRandom(random.randint(1,1000000))
        st.session_state.city_mapping,st.session_state.random_city_index=get_city_mapping()
        # st.session_state.random_city_index=random.choice(range(len(st.session_state.city_mapping)))
        st.balloons()
        st.snow()