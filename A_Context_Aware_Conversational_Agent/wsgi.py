"""
WSGI config for A_Context_Aware_Conversational_Agent project.

This file exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "A_Context_Aware_Conversational_Agent.settings")

application = get_wsgi_application()
