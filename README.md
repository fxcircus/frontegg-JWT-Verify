# JWT Verification Service

This application implements the [guidelines provided by Frontegg](https://developers.frontegg.com/guides/integrations/protect-backend-api/validate-jwt#validate-jwt-token-without-frontegg-middleware) for validating JWT tokens without using Frontegg's middleware.

- **JWT Decoding**: The application decodes the JWT using the `jwt.decode` method from the `pyjwt` library, specifying the public key and the RS256 algorithm.
- **Public Key Usage**:  verify the public key from your Frontegg account.
- **Audience Verification**: The application verifies the `aud` claim in the JWT.
- **[Error Handling](#error-handling)**

By following these steps, the application effectively implements the JWT validation process as described in the [Frontegg documentation](https://developers.frontegg.com/guides/integrations/protect-backend-api/validate-jwt#validate-jwt-token-without-frontegg-middleware), ensuring secure backend API protection without relying on Frontegg middleware.

## Setup

1. **Install dependencies**: Make sure you have Python and pip installed. Then, install the required packages using:

   ```bash
   pip install flask pyjwt flask-cors python-dotenv
   ```

2. **Set the Public Key**: You can find the public key in the `Frontegg Portal ➜ [ENVIRONMENT] ➜ Security ➜ JWT ➜ "JWT Signature" tab`. For example:

   ```plaintext
   PUBLIC_KEY_FROM_FRONTEGG_PORTAL="""-----BEGIN PUBLIC KEY-----
   MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6gVJE15fQAR8e8ENjfoW
   fpZ5B25vmOaZIey8I/WxhJPjDT1RB9aSTR1uDoYy+5zGC3F4LFFxmIJzTtsJfwBM
   jJNUjh1QZHxZhzd9ozKMfAR/Bw+F+4U6gmfdvBBkAjQO3IYp5UMFs8Iw/HUjyRTX
   EL0fDOHo9oHQPkQYAol+K5g/CZxkwKO4VwAGVXs5TGGps93DEofjCZtvLRNjYIAb
   tXmKPHk0Ck0NDNj8czLcWmlKx4+kQTR9XRIpHyIKUFikHGQM1RFeg1Y4LHzbnsEy
   5os1uNC1GbsRlcilKEIRtfFlQNhhgFHjRfLnFySNx/mIJeCKTsQf9wlUIYAkSlxF
   2QIDAQAB
   -----END PUBLIC KEY-----"""
   ```

3. **Set the Expected Audience**: The expected audience is your Client ID, which can be found in the `Frontegg Portal ➜ [ENVIRONMENT] ➜ Keys & domains`. Update the `EXPECTED_AUDIENCE` variable in `app.py` with this value.

4. **Run the application**: Start the Flask server by running:

   ```bash
   python3 app.py
   ```

   The server will start on `http://0.0.0.0:8000`.

## Usage

Send a POST request to the root endpoint `/` with an `Authorization` header containing the JWT token:

```
POST /
Authorization: Bearer <your_jwt_token>
```

### Example using `curl`

You can use the following `curl` command to test the application:

```bash
curl -X POST http://0.0.0.0:8000/ -H "Authorization: Bearer <your_jwt_token>"
```

Replace `<your_jwt_token>` with your actual JWT token.

## Error Handling

The application includes robust error handling to manage common JWT-related issues:

- If the `Authorization` header is missing, the server will respond with a `400` status code.
- If the JWT token is expired, the server will respond with a `401` status code and a message indicating the token has expired.
- If the JWT token has an invalid audience, the server will respond with a `401` status code and a message indicating the audience is invalid.
- If the JWT token is invalid, the server will respond with a `401` status code and a message indicating the token is invalid.

These error handling mechanisms are part of the implementation details that ensure the application adheres to the Frontegg guidelines for secure backend API protection.