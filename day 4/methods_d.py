# myDict.keys() = returns all keys
# myDict.values() = returns all values
# myDict.items() = returns all (key,val) pairs as tuples
# myDict.get("key") = returns the key according to values 
# myDict.update(newDict) = inserts the sepecified items to the dictonary

novels = {
    "name" : ["fault in our stars" , "verity","kite runner"],
    "genre": {
        "emotional": "silent patient",
        "sci-fi": "stranger things",
        "mysterious": "verity",
    },
    "price":(999.3,599,799)
}
print (novels.keys())
print(novels.values())
print(novels.items())
print(novels.get("genre"))
print(novels.update({"author":"john green"}))
