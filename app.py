import streamlit as st
from PyPDF2 import PdfMerger
import io

st.set_page_config(page_title="Quick PDF Merger", layout="centered")

st.title("📄 Quick PDF Merger")
st.write("The simplest way to combine your PDF documents online for free.")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button("Merge Files"):
        merger = PdfMerger()
        for pdf in uploaded_files:
            merger.append(pdf)
        
        output = io.BytesIO()
        merger.write(output)
        merger.close()
        
        st.success("Your PDF is ready!")
        st.download_button(
            label="Download Now",
            data=output.getvalue(),
            file_name="merged_by_bandar.pdf",
            mime="application/pdf"
        )