# This file defines how your api endpoints are generated automatically.
# Instead of manually writing URLs, Django REST framework creates them using a router.

from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from django_app.users.api.views import UserViewSet

# Default router: provides a special page /api/ that lists all your endpoints (clickable) like a menu. generates api routes. useful for debugging purpose.
# Simple router: no special page, only generates api routes.
router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register(...) automatically generates all CRUD api endpoints for each viewset. example:- 
# /api/users/          → GET (name=user-list) 
# /api/users/1/        → GET (name=user-list)
# /api/users/          → POST (name=user-detail)
# /api/users/1/        → PUT/PATCH (name=user-detail)
# /api/users/1/        → DELETE (name=user-detail)

# names are used for reverse-lookups (read more about reverse lookups at: docs/reverse-lookup)
router.register("users", UserViewSet)

# provides a namespace ("api") for all URLs in this file, used for reverse lookups.
app_name = "api"

# Converts router urls into actual django url patterns.
urlpatterns = router.urls