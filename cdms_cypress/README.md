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
cd your-repo
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
php artisan migrate
```

6. **Install Sanctum**
```bash
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
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
    "email": "user@example.com",
    "password": "password123"
}
```

**Success Response:**
```json
{
    "token": "1|XYZ123...",
    "user": {
        "id": 1,
        "name": "User Name",
        "email": "user@example.com"
    }
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
3. Run the requests

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
