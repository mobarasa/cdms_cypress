# Laravel API Authentication System 🔐

A robust REST API authentication system built with Laravel, featuring token-based authentication using Laravel Sanctum.

## 🚀 Features

- Token-based authentication using Laravel Sanctum
- RESTful API endpoints for login and logout
- Comprehensive error handling and validation
- Automated testing suite using Python
- Postman collection included

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- PHP >= 8.1
- Composer
- MySQL/PostgreSQL
- Git

## 🛠️ Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/mobarasa/cdms_cypress.git
cd cdms_cypress/cdms_cypress
```

2. **Install dependencies**
```bash
composer install
```

3. **Configure environment**
```bash
cp .env.example .env
php artisan key:generate
```

4. **Configure database in .env**
```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

5. **Run migrations**
```bash
php artisan migrate:fresh --seed
```

6. **Install Sanctum**
```bash
php artisan install:api
```

## 🔧 Configuration

Update your `config/sanctum.php` with desired settings:

```php
return [
    'stateful' => explode(',', env('SANCTUM_STATEFUL_DOMAINS', sprintf(
        '%s%s',
        'localhost,localhost:3000,localhost:8080,127.0.0.1,127.0.0.1:8000,::1',
        env('APP_URL') ? ','.parse_url(env('APP_URL'), PHP_URL_HOST) : ''
    ))),
];
```

## 📚 API Documentation

### Authentication Endpoints

#### Login
```http
POST /api/login
Content-Type: application/json

{
    "email": "test@example.com",
    "password": "password123"
}
```

**Success Response:**
```json
{
    "success": true,
    "data": {
        "token": "3|95SbCHfQW1A8iYWMRubC1GkqWlw2mMn9UKKqUpoW3df10167",
        "name": "Test User"
    },
    "message": "User login successfully."
}
```

#### Logout
```http
POST /api/logout
Authorization: Bearer {token}
```

## 🧪 Testing

### Using Python Test Suite

```bash
# Install Python requirements
pip install requests unittest

# Run tests
python -m unittest test_login_api.py -v
```

### Using Postman
1. Import the provided Postman collection from `postman/collection.json`
2. Update the environment variables
 - In Postman, click the "Environment" dropdown (typically says "No Environment")
 - Click "New"
 - Create an environment named "Laravel Local"
 - Add these variables:
    ```
    base_url: http://localhost:8000/api
    token: [leave empty]
    ```
 - Click "Save"
 - Select your new environment from the dropdown
3. Run the requests
 - Make sure your Laravel server is running (php artisan serve)
 - In Postman, expand the "Authentication" folder
 - Run the requests in this order:
    ```
    "Login" - should return a token
    "Invalid Login" - should return an error
    "Logout" - should successfully logout
    ```
4. Test Features
 - The collection includes automatic token handling
 - Successful login automatically saves the token
 - All tests run automatically after each request
 - Tests verify response status codes and data structure

5. Collection Runner
 - Click "Runner" in Postman
 - Select your collection
 - Click "Run Laravel Auth API"
 - View the test results

## 🔍 Running the Application

```bash
# Start the Laravel server
php artisan serve

# Application will be available at
http://localhost:8000
```

## 📦 Directory Structure

```
├── app
│   ├── Http
│   │   └── Controllers
│   │       └── Auth
│   │           └── ApiAuthController.php
│   └── Models
│       └── User.php
├── routes
│   └── api.php
├── tests
│   └── Feature
│       └── AuthTest.php
└── postman
    └── collection.json
```

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security

If you discover any security-related issues, please email security@example.com instead of using the issue tracker.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [Laravel Documentation](https://laravel.com/docs)
- [Laravel Sanctum](https://laravel.com/docs/sanctum)

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/mobarasa/cdms_cypress](https://github.com/mobarasa/cdms_cypress)
