from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA


#load the documents from the .txt file
loader =  TextLoader('sample.txt') # Ensure that the file path is correct and the file exists
documents = loader.load()

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = text_splitter.split_documents(documents)

# Convert the text chunks into embeddings and store them in a FAISS vector store
vectorstore = FAISS.from_documents(chunks, OpenAIEmbeddings())

#create a retriever from the vector store(fetches relevant documnents based on the query)
retriever = vectorstore.as_retriever()

# # Mnaually Retreive Relevant documents
# query = "What is the main topic of the document?"
# relevant_documents = retriever.get_relevant_documents(query)

# #Combine Retreived Text into a single prompt
# retreived_text = "\n ".join([doc.page_content for doc in relevant_documents])

#Initialize the LLM
llm = OpenAI(model_name='text-davinci-003', temperature=0.9)


#Create Retreive QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retreiver=retriever)

#Manually pass retreived text to the LLM for processing
prompt = f"Based on the following text, answer the question"
answer = qa_chain.run(prompt)

#print the answer
print("Answer:", answer)
































































