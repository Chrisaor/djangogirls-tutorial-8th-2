from django.conf.urls import url

from .views import post_list

urlpatterns = [
    url('^$', post_list)
]