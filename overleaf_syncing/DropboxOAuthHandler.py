import os
import requests
from urllib.parse import urlencode, urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
from pprint import pprint


class DropboxOAuthHandler:
    AUTH_URL = "https://www.dropbox.com/oauth2/authorize"
    TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"

    def __init__(self, client_id, client_secret, port=5000):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = "http://localhost:5000/oauth/callback"
        self.port = port

        # Fields to store tokens
        self.access_token = None
        self.refresh_token = None

        # Initialize the OAuth flow
        self._authorize_and_get_tokens()

    def _get_authorization_url(self):
        # Build the authorization URL for Dropbox OAuth
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "token_access_type": "offline",  # Requesting refresh token
        }
        url = f"{self.AUTH_URL}?{urlencode(params)}"
        return url

    def _start_http_server(self):
        # Start the local HTTP server to catch the authorization code
        server_address = ("", self.port)
        httpd = HTTPServer(server_address, OAuthCodeHandler)
        return httpd

    def _authorize_and_get_tokens(self):
        # Step 1: Get the authorization URL and open it in the browser
        auth_url = self._get_authorization_url()
        #print(f"Opening the following URL in the browser: {auth_url}")
        webbrowser.open(auth_url)

        # Step 2: Start the HTTP server to capture the authorization code
        httpd = self._start_http_server()
        #print("Waiting for the authorization code...")

        # Wait for a single request (Dropbox will send a GET request after authorization)
        httpd.handle_request()

        # Step 3: Get the authorization code from the server and exchange it for tokens
        auth_code = httpd.auth_code
        #print(f"Received authorization code: {auth_code}")

        try:
            self._exchange_code_for_tokens(auth_code)
            #print("Tokens retrieved successfully!")
        except Exception as e:
            #print(f"Error during token retrieval: {e}")
            self.access_token = None
            self.refresh_token = None

    def _exchange_code_for_tokens(self, auth_code):
        # Exchange the authorization code for access and refresh tokens
        data = {
            "code": auth_code,
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
        }

        response = requests.post(self.TOKEN_URL, data=data)
        tokens = response.json()

        if response.status_code == 200:
            self.access_token = tokens.get("access_token")
            self.refresh_token = tokens.get("refresh_token")
        else:
            raise Exception(f"Failed to get tokens: {tokens}")

    def refresh_access_token(self):
        # Refresh the access token using the refresh token
        if not self.refresh_token:
            raise Exception("No refresh token available")

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        response = requests.post(self.TOKEN_URL, data=data)
        new_tokens = response.json()

        if response.status_code == 200:
            self.access_token = new_tokens.get("access_token")
            #pprint(new_tokens)
            return self.access_token
        else:
            raise Exception(f"Failed to refresh access token: {new_tokens}")

    def is_authorized(self):
        return self.access_token is not None and self.refresh_token is not None


class OAuthCodeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query string to extract the authorization code
        query_components = parse_qs(urlparse(self.path).query)
        if "code" in query_components:
            self.server.auth_code = query_components["code"][0]
            # Send a response to the browser with JavaScript to close the window
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"""
                <html>
                <body>
                    <h1>Authorization successful!</h1>
                    <p>You can close this window, or it will close automatically.</p>
                    <script type="text/javascript">
                        window.onload = function() {
                            window.close();
                        };
                    </script>
                </body>
                </html>
            """
            )
        else:
            self.send_response(400)
            self.end_headers()
