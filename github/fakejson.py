import requests, pprint

fakejson = 'https://jsonplaceholder.typicode.com/todos/'

response = requests.get(fakejson)

output = response.json()

# pprint.pprint(output)
# output = [{},{}....{}]

for i in output:
    print(i['id'])



