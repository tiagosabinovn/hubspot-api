from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import requests

# OAuth Information
CLIENT_ID = 'CLIENT_ID'  # Replace with your CLIENT_ID
CLIENT_SECRET = 'CLIENT_SECRET'  # Replace with your CLIENT_SECRET
REDIRECT_URI = 'REDIRECT_URI'  # Replace with your REDIRECT_URL

# Class to handle HTTP requests
class OAuthRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse.urlparse(self.path)
        query_params = urlparse.parse_qs(parsed_url.query)

        # Check if there's an authorization code in the URL
        if 'code' in query_params:
            authorization_code = query_params['code'][0]

            # Exchange the authorization code for an access token
            token_url = 'https://api.hubapi.com/oauth/v1/token'
            data = {
                'grant_type': 'authorization_code',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'redirect_uri': REDIRECT_URI,
                'code': authorization_code
            }

            # Make the POST request to obtain the access token
            response = requests.post(token_url, data=data)
            token_info = response.json()

            # Display the access token in the HTTP response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'Access Token: {token_info}'.encode())

        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Authorization Code not found.'.encode())

# Function to start the HTTP server on port 3000
def run_http_server(server_class=HTTPServer, handler_class=OAuthRequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'HTTP Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_http_server()

