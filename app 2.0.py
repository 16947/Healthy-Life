import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['axes.unicode_minus']=False
sns.set_theme(style="white",font_scale=2.5)
plt.rcParams['font.sans-serif']=['Simhei']

st.set_page_config(page_title="刘欣茹的健康生活总结",page_icon=":rainbow:",layout="wide",initial_sidebar_state="auto")
st.title('Healthy Life:heart:')
st.markdown('<br>',unsafe_allow_html=True)
st.markdown('<br>',unsafe_allow_html=True)


add_selectbox = st.sidebar.selectbox(
    "统计项目",
    ("每日汇总", "大项汇总", "小项汇总")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "选择日期",
        ("最近三天", "最近七天", "最近一月")
    )

s=pd.read_csv(r"huizong.txt", sep='\t')
x=s.iloc[:,0]
y=s.iloc[:,1]
fig1= plt.figure()
#st.write(x)
plt.plot(x,y,linestyle = '-',linewidth = 2,color = 'steelblue',marker = 'o',markersize = 6,markeredgecolor='black',markerfacecolor='steelblue',label='完成情况')
plt.title('每日情况汇总')
plt.xlabel('时间')
plt.ylabel('完成情况')
plt.xticks(rotation = 0)#x轴标签倾斜60度
plt.legend(loc='best',frameon=False)#图例，显示label，去掉边框
st.pyplot(fig1)

a=pd.read_csv(r"xiaoxiang.txt", sep='\t')
labels =a.iloc[:,0]
sizes = a.iloc[:,1]
fig = plt.figure()
plt.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)#'%1.1f'：指小数点后保留一位有效数值；'%1.2f%%'保留两位小数点，增加百分号（%）;startangle=90则从y轴正方向画起
plt.axis('equal')#该行代码使饼图长宽相等
plt.title('完成情况占比', fontdict={'size':15})
#plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)#添加图例
st.pyplot(fig)








#s=pd.read_csv(r"huizong.txt", sep='\t')
#sns.lineplot(data=s)

#from streamlit.server.server import Server
# from streamlit.script_run_context import get_script_run_ctx as get_report_ctx
#from streamlit.scriptrunner import get_script_run_ctx as get_report_ctx

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
