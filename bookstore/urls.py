from django.contrib import admin
from django.urls import path, include
from books import views
from stores import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('books/<int:book_id>', views.bookdetail, name="bookdetail"),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
