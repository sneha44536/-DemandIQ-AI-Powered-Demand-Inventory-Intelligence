import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from transformers import pipeline


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

VECTORSTORE_DIR = os.path.join(
    BASE_DIR,
    "genai",
    "vectorstore"
)


# ============================================================
# EMBEDDINGS
# ============================================================

print("Loading embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================================
# LOAD VECTOR DATABASE
# ============================================================

print("Loading furniture vector database...")

vectorstore = Chroma(
    persist_directory=VECTORSTORE_DIR,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


# ============================================================
# LOCAL LLM
# ============================================================

print("Loading local GenAI model...")

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)


# ============================================================
# PROMPT
# ============================================================

prompt = ChatPromptTemplate.from_template(
    """
You are an AI Furniture Business Assistant.

Use the following furniture catalog information to answer
the user's question.

CONTEXT:
{context}

QUESTION:
{question}

Give a clear and useful business answer.
If the answer is not available in the context,
say that the information is not available in the catalog.
"""
)


# ============================================================
# RAG FUNCTION
# ============================================================

def ask_question(question):

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    formatted_prompt = prompt.format(
        context=context,
        question=question
    )

    response = generator(
        formatted_prompt
    )[0]["generated_text"]

    return response


# ============================================================
# CHAT INTERFACE
# ============================================================

print()
print("========================================")
print("   AI FURNITURE GENAI ASSISTANT")
print("========================================")
print()
print("Type 'exit' to stop.")
print()

while True:

    question = input("Ask your question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question.strip():
        continue

    print()
    print("AI:")
    print(ask_question(question))
    print()