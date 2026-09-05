\# 🛒 Fresh Harvest — Ecommerce Web Application



A full-stack \*\*Django-based ecommerce web application\*\* for managing products, categories, shopping carts, orders, checkout, payments, and product search.



The application provides separate functionality for \*\*customers and administrators\*\*, with support for \*\*Cash on Delivery (COD)\*\* and \*\*Razorpay online payments\*\*.



\---



\## 📌 Overview



\*\*Fresh Harvest\*\* is an ecommerce platform developed using Python and Django.



The application allows customers to:



\* Create an account and log in

\* Browse product categories

\* View product details

\* Search for products

\* Add products to a shopping cart

\* Update or remove cart items

\* Checkout orders

\* Choose Cash on Delivery or online payment

\* Make payments using Razorpay

\* View previous orders



Administrators can:



\* Manage product categories

\* Add and manage products

\* Manage product stock

\* View and manage the ecommerce system



\---



\## ✨ Features



\### 👤 User Authentication



\* User registration

\* User login

\* User logout

\* Authentication-protected pages

\* Separate customer and administrator functionality



\### 📦 Product Management



\* Create product categories

\* Add products

\* Product descriptions

\* Product images

\* Product pricing

\* Stock management

\* Product availability

\* Product detail pages



\### 🛒 Shopping Cart



\* Add products to cart

\* Increase/decrease product quantities

\* Remove products from cart

\* Delete cart items

\* Automatic subtotal calculation

\* Stock updates based on cart operations



\### 💳 Checkout \& Payments



The application supports:



\* Cash on Delivery (COD)

\* Razorpay online payments

\* Order creation

\* Payment verification

\* Order history

\* Delivery status tracking



\### 🔎 Product Search



Users can search products using:



\* Product name

\* Product price



\### 🖥️ Frontend



The project includes:



\* Responsive ecommerce interface

\* Bootstrap-based UI

\* Custom CSS

\* JavaScript

\* SCSS

\* Product/category images

\* Custom fonts



\---



\## 🛠️ Technology Stack



| Technology          | Usage                     |

| ------------------- | ------------------------- |

| Python              | Backend programming       |

| Django 6.0.4        | Web framework             |

| SQLite              | Database                  |

| HTML5               | Frontend structure        |

| CSS3                | Styling                   |

| JavaScript          | Client-side functionality |

| Bootstrap 5         | UI framework              |

| Django Crispy Forms | Form rendering            |

| Razorpay            | Online payments           |

| Git \& GitHub        | Version control           |



\---



\## 📂 Project Structure



```text

fresh-harvest-ecommerce-web-application/

│

├── Ecommerce/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── shop/

│   ├── migrations/

│   ├── models.py

│   ├── views.py

│   ├── urls.py

│   └── ...

│

├── cart/

│   ├── migrations/

│   ├── models.py

│   ├── views.py

│   ├── context\_processors.py

│   └── ...

│

├── search/

│   ├── migrations/

│   ├── models.py

│   ├── views.py

│   └── urls.py

│

├── templates/

│   └── ...

│

├── static/

│   ├── css/

│   ├── js/

│   ├── images/

│   ├── fonts/

│   └── scss/

│

├── media/

│   ├── product/

│   └── category/

│

├── manage.py

├── .gitignore

└── .env

```



> `.env` is intentionally excluded from version control and should never be committed to GitHub.



\---



\## 🧩 Django Applications



\### `shop`



Responsible for the core ecommerce functionality:



\* User registration

\* Login/logout

\* Categories

\* Products

\* Product details

\* Stock management

\* Admin functionality



\### `cart`



Responsible for:



\* Shopping cart

\* Cart quantities

\* Cart removal

\* Checkout

\* Orders

\* Order items

\* COD

\* Razorpay payments



\### `search`



Responsible for:



\* Product search

\* Searching by product name

\* Searching by price



\---



\## 🗃️ Database Models



\### Category



Stores product category information.



```text

Category

├── name

├── description

└── image

```



\### Product



Stores product information.



```text

Product

├── name

├── description

├── image

├── stock

├── price

├── available

├── category

├── created\_at

└── updated\_at

```



\### Cart



Stores products added to a user's cart.



```text

Cart

├── product

├── user

├── quantity

└── date\_added

```



\### Order



Stores customer order information.



```text

Order

├── user

├── order\_amount

├── order\_id

├── ordered\_date

├── payment\_method

├── address

├── phone

├── is\_ordered

└── delivery\_status

```



\### OrderItems



Stores individual products belonging to an order.



```text

OrderItems

├── product

├── order

└── quantity

```



\---



\## 🔄 Application Workflow



\### Customer Workflow



```text

Register

&#x20;  ↓

Login

&#x20;  ↓

Browse Categories

&#x20;  ↓

View Products

&#x20;  ↓

Product Details

&#x20;  ↓

Add to Cart

&#x20;  ↓

View Cart

&#x20;  ↓

Checkout

&#x20;  ↓

Choose Payment Method

&#x20;  ├── COD

&#x20;  │    ↓

&#x20;  │  Place Order

&#x20;  │

&#x20;  └── Razorpay

&#x20;       ↓

&#x20;     Payment

&#x20;       ↓

&#x20;     Order

&#x20;       ↓

&#x20;   Order History

```



\### Administrator Workflow



```text

Admin Login

&#x20;    ↓

Admin Dashboard

&#x20;    ↓

Manage Categories

&#x20;    ↓

Manage Products

&#x20;    ↓

Manage Stock

```



\---



\## 🌐 Main Routes



\### Shop



| Route                 | Purpose              |

| --------------------- | -------------------- |

| `/`                   | Home page            |

| `/register`           | User registration    |

| `/login`              | User login           |

| `/logout`             | User logout          |

| `/adminhome`          | Admin dashboard      |

| `/userhome`           | User dashboard       |

| `/products/<id>`      | Products by category |

| `/addcategory`        | Add category         |

| `/addproduct`         | Add product          |

| `/productdetail/<id>` | Product details      |

| `/addstock/<id>`      | Update product stock |



\### Cart



| Route                   | Purpose              |

| ----------------------- | -------------------- |

| `/cart/addtocart/<id>`  | Add product to cart  |

| `/cart/cartview`        | View cart            |

| `/cart/cartremove/<id>` | Remove cart quantity |

| `/cart/cartdelete/<id>` | Delete cart item     |

| `/cart/checkout`        | Checkout             |

| `/cart/success`         | Payment success      |

| `/cart/myorder`         | View orders          |



\### Search



| Route      | Purpose        |

| ---------- | -------------- |

| `/search/` | Product search |



\---



\# 🚀 Installation \& Setup



\## 1. Clone the Repository



```bash

git clone https://github.com/harikrishnanpmdev/fresh-harvest-ecommerce-web-application.git

```



Navigate into the project:



```bash

cd fresh-harvest-ecommerce-web-application

```



\---



\## 2. Create a Virtual Environment



\### Windows



```powershell

python -m venv .venv

```



Activate it:



```powershell

.venv\\Scripts\\Activate.ps1

```



\### macOS/Linux



```bash

python3 -m venv .venv

source .venv/bin/activate

```



\---



\## 3. Install Dependencies



Install the required packages:



```bash

pip install django

pip install django-crispy-forms

pip install crispy-bootstrap5

pip install razorpay

pip install python-dotenv

```



Alternatively, if a `requirements.txt` file is provided:



```bash

pip install -r requirements.txt

```



\---



\## 4. Configure Environment Variables



Create a `.env` file in the same directory as `manage.py`.



```env

SECRET\_KEY=your\_django\_secret\_key

DEBUG=True



RAZORPAY\_KEY\_ID=your\_razorpay\_key\_id

RAZORPAY\_KEY\_SECRET=your\_razorpay\_key\_secret

```



\### Security



Never commit `.env` to Git.



The project `.gitignore` contains:



```gitignore

.env

```



The application loads these values using `python-dotenv`.



\---



\## 5. Run Database Migrations



```bash

python manage.py makemigrations

python manage.py migrate

```



\---



\## 6. Create a Superuser



```bash

python manage.py createsuperuser

```



Follow the prompts to create your administrator account.



\---



\## 7. Run the Development Server



```bash

python manage.py runserver

```



The application will be available at:



```text

http://127.0.0.1:8000/

```



Django Admin:



```text

http://127.0.0.1:8000/admin/

```



\---



\# 💳 Razorpay Configuration



The application supports Razorpay online payments.



Razorpay credentials should be stored only in `.env`:



```env

RAZORPAY\_KEY\_ID=your\_key\_id

RAZORPAY\_KEY\_SECRET=your\_key\_secret

```



The Django application accesses them through:



```python

settings.RAZORPAY\_KEY\_ID

settings.RAZORPAY\_KEY\_SECRET

```



\### Security Notice



Never place Razorpay credentials directly inside Python source code.



Do not commit:



```text

.env

```



to GitHub.



\---



\# 🔐 Security



Security improvements implemented in the project include:



\* Environment-based Django secret configuration

\* Environment-based Razorpay credentials

\* `.env` excluded from Git

\* Previously exposed credentials removed from Git history

\* Python cache files removed from version control

\* `.gitignore` configured for sensitive/generated files



Sensitive configuration should always be managed through environment variables in production.



\---



\# 🧪 Testing



Run Django's system checks:



```bash

python manage.py check

```



Expected output:



```text

System check identified no issues (0 silenced).

```



You can also test the application manually:



\* Registration

\* Login

\* Product browsing

\* Search

\* Cart operations

\* Checkout

\* COD orders

\* Razorpay payments

\* Order history

\* Admin product management

\* Stock management



\---



\# 📁 Media \& Static Files



Uploaded product and category images are stored under:



```text

media/

```



Frontend assets are stored under:



```text

static/

```



The project uses Django's static and media configuration to serve these resources during development.



\---



\# 🚀 Future Improvements



Possible improvements for future versions include:



\* PostgreSQL/MySQL production database

\* Production deployment

\* REST API

\* Product reviews and ratings

\* Wishlist functionality

\* Coupon and discount system

\* Advanced product filtering

\* Pagination

\* Email order notifications

\* Order tracking

\* User profile management

\* Improved admin dashboard

\* Automated testing

\* Docker support

\* CI/CD pipeline

\* Cloud media storage

\* Production payment configuration



\---



\# 📜 License



This project is intended for \*\*educational and portfolio purposes\*\*.



Add an appropriate open-source license if you plan to distribute the project publicly.



\---



\# 👨‍💻 Author



\*\*HARIKRISHNAN P M\*\*



Python Full Stack Developer



GitHub:

https://github.com/harikrishnanpmdev



\---



\# 🔗 Project Repository



\*\*Fresh Harvest — Ecommerce Web Application\*\*



https://github.com/harikrishnanpmdev/fresh-harvest-ecommerce-web-application



