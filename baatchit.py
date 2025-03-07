import pinecone
from  pinecone import Pinecone , ServerlessSpec
import os
from dotenv import load_dotenv
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def bott(search_query):

    load_dotenv()
    PINECONE_API_KEY = os.getenv("PINE_CONE_API")  # Ensure this is set
    # print(PINECONE_API_KEY)
    # Initialize Pinecone
    # pinecone.init(api_key=PINECONE_API_KEY, environment="us-east-1")  # Replace with your values
    pc = Pinecone(
    api_key=PINECONE_API_KEY
    )

    index = pc.Index("olympicdata")

    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # Query Example: Use an embedding vector to search
    query_embedding = embedding_model.embed_query(search_query)
    result = index.query(vector=query_embedding, top_k=2, include_metadata=True)

    ans = result.to_dict()#['matches'][0]['metadata']['text'] # type: ignore

    return ans
