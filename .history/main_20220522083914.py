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


   #find the specific spoken response to make it as a voice
    r: str = response['AllResults'][0]['InformationNuggets'][0]['SpokenResponseLong']

    #prit the response
    print(r)

    #save the responce as a MP3
    gTTS(text=r, lang="en", slow=False).save("result.mp3")