# HubSpot and Databricks Integration

This project aims to maintain the integration between HubSpot and Databricks via an API. The goal is to ensure data is processed efficiently, avoiding processing limit issues and additional costs. Below are the instructions and code examples needed to set up and run the integration.

## Project Structure

- `app.py`: Contains the main code for the integration between HubSpot and Databricks.
- `requirements.txt`: List of required Python dependencies for running the code.
- `README.md`: Project documentation, including setup and usage instructions.

## Installation

Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Configuration

### Create a New Private App in HubSpot

1. Go to “Settings” > “Integrations” > "Private Apps".
2. Click on "Create a private app".
3. Name your private app (e.g., "Databricks Integration").
4. Select the necessary permissions, such as CRM.
5. Save the app and copy the generated token.

### Configure the Integration Code

In the integration code (`app.py`), insert the token generated in HubSpot to authenticate your requests.

## Usage

The code in the `app.py` file executes the query in Databricks and updates records in HubSpot with the processed data. For more details, see the source code in `app.py`.

If OAuth2 authentication is needed, check the 'Oauth2' library and refer to the [OAuth2 documentation](https://www.notion.so/API-com-Oauth2-939b0809b49b4840bb7a5c9e9946c4d4?pvs=21).

