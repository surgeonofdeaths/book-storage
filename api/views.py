from rest_framework import generics, views, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import BookSerializer
from .permissions import IsAdminOrRelatedUserCanDelete
from book.models import Book, CommentBook, Author


class BookAPIList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BookAPIUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'


class BookAPIDestroy(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminOrRelatedUserCanDelete, )


# class BookViewSet(viewsets.ModelViewSet):
#     # queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     parser_classes = (FormParser, MultiPartParser, JSONParser)
#     lookup_field = 'slug'
#
#     def get_queryset(self):
#         slug = self.kwargs.get('slug')
#         if not slug:
#             return Book.objects.all()
#         return Book.objects.filter(slug=slug)
#
#     @action(methods=['get'], detail=True)
#     def authors(self, request, slug):
#         author = get_object_or_404(Author, slug=slug)
#         return Response(
#             {
#                 'author': {
#                     'first_name': author.first_name, 'middle_name': author.middle_name, 'last_name': author.last_name,
#                     'slug': author.slug,
#                 }
#             }
#         )

# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     parser_classes = (FormParser, MultiPartParser, JSONParser)
#
#
# class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     parser_classes = (FormParser, MultiPartParser, JSONParser)

# class BookAPIView(views.APIView):
#     def get(self, request):
#         authors = Book.objects.all()
#         return Response({'authors': BookSerializer(authors, many=True).data})
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'book': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         """Put overrides an instance with new data. Patch updates an instance"""
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'message': 'Method PUT not allowed'})
#
#         try:
#             instance = Book.objects.get(pk=pk)
#         except Exception as err:
#             return Response({'message': "Object doesn't exist", 'error': err})
#
#         serializer = BookSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'message': 'Method DELETE not allowed'})
#
#         try:
#             instance = Book.objects.get(pk=pk)
#             instance.delete()
#         except Exception as err:
#             return Response({'message': "Object doesn't exist", 'error': err})
#         return Response({'message': f"Successfully deleted object '{pk}'"})
