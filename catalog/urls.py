from django.urls import path
from .views import views

urlpatterns = [
     path('', views.index, name="index"),
    
 ]
urlpatterns +=[
    path("book", views.BookListView.as_view(), name="book"),
    path("book/<int:pk>",views.BookDetailView.as_view(), name="book_detail")
     #url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns +=[
    path("author", views.AuthorListView.as_view(), name="author"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author_detail")
]

