from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.seriazilers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
