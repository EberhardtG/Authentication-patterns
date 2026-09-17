

# 🔐 Auth Patterns — Exploring GitHub API Authentication  
A Python project demonstrating how authentication affects access to GitHub API endpoints.  
This script performs unauthenticated requests to both protected and public endpoints, then shows how to generate proper authentication headers using common patterns such as **Bearer tokens** and **API keys**.

The goal is to help developers understand how GitHub handles authentication and how clients should structure their headers depending on the auth scheme.

---

## 🚀 Features  
- Unauthenticated request to **GitHub /user** → expected **401 Unauthorized**  
- Unauthenticated request to **GitHub /users/octocat** → expected **200 OK**  
- A reusable function:
  - **`create_auth_headers(api_key, auth_type)`**  
  - Supports `"bearer"` and `"api-key"`  
  - Returns correctly formatted authentication headers  
- Demonstration block showing both header types  
- Includes WHY/DESIGN commentary explaining the purpose of each section  

---

## 📁 Project Structure  
```
auth_patterns.py      # Main script demonstrating authentication patterns
README.md             # Project documentation
```

---

## 🔧 Technologies Used  
- Python 3  
- requests library  
- GitHub REST API  

---

## 📦 Installation  
Clone the repository:

```
git clone https://github.com/yourusername/auth-patterns.git
cd auth-patterns
```

Install dependencies:

```
pip install requests
```

Run the script:

```
python auth_patterns.py
```

---

## 🧠 How the Script Works  

### 1️⃣ GET `/user` — Protected Endpoint  
This endpoint requires authentication.  
Unauthenticated requests always return:

- **401 Unauthorized**  
- A message indicating that authentication is required  

This demonstrates how GitHub protects user‑specific data.

### 2️⃣ GET `/users/octocat` — Public Endpoint  
This endpoint is fully public.  
Unauthenticated requests return:

- **200 OK**  
- JSON describing the Octocat user  

This shows how GitHub exposes public profile data without requiring tokens.

### 3️⃣ `create_auth_headers()` — Authentication Header Generator  
This function accepts:

- an API key  
- an authentication type (`"bearer"` or `"api-key"`)

It returns the correct header dictionary:

- Bearer → `{"Authorization": "Bearer <token>"}`  
- API key → `{"X-API-Key": "<key>"}`  

The script includes a demonstration block showing both header types.

---

## 🧩 WHY / DESIGN Philosophy  

### WHY  
APIs use different authentication schemes depending on their security model.  
Understanding how to structure headers is essential for:

- accessing protected endpoints  
- writing reusable API clients  
- debugging authentication failures  

### DESIGN  
The script separates each request into its own function for clarity.  
The `create_auth_headers()` function abstracts header creation, preventing duplication and enforcing correct patterns.  
The demonstration block ensures the function’s behavior is visible and testable.

---

## 📝 Example Output  
The script prints:

- Status codes for both unauthenticated requests  
- Human‑readable explanations of the results  
- Generated authentication headers for both supported auth types  

This makes the project ideal for learning how GitHub handles authentication.

---

## 🎯 Learning Outcomes  
By completing this project, you gain experience with:

- GitHub API authentication  
- Protected vs. public endpoints  
- Bearer token patterns  
- API key header formats  
- Writing reusable authentication utilities  
- Defensive programming with validation  

---

## 📄 License  
This project is open‑source under the MIT License.

