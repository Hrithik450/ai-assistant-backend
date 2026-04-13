# Reverse Lookup — Quick Guide

## What is Reverse Lookup?

Reverse lookup means **generating a URL from its name instead of hardcoding the path**.
Django maps a route name (like `"api:user-list"`) back to its actual URL (like `/api/users/`).

---

## Why is it needed?

Hardcoding URLs is risky:

```python
"/api/users/"  (breaks if URL changes)
```

Using reverse:

```python
reverse("api:user-list")
```

If the URL changes (e.g., `/api/v1/users/`), no code changes are needed.

---

## How it works with your API

From DRF (Django rest framework) router:

```python
router.register("users", UserViewSet)
```

Generates:

- `user-list` → `/api/users/`
- `user-detail` → `/api/users/{id}/`

With namespace:

```python
app_name = "api"
```

Final names:

- `api:user-list`
- `api:user-detail`

---

## Common Use Cases

### 1. Redirects

```python
return redirect(reverse("api:user-list"))
```

---

### 2. DRF Serializers (very common)

```python
reverse("api:user-detail", args=[obj.id])
```

Generates dynamic API URLs

---

### 3. Testing

```python
url = reverse("api:user-list")
client.get(url)
```

Avoids hardcoding in tests

---

### 4. Future-proofing URLs

```python
path("api/v1/", include("config.api_router"))
```

All reverse calls still work without changes

---

## Summary

- Reverse lookup = **get URL from name**
- Avoids hardcoding URLs
- Makes code maintainable and scalable
- Works perfectly with DRF routers (`user-list`, `user-detail`)

Reverse lookup lets you safely generate URLs using names instead of writing paths manually.
