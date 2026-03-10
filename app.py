import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pdfplumber
import io

# Page Configuration
st.set_page_config(page_title="Smart PDF Tools", layout="wide")

# Sidebar Navigation
st.sidebar.title("🛠️ PDF Toolbox")
choice = st.sidebar.radio("Select a Tool:", 
    ["Merge PDF", "Split PDF", "Protect PDF (Password)", "Extract Text", "About"])

# --- 1. MERGE PDF ---
if choice == "Merge PDF":
    st.title("📄 Merge Multiple PDFs")
    st.write("Combine several PDF files into one single document.")
    files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    if files and st.button("Merge Now"):
        merger = PdfMerger()
        for f in files:
            merger.append(f)
        output = io.BytesIO()
        merger.write(output)
        st.success("Done!")
        st.download_button("Download Merged PDF", output.getvalue(), "merged.pdf")

# --- 2. SPLIT PDF ---
elif choice == "Split PDF":
    st.title("✂️ Split PDF Pages")
    st.write("Extract each page of a PDF into a separate file.")
    file = st.file_uploader("Upload PDF", type="pdf")
    if file and st.button("Split Pages"):
        reader = PdfReader(file)
        for i in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[i])
            out = io.BytesIO()
            writer.write(out)
            st.download_button(f"Download Page {i+1}", out.getvalue(), f"page_{i+1}.pdf")

# --- 3. PROTECT PDF ---
elif choice == "Protect PDF (Password)":
    st.title("🔒 Protect PDF with Password")
    file = st.file_uploader("Upload PDF to Encrypt", type="pdf")
    password = st.text_input("Enter Password", type="password")
    if file and password and st.button("Encrypt Now"):
        reader = PdfReader(file)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        out = io.BytesIO()
        writer.write(out)
        st.success("File Protected!")
        st.download_button("Download Protected PDF", out.getvalue(), "protected.pdf")

# --- 4. EXTRACT TEXT ---
elif choice == "Extract Text":
    st.title("🔍 Extract Text from PDF")
    st.write("Copy the text content from your PDF files.")
    file = st.file_uploader("Upload PDF", type="pdf")
    if file:
        with pdfplumber.open(file) as pdf:
            all_text = ""
            for page in pdf.pages:
                all_text += page.extract_text() + "\n"
        st.text_area("Extracted Text:", all_text, height=300)
        st.download_button("Download as TXT", all_text, "extracted_text.txt")

# --- ABOUT ---
elif choice == "About":
    st.title("About Smart PDF Tools")
    st.info("A fast, secure, and free tool for all your PDF needs. Created by Bandar.")
