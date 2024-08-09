# OAuth Information

import requests
import json
import time
from pyspark.sql import SparkSession
from requests.exceptions import HTTPError, RequestException

# OAuth 2.0 Settings
client_id = 'client_id'  # Replace with your client_id
client_secret = 'client_secret'  # Replace with your client_secret
refresh_token = 'refresh_token'  # Replace with your refresh_token
token_url = 'https://api.hubapi.com/oauth/v1/token'

def get_access_token(client_id, client_secret, refresh_token):
    data = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    response = requests.post(token_url, data=data)
    response_data = response.json()
    return response_data['access_token']

def check_association_exists(note_id, company_id, access_token):
    url = f"https://api.hubapi.com/crm/v4/objects/notes/{note_id}/associations/company"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        associations = response.json().get('results', [])
        for association in associations:
            if association.get('toObjectId') == company_id:
                return True
    return False

def associate_note_to_company(note_id, company_id, access_token):
    url = f"https://api.hubapi.com/crm/v4/objects/notes/{note_id}/associations/default/company/{company_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    if check_association_exists(note_id, company_id, access_token):
        return access_token, note_id

    while True:
        try:
            response = requests.put(url, headers=headers)
            response.raise_for_status()
            return access_token, None
        except HTTPError as http_err:
            if response.status_code == 401:
                if 'Token expired, obtaining a new token...' not in globals():
                    globals()['Token expired, obtaining a new token...'] = True
                    print("Token expired, obtaining a new token...")
                access_token = get_access_token(client_id, client_secret, refresh_token)
                headers["Authorization"] = f"Bearer {access_token}"
            else:
                print(f"Failed to associate note {note_id} with company {company_id}. Response code: {response.status_code}")
                break
        except RequestException as req_err:
            print(f"Request error: {req_err}")
            time.sleep(5)

def import_notes_to_company(batch_size=100):
    access_token = get_access_token(client_id, client_secret, refresh_token)
    spark = SparkSession.builder.appName("HubSpotIntegration").getOrCreate()
    notes_df = spark.table("table.notes").orderBy("primary").collect()

    total_rows = len(notes_df)
    already_associated = []

    for start in range(0, total_rows, batch_size):
        batch = notes_df[start:start + batch_size]
        for idx, row in enumerate(batch, start=start+1):
            company_id = row['primary']
            note_ids = row['secundary'].split(';')
            for note_id in note_ids:
                access_token, existing_note_id = associate_note_to_company(note_id, company_id, access_token)
                if existing_note_id:
                    already_associated.append(existing_note_id)
                time.sleep(1)

            print(f"Company {company_id} processed.")

        percent_complete = (start + batch_size) / total_rows * 100
        print(f"Progress: {percent_complete:.2f}% complete")

    print("Association process completed.")

import_notes_to_company()

