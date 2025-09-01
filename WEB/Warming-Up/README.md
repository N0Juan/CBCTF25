# Warming Up the Parameters - Web Security Challenge

## Challenge Information
- **Category:** Web Application Security
- **Points:** TBD
- **Difficulty:** Easy/Medium
- **Vulnerabilities:** SQL Injection + Insecure Direct Object Reference (IDOR)

## Challenge Description
A beginner-friendly web security challenge that demonstrates two fundamental web application vulnerabilities: SQL Injection for authentication bypass and Insecure Direct Object Reference for unauthorized data access.

## Vulnerabilities Overview
This challenge combines two classic web security flaws:
1. **SQL Injection (SQLi)** - Authentication bypass
2. **Insecure Direct Object Reference (IDOR)** - Unauthorized access to user records

## Solution Process

### Step 1: SQL Injection Authentication Bypass
The login form is vulnerable to SQL injection, allowing authentication bypass.

**Credentials:**
- **Username:** `admin' OR '1'='1'--`
- **Password:** `123` (any value works due to SQLi)

**SQLi Payload Explanation:**
```sql
-- Original query (assumed):
SELECT * FROM users WHERE username='admin' AND password='123'

-- Injected query:
SELECT * FROM users WHERE username='admin' OR '1'='1'--' AND password='123'
```

The `OR '1'='1'` condition is always true, and `--` comments out the password check.

### Step 2: IDOR Exploitation
After successful login, the application displays user records with predictable ID parameters.

**IDOR Process:**
1. Access the dashboard after login
2. Observe URL parameter containing user ID (likely `id=1`)
3. Systematically change ID values from 1-30
4. Access unauthorized user records through direct object reference manipulation

**ID Range:** 1-30 (as specified in the solution notes)

## Screenshots Walkthrough
- `1. Homepage.png` - Application homepage/login form
- `2. Login.png` - Login interface demonstrating SQL injection
- `3. SQLi.png` - Successful SQL injection authentication bypass
- `4. Dashboard.png` - Post-login dashboard showing user data
- `5. IDOR.png` - IDOR exploitation by changing ID parameters

## Key Learning Objectives
- **SQL Injection Fundamentals**: Understanding how unsanitized input affects database queries
- **Authentication Bypass**: Using SQLi to circumvent login mechanisms
- **IDOR Vulnerability**: Exploiting predictable object references
- **Parameter Manipulation**: Systematic enumeration of accessible resources

## Technical Details

### SQL Injection
- **Vulnerability Type**: Authentication bypass
- **Attack Vector**: OR-based boolean injection with comment termination
- **Impact**: Complete authentication bypass

### IDOR
- **Vulnerability Type**: Authorization flaw
- **Attack Vector**: Direct manipulation of ID parameters
- **Impact**: Unauthorized access to other users' data
- **Enumeration Range**: IDs 1-30

## Tools Used
- Web browser for manual testing
- Burp Suite (optional for systematic IDOR testing)
- Parameter manipulation tools

## Flag Format
`CBCTF{...}`

## Difficulty Assessment
- **Beginner-friendly** for learning fundamental web security concepts
- **Real-world relevance** - these vulnerabilities are commonly found in production applications
