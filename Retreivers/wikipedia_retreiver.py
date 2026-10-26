from langchain_community.retrievers import WikipediaRetriever

#initialize the retreiver (optional: set of language and top_k)
retreiver = WikipediaRetriever(top_k_results=2, lang="en")

#define the query
query = "political history of india and pakistan from the perspective of china"

#get relevant wiki document
docs = retreiver.invoke(query) 
# runnables are all those functions who have a capability to invoke function


#print retreived content

for i, doc in enumerate(docs):
    print(f"\n ---Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display


































