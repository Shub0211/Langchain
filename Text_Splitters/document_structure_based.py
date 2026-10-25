from langchain_text_splitters import RecursiveCharacterTextSplitter, Language



text = """

"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,   #python based text splitter. Same way can be splitted with different kind of language
    chunk_size = 300,
    chunk_overlap= 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[1])















































