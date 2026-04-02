import streamlit as st

# 設定網頁標題與排版
st.set_page_config(page_title="美綠藤印加果油 - 世界金質獎", page_icon="🌿", layout="centered")

# 區塊一：主視覺
st.image("images/877125.jpg", use_container_width=True)
st.title("建立「油」好關係！")
st.subheader("🏆 榮獲 2022 世界品質評鑑大賞【金質獎】肯定")
st.write("台灣嘉義在地契作，從產地到餐桌的純淨。給家人最好的，就從換一瓶世界級的好油開始。")

st.divider() # 分隔線

# 區塊二：痛點與理念
col1, col2 = st.columns(2)
with col1:
    st.header("為什麼我們堅持自己種？")
    st.write("**因為「想做出自己想用、對人與環境都好的產品。」**")
    st.write("創辦人曾受疾病困擾多年，直到遇見了「印加果」，親身經歷了健康的改善。為此成立了「嘉義縣印加果生產合作社（美綠藤）」。我們不依賴進口不明原料，深耕台灣照顧在地小農，從泥土到瓶裝全程守護。")
with col2:
    st.image("images/877124_0.jpg", use_container_width=True)

st.divider()

# 區塊三：四大黃金優勢
col3, col4 = st.columns(2)
with col3:
    st.image("images/877123_0.jpg", use_container_width=True)
with col4:
    st.header("滴滴珍貴，健康管理的超級神隊友")
    st.write("- **優勢 1｜不飽和脂肪酸高達 92%**：告別壞油負擔，輕鬆攝取身體真正需要的好油脂。")
    st.write("- **優勢 2｜黃金比例 Omega 3:6 = 1:1**：符合國際最推薦的攝取比例，完美平衡體內所需。")
    st.write("- **優勢 3｜維生素 E 是橄欖油的 15 倍**：強大的抗氧化力，為你的青春與活力打底。")
    st.write("- **優勢 4｜高科技超臨界 CO2 萃取**：全程低溫、無溶劑殘留，完美封存印加果極致營養。")

st.divider()

# 區塊四：權威認證
st.header("世界級的榮耀，來自最嚴苛的把關")
st.write("由國際專家嚴格盲測評選，品質獲世界級認可！每一批印加果仁均通過 380 項農藥殘留、重金屬、黃麴毒素等檢驗。無農藥、無化肥、無添加。")
col5, col6 = st.columns(2)
with col5:
    st.image("images/877121_0.jpg", use_container_width=True)
with col6:
    st.image("images/877116_0.jpg", use_container_width=True)

st.divider()

# 區塊五：產地直送
col7, col8 = st.columns(2)
with col7:
    st.header("看得見的豐收，真材實料的堅持")
    st.write("這不是代工廠的現成原料，這是嘉義中埔鄉陽光孕育出的驕傲。每一顆印加果，都承載著我們對品質的執著與對土地的熱愛。")
with col8:
    st.image("images/877117_0.jpg", use_container_width=True)

st.divider()

# 區塊六：結帳促銷
st.header("健康不等待，即刻啟動您的好油生活")
st.write("選擇最適合您的保養方案，今天就開始改變。")
st.markdown("### 單瓶體驗價 NT$ XXX")

# 行動呼籲按鈕
if st.button("立即加入購物車", type="primary"):
    st.success("已將美綠藤印加果油加入購物車！（註：這裡後續可串接您的結帳表單或蝦皮網址）")