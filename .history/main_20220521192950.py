#!/usr/bin/env python3
from gtts import gTTS
import houndify
import argparse
import config
import json


def send_text_query(text_query, client_id, client_key):
  requestInfo = {
    'Latitude': 37.388309, 
    'Longitude': -121.973968
  }

  client = houndify.TextHoundClient(client_id, client_key, "test_user", requestInfo)

  response = client.query(text_query)
  return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str, help='The text query that will be sent to the Hybrid Engine')

    args = parser.parse_args()

    response = send_text_query(args.QUERY, config.CLIENT_ID, config.CLIENT_KEY)

    # with open('file.json', 'w') as file:
    #     json.dump(response, file)

#   print(json.dumps(response, indent=2, sort_keys=True, ensure_ascii=False))

    myobj = gTTS(text=mytext, lang=language, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")