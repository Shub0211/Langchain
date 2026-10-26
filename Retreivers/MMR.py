from langchain_community.vectorstores import FAISS 
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

docs = [
    Document(page_content="Langchain makes it easy to work with LLMs"),
    Document(page_content="Langchain is used to build LLM based apps"),
    Document(page_content="Chroma is used to store and search document embeddings"),
    Document(page_content="Embeddings are vector representation of text"),
    Document(page_content="MMR helps you get diverse results when doing similarity search"),
    Document(page_content="Langchain supports Chroma, FAISS, Pinecone, and more"),

]

# initialize open ai embeddings
embedding_model = OpenAIEmbeddings()


# create the faiss vector store from documents
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

#enable MMR in the rtetreiver

retreiver = vector_store.as_retriever(
    search_type = "mmr",                #this enables MMR
    search_kwargs={"k":3, "lambda_mult":1} # k = top results, lambda_mult= relevance-diversity balance | if 1 then mmr behaves as similarity search but if value 0 the most diverse result. Value lies between 0 and 1.
)

query="what is langchain?"
results = retreiver.invoke(query)

for i, doc in enumerate(results):
    print(f"\n ---Result {i+1} ---")
    print(doc.page_content)



































