from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian.name
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library {library_name}"

# Sample usage
if __name__ == "__main__":
    print(get_books_by_author("George Orwell"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))

