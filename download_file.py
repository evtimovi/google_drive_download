"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.

Prereqs:
pip3 install --user --upgrade oauth2client google-api-python-client google-auth-httplib2 google-auth-oauthlib
run as python3 download_gdrive.py --noauth_local_webserver so that browser does not launch
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaIoBaseDownload
import io

if __name__ == "__main__":
    # Setup the Drive v3 API
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    store = file.Storage('credentials.json')
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    filesresource = service.files()

    # Call the Drive v3 API
    file_id = input("Google Drive file id: ")

    fileinfo = filesresource.get(fileId=file_id).execute()
    filename = fileinfo["name"]
    print("Downloading %s"%filename)
    request = filesresource.get_media(fileId=file_id)
    fh = open(filename, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    fh.close()
