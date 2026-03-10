import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import io

# 1. إعدادات الصفحة
st.set_page_config(page_title="PDF Elite - Color Edition", layout="wide", page_icon="🎨")

# 2. اللغات (عربي وانجليزي)
languages = {
    "English": {
        "title": "💎 PDF Global Pro",
        "subtitle": "Clear. Fast. Professional.",
        "merge": "Merge PDF", "split": "Split PDF", "lock": "Protect PDF", "del": "Delete Pages",
        "btn": "Open Tool", "back": "⬅ Back", "start": "Process Now"
    },
    "العربية": {
        "title": "💎 بي دي إف برو",
        "subtitle": "وضوح. سرعة. احترافية.",
        "merge": "دمج الملفات", "split": "تقسيم الملفات", "lock": "حماية الملفات", "del": "حذف صفحات",
        "btn": "افتح الأداة", "back": "⬅ عودة", "start": "ابدأ الآن"
    }
}

lang = st.sidebar.selectbox("Language / اللغة", ["العربية", "English"])
t = languages[lang]
dir = "rtl" if lang == "العربية" else "ltr"

# 3. تصميم الألوان والتباين (CSS)
st.markdown(f"""
    <style>
    /* تحسين لون الخلفية العام */
    .stApp {{
        background-color: #F0F2F6;
        direction: {dir};
    }}
    /* نصوص العناوين - لون كحلي غامق جداً للبروز */
    h1, h2, h3 {{
        color: #1A1A1A !important;
        font-weight: 800 !important;
    }}
    /* نصوص الوصف - رمادي غامق وواضح */
    p {{
        color: #333333 !important;
        font-size: 1.1rem;
    }}
    /* بطاقات الأدوات بألوان حدود مختلفة */
    .card {{
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #007BFF; /* لون افتراضي */
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }}
    /* تلوين الأزرار بناءً على النوع */
    .stButton>button {{
        border-radius: 12px;
        height: 3em;
        font-weight: bold;
        transition: 0.3s;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. الهيدر
st.markdown(f"<h1 style='text-align: center;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{t['subtitle']}</p>", unsafe_allow_html=True)
st.markdown("---")

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- القائمة الرئيسية بتنسيق ملون ---
if st.session_state.page == 'home':
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f"<div class='card' style='border-top-color: #28a745;'><h3>📑 {t['merge']}</h3><p>Combine multiple PDFs</p></div>", unsafe_allow_html=True)
        if st.button(t['btn'], key="m"): st.session_state.page = 'merge'; st.rerun()

    with c2:
        st.markdown(f"<div class='card' style='border-top-color: #dc3545;'><h3>✂️ {t['split']}</h3><p>Extract individual pages</p></div>", unsafe_allow_html=True)
        if st.button(t['btn'], key="s"): st.session_state.page = 'split'; st.rerun()

    with c3:
        st.markdown(f"<div class='card' style='border-top-color: #ffc107;'><h3>🔒 {t['lock']}</h3><p>Add secure password</p></div>", unsafe_allow_html=True)
        if st.button(t['btn'], key="l"): st.session_state.page = 'lock'; st.rerun()

# --- الصفحات الداخلية (مثال الدمج) ---
elif st.session_state.page == 'merge':
    if st.button(t['back']): st.session_state.page = 'home'; st.rerun()
    st.subheader(t['merge'])
    files = st.file_uploader("Choose Files", type="pdf", accept_multiple_files=True)
    if files and st.button(t['start']):
        merger = PdfMerger()
        for f in files: merger.append(f)
        out = io.BytesIO(); merger.write(out)
        st.success("Success!")
        st.download_button("Download", out.getvalue(), "merged.pdf")

# (بقية الأدوات تتبع نفس التنسيق)
