import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


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
    search_kwargs={"k": 10}
)


# ============================================================
# LOCAL LLM
# ============================================================

print("Loading local GenAI model...")

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
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

    question_lower = question.lower()

    # ========================================================
    # SPECIAL: LIST ALL MATERIALS
    # ========================================================

    if "material" in question_lower and (
        "list" in question_lower
        or "available" in question_lower
        or "all" in question_lower
    ):

        documents = vectorstore.similarity_search(
            "furniture materials",
            k=65
        )

        materials = set()

        for document in documents:
            text = document.page_content

            if "Material:" in text:
                material = text.split("Material:")[1].split("Style:")[0].strip()
                materials.add(material)

        if materials:
            result = "Available Materials:\n"

            for i, material in enumerate(sorted(materials), 1):
                result += f"{i}. {material}\n"

            return result

        return "No material information found in the catalog."

    # ========================================================
    # SPECIAL: LIST ALL PRODUCTS
    # ========================================================

    if "product" in question_lower and (
        "list" in question_lower
        or "available" in question_lower
        or "all" in question_lower
    ):

        documents = vectorstore.similarity_search(
            "furniture products",
            k=65
        )

        products = []

        for document in documents:
            text = document.page_content

            if " - " in text:
                first_part = text.split(" - ")[0].strip()

                if first_part.startswith("P"):
                    products.append(first_part)

        products = sorted(set(products))

        if products:
            result = "Available Furniture Products:\n"

            for product in products:
                result += f"- {product}\n"

            return result

        return "No products found in the catalog."

    # ========================================================
    # NORMAL RAG QUESTION
    # ========================================================

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    formatted_prompt = prompt.format(
        context=context,
        question=question
    )

    inputs = tokenizer(
        formatted_prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

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