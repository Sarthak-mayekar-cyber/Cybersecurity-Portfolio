import sys
import time

# Simulated secure API gateway matching the IIT Kanpur B.Cyber syllabus
def simulate_api_request(provided_token):
    # Hardcoded simulation token acting as the cryptographic key
    SECRET_ADMIN_TOKEN = "IITK_SECURE_AUTH_TOKEN_2026"
    
    print("[+] Connecting to Secure Web API Gateway...")
    time.sleep(1)
    
    # Logic checking for Broken Object Level Authentication / API security flaws
    if provided_token == SECRET_ADMIN_TOKEN:
        print("[SUCCESS] Status Code: 200 OK")
        print("[+] Access Granted. Fetching administrative endpoint data payload...\n")
    else:
        print("[ERROR] Status Code: 403 Forbidden")
        print("[!] Warning: Unauthorized token payload detected. Request blocked.\n")

if __name__ == "__main__":
    # Check if a token argument was passed via the command line interface (CLI)
    if len(sys.argv) > 1:
        user_token = sys.argv[1]
    else:
        print("[!] No CLI argument passed. Falling back to manual verification.")
        user_token = input("Enter API Authentication Token: ")
        
    simulate_api_request(user_token)
