from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


doc1 = Document(
    page_content="",
    metadata={}
)

doc2 = Document(
    page_content="",
    metadata={}
)

doc3 = Document(
    page_content="",
    metadata={}
)

doc4 = Document(
    page_content="",
    metadata={}
)

doc5 = Document(
    page_content="",
    metadata={}
)

docs = [doc1, doc2, doc3, doc4, doc5]

vectore_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory='mychroma_db',
    collection_name='sample'
)

#add documents
ad = vectore_store.add_documents(docs)

# each document assigned a new id

#view documents
# vectore_store.get(include=['embeddings,'documents','metadatas'])
vectore_store.get(include=['embeddings','documents','metadatas'])

#search documents
sd = vectore_store.similarity_search(
    query='Who among these are a bowler?',
    k=2 #how many similar objects/documents or there corresponding document we want to show
)


#search with similarity score
ss = vectore_store.similarity_search_with_score( #show score against each result
    query='who among these are a bowler?',
    k=2
)

#metadata filtering
ss_filter = vectore_store.similarity_search_with_score( #show score against each result
    query='',
    filter={'team':'CSK'}
)

#update documents
update_doc1= Document(
    page_content="virat kohli, the former captain of RCB",
    metadata={"team":"RCB"}
)

vectore_store.update_document(document_id='fdhgv-hghgsy-hshsdb-ahjhjj', document=updated_doc1)

#delete_document
vectore_store.delete(ids='sgjhkisu-jsijsuh-nksjisji')

#view document
vectore_store.get(include=['embeddings','documents','metadatas'])




























