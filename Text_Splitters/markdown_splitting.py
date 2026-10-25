from langchain_text_splitters import RecursiveCharacterTextSplitter, Language



text = """
# Introduction to Python

## What Is Python?
Python is a high-level, interpreted programming language.
It is popular because of its simple syntax and readability.

## Python Features
Python supports object-oriented, procedural, and functional programming.
It provides dynamic typing and automatic memory management.
Python is widely used in web development, automation, and data science.

## Python Data Types
Python includes integers, floats, strings, booleans, lists, tuples, and dictionaries.
Lists are mutable, whereas tuples are immutable.
Dictionaries store data in key-value pairs.

## Control Flow
Conditional statements include `if`, `elif`, and `else`.
Loops such as `for` and `while` help repeat operations.
Functions are defined using the `def` keyword.

## Object-Oriented Programming
Classes define the structure and behaviour of objects.
Inheritance allows one class to reuse features of another class.
Encapsulation and polymorphism are important OOP concepts.

## Python Libraries
NumPy supports numerical computing and array operations.
Pandas is used for data manipulation and analysis.
FastAPI helps developers build modern APIs using Python.

## Conclusion
Python is an excellent language for beginners and experienced developers.
Regular practice with coding problems improves Python
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,  
    chunk_size = 400,
    chunk_overlap= 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[0])















































