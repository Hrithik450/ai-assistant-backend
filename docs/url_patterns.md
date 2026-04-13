# Django URL Patterns (Minimal)

## Basic

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## Multiple URLs

```python
urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

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
```

---

## Reverse URL

### Python

```python
from django.urls import reverse

reverse('home')
```

### Template

```html
<a href="{% url 'home' %}">Home</a>
```

---

## Key Points

- `urlpatterns` → list of routes
- `path()` → connects URL to view
- `name` → used for reverse lookup
