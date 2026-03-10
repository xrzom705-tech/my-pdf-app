import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Roblox Codes Elite", layout="wide", page_icon="🎮")

# اسم الموقع الموحد
st.markdown("<h1 style='text-align: center; color: #FF0000;'>🎮 Roblox Codes Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Latest & Active Reward Codes for your favorite maps!</p>", unsafe_allow_html=True)

# القائمة الجانبية للغات والمابات
with st.sidebar:
    lang = st.selectbox("Language", ["English", "العربية"])
    st.markdown("---")
    map_choice = st.selectbox("Select Map / اختر الماب", ["Blox Fruits", "Pet Simulator 99", "Brookhaven", "All Star Tower Defense"])

# قاعدة بيانات بسيطة للأكواد (تقدر تحدثها بنفسك من هنا بسهولة)
codes_data = {
    "Blox Fruits": [
        {"code": "REWARD_2026", "reward": "2x Experience (20 min)", "status": "Active ✅"},
        {"code": "SUB2GAMERROBOT_RESET1", "reward": "Stat Reset", "status": "Active ✅"},
    ],
    "Pet Simulator 99": [
        {"code": "FREE_PET_66", "reward": "Diamond Potion", "status": "Active ✅"},
    ]
}

# نصوص الواجهة
t = {
    "English": {"header": "Active Codes for", "copy": "Click code to copy", "status": "Status"},
    "العربية": {"header": "الأكواد الشغالة لـ", "copy": "اضغط على الكود للنسخ", "status": "الحالة"}
}
txt = t[lang]

# عرض الأكواد بتنسيق جذاب (Cards)
st.subheader(f"{txt['header']} {map_choice}")

for item in codes_data.get(map_choice, []):
    with st.container():
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            # زر النسخ التلقائي (استخدمنا كود مدمج للنسخ)
            st.code(item['code'], language="text")
        with col2:
            st.write(f"🎁 **{item['reward']}**")
        with col3:
            st.success(item['status'])
        st.markdown("---")

# مساحة للإعلانات (نصيحة للربح)
st.sidebar.info("Ad Space: Place your ads here later!")
