import streamlit as st

# اسم البراند ثابت وموحد
BRAND_NAME = "Roblox Codes Elite"

st.set_page_config(page_title=BRAND_NAME, layout="centered")

# القائمة الجانبية للتنقل بين المقالات (مثل أقسام المواقع الكبرى)
with st.sidebar:
    st.title("🎮 Navigation")
    selection = st.radio("Choose a Game:", ["Home", "Dungeons Incremental 2", "Blox Fruits", "Pet Simulator 99"])
    st.markdown("---")
    st.write(f"© 2026 {BRAND_NAME}")

# تصميم الواجهة (نفس ستايل المواقع العالمية)
st.markdown("""
<style>
    .article-title { font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 5px; }
    .code-card { background: #fdfdfd; border: 2px solid #eee; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 6px solid #ff0000; }
    .active-badge { background: #22c55e; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; }
</style>
""", unsafe_allow_html=True)

if selection == "Home":
    st.markdown(f"<h1 class='article-title'>Welcome to {BRAND_NAME}</h1>", unsafe_allow_html=True)
    st.write("Your #1 source for the latest, working Roblox reward codes. Select a game from the sidebar to start!")
    st.image("https://blog.roblox.com/wp-content/uploads/2022/05/ShareGraph_v1.png")

elif selection == "Dungeons Incremental 2":
    st.markdown("<h1 class='article-title'>Dungeons Incremental 2 Codes</h1>", unsafe_allow_html=True)
    st.caption("Updated: March 10, 2026")
    
    st.markdown("### Active Codes")
    st.markdown("<div class='code-card'><span class='active-badge'>ACTIVE</span><br><code style='font-size: 1.5rem;'>GEMS2026</code><br>Reward: 5,000 Gems</div>", unsafe_allow_html=True)
    st.markdown("<div class='code-card'><span class='active-badge'>ACTIVE</span><br><code style='font-size: 1.5rem;'>RELEASE</code><br>Reward: 2x Boost</div>", unsafe_allow_html=True)

# يمكنك إضافة بقية المابات بنفس الطريقة هنا...
# 8. الفوتر (Footer)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #999;'>© 2026 Roblox Codes Elite. All Rights Reserved.</p>", unsafe_allow_html=True)

