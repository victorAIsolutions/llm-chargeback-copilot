import os
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone.vectorstores import PineconeVectorStore

# Initialize Pinecone client (Serverless)
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    spec=ServerlessSpec(
        cloud="aws",
        region=os.getenv("PINECONE_ENV_REGION", "us-east1-gcp")
    )
)

# Reference or create index
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
# Assuming index already exists
index = pc.Index(INDEX_NAME)


def classify_documents(texts):
    """Classify each document by retrieving the top semantic match from Pinecone."""
    # Initialize embeddings via langchain-openai
    embeddings = OpenAIEmbeddings()

    # Build LangChain PineconeVectorStore
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        text_key="text"
    )

    predictions = []
    for text in texts:
        docs = vector_store.similarity_search(text, k=1)
        if docs:
            predictions.append(docs[0].metadata.get("category", "unknown"))
        else:
            predictions.append("unknown")
    return predictions