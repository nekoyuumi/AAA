import streamlit as st

# ==========================================
# 1. 網頁基本設定與 CSS 精品樣式 (包含卡片設計)
# ==========================================
st.set_page_config(page_title="美綠藤印加果油 | 官方旗艦店", page_icon="🌿", layout="wide")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 4rem; }
    
    h1, h2, h3, h4 { font-family: '微軟正黑體', sans-serif; text-align: center; margin-bottom: 10px; }
    .title-main { color: #2c5e1b; font-size: 3.5em !important; font-weight: 900; }
    .title-sub { color: #d4a72d; font-size: 1.8em !important; letter-spacing: 2px; }
    .text-desc { text-align: center; font-size: 1.2em; color: #5a5a5a; line-height: 1.8; margin-bottom: 30px; }
    
    /* 商品定價卡片樣式 */
    .pricing-card {
        background-color: #f9fff6;
        padding: 30px 20px;
        border: 1px solid #e0e0e0;
        border-top: 5px solid #2c5e1b;
        border-radius: 8px;
        height: 100%;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    .pricing-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    /* 凸顯最高 C/P 值的卡片 */
    .pricing-card.best-value {
        border-top: 5px solid #d4a72d;
        background-color: #fffaf0;
        border: 2px solid #d4a72d;
    }
    
    .price { color: #d4a72d; font-size: 2.2em; font-weight: bold; margin: 15px 0; }
    .original-price { text-decoration: line-through; color: #aaa; font-size: 1em; }
    .save-tag { color: #d9534f; font-weight: bold; background: #fde8e8; padding: 4px 10px; border-radius: 4px; font-size: 0.9em; display: inline-block; margin-bottom: 10px;}
    
    /* 按鈕共用樣式 */
    div.stButton > button:first-child { background-color: #2c5e1b; color: white; width: 100%; height: 50px; font-size: 18px; font-weight: bold; border-radius: 5px; margin-top: 15px; }
    div.stButton > button:first-child:hover { background-color: #d4a72d; border-color: #d4a72d; color: white; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 品牌視覺與故事區塊
# ==========================================
st.markdown('<h1 class="title-main">來自嘉義的黃金雨</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="title-sub">2022 Monde Selection 金質獎得主</h2>', unsafe_allow_html=True)
st.image("images/877118_0.jpg", use_container_width=True)
st.markdown("---")

# 獲獎與產地證明並排
st.markdown('<br><h2 style="color: #d4a72d;">世界級的最高肯定</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">由國際專家嚴格盲測評選，品質獲世界級認可！無農藥、無化肥、無添加。</p>', unsafe_allow_html=True)
col_cert1, col_cert2, col_cert3 = st.columns(3)
with col_cert1:
    st.image("images/877121_0.jpg", use_container_width=True)
with col_cert2:
    st.image("images/877120_0.jpg", use_container_width=True)
with col_cert3:
    st.image("images/877116_0.jpg", use_container_width=True)

st.markdown("---")

# ==========================================
# 3. 商品方案並排顯示區塊 (Pricing Cards)
# ==========================================
st.markdown('<br><h1 class="title-main" style="font-size: 2.8em !important;">選擇您的健康護航方案</h1>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">健康不等待，即刻啟動您的好油生活</p>', unsafe_allow_html=True)

# 建立三個並排的直列
col_single, col_3pack, col_6pack = st.columns(3)

with col_single:
    st.image("images/877123_0.jpg", use_container_width=True)
    st.markdown("""
    <div class="pricing-card">
        <h3 style="color: #2c5e1b;">【初次相遇】<br>單瓶體驗方案</h3>
        <p style="color: #7a5f3e; height: 45px;">適合想初步嘗試替換家中食用油的您。</p>
        <div class="original-price"><br></div>
        <div class="price">NT$ XXX</div>
        <div style="height: 31px;"></div> </div>
    """, unsafe_allow_html=True)
    if st.button("🛒 單瓶加入購物車", key="btn_1"):
        st.success("已將【單瓶體驗組】加入購物車！")

with col_3pack:
    st.image("images/877125.jpg", use_container_width=True)
    st.markdown("""
    <div class="pricing-card">
        <h3 style="color: #2c5e1b;">【精打細算】<br>3 瓶守護組</h3>
        <p style="color: #7a5f3e; height: 45px;">適合 1-2 人小家庭，穩定建立好油習慣。</p>
        <div class="original-price">原價 NT$ XXXX</div>
        <div class="price">NT$ XXXX</div>
        <span class="save-tag">現省 NT$ XXX</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🛒 購買 3 瓶組", key="btn_3"):
        st.success("已將【3 瓶守護組】加入購物車！")

with col_6pack:
    st.image("images/877125.jpg", use_container_width=True) # 可以換成其他大合照如果有的話
    st.markdown("""
    <div class="pricing-card best-value">
        <div style="background: #d4a72d; color: white; padding: 5px; font-weight: bold; border-radius: 4px; margin-bottom: 15px;">🔥 極致熱銷 / 免運費</div>
        <h3 style="color: #2c5e1b;">【最高 C/P 值】<br>6 瓶家庭組</h3>
        <p style="color: #7a5f3e; height: 45px;">適合全家老小日常保養，或親友團購分享。</p>
        <div class="original-price">原價 NT$ XXXX</div>
        <div class="price">NT$ XXXX</div>
        <span class="save-tag">現省 NT$ XXX (免運)</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🛒 購買 6 瓶組", key="btn_6"):
        st.balloons()
        st.success("已將【6 瓶家庭組】加入購物車！恭喜享有免運優惠！")
