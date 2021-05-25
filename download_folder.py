"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaIoBaseDownload
import io
import sys

if __name__ == "__main__":
    # Setup the Drive v3 API
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    store = file.Storage('credentials.json')
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    filesresource = service.files()

    folder_id = input("Google Drive folder id: ")

    should_break = False
    while not should_break:
        list_of_files = filesresource.list(
            q="'{folder_id}' in parents".format(folder_id=folder_id),
            pageSize=1000,
            pageToken=list_of_files['nextPageToken']
        ).execute()

        if not ('nextPageToken' in list_of_files and list_of_files['nextPageToken'] != ''):
            should_break = True

        for file_dict in list_of_files["files"]:
            file_id = file_dict["id"]
            filename = file_dict["name"]

            print("Downloading %s"%filename)
            request = filesresource.get_media(fileId=file_id)
            fh = open("downloaded/" + filename, "wb")
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
            fh.close()

