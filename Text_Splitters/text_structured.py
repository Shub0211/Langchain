from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """ 

"""



splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=0,    #  Overlapping of characters between the chunks
    # separator='' 
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)





























