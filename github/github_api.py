import requests

nameList = []

gh_link = 'https://api.github.com/search/repositories?q=language:python+sort:stars'

response = requests.get(gh_link)

# convert json response intp python object

output = response.json() # {}

# print(output["items"][0]["name"])

for item in output["items"]:
    nameList = nameList + [item["name"]]

print(nameList)

# def fakejson():

#     fake_api = "https://jsonplaceholder.typicode.com/todos/"

#     response = requests.get(fake_api)

#     outout = response.json()

#     # print(len(outout))

#     for i in outout[:5]:
#         print(i["title"])

# fakejson()