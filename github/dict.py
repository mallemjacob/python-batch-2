spam = ['a','b']

np1 = ["val", 24, ['black','grey'], {"name":"val"}]

print(np1[2][1])
print(np1[3]["name"])

names = {
    "name": "val",
    "age": 24,
    "colors": ['black','grey'],
    "persons": [
        {
        "n1":"aaa"
    },{
        "n2": "bbb"
    }]
}

spam[0]

print(names["name"])
print(names["age"])
print(names["colors"][1])
print(names["persons"][0]["n1"])


spam = ['cat','bat','mat']

for i in spam:
    print(i)


[] + []