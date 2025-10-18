import requests

user_input = input('Enter a id number: ')

response = requests.get('https://jsonplaceholder.typicode.com/todos/' + user_input)

output = response.json()

print(output['title'])