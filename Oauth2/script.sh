#!/bin/bash

# Script to execute data import/export

# Example command to import data from HubSpot using the access token
curl -X GET \
  'https://api.hubapi.com/crm/v3/companies' \
  -H 'Authorization: Bearer your_oauth_token_here' \
  -H 'Content-Type: application/json'
