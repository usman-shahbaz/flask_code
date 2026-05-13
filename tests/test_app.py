import sys
import os
import json

# ✅ Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data

def test_home_response_type():
    client = app.test_client()
    
