import sys
import hashlib

# Fallback to interactive mode if no arguments are passed via CLI
text = sys.argv[1] if len(sys.argv) > 1 else input("Enter text string to hash: ")

print("MD5 Payload Hash: ", hashlib.md5(text.encode()).hexdigest())
print("SHA256 Payload Hash:", hashlib.sha256(text.encode()).hexdigest())
