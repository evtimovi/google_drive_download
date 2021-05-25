# Google Drive Downloader Scripts 

Every time I need to download a lot of files from Google Drive (e.g. a dataset), it's always incredibly frustrating and slow to get that done. The browser UI very often fails mysteriously and when it does work, it is slow. So here are two scripts to download a file and download a folder programmatically, in case they are more broadly useful. 

## Prereqs
You would need to do the prerequisites [here](https://developers.google.com/drive/api/v3/quickstart/python) and in particular [Create credentials](https://developers.google.com/workspace/guides/create-credentials). The scripts expect you to put the OAuth file you create as `client_secret.json` in the same folder as the script (obviously you can change this in the script). I also needed to `pip install oauth2client` in addition to the 3 libraries they list, so e.g.
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
```

# Running
Run them with the `--noauth_local_webserver` option, e.g. `python3 download_folder.py --noauth_local_webserver`
This will spit out a link and then pause and wait for input. Copy and paste the link to a browser where you are logged in to a Google account with access to the folder. It will give you a prompt to authorize the app/project/whatever it's called thing you created when creating your credentials. After you allow it (as best as I can tell this is one time and not a permanent permission), it will give you a code that you can copy and paste as a response to the script.

Both scripts prompt you for a file id/folder id on the command line. You can find these in the URL from the web UI, e.g `https://drive.google.com/drive/folders/<folder_id>`

## Outputs
Obviously, feel free to change where the scripts write but the `download_file.py` one spits out the file in the same folder as the script and `download_folder.py` spits them out in a `downloaded/` subfolder (but it does not create it).

## Misc
Some of this code was originally given in the [Python Google Drive API Quickstart](https://developers.google.com/drive/api/v3/quickstart/python)
That code is available in a [Google repo](https://github.com/googleworkspace/python-samples/blob/master/drive/quickstart/quickstart.py) and it carries [an Apache license](https://github.com/googleworkspace/python-samples/blob/master/LICENSE).
It is also useful to refer to the [docs for the functions](https://developers.google.com/drive/api/v3/reference/files/list)

## Similar Tools
I also heard there are two other tools that get this job done. They are probably more bug-free and better maintained, so here they are:
* `rclone` at rclone.org
* `gdown` at https://pypi.org/project/gdown/ 
