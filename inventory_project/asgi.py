
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_project.settings')

application = get_asgi_application()

# Create superuser if not exists
try:
    from create_superuser import *
except Exception as e:
    print(f"Superuser creation skipped or failed: {e}")
