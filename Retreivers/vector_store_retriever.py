from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


#step 1 : Source documents

documents = [
    Document(page_content=""),
    Document(page_content=""),
    Document(page_content=""),
    Document(page_content="")
]


# step 2 -Initialize the embedding model
embedding_model = OpenAIEmbeddings()

# step 3 - create chroma vector store in memmory
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

#step 4 - convert vector store into a retreiver
retreiver = vector_store.as_retriever(search_kwargs={"k":2})

query = 'what is chroma used for?'

results = retreiver.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
















































