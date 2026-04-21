import streamlit as st

# ==========================================
# 1. 網頁基本設定與 CSS 精品樣式
# ==========================================
st.set_page_config(page_title="印加果油 | 官方旗艦店", page_icon="🌿", layout="wide")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    
    h1, h2, h3, h4 { font-family: '微軟正黑體', sans-serif; text-align: center; margin-bottom: 10px; }
    .title-main { color: #2c5e1b; font-size: 3.5em !important; font-weight: 900; }
    .title-sub { color: #d4a72d; font-size: 1.8em !important; letter-spacing: 2px; }
    .text-desc { text-align: center; font-size: 1.2em; color: #5a5a5a; line-height: 1.8; margin-bottom: 30px; }
    
    .feature-box { background-color: #f9fff6; padding: 25px; border-left: 5px solid #d4a72d; border-radius: 4px; height: 100%; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .feature-box h4 { color: #2c5e1b; text-align: left; }
    .feature-box p { color: #7a5f3e; }
    
    /* 按鈕共用樣式 */
    div.stButton > button:first-child { background-color: #2c5e1b; color: white; width: 100%; height: 50px; font-size: 18px; font-weight: bold; border-radius: 5px; }
    div.stButton > button:first-child:hover { background-color: #d4a72d; border-color: #d4a72d; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 側邊欄 (Sidebar) 導覽選單
# ==========================================
st.sidebar.image("images/877125.jpg", use_container_width=True) # 側邊欄放個產品小圖
st.sidebar.title("🌿 官方旗艦店")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "請選擇您想瀏覽的頁面：",
    ["📖 品牌故事與介紹", "🥇 單瓶首購體驗", "🎁 多瓶組合優惠"]
)
st.sidebar.markdown("---")
st.sidebar.info("🏆 2022 Monde Selection 金質獎得主\n\n🛡️ 380項嚴格檢驗合格")

# ==========================================
# 3. 頁面內容邏輯切換
# ==========================================

# ----------------- 頁面 1：品牌故事 -----------------
if page == "📖 品牌故事與介紹":
    st.markdown('<h1 class="title-main">來自嘉義的黃金雨</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="title-sub">2022 Monde Selection 金質獎得主</h2>', unsafe_allow_html=True)
    st.image("images/877118_0.jpg", use_container_width=True)
    st.markdown("---")
    
    st.markdown('<br><h2 style="color: #2c5e1b;">大地之星</h2>', unsafe_allow_html=True)
    st.markdown('<p class="text-desc">源自亞馬遜，在嘉義綻放。獨特的星形果實，包裹著最純淨的營養精華。<br>每一個都是我們對土地的堅持與熱愛。</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/877124_0.jpg", use_container_width=True)
    st.markdown("---")
    
    st.markdown('<br><h2 style="color: #d4a72d;">看得見的豐收，世界級的榮耀</h2>', unsafe_allow_html=True)
    st.markdown('<p class="text-desc">這不是代工廠的現成原料。整車的希望正在淬煉中，並獲得了國際專家盲測的最高肯定。</p>', unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    with col4:
        st.image("images/877117_0.jpg", caption="嘉義中埔鄉 產地直送", use_container_width=True)
    with col5:
        st.image("images/877116_0.jpg", caption="榮獲世界品質評鑑大賞", use_container_width=True)

# ----------------- 頁面 2：單瓶首購 -----------------
elif page == "🥇 單瓶首購體驗":
    st.markdown('<h1 class="title-main">單瓶體驗方案</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="title-sub">初次相遇，感受純淨的好油</h2>', unsafe_allow_html=True)
    
    col_img, col_info = st.columns([1, 1.2])
    with col_img:
        st.image("images/877123_0.jpg", use_container_width=True) # 使用有專家的照片增加單瓶信任感
    
    with col_info:
        st.markdown("### 🌿 頂級印加果油 (250ml)")
        st.write("**適合對象**：想初步嘗試替換家中食用油、注重日常基礎保養的您。")
        st.markdown("""
        * **15 倍維生素 E**：強大的抗氧化力。
        * **高科技萃取**：超臨界 CO2 低溫無溶劑殘留。
        * **無農藥、無化肥**：380 項檢驗合格。
        """)
        st.markdown('<h2 style="color: #d4a72d; text-align: left;">體驗價 NT$ XXX</h2>', unsafe_allow_html=True)
        
        if st.button("🛒 單瓶加入購物車"):
            st.balloons()
            st.success("已將【單瓶體驗組】加入購物車！")

# ----------------- 頁面 3：多瓶組合 -----------------
elif page == "🎁 多瓶組合優惠":
    st.markdown('<h1 class="title-main">多瓶組合優惠</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="title-sub">長久陪伴，守護全家人的健康</h2>', unsafe_allow_html=True)
    
    st.image("images/877125.jpg", use_container_width=True) # 產品合照非常適合放這裡
    st.markdown("---")
    
    # 建立兩個組合方案的對比
    bundle1, bundle2 = st.columns(2)
    
    with bundle1:
        st.markdown("""
        <div class="feature-box" style="text-align: center;">
            <h3 style="color: #2c5e1b;">【精打細算】3 瓶守護組</h3>
            <p style="color: #7a5f3e;">適合 1-2 人小家庭，穩定建立好油習慣。</p>
            <h2 style="color: #d4a72d;">特價 NT$ XXXX</h2>
            <p style="text-decoration: line-through; color: #aaa;">原價 NT$ XXXX</p>
            <p style="color: red; font-weight: bold;">現省 NT$ XXX</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("") # 稍微空一行
        if st.button("🛒 購買 3 瓶組"):
            st.snow() # 用雪花特效區分大訂單
            st.success("已將【3 瓶守護組】加入購物車！")

    with bundle2:
        st.markdown("""
        <div class="feature-box" style="text-align: center; border-left: 5px solid #ff4b4b;">
            <h3 style="color: #d4a72d;">🔥【極致熱銷】6 瓶家庭組</h3>
            <p style="color: #7a5f3e;">最高 C/P 值！適合全家老小，或與親友團購分享。</p>
            <h2 style="color: #d4a72d;">特價 NT$ XXXX</h2>
            <p style="text-decoration: line-through; color: #aaa;">原價 NT$ XXXX</p>
            <p style="color: red; font-weight: bold;">現省 NT$ XXX (免運費)</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("") 
        if st.button("🛒 購買 6 瓶組"):
            st.balloons()
            st.success("已將【6 瓶家庭組】加入購物車！恭喜享有免運優惠！")
