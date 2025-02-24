# Django Login System

This project implements a simple **User Authentication System** in Django, supporting:

✅ User Signup  
✅ User Login & Logout  
✅ Secure Password Hashing  
✅ CRUD Operations via Django Admin & Postman  
✅ API Endpoints for User Management  

## 📌 **Setup Instructions**
1. Clone the repo and navigate to the project:  
   ```bash
   git clone [<YOUR_GITHUB_REPO_URL>](https://github.com/geeta-kukreja/LoginifyDjango)
   cd LoginSystem
```
2.Create a virtual environment and install dependencies:
 ```bash
python -m venv DjangoAssignment
source DjangoAssignment/bin/activate  # On Mac/Linux
DjangoAssignment\Scripts\activate  # On Windows
pip install django
```
3.Run migrations:
```bash
python manage.py migrate
```
4.Create a superuser:
```bash
python manage.py createsuperuser
```
5.Start the server:
```bash
python manage.py runserver
```
📌 API Endpoints
Get All Users-	GET	/loginify/users/
Get User by Email-	GET	/loginify/user/<email>/
Update User-	POST	/loginify/user/update/<email>/
Delete User-	GET	/loginify/user/delete/<email>/

