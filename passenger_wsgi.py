import os
import sys
from pathlib import Path

# Ensure the project root is on sys.path for Passenger.
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsproject.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
