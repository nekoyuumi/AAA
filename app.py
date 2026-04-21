import streamlit as st

# ==========================================
# 1. 網頁基本設定與精品 CSS 樣式
# ==========================================
st.set_page_config(page_title="印加果油 | 黃金淬煉之旅", page_icon="🌿", layout="wide")

st.markdown("""
<style>
    /* 隱藏預設元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 4rem; }
    
    /* 精品字體與排版 */
    h1, h2, h3, h4 { font-family: '微軟正黑體', sans-serif; text-align: center; margin-bottom: 10px; }
    .title-main { color: #2c5e1b; font-size: 3.5em !important; font-weight: 900; }
    .title-sub { color: #d4a72d; font-size: 1.8em !important; letter-spacing: 2px; }
    .text-desc { text-align: center; font-size: 1.2em; color: #5a5a5a; line-height: 1.8; margin-bottom: 40px; }
    
    /* 故事區塊特徵盒 */
    .story-box { background-color: #f9fff6; padding: 25px; border-left: 5px solid #d4a72d; border-radius: 4px; height: 100%; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .story-box h4 { color: #2c5e1b; text-align: left; margin-bottom: 10px;}
    .story-box p { color: #7a5f3e; }
    
    /* 精品定價卡片 */
    .pricing-card {
        background-color: #ffffff;
        padding: 40px 20px;
        border: 1px solid #eaeaea;
        border-top: 5px solid #2c5e1b;
        border-radius: 4px;
        height: 100%;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .pricing-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    }
    
    /* 尊榮推薦卡片 (最高 CP 值) */
    .pricing-card.premium {
        border-top: 5px solid #d4a72d;
        background-color: #fffdf8;
        border: 1px solid #f2e2b3;
    }
    
    .price { color: #d4a72d; font-size: 2.5em; font-weight: bold; margin: 15px 0; font-family: 'Georgia', serif;}
    .original-price { text-decoration: line-through; color: #b3b3b3; font-size: 1em; margin-top: 15px;}
    .save-tag { color: #ffffff; background: #d4a72d; padding: 4px 12px; border-radius: 2px; font-size: 0.9em; display: inline-block; margin-bottom: 15px; letter-spacing: 1px;}
    
    /* 購買按鈕 */
    div.stButton > button:first-child { background-color: #2c5e1b; color: white; width: 100%; height: 55px; font-size: 18px; font-weight: bold; border-radius: 2px; margin-top: 10px; transition: background 0.3s; }
    div.stButton > button:first-child:hover { background-color: #d4a72d; border-color: #d4a72d; color: white; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 沉浸式故事區塊
# ==========================================
# Hero Section
st.markdown('<h1 class="title-main">來自嘉義的黃金雨</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="title-sub">2022 Monde Selection 金質獎得主</h2>', unsafe_allow_html=True)
st.image("images/877118_0.jpg", use_container_width=True) 
st.markdown("---")

# 理念與起源
st.markdown('<br><h2 style="color: #2c5e1b;">大地之星</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">源自亞馬遜，在嘉義綻放。獨特的星形果實，包裹著最純淨的營養精華。<br>每一個都是我們對土地的堅持與熱愛。</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.image("images/877124_0.jpg", use_container_width=True)
st.markdown("---")

# 萃取與堅持
st.markdown('<br><h2 style="color: #2c5e1b;">淬煉，永不妥協</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">不只是油，更是 Nature\'s Pure Fuel。</p>', unsafe_allow_html=True)

r1c1, r1c2 = st.columns(2)
with r1c1:
    st.markdown("""<div class="story-box"><h4>92% 純淨不飽和脂肪酸</h4><p>告別壞油負擔，輕鬆攝取身體真正需要的好油脂，給身體最純粹的能量。</p></div>""", unsafe_allow_html=True)
with r1c2:
    st.markdown("""<div class="story-box"><h4>黃金比例 Omega 3:6 = 1:1</h4><p>完美的平衡。符合國際最佳建議攝取比例，調節生理機能的最佳輔助。</p></div>""", unsafe_allow_html=True)
st.write("")
r2c1, r2c2 = st.columns(2)
with r2c1:
    st.markdown("""<div class="story-box"><h4>15 倍維生素 E</h4><p>青春之源。強大的抗氧化力，不僅維持油品穩定，更封存自然的活力底蘊。</p></div>""", unsafe_allow_html=True)
with r2c2:
    st.markdown("""<div class="story-box"><h4>高科技超臨界 CO2 萃取</h4><p>尖端設備。全程低溫、無溶劑殘留，滴滴珍貴，完美封存印加果極致營養。</p></div>""", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 3. 榮耀與產地證明
# ==========================================
st.markdown('<br><h2 style="color: #d4a72d;">看得見的豐收，世界級的榮耀</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">這不是代工廠的現成原料。整車的希望正在淬煉中，並獲得了國際專家盲測的最高肯定。</p>', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    st.image("images/877117_0.jpg", use_container_width=True)
with col5:
    st.image("images/877121_0.jpg", use_container_width=True)
with col6:
    st.image("images/877116_0.jpg", use_container_width=True)

st.markdown("---")
# ==========================================
# 3.5 沉浸式生活提案：一分鐘好油食譜 (新增區塊)
# ==========================================
st.markdown('<br><h2 style="color: #2c5e1b;">一分鐘，為生活注入黃金能量</h2>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">不用動腦的日常保養。頂級冷壓初榨，保留最完整的營養，請避免高溫煎炸，讓純淨能量直接吸收。</p>', unsafe_allow_html=True)

# 為了食譜區塊增加一點特定的 CSS
st.markdown("""
<style>
    .recipe-card {
        background-color: #ffffff;
        padding: 30px;
        border: 1px solid #f0f0f0;
        border-radius: 8px;
        height: 100%;
        text-align: center;
        transition: all 0.3s ease;
    }
    .recipe-card:hover {
        border-color: #d4a72d;
        box-shadow: 0 5px 20px rgba(212, 167, 45, 0.1);
    }
    .recipe-icon {
        font-size: 2.5em;
        margin-bottom: 15px;
    }
    .recipe-title {
        color: #2c5e1b;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .recipe-text {
        color: #7a5f3e;
        font-size: 1em;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# 使用 2x2 網格呈現四種簡單吃法
recipe_row1_col1, recipe_row1_col2 = st.columns(2)

with recipe_row1_col1:
    st.markdown("""
    <div class="recipe-card">
        <div class="recipe-icon">☀️</div>
        <div class="recipe-title">晨起・純淨甦醒</div>
        <div class="recipe-text">空腹時直接飲用 5~10ml（約一小湯匙）。最純粹的攝取方式，讓滿滿的 Omega-3 喚醒一天的活力。</div>
    </div>
    """, unsafe_allow_html=True)

with recipe_row1_col2:
    st.markdown("""
    <div class="recipe-card">
        <div class="recipe-icon">☕</div>
        <div class="recipe-title">早晨・拿鐵升級</div>
        <div class="recipe-text">滴入 3-5 滴到您的黑咖啡、豆漿或燕麥奶中。輕輕攪拌，不僅增添淡淡堅果香氣，口感更加滑順。</div>
    </div>
    """, unsafe_allow_html=True)

st.write("") # 增加排版間距

recipe_row2_col1, recipe_row2_col2 = st.columns(2)

with recipe_row2_col1:
    st.markdown("""
    <div class="recipe-card">
        <div class="recipe-icon">🥗</div>
        <div class="recipe-title">午間・輕食點綴</div>
        <div class="recipe-text">完美取代沙拉醬！將印加果油淋在生菜沙拉、優格或溫燙青菜上，撒點海鹽，清爽零負擔。</div>
    </div>
    """, unsafe_allow_html=True)

with recipe_row2_col2:
    st.markdown("""
    <div class="recipe-card">
        <div class="recipe-icon">🍚</div>
        <div class="recipe-title">晚膳・熱湯添香</div>
        <div class="recipe-text">不需開火煎炸！在煮好的熱湯、剛起鍋的義大利麵或熱白飯上，直接淋上一匙，健康與風味瞬間升級。</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
# ==========================================
# 4. 精品定價選擇區 (Pricing Cards)
# ==========================================
st.markdown('<br><h1 class="title-main" style="font-size: 2.8em !important;">啟動您的好油生活</h1>', unsafe_allow_html=True)
st.markdown('<p class="text-desc">選擇最適合您的健康護航方案</p>', unsafe_allow_html=True)

# 三卡並排
col_single, col_3pack, col_6pack = st.columns(3)

with col_single:
    st.image("images/877123_0.jpg", use_container_width=True)
    st.markdown("""
    <div class="pricing-card">
        <h3 style="color: #2c5e1b;">初次相遇<br><span style="font-size: 0.7em; color: #7a5f3e;">單瓶體驗</span></h3>
        <p style="color: #999; height: 40px; font-size: 0.9em;">適合想初步嘗試替換家中食用油的您。</p>
        <div class="original-price"><br></div>
        <div class="price">NT$ XXX</div>
        <div style="height: 31px;"></div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🛒 單瓶加入購物車", key="btn_1"):
        st.success("已將【單瓶體驗】加入購物車！")

with col_3pack:
    st.image("images/877125.jpg", use_container_width=True)
    st.markdown("""
    <div class="pricing-card">
        <h3 style="color: #2c5e1b;">精打細算<br><span style="font-size: 0.7em; color: #7a5f3e;">3 瓶守護組</span></h3>
        <p style="color: #999; height: 40px; font-size: 0.9em;">適合 1-2 人小家庭，穩定建立好油習慣。</p>
        <div class="original-price">原價 NT$ XXXX</div>
        <div class="price">NT$ XXXX</div>
        <span class="save-tag">現省 NT$ XXX</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🛒 購買 3 瓶組", key="btn_3"):
        st.success("已將【3 瓶守護組】加入購物車！")

with col_6pack:
    st.image("images/877125.jpg", use_container_width=True)
    st.markdown("""
    <div class="pricing-card premium">
        <div style="color: #d4a72d; font-weight: bold; margin-bottom: 10px; letter-spacing: 2px;">✦ 尊榮免運 ✦</div>
        <h3 style="color: #d4a72d;">極致熱銷<br><span style="font-size: 0.7em; color: #7a5f3e;">6 瓶家庭組</span></h3>
        <p style="color: #999; height: 40px; font-size: 0.9em;">最高 C/P 值。適合全家老小，或與親友分享。</p>
        <div class="original-price">原價 NT$ XXXX</div>
        <div class="price">NT$ XXXX</div>
        <span class="save-tag" style="background:#2c5e1b;">現省 NT$ XXX</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🛒 購買 6 瓶組", key="btn_6"):
        st.balloons()
        st.success("已將【6 瓶家庭組】加入購物車！恭喜享有免運優惠！")
