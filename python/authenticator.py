import hashlib

import jwt

SECRET = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"
ALGORITHM = "HS256"

#dddd

class Authenticator:
    def get_hash(self, password, salt):
        return hashlib.sha512(str(f"{password}{salt}").encode("utf-8")).hexdigest()

    def is_password_correct(self, password, hash):
        return password == hash

    def create_jwt(self, role):
        return jwt.encode({"role": f"{role}"}, SECRET, algorithm=ALGORITHM)