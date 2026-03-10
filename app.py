import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pdfplumber
import io

# 1. إعدادات الصفحة المتقدمة
st.set_page_config(page_title="PDF Global - Smart Tools", layout="wide", page_icon="🌐")

# 2. نظام اللغات (العربية والإنجليزية)
languages = {
    "English": {
        "title": "💎 PDF Global Elite",
        "subtitle": "Professional & Secure PDF Solutions",
        "merge_title": "Merge PDF",
        "merge_desc": "Combine multiple files into one.",
        "split_title": "Split PDF",
        "split_desc": "Separate pages into individual files.",
        "lock_title": "Protect PDF",
        "lock_desc": "Secure your documents with a password.",
        "btn_open": "Open Tool",
        "btn_back": "⬅ Back to Menu",
        "success": "Task completed successfully!",
        "error": "An error occurred with the file. Please try again."
    },
    "العربية": {
        "title": "💎 بي دي إف جلوبال",
        "subtitle": "حلول PDF احترافية وآمنة",
        "merge_title": "دمج الملفات",
        "merge_desc": "دمج عدة ملفات في مستند واحد.",
        "split_title": "تقسيم الملفات",
        "split_desc": "فصل الصفحات إلى ملفات مستقلة.",
        "lock_title": "حماية الملفات",
        "lock_desc": "تأمين مستنداتك بكلمة مرور.",
        "btn_open": "افتح الأداة",
        "btn_back": "⬅ العودة للقائمة",
        "success": "تمت العملية بنجاح!",
        "error": "حدث خطأ في الملف، يرجى المحاولة مرة أخرى."
    }
}

# اختيار اللغة (يمكن للمستخدم التغيير يدوياً أيضاً)
lang_choice = st.sidebar.selectbox("Language / اللغة", ["English", "العربية"])
texts = languages[lang_choice]

# 3. تصميم CSS احترافي يدعم الجهتين (RTL & LTR)
alignment = "right" if lang_choice == "العربية" else "left"
direction = "rtl" if lang_choice == "العربية" else "ltr"

st.markdown(f"""
    <style>
    .stApp {{
        direction: {direction};
        text-align: {alignment};
        background: #f8fafc;
    }}
    .tool-card {{
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
        height: 200px;
    }}
    .stButton>button {{
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. الهيكل الرئيسي
st.markdown(f"<h1 style='text-align: center; color: #1e3a8a;'>{texts['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #64748b;'>{texts['subtitle']}</p>", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"<div class='tool-card'><h3>📑 {texts['merge_title']}</h3><p>{texts['merge_desc']}</p></div>", unsafe_allow_html=True)
        if st.button(texts['btn_open'], key="m1"): 
            st.session_state.page = 'merge'
            st.rerun()

    with col2:
        st.markdown(f"<div class='tool-card'><h3>✂️ {texts['split_title']}</h3><p>{texts['split_desc']}</p></div>", unsafe_allow_html=True)
        if st.button(texts['btn_open'], key="s1"): 
            st.session_state.page = 'split'
            st.rerun()

    with col3:
        st.markdown(f"<div class='tool-card'><h3>🔒 {texts['lock_title']}</h3><p>{texts['lock_desc']}</p></div>", unsafe_allow_html=True)
        if st.button(texts['btn_open'], key="l1"): 
            st.session_state.page = 'lock'
            st.rerun()

# --- المنطق البرمجي للأدوات مع معالجة الأخطاء ---
elif st.session_state.page == 'merge':
    st.button(texts['btn_back'], on_click=lambda: setattr(st.session_state, 'page', 'home'))
    files = st.file_uploader(texts['merge_title'], type="pdf", accept_multiple_files=True)
    if files and st.button("Start"):
        try:
            merger = PdfMerger()
            for f in files: merger.append(f)
            out = io.BytesIO()
            merger.write(out)
            st.success(texts['success'])
            st.download_button("Download", out.getvalue(), "merged.pdf")
        except:
            st.error(texts['error'])

elif st.session_state.page == 'split':
    st.button(texts['btn_back'], on_click=lambda: setattr(st.session_state, 'page', 'home'))
    file = st.file_uploader(texts['split_title'], type="pdf")
    if file and st.button("Start"):
        try:
            reader = PdfReader(file)
            for i in range(len(reader.pages)):
                writer = PdfWriter(); writer.add_page(reader.pages[i])
                out = io.BytesIO(); writer.write(out)
                st.download_button(f"Page {i+1}", out.getvalue(), f"p{i+1}.pdf")
        except:
            st.error(texts['error'])

elif st.session_state.page == 'lock':
    st.button(texts['btn_back'], on_click=lambda: setattr(st.session_state, 'page', 'home'))
    file = st.file_uploader(texts['lock_title'], type="pdf")
    pwd = st.text_input("Password", type="password")
    if file and pwd and st.button("Lock"):
        try:
            writer = PdfWriter()
            for p in PdfReader(file).pages: writer.add_page(p)
            writer.encrypt(pwd)
            out = io.BytesIO(); writer.write(out)
            st.download_button("Download", out.getvalue(), "locked.pdf")
        except:
            st.error(texts['error'])
