#grades/api_client.py
import requests

def fetch_grades(student_id):
    """Fetch grades for a student from an external API."""
    url = f"https://api.example.com/students/{student_id}/grades"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()