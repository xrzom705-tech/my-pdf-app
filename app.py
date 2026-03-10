import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pdfplumber
import io

# 1. إعدادات الصفحة
st.set_page_config(page_title="PDF Elite - All-in-One Tools", layout="wide", page_icon="💎")

# 2. تصميم CSS احترافي (Modern UI)
st.markdown("""
    <style>
    /* تنسيق الخلفية العامة */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* تصميم البطاقات (Cards) */
    .tool-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
        border: 1px solid #e1e4e8;
        margin-bottom: 20px;
    }
    
    .tool-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        border-color: #007bff;
    }

    .tool-icon {
        font-size: 50px;
        margin-bottom: 15px;
    }

    /* تنسيق الأزرار */
    .stButton>button {
        background: linear-gradient(90deg, #007bff 0%, #00d4ff 100%);
        color: white;
        border-radius: 30px;
        border: none;
        padding: 10px 25px;
        font-weight: 600;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر (العنوان الرئيسي)
st.markdown("<h1 style='text-align: center; color: #1e3a8a; font-size: 3rem;'>💎 PDF Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 1.2rem;'>Fast, Secure, and Professional PDF Tools</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. الحالة الافتراضية للتنقل (بدون قائمة جانبية بدائية)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_home():
    st.session_state.page = 'home'

# --- الصفحة الرئيسية (توزيع الأدوات) ---
if st.session_state.page == 'home':
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""<div class='tool-card'><div class='tool-icon'>📑</div><h3>Merge PDF</h3><p>Combine multiple files into one document.</p></div>""", unsafe_allow_html=True)
        if st.button("Open Merge Tool"):
            st.session_state.page = 'merge'
            st.rerun()

    with col2:
        st.markdown("""<div class='tool-card'><div class='tool-icon'>✂️</div><h3>Split PDF</h3><p>Separate pages into individual files.</p></div>""", unsafe_allow_html=True)
        if st.button("Open Split Tool"):
            st.session_state.page = 'split'
            st.rerun()

    with col3:
        st.markdown("""<div class='tool-card'><div class='tool-icon'>🔒</div><h3>Protect PDF</h3><p>Secure your documents with a password.</p></div>""", unsafe_allow_html=True)
        if st.button("Open Lock Tool"):
            st.session_state.page = 'lock'
            st.rerun()

# --- صفحة دمج الملفات ---
elif st.session_state.page == 'merge':
    st.button("⬅ Back to Menu", on_click=go_home)
    st.title("📑 Merge PDF Files")
    files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
    if files and st.button("Start Merging"):
        merger = PdfMerger()
        for f in files: merger.append(f)
        out = io.BytesIO()
        merger.write(out)
        st.success("Documents Merged Successfully!")
        st.download_button("📥 Download Result", out.getvalue(), "merged_elite.pdf")

# --- صفحة تقسيم الملفات ---
elif st.session_state.page == 'split':
    st.button("⬅ Back to Menu", on_click=go_home)
    st.title("✂️ Split PDF Pages")
    file = st.file_uploader("Upload PDF", type="pdf")
    if file and st.button("Split Now"):
        reader = PdfReader(file)
        for i in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[i])
            out = io.BytesIO()
            writer.write(out)
            st.download_button(f"Page {i+1}", out.getvalue(), f"p_{i+1}.pdf")

# --- صفحة حماية الملفات ---
elif st.session_state.page == 'lock':
    st.button("⬅ Back to Menu", on_click=go_home)
    st.title("🔒 Protect PDF")
    file = st.file_uploader("Upload PDF", type="pdf")
    pwd = st.text_input("Set Password", type="password")
    if file and pwd and st.button("Lock File"):
        writer = PdfWriter()
        for p in PdfReader(file).pages: writer.add_page(p)
        writer.encrypt(pwd)
        out = io.BytesIO()
        writer.write(out)
        st.download_button("📥 Download Protected PDF", out.getvalue(), "locked.pdf")

