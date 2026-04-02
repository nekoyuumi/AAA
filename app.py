import streamlit as st

# 1. 設定網頁排版為「寬版(wide)」，這對展現大圖非常有幫助
st.set_page_config(page_title="美綠藤印加果油 | 黃金淬煉之旅", page_icon="🌿", layout="wide")

# 2. 注入自訂 CSS，隱藏預設邊界，打造精品感的大地色系
st.markdown("""
<style>
    /* 隱藏上方選單與底部浮水印 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 調整主容器邊距 */
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    
    /* 自訂標題與內文樣式 */
    h1, h2, h3 { font-family: '微軟正黑體', sans-serif; text-align: center; margin-bottom: 10px; }
    .title-main { color: #2c5e1b; font-size: 3.5em !important; font-weight: 900; }
    .title-sub { color: #d4a72d; font-size: 1.8em !important; letter-spacing: 2px; }
    
    .text-desc { text-align: center; font-size: 1.3em; color: #5a5a5a; line-height: 1.8; margin-bottom: 40px; }
    
    /* 精品風的特色區塊 */
    .feature-box {
        background-color: #f9fff6;
        padding: 25px;
        border-left: 5px solid #d4a72d;
        border-radius: 4px;
        height: 100%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .feature-box h4 { color: #2c5e1b; font-size: 1.5em; text-align: left; margin-bottom: 10px; }
    .feature-box p { color: #7a5f3e; font-size: 1.1em; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 區塊一：主視覺 (Hero) - 滿版震撼
# ==========================================
st.markdown('<h1 class="title-main">來自嘉義的黃金雨</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="title-sub">2022 Monde Selection 金質獎得主</h2>', unsafe_allow_html=True)
st.image("images/877118_0.jpg", use_container_width=True) # 使用果園大圖營造沉浸感
st.markdown("---")

# ==========================================
# 區塊二：大地之星 (Origin) - 留白與故事
# ==========================================
st.markdown('<br><h2 style="color: #2c5e1b;">大地之星</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">源自亞馬遜，在嘉義綻放。獨特的星形果實，包裹著最純淨的營養精華。<br>每一個都是我們對土地的堅持與熱愛。</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1]) # 中間放圖片，兩側留白增加質感
with col2:
    st.image("images/877124_0.jpg", use_container_width=True)
st.markdown("---")

# ==========================================
# 區塊三：淬煉與堅持 (Tech) - 質感網格
# ==========================================
st.markdown('<br><h2 style="color: #2c5e1b;">淬煉，永不妥協</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">不只是油，更是 Nature\'s Pure Fuel。</p>', unsafe_allow_html=True)

# 使用 2x2 網格排列四大優勢
r1c1, r1c2 = st.columns(2)
with r1c1:
    st.markdown("""
    <div class="feature-box">
        <h4>92% 純淨不飽和脂肪酸</h4>
        <p>告別壞油負擔，輕鬆攝取身體真正需要的好油脂，給身體最純粹的能量。</p>
    </div>
    """, unsafe_allow_html=True)
with r1c2:
    st.markdown("""
    <div class="feature-box">
        <h4>黃金比例 Omega 3:6 = 1:1</h4>
        <p>完美的平衡。符合國際最佳建議攝取比例，調節生理機能的最佳輔助。</p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # 增加一點間距

r2c1, r2c2 = st.columns(2)
with r2c1:
    st.markdown("""
    <div class="feature-box">
        <h4>15 倍維生素 E</h4>
        <p>青春之源。強大的抗氧化力，不僅維持油品穩定，更封存自然的活力底蘊。</p>
    </div>
    """, unsafe_allow_html=True)
with r2c2:
    st.markdown("""
    <div class="feature-box">
        <h4>高科技超臨界 CO2 萃取</h4>
        <p>尖端設備。全程低溫、無溶劑殘留，滴滴珍貴，完美封存印加果極致營養。</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 區塊四：豐收與榮耀 (Scale & Awards) - 視覺衝擊
# ==========================================
st.markdown('<br><h2 style="color: #d4a72d;">看得見的豐收，世界級的榮耀</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">這不是代工廠的現成原料。整車的希望正在淬煉中，並獲得了國際專家盲測的最高肯定。</p>', unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.image("images/877117_0.jpg", caption="嘉義中埔鄉 產地直送", use_container_width=True)
with col5:
    st.image("images/877116_0.jpg", caption="榮獲世界品質評鑑大賞 實體紅布條", use_container_width=True)

st.markdown("---")

# ==========================================
# 區塊五：啟動體驗 (CTA) - 聚焦產品
# ==========================================
st.markdown('<br><h2 style="color: #2c5e1b;">啟動您的好油生活</h2>', unsafe_allow_html=True)

col6, col7, col8 = st.columns([1, 1.5, 1])
with col7:
    st.image("images/877125.jpg", use_container_width=True) # 產品合照
    
    st.markdown('<h3 style="color: #d4a72d;">單瓶體驗價 NT$ XXX</h3>', unsafe_allow_html=True)
    
    # 讓按鈕置中並加大
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #2c5e1b;
        color: white;
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 5px;
    }
    div.stButton > button:first-child:hover {
        background-color: #d4a72d;
        border-color: #d4a72d;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if st.button("立即體驗黃金奇蹟"):
        st.balloons() # 加入 Streamlit 專屬的氣球動畫！
        st.success("感謝您選擇美綠藤印加果油！即將為您導向結帳頁面...")
