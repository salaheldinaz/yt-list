import requests
import simplejson as json
import os


ver = "0.2"
logo = """\n__   _______   _     _     _     _____ _ _   _      
\ \ / /_   _| | |   (_)___| |_  |_   _(_) |_| | ___ 
 \ V /  | |   | |   | / __| __|   | | | | __| |/ _ \/
  | |   | |   | |___| \__ \ |_    | | | | |_| |  __/
  |_|   |_|   |_____|_|___/\__|   |_| |_|\__|_|\___|
  \n"""

title = "Youtube List Title Grabber"
contact = "\n-=-=-=--=-=-=-=-=-=-=-=-=-" \
          "\nTwitter-->  @salaheldinaz " \
          "\nGithub -->  salaheldinaz " \
          "\n-=-=-=--=-=-=-=-=-=-=-=-=-"

print(logo, title, "v" + ver, contact, "\n")


# Import lists urls into json object
# Check if api data file exists then Get data from file
if os.path.isfile("./lists.txt") and os.stat("./lists.txt").st_size != 0:
    lists = open("./lists.txt", "r")
    ids = lists.readlines()

    # Get lists titles
    api_url = "https://www.googleapis.com/youtube/v3/playlists"
    headers = {'Accept': "application/json"}
    api_key = str(input("Enter Youtube API Key:"))

    i = 1
    lists_t = open("./lists+titles.txt", "w+")
    print("\n -------Start-------")

    for list_id in ids:
        querystring = {"part": "snippet", "id": list_id[38:], "key": api_key}
        response = requests.request("GET", api_url, headers=headers, params=querystring)
        title = json.loads(response.text)['items'][0]['snippet']['title']
        title_ = "\n" + str(i) + "\n" + title + "\n" + list_id
        print(title_)
        lists_t.write(title_)
        i = i + 1

    print("\n -------End-------")
    lists_t.close()
    lists.close()

else:
    print("lists urls file is empty")

#to do
