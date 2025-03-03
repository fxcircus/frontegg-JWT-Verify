from flask import Flask, request
import jwt
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

PORT = 8000

# Replace with your Public key from `Frontegg Portal ➜ [ENVIRONMENT] ➜ Security ➜ JWT ➜ "JWT Signature" tab
PUBLIC_KEY_FROM_FRONTEGG_PORTAL = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6gVJE15fQAR8e8ENjfoW
fpZ5B25vmOaZIey8I/WxhJPjDT1RB9aSTR1uDoYy+5zGC3F4LFFxmIJzTtsJfwBM
jJNUjh1QZHxZhzd9ozKMfAR/Bw+F+4U6gmfdvBBkAjQO3IYp5UMFs8Iw/HUjyRTX
EL0fDOHo9oHQPkQYAol+K5g/CZxkwKO4VwAGVXs5TGGps93DEofjCZtvLRNjYIAb
tXmKPHk0Ck0NDNj8czLcWmlKx4+kQTR9XRIpHyIKUFikHGQM1RFeg1Y4LHzbnsEy
5os1uNC1GbsRlcilKEIRtfFlQNhhgFHjRfLnFySNx/mIJeCKTsQf9wlUIYAkSlxF
2QIDAQAB
-----END PUBLIC KEY-----"""

EXPECTED_AUDIENCE = '04017595-4e5d-4e7e-aff6-93c58d489d2f'  # Your Client ID from Frontegg Portal ➜ [ENVIRONMENT] ➜ Keys & domains

options = {
    'verify_exp': True,  # Switch to False to skip expiration date check
    'verify_aud': True    # Enable audience verification
}



@app.route('/', methods=['POST'])
def verify_jwt():
    print("New request!")
    try:
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return "Authorization header missing", 400

        token = authorization_header.split(' ')[1]

        decoded_token = jwt.decode(
            jwt=token,
            key=PUBLIC_KEY_FROM_FRONTEGG_PORTAL,
            algorithms=['RS256'],
            options=options,
            audience=EXPECTED_AUDIENCE  # Specify the expected audience
        )
        return f"OK! decoded_token:\n{decoded_token}", 200

    except jwt.ExpiredSignatureError:
        return "JWT token has expired", 401
    except jwt.InvalidAudienceError:
        return "Invalid audience in JWT token", 401
    except jwt.InvalidTokenError:
        return "Invalid JWT token", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)