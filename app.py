import streamlit as st
import cv2
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image
import time

# --- 1. 全局配置与美化 ---
st.set_page_config(page_title="DIP Intelligence Nexus", layout="wide", page_icon="🧠")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .module-box { border: 1px solid #30363d; padding: 20px; border-radius: 10px; background: #161b22; margin-bottom: 20px; }
    .ai-badge { background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%); color: black; padding: 2px 8px; border-radius: 10px; font-size: 12px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- 2. 侧边栏：角色切换与导航 ---
with st.sidebar:
    st.title("🛡️ Nexus 导航中心")
    role = st.toggle("教师管理模式", value=False)
    st.markdown("---")
    if role:
        menu = st.radio("教师空间", ["备课助手", "课堂监控", "评价看板", "教研辅助"])
    else:
        menu = st.radio("学习空间", ["知识图谱", "AI实验室", "作业中心", "竞赛/资料"])

# --- 3. 核心逻辑实现 ---

# 模块一：课前设计 (教师端示例)
if role and menu == "备课助手":
    st.header("📝 AI 智能备课助手 <span class='ai-badge'>AI赋能</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("课程大纲智能生成")
        target = st.text_input("输入本节教学目标", "掌握空域直方图均衡化数学原理及OpenCV实现")
        if st.button("生成大纲 & 素材建议"):
            with st.status("AI 正在检索知识图谱..."):
                time.sleep(1)
                st.write("✅ **大纲已生成**：1. 概率密度函数(PDF)回顾 2. 累积分布函数(CDF)变换 3. 离散映射实现")
                st.write("📌 **素材推荐**：检测到您需要展示对比效果，已从库中调用‘经典灰度图像集’。")
    with col2:
        st.subheader("PPT 框架预览")
        st.code("# Slide 1: Introduction\n# Slide 2: Mathematical Foundation\n# Slide 3: Code Demo", language="markdown")

# 模块二：课中互动 (学生端：算法演示器)
elif not role and menu == "AI实验室":
    st.header("🧪 算法演示与在线实验 <span class='ai-badge'>GPU加速</span>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["参数调优可视化", "Jupyter 代码实验"])
    
    with tab1:
        uploaded_file = st.file_uploader("上传实验图像", type=["jpg", "png"])
        if uploaded_file:
            img = Image.open(uploaded_file)
            img_np = np.array(img)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c1:
                algo_type = st.selectbox("选择算法", ["高斯滤波", "Canny边缘检测", "阈值分割"])
                if algo_type == "高斯滤波":
                    k = st.slider("核尺寸 (ksize)", 1, 31, 5, 2)
                    sigma = st.slider("标准差 (sigma)", 0.1, 5.0, 1.0)
                    res = cv2.GaussianBlur(img_np, (k, k), sigma)
                elif algo_type == "Canny边缘检测":
                    low = st.slider("低阈值", 0, 255, 100)
                    high = st.slider("高阈值", 0, 255, 200)
                    res = cv2.Canny(img_np, low, high)
                
                st.button("保存实验结果至报告")
            
            with c2:
                st.image(res, caption="实时处理效果", use_column_width=True)
            with c3:
                st.markdown("### AI 诊断说明")
                st.info("当前核尺寸较大，图像细节损失严重，建议尝试减小 ksize。")

# 模块三：课后评价 (双端：学情分析)
elif menu in ["评价看板", "作业中心"]:
    st.header("📊 全过程学情评价系统")
    # 模拟雷达图数据
    df = pd.DataFrame(dict(r=[85, 92, 70, 88, 95],
                           theta=['数学推导', '代码实现', '工程应用', '文献综述', '创新设计']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True, template="plotly_dark")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.plotly_chart(fig, use_container_width=True)
    with col_b:
        st.subheader("个性化反馈报告")
        if role:
            st.write("班级整体掌握度：**优**")
            st.write("异常预警：3名同学编程作业存在逻辑重复，疑似代码拷贝。")
        else:
            st.success("你的代码实现能力已超过 90% 的同学！")
            st.warning("建议补充学习：‘快速傅里叶变换的蝴蝶操作’。")

# 模块四：课外拓展 (文献与项目库)
elif menu in ["教研辅助", "竞赛/资料"]:
    st.header("📚 创新拓展资源库")
    cols = st.columns(3)
    with cols[0]:
        st.subheader("📄 文献摘要助手")
        st.file_uploader("上传论文 PDF")
        st.button("AI 一键提取摘要")
    with cols[1]:
        st.subheader("🏆 竞赛案例")
        st.markdown("- [2024蓝桥杯] 图像修复赛题解析\n- [大创项目] 基于YOLO的农业病虫害检测")
    with cols[2]:
        st.subheader("💡 算法百科")
        st.markdown("**SIFT算子**：尺度不变特征变换...")
        st.button("查看动态演化原理")

# --- 4. 底部全天候AI助手 ---
st.markdown("---")
with st.expander("💬 24/7 AI 智能问答助手 (支持代码调试)"):
    st.text_input("请输入您的问题（如：这段代码报错的原因是？）")
    st.caption("基于课程知识库，为您提供精准解答")
