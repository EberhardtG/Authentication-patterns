import requests
import os

# =========================================================
# WHY:
# GitHub’s API exposes both authenticated and unauthenticated
# endpoints. This script demonstrates the difference by making
# requests to two endpoints:
#   - /user        → requires authentication (returns 401)
#   - /users/octocat → public profile (returns 200)
#
# DESIGN:
# Each request is wrapped in a small function for clarity.
# The output explains what happened and why, making the script
# useful for learning API authentication patterns.
# =========================================================


# ---------------------------------------------------------
# 1️⃣ Unauthenticated request to /user (should return 401)
# ---------------------------------------------------------

def make_unauthenticated_request():
    """
    Makes an unauthenticated request to the GitHub /user endpoint.
    This endpoint requires authentication, so the expected status
    code is 401 Unauthorized.
    """
    response = requests.get("https://api.github.com/user")
    print("\n=== Unauthenticated Request: /user ===")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print("⚠ Unauthorized: Authentication required for /user.")
    else:
        print("Unexpected status code:", response.status_code)


make_unauthenticated_request()


# ---------------------------------------------------------
# 2️⃣ Unauthenticated request to /users/octocat (should return 200)
# ---------------------------------------------------------

def make_public_request():
    """
    Makes an unauthenticated request to GitHub's public user endpoint.
    Public profiles do not require authentication, so the expected
    status code is 200 OK.
    """
    response = requests.get("https://api.github.com/users/octocat")
    print("\n=== Public Request: /users/octocat ===")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        print("✅ Success: Public endpoint accessible without authentication.")
    else:
        print("Unexpected status code:", response.status_code)


make_public_request()


# ---------------------------------------------------------
# 3️⃣ create_auth_headers(api_key, auth_type)
# ---------------------------------------------------------

def create_auth_headers(api_key, auth_type):
    """
    Returns the correct authentication header dictionary based on
    the provided auth_type.

    Supported types:
      - "bearer" → Authorization: Bearer <token>
      - "api-key" → X-API-Key: <key>

    WHY:
    APIs use different authentication schemes. This function
    abstracts the header creation so callers don’t need to remember
    the exact header names.

    DESIGN:
    The function validates auth_type and raises a clear error for
    unsupported values. This prevents silent failures and enforces
    correct usage.
    """
    if auth_type == "bearer":
        return {"Authorization": f"Bearer {api_key}"}
    elif auth_type == "api-key":
        return {"X-API-Key": api_key}
    else:
        raise ValueError("Invalid auth type. Use 'bearer' or 'api-key'.")


# --- Demonstration of the function (required by assignment) ---

print("\n=== Auth Header Demonstration ===")
demo_key = "example123"  # placeholder key for demonstration

bearer_headers = create_auth_headers(demo_key, "bearer")
print("Bearer headers:", bearer_headers)

api_key_headers = create_auth_headers(demo_key, "api-key")
print("API-key headers:", api_key_headers)
