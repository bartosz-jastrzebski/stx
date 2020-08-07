from rest_framework import generics
from ..models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):

        queryset = Book.objects.all()
        authors = self.request.query_params.getlist('author', None)
        published_date = self.request.query_params.get('published_date', None)
        sort = self.request.query_params.get('sort', None)

        if authors is not None:
            for author in authors:
                queryset = queryset.filter(authors__name=author)
        return queryset
    

class BookDetailView(generics.RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
