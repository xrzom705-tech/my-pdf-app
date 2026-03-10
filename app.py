import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pdfplumber
import io

# 1. إعدادات الصفحة وهوية الموقع
st.set_page_config(page_title="PDF Pro - Advanced Tools", layout="wide", page_icon="🚀")

# 2. إضافة لمسات CSS لتحسين الشكل (جماليات الموقع)
st.markdown("""
    <style>
    /* تغيير خلفية الموقع وتنسيق الخطوط */
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border: none;
        transform: scale(1.02);
    }
    .css-1kyxreq {
        justify-content: center;
    }
    /* تنسيق العناوين */
    h1 {
        color: #00d4ff;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .st-emotion-cache-16idsys p {
        font-size: 1.1rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية بشكل أنيق
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=100)
    st.title("PDF Master")
    st.markdown("---")
    choice = st.radio("CHOOSE A TOOL:", 
        ["✨ Merge PDF", "✂️ Split PDF", "🔒 Protect PDF", "🔍 Extract Text"])
    st.markdown("---")
    st.write("Developed by **Bandar**")

# --- وظيفة دمج الملفات ---
if choice == "✨ Merge PDF":
    st.markdown("<h1>✨ Merge Your PDF Files</h1>", unsafe_allow_html=True)
    st.write("Combine multiple documents into one professional file instantly.")
    
    files = st.file_uploader("", type="pdf", accept_multiple_files=True)
    
    if files:
        st.info(f"You have selected {len(files)} files.")
        if st.button("PROCEED & MERGE"):
            with st.spinner('Working on it...'):
                merger = PdfMerger()
                for f in files:
                    merger.append(f)
                output = io.BytesIO()
                merger.write(output)
                st.success("Your merged PDF is ready!")
                st.download_button("📥 Download Merged File", output.getvalue(), "merged_pro.pdf")

# --- وظيفة تقسيم الملفات ---
elif choice == "✂️ Split PDF":
    st.markdown("<h1>✂️ Split PDF Pages</h1>", unsafe_allow_html=True)
    file = st.file_uploader("Upload the file you want to split", type="pdf")
    if file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        st.write(f"This PDF has **{num_pages}** pages.")
        
        if st.button("SPLIT ALL PAGES"):
            for i in range(num_pages):
                writer = PdfWriter()
                writer.add_page(reader.pages[i])
                out = io.BytesIO()
                writer.write(out)
                st.download_button(f"Download Page {i+1}", out.getvalue(), f"page_{i+1}.pdf")

# --- وظيفة حماية الملف ---
elif choice == "🔒 Protect PDF":
    st.markdown("<h1>🔒 Secure Your PDF</h1>", unsafe_allow_html=True)
    file = st.file_uploader("Upload PDF to add password", type="pdf")
    password = st.text_input("Set your secret password", type="password")
    
    if file and password:
        if st.button("ENCRYPT FILE"):
            reader = PdfReader(file)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            out = io.BytesIO()
            writer.write(out)
            st.success("File encrypted successfully!")
            st.download_button("📥 Download Protected PDF", out.getvalue(), "secure_file.pdf")

# --- وظيفة استخراج النصوص ---
elif choice == "🔍 Extract Text":
    st.markdown("<h1>🔍 PDF Text Extractor</h1>", unsafe_allow_html=True)
    file = st.file_uploader("Upload PDF to copy text", type="pdf")
    if file:
        with pdfplumber.open(file) as pdf:
            all_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"
        
        if all_text:
            st.text_area("Content:", all_text, height=300)
            st.download_button("📥 Save as Text File", all_text, "text_content.txt")
        else:
            st.error("Could not find any text in this file.")

