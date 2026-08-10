import os

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


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

print(f"Documents loaded: {len(documents)}")


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
    documents=documents,
    embedding=embeddings,
    persist_directory=VECTORSTORE_PATH
)


print("==========================================")
print("RAG INGESTION COMPLETED")
print("==========================================")
print("Vector database created successfully!")
print(f"Location: {VECTORSTORE_PATH}")