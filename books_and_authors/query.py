import graphene
from .object_types import BookType, AuthorType
from books_and_authors.booksAndAuthors.models import Book, Author

class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    authors = graphene.List(AuthorType)
    book = graphene.Field(BookType, id = graphene.Int(required=True))
    author = graphene.Field(AuthorType, id = graphene.Int(required=True))

    def resolve_books(root, info):
        return Book.objects.all()

    def resolve_authors(root, info):
        return Author.objects.all()

    def resolve_book(root, info, id):
        return Book.objects.all().filter(id=id)

    def resolve_author(root, info, id):
        return Author.objects.all().filter(id=id)

