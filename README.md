## License

This project is licensed under the [Apache License 2.0](./LICENSE).

# Peu's littleMarket
Peu's littleMarket is a project developed for college, simulating a complete ecommerce system. The backend is built with Django, using PostgreSQL as the database and Tailwind CSS for responsive design. The goal is to provide a simple and efficient shopping experience, with a modern and functional interface.

#### STATUS: IN PROGRESS

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Product Catalog**: Browse and search for products across various categories.
- **Shopping Cart**: Add products to the cart and proceed to checkout.
- **Order Management**: View order history and track current orders.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Tailwind CSS**: A utility-first CSS framework for creating custom designs.
- **[django-tailwind](https://github.com/timonweb/django-tailwind/tree/master)**: Integrates Tailwind CSS into Django projects.
- **django-browser-reload**: Automatically reloads the browser during development.
- **psycopg2-binary**: PostgreSQL adapter for Python.
- **[django-jazzmin](https://django-jazzmin.readthedocs.io/)**: A modern Django admin interface.
- **mypy**: An optional static type checker for Python, helping to enforce type safety and improve code quality.


## Using Tailwind

To set up Tailwind CSS, follow these steps:

1. Install Tailwind:

   ```bash
   python manage.py tailwind install
   ```

2. Start the Tailwind development server:

   ```bash
   python manage.py tailwind start
   ```

   This will enable live CSS changes while you work on the frontend.

### Troubleshooting

Sometimes (especially on Windows), the Python executable cannot find the npm binary installed on your system. In this case, you need to set the path to the npm executable in the `settings.py` file manually.

- For Linux/Mac:

   ```python
   NPM_BIN_PATH = '/usr/local/bin/npm'
   ```

- For Windows, if `npm` is on `$PATH`, but it’s `npm.cmd` rather than `npm`, you can override the default `NPM_BIN_PATH` like this:

   ```python
   NPM_BIN_PATH = 'npm.cmd'
   ```

   Alternatively, for maximum reliability, you can use a fully qualified path:

   ```python
   NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
   ```

Tailwind CSS requires Node.js to be installed on your machine. Node.js is a JavaScript runtime that allows you to run JavaScript code outside the browser. Most (if not all) of the current frontend tools depend on Node.js.

For more information, check the [django-tailwind documentation](https://arc.net/l/quote/lftzfxgn).

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


## Using Makefile (optional)

You can automate the migration and server startup process with the `Makefile`.

### To apply migrations (including makemigrations and migrate):

```bash
make run-migrate

```

### To start the development server::

```bash
make run-server

```
