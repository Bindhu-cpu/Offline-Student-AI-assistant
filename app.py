import streamlit as st
from utils.chatbot import get_response
from utils.pdf_reader import load_pdf

st.title("📚 Offline Student AI Assistant")

mode = st.selectbox("Choose Mode", ["Chat", "PDF"])


if mode == "Chat":
    st.markdown("### 💬 Ask your doubts below:")
    
    user_input = st.text_input("Ask something:")
    
    if user_input:
        with st.spinner("Thinking..."):
            response = get_response( user_input)
            st.write(response)
            
elif mode == "PDF":
    uploaded_file = st.file_uploader("Upload PDF")

    if uploaded_file:
        pages = load_pdf(uploaded_file.name)
        st.write("PDF Loaded Successfully!")

        question = st.text_input("Ask about PDF:")
        if question:
            response = get_response( question)
            st.write(response)