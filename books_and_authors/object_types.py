from graphene_django import DjangoObjectType
from books_and_authors.booksAndAuthors.models import Book, Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"

