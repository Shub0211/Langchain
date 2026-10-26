from langchain_community.vectorstores import FAISS 
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever


docs = [
    Document(page_content=(""), metadata = {"source":"Doc1"}),
    Document(page_content=(""), metadata = {"source":"Doc2"}),
    Document(page_content=(""), metadata = {"source":"Doc3"}),
    Document(page_content=(""), metadata = {"source":"Doc4"})
]

# initialize open ai embeddings
embedding_model = OpenAIEmbeddings()


# create the faiss vector store from documents
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

#base retreiver - prerequisite for contextual compression retreiver
base_retreiver = vector_store.as_retriever(search_kwargs={'k':5})

#set up the comprressor using an LLM - prerequisite for contextual compression retreiver
llm = ChatOpenAI(model="gpt-3.5-turbo")
compressor = LLMChainExtractor.from_llm(llm)

# create the contextual compression retreiver

compression_retreiver = ContextualCompressionRetriever(
    base_retriever=base_retreiver,
    base_compressor=compressor
)

#query the retreiver

query = "what is photosynthesis"

compressor_result = compression_retreiver.invoke(query)

for i, doc in enumerate(compressor_result):
    print(f"\n ---Result {i+1} ---")
    print(doc.page_content)


















