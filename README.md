# Peu's littleMarket
Peu's littleMarket is a project developed for college, simulating a complete ecommerce system. The backend is built with Django, using PostgreSQL as the database and Tailwind CSS for responsive design. The goal is to provide a simple and efficient shopping experience, with a modern and functional interface.

## License

This project is licensed under the [Apache License 2.0](./LICENSE).



## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Product Catalog**: Browse and search for products across various categories.
- **Shopping Cart**: Add products to the cart and proceed to checkout.
- **Order Management**: View order history and track current orders.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Tailwind CSS**: A utility-first CSS framework for creating custom designs.
- **django-tailwind**: Integrates Tailwind CSS into Django projects.
- **django-browser-reload**: Automatically reloads the browser during development.
- **psycopg2-binary**: PostgreSQL adapter for Python.
- **django-jazzmin**: A modern Django admin interface.
- **mypy**: An optional static type checker for Python, helping to enforce type safety and improve code quality.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pedrorcruzz/peus-littlemarket.git
   ```

2. Navigate to the project directory:

   ```bash
   cd peus-littlemarket
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```


6. Apply env:

There is a `.env_example` file in the project directory. You should copy this file and rename it to `.env`. Inside the `.env` file, you will need to provide your database connection details, such as the PostgreSQL credentials.

example:

```bash
DB_DATABASE=database
DB_USER=username
DB_PASSOWRD=passoword
DB_HOST=localhost
DB_PORT=5432


```

7. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

8. Create a superuser to access the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.


