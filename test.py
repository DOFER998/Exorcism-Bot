from httpx import Client
import pymongo

cluster = pymongo.MongoClient('mongodb://localhost:27017')
agent = cluster.Exorcism_Bot.agents

client = Client(
    headers={
        'Content-Type': 'application/json',
    },
    base_url='https://valorant-api.com/v1'
)

r = client.get('/agents?isPlayableCharacter=true&language=all')
for i in r.json()['data']:
    new_dict = {"_id": i['uuid']} | i
    print(new_dict)

