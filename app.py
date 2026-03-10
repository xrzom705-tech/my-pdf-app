import streamlit as st

# 1. إعدادات الصفحة (اسم الموقع الثابت)
st.set_page_config(page_title="Roblox Codes Elite - Latest Rewards", layout="centered", page_icon="🎮")

# 2. تصميم CSS متقدم (ليشبه GameRant و TheGamer)
st.markdown("""
    <style>
    /* خلفية الموقع ناصعة البياض مثل المواقع الإخبارية */
    .stApp {
        background-color: #ffffff;
    }
    /* تنسيق العنوان الرئيسي الضخم */
    .main-title {
        font-family: 'Oswald', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        color: #1a1a1a;
        text-align: left;
        line-height: 1.1;
        margin-bottom: 10px;
    }
    /* تاريخ التحديث لزيادة الثقة */
    .update-date {
        color: #666;
        font-size: 0.9rem;
        border-bottom: 2px solid #eee;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }
    /* مربع الأكواد (مثل الصندوق في المواقع العالمية) */
    .code-box {
        background-color: #f8f9fa;
        border: 2px dashed #d1d5db;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
    }
    .active-tag {
        background-color: #22c55e;
        color: white;
        padding: 2px 10px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .expired-tag {
        background-color: #ef4444;
        color: white;
        padding: 2px 10px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    /* عناوين الأقسام */
    h2 {
        border-left: 5px solid #ff0000;
        padding-left: 15px;
        color: #1a1a1a;
        margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر (News Header Style)
st.markdown('<h1 class="main-title">Roblox Dungeons Incremental 2 Codes (March 2026)</h1>', unsafe_allow_html=True)
st.markdown('<p class="update-date">Published Mar 10, 2026 — <b>By Bandar</b></p>', unsafe_allow_html=True)

# 4. مقدمة المقال (SEO Content)
st.write("""
Looking for the latest rewards in **Dungeons Incremental 2**? You've come to the right place. 
In this guide, we provide a complete list of all active codes that you can redeem for Gems, 
Boosts, and exclusive items to help you progress faster.
""")

st.image("https://img.youtube.com/vi/placeholder/maxresdefault.jpg", caption="Dungeons Incremental 2 Gameplay") # صورة تعبيرية

# 5. قسم الأكواد الشغالة (Active Codes)
st.markdown("<h2>Active Dungeons Incremental 2 Codes</h2>", unsafe_allow_html=True)
st.write("Here are all the working codes for this month:")

# عرض الأكواد بطريقة الصناديق
def display_code(code, reward):
    st.markdown(f"""
    <div class="code-box">
        <span class="active-tag">ACTIVE</span><br>
        <strong style="font-size: 1.5rem; color: #ff0000;">{code}</strong><br>
        <p style="margin-top: 5px;">🎁 <b>Reward:</b> {reward}</p>
    </div>
    """, unsafe_allow_html=True)
    st.button(f"Copy {code}", key=code)

display_code("GEMS2026", "5,000 Free Gems")
display_code("RELEASE", "2x XP Boost (30 Mins)")
display_code("BANDAR_ELITE", "Exclusive Sword Skin")

# 6. قسم الأكواد المنتهية (Expired Codes)
st.markdown("<h2>Expired Codes</h2>", unsafe_allow_html=True)
st.write("These codes no longer work, but we keep them here for reference:")
st.markdown("""
<ul style="color: #666;">
    <li>BETA_TESTER - 100 Gems</li>
    <li>WINTER2025 - Snow Pet</li>
</ul>
""", unsafe_allow_html=True)

# 7. طريقة التفعيل (How to Redeem)
st.markdown("<h2>How to Redeem Codes in Dungeons Incremental 2</h2>", unsafe_allow_html=True)
st.write("""
1. Launch **Dungeons Incremental 2** on Roblox.
2. Click on the **Twitter/Codes Icon** on the left side of the screen.
3. Enter the code exactly as shown above.
4. Hit **Redeem** to claim your rewards!
""")

# 8. الفوتر (Footer)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #999;'>© 2026 Roblox Codes Elite. All Rights Reserved.</p>", unsafe_allow_html=True)
