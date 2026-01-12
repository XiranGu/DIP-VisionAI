import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd
import plotly.express as px

# --- 页面基础配置 ---
st.set_page_config(page_title="VisionAI Hub - 智图工坊", layout="wide", page_icon="🖼️")

# --- 界面美化 (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #f8f9fa; border-radius: 4px; border: 1px solid #e0e0e0; }
    .stTabs [aria-selected="true"] { background-color: #1A237E; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 侧边栏导航 ---
st.sidebar.title("🖼️ 智图工坊 VisionAI Hub")
st.sidebar.markdown("---")
menu = st.sidebar.radio("教学流程导航", ["首页·全景概览", "课前·智算设计", "课中·智感互动", "课后·精准评价", "课外·创新拓展"])

# --- 模块 1: 首页 ---
if menu == "首页·全景概览":
    st.title("《数字图像处理》全流程智慧教学空间")
    st.info("💡 教学理念：AI赋能全链路 (BOPPPS) + 产教融合实战")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("核心模块说明")
        st.write("1. **智算设计**：AI分析学生画像，精准锚定教学起点。")
        st.write("2. **智感互动**：AI镜像实验室，实现算法逻辑实时推演。")
        st.write("3. **精准评价**：全过程数据采集，生成个人素质画像。")
        st.write("4. **创新拓展**：链接前沿科研与工业视觉案例。")
    with col2:
        # 基于报告图22的数据模拟达成度
        radar_df = pd.DataFrame(dict(r=[92, 88, 95, 85, 90],
                                   theta=['基础知识','算法实践','创新思维','工程素养','团队协作']))
        fig = px.line_polar(radar_df, r='r', theta='theta', line_close=True)
        st.plotly_chart(fig, use_container_width=True)

# --- 模块 2: 课前 (AI赋能学情预测) ---
elif menu == "课前·智算设计":
    st.header("🔍 课前学情监测与知识图谱")
    tab1, tab2 = st.tabs(["立体化课程图谱", "AI 预习诊断"])
    with tab1:
        st.write("点击节点查看知识点依赖关系（模拟知识图谱视图）")
        st.image("https://img.icons8.com/color/480/network.png", width=300) # 此处可替换为您报告中的图谱
    with tab2:
        st.markdown("### 📊 本周学情画像")
        st.warning("系统发现：35% 的同学对‘频域滤波’的基础数学概念理解较弱。")
        st.button("AI 自动优化本课导学案")

# --- 模块 3: 课中 (AI实验室 - 核心功能) ---
elif menu == "课中·智感互动":
    st.header("🧪 AI 镜像实验室")
    st.write("无需配置环境，在线运行 OpenCV 算法进行逻辑验证。")
    
    uploaded_file = st.file_uploader("请上传一张待处理图像", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        
        col_l, col_r = st.columns(2)
        with col_l:
            st.image(image, caption="原始图像", use_column_width=True)
            
        with col_r:
            algo = st.selectbox("选择算法算子", ["均值滤波", "Canny边缘检测", "灰度直方图均衡化"])
            
            if algo == "均值滤波":
                k = st.slider("核尺寸", 1, 31, 5, step=2)
                res = cv2.blur(img_array, (k, k))
            elif algo == "Canny边缘检测":
                t1 = st.slider("低阈值", 0, 255, 100)
                t2 = st.slider("高阈值", 0, 255, 200)
                res = cv2.Canny(img_array, t1, t2)
            elif algo == "灰度直方图均衡化":
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                res = cv2.equalizeHist(gray)
            
            st.image(res, caption="AI 实时处理结果", use_column_width=True)

# --- 模块 4: 课后 (AI 评价) ---
elif menu == "课后·精准评价":
    st.header("🤖 AI 专项辅导与评价")
    st.text_input("输入你的代码问题或算法困惑：")
    if st.button("AI 导师诊断"):
        st.success("根据你的描述，建议检查卷积核是否进行了归一化处理，防止溢出。")
    
    st.markdown("---")
    st.subheader("学生满意度分析词云")
    st.image("https://via.placeholder.com/600x200.png?text=AI+Generated+WordCloud", caption="基于真实评价生成的词云")

# --- 模块 5: 课外 ---
elif menu == "课外·创新拓展":
    st.header("🏗️ 产教融合与科研孵化")
    st.write("提供真实工业数据集与竞赛指导。")
    st.button("下载：工业缺陷检测数据集")
    st.button("查看：2025年蓝桥杯图像处理算法解析")