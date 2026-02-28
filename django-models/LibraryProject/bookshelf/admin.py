from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a search bar to search by title or author
    search_fields = ('title', 'author')
    
    # Add a sidebar filter for the publication year
    list_filter = ('publication_year',)