from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)


document = [
    "Virat kohli is the number 1 batter in the world",
    "MS DHoni is the number 1 captain in the world",
    "Sachin Tendulkar is the number 1 fielder in the world",
    "Jasprit bumrah is the number 1 bowler in the world",
    "Rohit sharma is the number 1 opening batsman in the world"
]


query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)


scores = cosine_similarity([query_embedding], doc_embeddings)

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(document[index])

print("similarity score is ", score)




















