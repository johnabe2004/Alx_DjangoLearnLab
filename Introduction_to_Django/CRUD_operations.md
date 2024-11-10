```python
# Open the Django shell
python manage.py shell

# Command to create a Book instance
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output
# <Book: 1984>

#### **Retrieve Operation**

- **Command**: Retrieve and display all attributes of the created book.
- **File**: `retrieve.md`

```markdown
# retrieve.md

```python
# Open the Django shell
python manage.py shell

# Command to retrieve the created book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output
# ('1984', 'George Orwell', 1949)


#### **Update Operation**

- **Command**: Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.
- **File**: `update.md`

```markdown
# update.md

```python
# Open the Django shell
python manage.py shell

# Command to update the title of the book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Expected Output
# 'Nineteen Eighty-Four'
#### **Delete Operation**

- **Command**: Delete the book instance and confirm deletion by trying to retrieve all books.
- **File**: `delete.md`

```markdown
# delete.md

```python
# Open the Django shell
python manage.py shell

# Command to delete the book
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
Book.objects.all()
# Expected Output
# <QuerySet []>


