from django.urls import path
from .views import helloAPI, HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins, BookAPIGenerics, BooksAPIGenerics

# Router 사용
from rest_framework import routers
from .views import BookViewSet

urlpatterns = [
    path("fbv/hello/", helloAPI),
    path("cbv/hello/", HelloAPI.as_view()),
    
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
    
    path("generics/books/", BooksAPIGenerics.as_view()),
    path("generics/book/<int:bid>/", BookAPIGenerics.as_view()),
]

# Router 사용
router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls