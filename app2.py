import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import time



plt.rcParams['axes.unicode_minus']=False
sns.set_theme(style="white",font_scale=2.5)
plt.rcParams['font.sans-serif']=['Simhei']

st.set_page_config(page_title="刘欣茹的健康生活总结",page_icon=":rainbow:",layout="wide",initial_sidebar_state="auto")
st.title('Healthy Life:heart:')
st.markdown('<br>',unsafe_allow_html=True)
st.markdown('<br>',unsafe_allow_html=True)
#######################################

s=pd.read_csv(r"huizong.txt", sep='\t')

########################################
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


#####################################
st.title("")
st.title("")
st.title("分项统计")

bar1 = st.progress(s.iloc[-1,-1], text='汇总统计')
a=int(s.iloc[-1,-1]*100)


bar2 = st.progress(s.iloc[-1,1], text='早餐')
b=int(s.iloc[-1,-1]*100)
#for percent_complete in range(b):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='早餐')

bar3 = st.progress(s.iloc[-1,2], text='午餐')
c=int(s.iloc[-1,-1]*100)
#for percent_complete in range(c):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='午餐')
#
bar4 = st.progress(s.iloc[-1,3], text='晚餐')
d=int(s.iloc[-1,-1]*100)
#for percent_complete in range(d):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='晚餐')

bar5 = st.progress(s.iloc[-1,4], text='早起')
e=int(s.iloc[-1,-1]*100)
#for percent_complete in range(e):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='早起')

bar6 = st.progress(s.iloc[-1,5], text='早睡')
f=int(s.iloc[-1,-1]*100)
#for percent_complete in range(f):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='早睡')

bar7 = st.progress(s.iloc[-1,6], text='单词')
g=int(s.iloc[-1,-1]*100)
#for percent_complete in range(g):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='单词')

bar8 = st.progress(s.iloc[-1,7], text='阅读')
h=int(s.iloc[-1,-1]*100)
#for percent_complete in range(h):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='阅读')

bar9 = st.progress(s.iloc[-1,8], text='运动')
i=int(s.iloc[-1,-1]*100)
#for percent_complete in range(i):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='运动')
#
bar10 = st.progress(s.iloc[-1,9], text='摄入量')
j=int(s.iloc[-1,-1]*100)
#for percent_complete in range(j):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='摄入量')

bar11 = st.progress(s.iloc[-1,10], text='摄入时间')
k=int(s.iloc[-1,-1]*100)
#for percent_complete in range(k):
#    time.sleep(0.1)
#    bar1.progress(percent_complete + 1, text='摄入时间')


for percent_complete in range(a):
    time.sleep(0.1)
    bar1.progress(percent_complete + 1, text='汇总统计' )




#st.balloons()



################每日汇总###################
st.title("每日汇总")

x=s.iloc[0:-4,0]
y=s.iloc[0:-4,11]
#ax1 = plt.subplot(121) 
fig1= plt.figure(figsize=(8,6))
#st.write(x)
plt.plot(x,y,linestyle = '-',linewidth = 3,color = 'steelblue',marker = 'o',markersize = 10,markeredgecolor='black',markerfacecolor='steelblue')
#,label='完成情况'
#plt.title('Daily summary')
plt.xlabel('日期', labelpad=20,fontproperties='simhei',fontsize=30)
plt.ylabel('完成情况',rotation =90, labelpad=20,fontproperties='simhei',fontsize=30)        #,linespacing=2
plt.xticks(rotation = 0,fontproperties = 'Times New Roman', fontsize=15)#x轴标签倾斜60度
plt.yticks(fontproperties = 'Times New Roman', size =15)
#plt.legend(loc='best',frameon=False)#图例，显示label，去掉边框
st.pyplot(fig1)




###############小项###################
#ax2 = plt.subplot(122)
st.title("")
st.title("")
st.title("每日汇总")
a=pd.read_csv(r"xiaoxiang.txt", sep='\t')
labels =a.iloc[:,0]
sizes = a.iloc[:,1]
fig = plt.figure()

patches,l_text,p_text=plt.pie(sizes,  labels=labels, autopct='%1.1f%%',labeldistance = 1.1, textprops={'color':'black', 'size':10, 'weight':'bold'},
        shadow=False, startangle=90)#'%1.1f'：指小数点后保留一位有效数值；'%1.2f%%'保留两位小数点，增加百分号（%）;startangle=90则从y轴正方向画起

plt.axis('equal')#该行代码使饼图长宽相等
#plt.title('完成情况占比', fontdict={'size':15})
#plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)#添加图例
st.pyplot(fig)
