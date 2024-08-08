sudo tar -xvzf ~/Downloads/https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
ngrok config add-authtoken token
ngrok authtoken token
ngrok http 3000
