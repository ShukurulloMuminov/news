
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('newsletter-create/', NewsLetterCreateView.as_view(), name="newsletter_create"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('comment_create/<slug:slug>/', CommentCreateView.as_view(), name="comment_create" ),
    path('categories/<slug:slug>/articles', ArticleCategoriesView.as_view(), name='categories'),
    path('<slug:slug>/', ArricleDetailsView.as_view(), name="details"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

