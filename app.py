import streamlit as st

# 1. إعدادات الصفحة والاسم الموحد
st.set_page_config(page_title="Roblox Codes Elite", layout="wide", page_icon="🎮")

# 2. القائمة الجانبية الثابتة (Settings)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
    lang = st.selectbox("Select Language / اختر اللغة", ["English", "العربية"])
    st.markdown("---")
    st.write("Platform: **Roblox Codes Elite**")
    st.write("Developer: **Bandar**")
    st.info("Tip: Bookmark this page to get new codes every day!")

# 3. نظام النصوص والترجمة
texts = {
    "English": {
        "subtitle": "Get the latest active reward codes!",
        "search_label": "🔍 Search for your Map (e.g. Blox Fruits)",
        "no_results": "No maps found with this name.",
        "copy_msg": "Click to copy",
        "reward": "Reward:",
        "status": "Status"
    },
    "العربية": {
        "subtitle": "احصل على أحدث أكواد المكافآت الشغالة!",
        "search_label": "🔍 ابحث عن الماب (مثلاً: بلوكس فروت)",
        "no_results": "لم يتم العثور على مابات بهذا الاسم.",
        "copy_msg": "اضغط للنسخ",
        "reward": "المكافأة:",
        "status": "الحالة"
    }
}
t = texts[lang]
dir = "rtl" if lang == "العربية" else "ltr"

# 4. قاعدة البيانات (تقدر تزيد المابات هنا بسهولة)
all_maps = {
    "Blox Fruits": [
        {"code": "REWARD_2026", "gift": "2x EXP Boost", "active": True},
        {"code": "SUB2CAPTAINMAI", "gift": "Stat Reset", "active": True}
    ],
    "Pet Simulator 99": [
        {"code": "DIAMONDS88", "gift": "50k Diamonds", "active": True},
        {"code": "FREEPET", "gift": "Random Egg", "active": False}
    ],
    "Brookhaven": [
        {"code": "GIFT2026", "gift": "Special Car Skin", "active": True}
    ],
    "All Star Tower Defense": [
        {"code": "NEWYEAR_GEMS", "gift": "1000 Gems", "active": True}
    ]
}

# 5. تصميم الواجهة (CSS)
st.markdown(f"""
    <style>
    .stApp {{ direction: {dir}; background-color: #f0f2f5; }}
    .map-card {{
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px;
        border-left: 10px solid #FF0000;
    }}
    h1 {{ color: #FF0000 !important; font-family: 'Arial Black', sans-serif; }}
    </style>
    """, unsafe_allow_html=True)

# 6. الهيدر (اسم موحد)
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>🎮 Roblox Codes Elite</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #4B5563;'>{t['subtitle']}</p>", unsafe_allow_html=True)

# 7. محرك البحث الذكي
search_query = st.text_input(t['search_label'], placeholder="Type map name here...")

# منطق البحث والعرض
filtered_maps = {name: data for name, data in all_maps.items() if search_query.lower() in name.lower()}

if filtered_maps:
    for map_name, codes in filtered_maps.items():
        st.markdown(f"### 📍 {map_name}")
        for c in codes:
            with st.container():
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    st.code(c['code'], language="text")
                    st.caption(t['copy_msg'])
                with col2:
                    st.write(f"🎁 **{t['reward']}** {c['gift']}")
                with col3:
                    if c['active']:
                        st.success("Active ✅")
                    else:
                        st.error("Expired ❌")
        st.markdown("---")
else:
    st.warning(t['no_results'])
