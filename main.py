import requests
import pprint
import json
auto_key = '90f34d407cf74501ab873876e02912e6'
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers_auth_only = {'authorization': auto_key}

headers = {
    "authorization": auto_key,
    "content-type":"application/json"
}

CHUNK_SIZE = 5_242_880 # 5MB

def upload(filename):
    def read_file(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data
    
    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file)
    pprint(upload_response.json())
    return upload_response.json()['upload_url']
