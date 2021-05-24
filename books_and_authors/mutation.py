import graphene
from .object_types import BookType, AuthorType
from books_and_authors.booksAndAuthors.models import Book, Author

class CreateBookMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        author = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, name, price, author):
        print(name, price, author)
        book = Book(name = name, price = price, author = Author.objects.get(id=author))
        book.save()
        print(book)
        return CreateBookMutation(book=book)

class DeleteBookMutation(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.Int(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, id):
        book = Book.objects.get(id=id)
        book.delete()
        return cls(ok=True)

class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        author = graphene.Int(required=True)
        
    book = graphene.Field(BookType)

    def mutate(root, info, id, name, price, author):
        book = Book.objects.get(id=id)
        book.name = name
        book.price = price
        book.author = Author.objects.get(id=author)
        book.save()
        return UpdateBookMutation(book=book)

class CreateAuthorMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    def mutate(root, info, name, age):
        author = Author(name = name, age=age)
        author.save()
        return CreateAuthorMutation(author=author)

class DeleteAuthorMutation(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id):
        author = Author.objects.get(id=id)
        author.delete()
        return cls(ok=True)

class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        
    author = graphene.Field(AuthorType)

    def mutate(root, info, id, name, age):
        print(id, name, age)
        author = Author.objects.get(id=id)
        author.name = name
        author.age = age
        author.save()
        return UpdateAuthorMutation(author=author)

class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    create_author = CreateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()