"""Demo application with security issues."""

import os
import requests

# Hardcoded secrets (intentional for testing)
AWS_ACCESS_KEY = "AKIA1234567890ABCDEF"  # ISSUE: AWS key
AWS_SECRET_KEY = "aws_secret_key_1234567890abcdefghijklmnopqrs"  # ISSUE: AWS secret

GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"  # ISSUE: GitHub PAT

def get_data():
    """Fetch data from API."""
    api_key = "sk_test_1234567890abcdefghijklmnop"  # ISSUE: Stripe key
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

if __name__ == "__main__":
    print("Demo app running...")
