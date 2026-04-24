from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file):
    loader = PyPDFLoader(file)
    pages = loader.load()
    return pages