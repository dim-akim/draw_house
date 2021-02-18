import requests
import time

last_time = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/get_messages',
        params={'after': last_time}
    )

    for message in response.json()['messages']:
        print(message['username'])
        print(message['text'])
        print()
        last_time = message['timestamp']

    time.sleep(.5)
