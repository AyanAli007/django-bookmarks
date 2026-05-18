# Django Bookmarks

A social bookmarking web application built with Django 5. This project allows users to share images they find on the internet, discover other users' bookmarks, and interact with them. 

## Features

* **User Authentication:** Complete authentication system including login, logout, password change, and password reset.
* **User Profiles:** Custom user profiles with profile pictures using the `Pillow` library.
* **Social Authentication:** Login integration with social accounts (e.g., Google) using `social-auth-app-django`.
* **Image Bookmarking:** Users can bookmark images from other websites.
* **Django Messages Framework:** Displays one-time notifications to users for actions like successful login or profile updates.
* **Secure Setup:** Configured to run on HTTPS locally for secure social authentication testing.

## Prerequisites

Make sure you have the following installed on your machine:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

## Local Development Setup

Follow these steps to get the project running on your local machine:

**1. Clone the repository:**
```bash
git clone https://github.com/AyanAli007/django-bookmarks.git
cd django-bookmarks
```

**2. Create and activate a virtual environment:**
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

**3. Install the dependencies:**
Make sure you install Django and the required libraries (like Pillow for image processing and social-auth-app-django for Google login):
```bash
pip install django Pillow social-auth-app-django django-extensions Werkzeug pyOpenSSL
```

**4. Run database migrations:**
```bash
python manage.py migrate
```

**5. Start the development server:**
```bash
python manage.py runserver
```
*(Note: If you are testing social authentication with Google, you may need to run the server with HTTPS using Django extensions: `python manage.py runserver_plus --cert-file cert.crt`)*

**6. Access the site:**
Open your web browser and navigate to `http://127.0.0.1:8000/` (or `https://127.0.0.1:8000/` if running securely).

## Future Enhancements
* Adding a JavaScript bookmarklet to easily bookmark images from external sites.
* Implementing user follow/unfollow functionality.
* Adding a user activity stream (timeline).

---
*Developed as part of the "Django 5 By Example" curriculum.*
