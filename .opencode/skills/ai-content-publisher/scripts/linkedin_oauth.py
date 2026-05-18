import os
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "")
REDIRECT_URI = "http://localhost:8080/callback"

AUTH_URL = (
    "https://www.linkedin.com/oauth/v2/authorization"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&scope=w_member_social%20openid%20profile%20email"
)

token_data = {}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        code = params.get("code", [None])[0]
        if code:
            resp = requests.post(
                "https://www.linkedin.com/oauth/v2/accessToken",
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "redirect_uri": REDIRECT_URI,
                },
            )
            resp.raise_for_status()
            token_data["access_token"] = resp.json()["access_token"]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>OK</h1>"
                b"<p>Copy this and save to .env:</p>"
                b"<pre>"
                + token_data["access_token"].encode()
                + b"</pre></body></html>"
            )
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization failed - no code received")


if __name__ == "__main__":
    print("1. Open this URL in your browser:")
    print(AUTH_URL)
    print("\n2. Authorize the app")
    print("3. Copy the access token from the page that opens\n")
    print("Waiting for callback on http://localhost:8080 ...")
    server = HTTPServer(("localhost", 8080), Handler)
    server.handle_request()
