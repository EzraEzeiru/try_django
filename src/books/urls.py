from django.urls import path
from .views import IndexView, BookDetailView, GenreView, AddBookView, BookEditView, BookDeleteView

app_name = "books"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddBookView.as_view(), name='add_book'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('<slug:slug>/edit', BookEditView.as_view(), name='edit_book'),
    path('<slug:slug>/delete', BookDeleteView.as_view(), name='delete_book'),
    path('g/<str:genre>/', GenreView.as_view(), name="genre"),
]
