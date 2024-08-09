# HubSpot OAuth2 Integration

This repository contains code examples for performing OAuth2 authentication with HubSpot and executing data import/export operations using Flask, Ngrok, and a shell script.

## Project Structure

- `app.py`: Sets up and runs a Flask server to handle OAuth2 authentication.
- `oauth_server.py`: Starts an HTTP server that processes the OAuth2 authorization code and retrieves the access token.
- `script.sh`: Shell script to automate the data import/export process from HubSpot.
- `README.md`: This file, containing the project description and setup instructions.

## Setup Steps

### 1. Creating the Application in HubSpot
- Create an application in [HubSpot Developer Account](https://developers.hubspot.com/).
- Configure the necessary scopes for your application.

### 2. Environment Setup

#### Installing Dependencies

In the terminal, run:

```bash
sudo apt-get update
sudo apt-get install jq python3
pip install flask requests hubspot hubspot-api-client pandas sqlalchemy psycopg2-binary
```

Flask Setup
In the terminal, run:
```bash
python app.py
```

Ngrok Setup

After registering an account in Ngrok, configure the authtoken and run:
```bash
ngrok http 3000
```

3. Obtaining the Access Token
Run oauth_server.py to start the HTTP server and follow the instructions to obtain the OAuth2 access token.


4. Data Import/Export
Edit script.sh with the necessary information and run:

```bash
./script.sh
```

Additional Documentation
Hubspot CRM API Documentation | Associations
Hubspot CRM API Documentation | Engagements
