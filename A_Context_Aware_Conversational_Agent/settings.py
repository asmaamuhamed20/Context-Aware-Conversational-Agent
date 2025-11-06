import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Security and debug settings
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Django applications configuration
INSTALLED_APPS = [
    "django.contrib.admin",              # Django admin interface
    "django.contrib.auth",               # Authentication system
    "django.contrib.contenttypes",       # Content type framework
    "django.contrib.sessions",           # Session management
    "django.contrib.messages",           # Messaging framework
    "django.contrib.staticfiles",        # Static file management
    "ui",                                # Custom UI app for frontend
]

# Middleware configuration (order matters)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # Must come before AuthenticationMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL configuration entry point
ROOT_URLCONF = "A_Context_Aware_Conversational_Agent.urls"

# Template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "ui" / "templates"],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",   
                "django.contrib.auth.context_processors.auth",  
                "django.contrib.messages.context_processors.messages",  
            ],
        },
    },
]

# WSGI entry point for deployment
WSGI_APPLICATION = "A_Context_Aware_Conversational_Agent.wsgi.application"

# Static files configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "ui" / "static"]  # Folder for static assets (CSS, JS, images)

# Environment variables for LLM configuration (OpenRouter / OpenAI)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")

# Default database configuration (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
