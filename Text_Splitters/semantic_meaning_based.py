from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation", 
    breakpoint_threshold_amount=1   # will test for accuracy %
)

sample = """
    Contributed to the Deutsche Bank migration project, supporting end-to-end application and data migration activities.
Developed and executed migration utilities, data validation scripts, and test scripts to streamline migration activities.
Implemented and validated configuration changes across product-specific APIs.
Primary Technologies: Python, AWS, Generative AI, RAG, Agentic AI, LLMs Secondary Technologies: .NET Core, ASP.NET, MVC, C#, JavaScript, HTML5, CSS3
Performed end-to-end migration data testing and validation to ensure data accuracy and integrity.
Extracted code review reports from Bitbucket and supported deployment activities.
Troubleshot and analyzed data and application issues, identifying root causes and implementing performance improvements.
Worked with Oracle, MySQL, and MS SQL Server databases for data analysis, validation, and migration support.
Designed robust technical solutions to mitigate failure scenarios and resolve complex migration issues.
Executed system upgrades, migration activities, and associated test plans.
Analyzed and modified application code to support upgrade and migration requirements, and developed utilities to simplify and accelerate migration analysis.

"""
docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)































