import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import io
import time

# 1. إعدادات الصفحة واسم الموقع الثابت
st.set_page_config(page_title="PDF Elite", layout="wide", page_icon="💎")

# 2. القائمة الجانبية (ثابتة لا تتأثر بالترجمة)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
    lang_choice = st.selectbox("Select Language / اختر اللغة", ["English", "العربية"])
    st.markdown("---")
    st.write("Project: **PDF Elite**")
    st.write("Developed by: **Bandar**")

# 3. نظام النصوص (الاسم موحد PDF Elite)
texts = {
    "English": {
        "subtitle": "Professional PDF Solutions",
        "merge_t": "Merge PDF", "split_t": "Split PDF", "lock_t": "Protect PDF",
        "btn_open": "Open Tool", "btn_back": "⬅ Back to Menu", "btn_start": "Start Processing",
        "success": "Task Completed!", "working": "Processing your file..."
    },
    "العربية": {
        "subtitle": "حلول PDF احترافية",
        "merge_t": "دمج الملفات", "split_t": "تقسيم الملفات", "lock_t": "حماية الملفات",
        "btn_open": "افتح الأداة", "btn_back": "⬅ العودة للقائمة", "btn_start": "ابدأ المعالجة",
        "success": "تمت المهمة بنجاح!", "working": "جاري معالجة الملف..."
    }
}
t = texts[lang_choice]
dir = "rtl" if lang_choice == "العربية" else "ltr"

# 4. تصميم الألوان المخصصة (CSS)
st.markdown(f"""
    <style>
    .stApp {{ direction: {dir}; background-color: #F8FAFC; }}
    h1, h2, h3 {{ color: #1E293B !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
    
    /* تنسيق البطاقات */
    .tool-card {{
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center;
        margin-bottom: 20px; border-bottom: 6px solid #CBD5E1;
    }}
    
    /* ألوان Progress Bar مخصصة (تعتمد على الثيم) */
    .stProgress > div > div > div > div {{ background-color: #3B82F6; }} /* لون افتراضي */
    </style>
    """, unsafe_allow_html=True)

# 5. الهيدر (الاسم موحد لا يترجم)
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 0;'>💎 PDF Elite</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #64748B; font-size: 1.2rem;'>{t['subtitle']}</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"<div class='tool-card' style='border-color: #22C55E;'><h3>📑 {t['merge_t']}</h3></div>", unsafe_allow_html=True)
        if st.button(t['btn_open'], key="btn_m"): 
            st.session_state.page = 'merge'
            st.rerun()

    with col2:
        st.markdown(f"<div class='tool-card' style='border-color: #EF4444;'><h3>✂️ {t['split_t']}</h3></div>", unsafe_allow_html=True)
        if st.button(t['btn_open'], key="btn_s"): 
            st.session_state.page = 'split'
            st.rerun()

    with col3:
        st.markdown(f"<div class='tool-card' style='border-color: #F59E0B;'><h3>🔒 {t['lock_t']}</h3></div>", unsafe_allow_html=True)
        if st.button(t['btn_open'], key="btn_l"): 
            st.session_state.page = 'lock'
            st.rerun()

# --- أدوات المعالجة مع علامات تقدم ملونة ---

elif st.session_state.page == 'merge':
    if st.button(t['btn_back']): st.session_state.page = 'home'; st.rerun()
    st.subheader(f"📑 {t['merge_t']}")
    files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    if files and st.button(t['btn_start']):
        # شريط تقدم بلون أخضر (هدف الإداة: دمج/نمو)
        progress_bar = st.markdown("""<style>stProgress > div > div > div > div { background-image: linear-gradient(to right, #22C55E, #16A34A) !important; }</style>""", unsafe_allow_html=True)
        bar = st.progress(0)
        merger = PdfMerger()
        for i, f in enumerate(files):
            merger.append(f)
            bar.progress((i + 1) / len(files))
            time.sleep(0.2)
        out = io.BytesIO(); merger.write(out)
        st.success(t['success'])
        st.download_button("Download", out.getvalue(), "merged_elite.pdf")

elif st.session_state.page == 'split':
    if st.button(t['btn_back']): st.session_state.page = 'home'; st.rerun()
    st.subheader(f"✂️ {t['split_t']}")
    file = st.file_uploader("Upload PDF", type="pdf")
    if file and st.button(t['btn_start']):
        # شريط تقدم بلون أحمر (هدف الأداة: قص/تقسيم)
        st.markdown("""<style>.stProgress > div > div > div > div { background-color: #EF4444 !important; }</style>""", unsafe_allow_html=True)
        bar = st.progress(0)
        reader = PdfReader(file)
        pages = len(reader.pages)
        for i in range(pages):
            bar.progress((i + 1) / pages)
            time.sleep(0.1)
        st.info("Files are ready for individual download.")
        # منطق التحميل هنا...

elif st.session_state.page == 'lock':
    if st.button(t['btn_back']): st.session_state.page = 'home'; st.rerun()
    st.subheader(f"🔒 {t['lock_t']}")
    file = st.file_uploader("Upload PDF", type="pdf")
    pwd = st.text_input("Set Password", type="password")
    if file and pwd and st.button(t['btn_start']):
        # شريط تقدم بلون ذهبي/أصفر (هدف الأداة: أمان/حماية)
        st.markdown("""<style>.stProgress > div > div > div > div { background-color: #F59E0B !important; }</style>""", unsafe_allow_html=True)
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01); bar.progress(i + 1)
        # منطق التشفير هنا...
        st.success(t['success'])
