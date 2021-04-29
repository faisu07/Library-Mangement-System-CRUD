from django.urls import path
from . import views
from Library.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateView

urlpatterns = [
	path('', BookListView.as_view(), name = 'book_list'),
	path('create/', BookCreateView.as_view(), name="book_create"),
	path('<int:pk>/',BookDetailView.as_view(),name="book_detail"),
	path('update/<int:pk>/', BookUpdateView.as_view(), name="book_update"),
	path('delete/<int:pk>/', BookDeleteView.as_view(), name="book_delete"),
]


urlpatterns = urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)
