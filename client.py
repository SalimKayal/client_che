import requests

print(requests.get('http://localhost:8000/hello', params={'request':' world'}).text)
