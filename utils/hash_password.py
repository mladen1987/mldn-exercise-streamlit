import hashlib
import sys


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_password_hash.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    print(hash_password(password))
