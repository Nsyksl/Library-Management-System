#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(",")
            st.write(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self, title, author, release_year, num_pages):
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)

    def remove_book(self, title):
        self.file.seek(0)
        books = self.file.readlines()
        if not any(title in book for book in books):
            st.write("The book you want to remove does not exist.")
            return

        new_books = []
        for book in books:
            if title not in book:
                new_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(new_books)
        st.write("Book removed successfully.")

    def download_books_txt(self):
        with open(self.file_name, "r") as file:
            data = file.read()
        st.download_button(
            label="Download Books.txt",
            data=data,
            file_name="Books.txt",
            mime="text/plain",
        )


# Create Library object
lib = Library("books.txt")

# Sidebar
st.sidebar.title("Library Management System")
menu_choice = st.sidebar.selectbox("Menu", ["List Books", "Add Book", "Remove Book", "Download"])

# Main content
st.title("Library Management System")

if menu_choice == "List Books":
    st.header("List Books")
    lib.list_books()
elif menu_choice == "Add Book":
    st.header("Add Book")
    title = st.text_input("Enter book title:")
    author = st.text_input("Enter book author:")
    release_year = st.number_input("Enter release year:", min_value=0, step=1)
    num_pages = st.number_input("Enter number of pages:", min_value=0, step=1)
    if st.button("Add Book"):
        lib.add_book(title, author, release_year, num_pages)
        st.success("Book added successfully.")
elif menu_choice == "Remove Book":
    st.header("Remove Book")
    title = st.text_input("Enter the title of the book you want to remove:")
    if st.button("Remove Book"):
        lib.remove_book(title)
elif menu_choice == "Download":
    lib.download_books_txt()


# In[4]:





# In[ ]:




