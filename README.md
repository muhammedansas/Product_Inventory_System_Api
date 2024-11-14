# Product Inventory System with Stock Management


## Features

- Product Management:
  - Admin can create, update, and delete products with support for product variants (e.g., Large, Medium, Small).
    Admin can add sub-variants (e.g., Red, Blue) for each product variant, creating a detailed inventory system.
    
- Stock Management:
  - Admin can add and remove stock for any product variant or subvariant, enabling real-time stock updates.
  
- JWT Authentication:
  - Implemented JWT (JSON Web Token) for secure authentication.
    Users and Admins must authenticate to access protected routes and perform actions, such as adding products or modifying stock.
    
- Product Variant and Subvariant Management:
  - Support for variants (e.g., sizes like Large, Medium, Small) and sub-variants (e.g., colors like Red, Blue) for each product.
  - Flexible configuration for different combinations of product variants and sub-variants.
  
- Database Models:
  - Custom database models for products, variants, sub-variants, and stock to manage relationships between them effectively.
    Unit Testing:
  - Comprehensive unit tests for API endpoints and business logic, ensuring the stability and correctness of the backend operations.

## Getting Started

### Prerequisites

- Python
- Django

### Installation

1. Clone the repository:

   ```bash
   https://github.com/muhammedansas/Product_Inventory_System_Api.git
  

2. Create a Virtual Environment:

   ```bash
   python -m venv venv
   #for windows
   venv\Scripts\activate

3. Install Dependencies:

   ```bash
  pip install -r requirements.txt

4.  Run Migrations:
  python manage.py migrate

5. Create a Superuser:
  python manage.py createsuperuser

6. Start the Development Server:
  python manage.py runserver


## Running Tests:

  python manage.py test


   

