from langchain_community.vectorstores import FAISS 
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever


all_docs = [
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""}),
    Document(page_content="", metadata={"":""})
]


embedding_model = OpenAIEmbeddings()

vector_store = FAISS.from_documents(documents=all_docs, embedding=embedding_model)

# normal retreiver
similarity_retreiver = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# multi query reteriver

multi_query_retreiver = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k":5}),
    llm=ChatOpenAI(model="gpt-3.5-turbo")
)

#query 
query = "how to improve energy levels and maintain balance"


#retreiver result
similarity_result = similarity_retreiver.invoke(query)
multi_query_result = multi_query_retreiver.invoke(query)

for i, doc in enumerate(similarity_result):
    print(f"\n ---Result {i+1} ---")
    print(doc.page_content)


for i, doc in enumerate(multi_query_result):
    print(f"\n ---Result {i+1} ---")
    print(doc.page_content)


























