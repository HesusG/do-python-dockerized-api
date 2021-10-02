# These functions need to be implemented
import jwt

roles = ['admin', 'viewer', 'editor']

class Token():
    def generate_token(self, data):
        if data is None or data == '':
            return None
        return jwt.encode(data, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithm="HS256")


class Restricted():
    def access_data(self, authorization):
        if authorization is None or authorization == '':
            return None

        decodeData = jwt.decode(authorization, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithms=["HS256"])
        if 'role' in decodeData and decodeData['role'] in roles:
            return decodeData['role']
        else:
            return None
