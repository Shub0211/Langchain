from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """ 
Contributed to the Deutsche Bank migration project, supporting end-to-end application and data migration activities.
Developed and executed migration utilities, data validation scripts, and test scripts to streamline migration activities.
Implemented and validated configuration changes across product-specific APIs.
Performed end-to-end migration data testing and validation to ensure data accuracy and integrity.
Extracted code review reports from Bitbucket and supported deployment activities.
Troubleshot and analyzed data and application issues, identifying root causes and implementing performance improvements.
Worked with Oracle, MySQL, and MS SQL Server databases for data analysis, validation, and migration support.
Designed robust technical solutions to mitigate failure scenarios and resolve complex migration issues.
Executed system upgrades, migration activities, and associated test plans.
Analyzed and modified application code to support upgrade and migration requirements, and developed utilities to simplify and accelerate migration analysis.
"""



splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=0,    #  Overlapping of characters between the chunks
    # separator='' 
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)





























