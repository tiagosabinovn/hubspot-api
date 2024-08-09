# Integration: Databricks, Google Sheets, and HubSpot

## Objective
Integrate Databricks, Google Sheets, and HubSpot to perform bulk note associations to companies using OAuth2.

## Requirements
- Google Sheets with organized data.
- A table in Databricks for data import.
- OAuth2 authentication for HubSpot integration.

## Project Structure

- **`integration_config.py`**: Initial configuration code and dependency installation.
- **`data_processing.py`**: Code for processing and importing data from Google Sheets to Databricks.
- **`hubspot_integration.py`**: Code for associating notes to companies in HubSpot.
- **`requirements.txt`**: List of necessary dependencies for the project.

## How to Use

1. **Initial Configuration**:
   - Run `integration_config.py` to install dependencies and configure the environment.

2. **Data Processing**:
   - Use `data_processing.py` to load and process data from Google Sheets into Databricks.

3. **HubSpot Integration**:
   - Run `hubspot_integration.py` to associate notes with companies in HubSpot.

## Additional Documentation

- [API with OAuth2](https://www.notion.so/API-com-Oauth2-939b0809b49b4840bb7a5c9e9946c4d4?pvs=21)
- [Daily Data Update API](https://www.notion.so/API-para-Atualiza-o-Di-ria-do-Dados-d0a000f7cd214fffa26e73dc59fce39c?pvs=21)
- [Google Sheets API Overview](https://developers.google.com/sheets/api)
- [Databricks Documentation](https://docs.databricks.com/)
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview)

## Notes
- For OAuth2 authentication, see the `Oauth2` library. If a different authentication is needed, adjust as indicated in the documentation.

