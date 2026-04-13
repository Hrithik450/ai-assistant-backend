# URL Patterns - Quick Guide

## Basic Structure

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

path() -> maps a URL to a view.
views.home -> function or class based view handling the request.
name='home' -> namespace, used for reverse URL lookup.

[Read more about ViewSet](docs/viewset.md)

---

## Dynamic URL

```python
path('user/<int:id>/', views.user_detail, name='user_detail')
```

- `<int:id>` → value passed to view

---

## Include (App Routing)

```python
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]

Includes URL patterns from another app, allowing you to split and organize routes across multiple files (e.g., routing all `/api/` requests to `api.urls`).
```

---

## Reverse URL

```python
from django.urls import reverse

reverse('home')
```

Generates the URL from its name instead of hardcoding the path, making your code flexible and safe if URLs change.

[Read more about Reverse lookup](docs/reverse_lookup.md)
