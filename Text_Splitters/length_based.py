from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# loader = PyPDFLoader('Shivani Chauhan_resume.pdf')

# text = """ """

# Get the folder where text_loader.py is located
file_path = Path(__file__).parent / "abc.pdf"

loader = PyPDFLoader(str(file_path))

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=0,    #  Overlapping of characters between the chunks
    separator='' 
)

result = splitter.split_documents(docs)

print(result[10].page_content)


















