# TASK 4: API Testing (OrangeHRM Login)

**Endpoint:** `POST https://opensource-demo.orangehrmlive.com/web/index.php/auth/validate`

### 1. Request Body (JSON)
```json
{
    "username": "Admin",
    "password": "admin123"
}
{
    "success": true,
    "message": "Login Successful",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
{
    "success": false,
    "message": "Invalid credentials"
}