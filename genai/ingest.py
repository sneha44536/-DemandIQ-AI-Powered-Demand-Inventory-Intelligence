import os

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DOCUMENT_PATH = os.path.join(
    BASE_DIR,
    "genai",
    "documents",
    "product_catalog.txt"
)

VECTORSTORE_PATH = os.path.join(
    BASE_DIR,
    "genai",
    "vectorstore"
)


# ============================================================
# LOAD DOCUMENT
# ============================================================

print("Loading furniture catalog...")

loader = TextLoader(
    DOCUMENT_PATH,
    encoding="utf-8"
)

documents = loader.load()

print(f"Original documents loaded: {len(documents)}")


# ============================================================
# SPLIT PRODUCTS
# ============================================================

print("Splitting product catalog...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Product chunks created: {len(chunks)}")


# ============================================================
# CREATE EMBEDDINGS
# ============================================================

print("Creating embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================================
# CREATE VECTOR DATABASE
# ============================================================

print("Creating Chroma vector database...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=VECTORSTORE_PATH
)


# ============================================================
# COMPLETED
# ============================================================

print("==========================================")
print("RAG INGESTION COMPLETED")
print("==========================================")

print(f"Products/Chunks stored: {len(chunks)}")
print(f"Vector database: {VECTORSTORE_PATH}")