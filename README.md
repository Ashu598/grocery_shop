# GroceryShop — Django E‑commerce (Groceries)

A minimal but complete starter for a grocery e‑commerce site with:
- Customer signup/login/logout
- Product catalogue with categories
- Session-based cart (add/update/remove)
- Checkout that creates orders & order items
- Order history for customers
- Admin panel to manage products & categories

## Quickstart

```bash
# 1) Create and activate a virtual environment
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Mac/Linux:
# source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Create .env from example
copy .env.example .env

# 4) Apply migrations and create a superuser
python manage.py migrate
python manage.py createsuperuser

# 5) Run the dev server
python manage.py runserver
```

Open http://127.0.0.1:8000/ to see the store.

## Where to go in the Admin

- Add **Categories** and **Products** (with images/price/stock).
- Test the storefront at `/`.
- Sign up as a customer, add to cart, and checkout.
- View your order history at **My Orders** in the navbar.

## Project Layout (key files)

```
groceryshop/
├─ manage.py
├─ requirements.txt
├─ .env.example
├─ groceryshop/                # project module (settings/urls)
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  ├─ wsgi.py
│  ├─ templates/
│  │  ├─ base.html
│  │  └─ includes/nav.html
│  └─ static/css/styles.css
├─ core/
│  ├─ apps.py, urls.py, views.py
├─ accounts/
│  ├─ apps.py, urls.py, views.py, forms.py
│  └─ templates/accounts/{signup.html,login.html,profile.html}
├─ store/
│  ├─ models.py, admin.py, urls.py, views.py
│  └─ templates/store/{product_list.html,product_detail.html}
├─ cart/
│  ├─ cart.py, urls.py, views.py
│  └─ templates/cart/cart.html
└─ orders/
   ├─ models.py, admin.py, urls.py, views.py
   └─ templates/orders/{checkout.html,order_success.html,order_history.html}
```

Let’s add some daily-use grocery items so your customers have products to browse and order. We’ll do it with a fixture JSON file so you can load them directly into the database.

1. Create fixture file

Inside your project root (same place as manage.py), create a folder called:
fixtures/

Then create a file named:
grocery_data.json

2. Load the data

Run this command:
   python manage.py loaddata fixtures/grocery_data.json
