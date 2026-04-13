# This file defines the URL routing system of your Django project, 
# which maps incoming HTTP requests (URLs) to the appropriate views or handlers.

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

# The urlpatterns list contains all the routes of your application. 
# Each path() defines a URL pattern and tells Django what to do when that URL is accessed. 
# For example, the root URL ("") renders the home page using a template, while /about/ renders the about page. 
# The admin panel is accessible via a configurable URL (settings.ADMIN_URL).

# path("") means the root URL (homepage /), and TemplateView.as_view(...) is a built-in Django generic view used to directly render a template without writing custom logic. 
# template_name="pages/home.html" tells Django which HTML file to display (it must be inside the templates folder), 
# and name="home" assigns a name to this route so it can be easily referenced using URL reversing.

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("django_app.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # ...
    # Media files
    # Static function creates URL patterns that map media URLs to user uplaoded files in the media directory.
    # The * operator unpacks (expands) the list of generated patterns and inserts them directly into urlpatterns.
    # This lets Django’s dev server serve uploaded files by resolving URLs to filesystem paths (production uses servers like Nginx).
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    # When DEBUG=True, staticfiles_urlpatterns() adds URL patterns to serve static files (CSS, JS, images) via Django. 
    # static files can be accessed in development This is only for development. production should serve static files using a server like Nginx.
    urlpatterns += staticfiles_urlpatterns()

# API URLS
# This section defines all API-related routes under /api/ for your Django project.
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("api/auth-token/", obtain_auth_token, name="obtain_auth_token"),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
