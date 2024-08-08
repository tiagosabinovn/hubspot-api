from http.server import BaseHTTPRequestHandler, HTTPServer
    import urllib.parse as urlparse
    import requests
    
    # Informações do OAuth
    CLIENT_ID = 'CLIENT_ID' # Substitua com seu CLIENT_ID
    CLIENT_SECRET = 'CLIENT_SECRET' # Substitua com seu CLIENT_SECRET
    REDIRECT_URI = 'REDIRECT_URI' # Substitua com seu REDIRECT_URL
    
    # Classe para manipular as requisições HTTP
    class OAuthRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse.urlparse(self.path)
            query_params = urlparse.parse_qs(parsed_url.query)
    
            # Verifica se há um código de autorização na URL
            if 'code' in query_params:
                authorization_code = query_params['code'][0]
    
                # Trocar o código de autorização por um token de acesso
                token_url = 'https://api.hubapi.com/oauth/v1/token'
                data = {
                    'grant_type': 'authorization_code',
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'redirect_uri': REDIRECT_URI,
                    'code': authorization_code
                }
    
                # Faz a requisição POST para obter o token de acesso
                response = requests.post(token_url, data=data)
                token_info = response.json()
    
                # Exibe o token de acesso na resposta HTTP
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f'Token de Acesso: {token_info}'.encode())
    
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('Código de Autorização não encontrado.'.encode())  # Convertendo para bytes
    
    # Função para iniciar o servidor HTTP na porta 3000
    def run_http_server(server_class=HTTPServer, handler_class=OAuthRequestHandler, port=3000):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f'Servidor HTTP rodando na porta {port}...')
        httpd.serve_forever()
    
    if __name__ == '__main__':
        run_http_server()
