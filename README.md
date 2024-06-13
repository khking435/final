# final
# Online Marketplace CLI Application

This is a Python CLI application for an online marketplace where users can browse products, make purchases, and view their purchase history.

## Features

- **User Authentication**: Users can sign up and log in securely using hashed passwords.
- **Browse Products**: Users can browse products available in the marketplace.
- **Purchase Products**: Authenticated users can purchase products.
- **View Purchase History**: Authenticated users can view their purchase history.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/khking435/final.git
    ```

2. Navigate to the project directory:

    ```bash
    cd final
    ```

3. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Follow the prompts to sign up, log in, browse products, make purchases, and view purchase history.

## File Structure

- `main.py`: Main entry point for the application.
- `user.py`: Contains the User class for managing user-related operations.
- `product.py`: Contains the Product class for managing product-related operations.
- `helpers.py`: Contains helper functions used in the application.
- `marketplace.db`: SQLite database file storing user and product data.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
