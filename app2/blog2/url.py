from django.urls import path
from .views import url, new_, iam

urlpatterns = [path("", url),
               path("new/", new_),  # local/relative
               path("hi/", iam)]

# local_url
# when we getting a path the
