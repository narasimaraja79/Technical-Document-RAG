
import streamlit as st
import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from rag_pipeline import run_rag_pipeline

# Page configuration
st.set_page_config(
    page_title="Technical Document RAG",
    page_icon="📚",
    layout="wide"
)

# Application title
st.title("📚 Technical Document Question Answering System")
st.write("Ask questions about your technical documents using RAG.")

# Multiple PDF upload
st.subheader("📂 Upload Your PDF Documents")

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

# Save uploaded PDFs
pdf_paths = []

if uploaded_files:

    os.makedirs("data/uploads", exist_ok=True)

    for uploaded_file in uploaded_files:

        st.success(f"Uploaded: {uploaded_file.name}")

        pdf_path = os.path.join(
            "data",
            "uploads",
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        pdf_paths.append(pdf_path)

    st.info(f"{len(pdf_paths)} PDF document(s) saved successfully!")

# User question
# Select document
document_options = ["All Documents"] + [
    os.path.basename(path) for path in pdf_paths
]

import streamlit as st
import sys
import os

# Add src folder to Python path
sys.path.append(
    os.path.join(os.path.dirname(__file__), "src")
)

from rag_pipeline import run_rag_pipeline


# Page configuration
st.set_page_config(
    page_title="Technical Document RAG",
    page_icon="📚",
    layout="wide"
)


# Application title
st.title("📚 Technical Document Question Answering System")

st.write(
    "Ask questions about your technical documents using RAG."
)


# PDF upload section
st.subheader("📂 Upload Your PDF Documents")

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True
)


# Save uploaded PDFs
pdf_paths = []

if uploaded_files:

    os.makedirs("data/uploads", exist_ok=True)

    for uploaded_file in uploaded_files:

        st.success(f"Uploaded: {uploaded_file.name}")

        pdf_path = os.path.join(
            "data",
            "uploads",
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        pdf_paths.append(pdf_path)

    st.info(
        f"{len(pdf_paths)} PDF document(s) saved successfully!"
    )


# Document selection
document_options = ["All Documents"] + [
    os.path.basename(path) for path in pdf_paths
]

selected_document = st.selectbox(
    "Select a document to search:",
    document_options
)

document_name = (
    None
    if selected_document == "All Documents"
    else selected_document
)


# User question
question = st.text_input(
    "Enter your question:"
)


# Ask button
if st.button("Ask"):

    if question.strip():

        with st.spinner("Generating answer..."):

            try:

                # Process uploaded documents
                if pdf_paths:

                    answer, sources = run_rag_pipeline(
                        question,
                        pdf_paths,
                        document_name
                    )

                # Process default document
                else:

                    answer, sources = run_rag_pipeline(
                        question
                    )


                # Display AI answer
                st.subheader("🤖 AI Answer")
                st.write(answer)


                # Display source references
                st.subheader("📄 Source References")

                if sources:

                    seen_sources = set()

                    for source in sources:

                        source_key = (
                            source["document_name"],
                            source["page_number"]
                        )

                        if source_key not in seen_sources:

                            with st.expander(
                                f"📄 {source['document_name']} - Page {source['page_number']}"
                            ):

                                st.write("Retrieved Evidence:")

                                st.write(source["text"])

                            seen_sources.add(source_key)

                else:

                    st.info(
                        "No source references found."
                    )


            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("Please enter a question.")




         