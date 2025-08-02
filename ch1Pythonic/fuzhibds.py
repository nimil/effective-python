fresh_fruits = {
    "apple":12,
    "banana":123,
    "orange":13
}

if value := fresh_fruits.get("apple"):
    print(value)
else:
    print("sorry, we don't have")

if value := fresh_fruits.get("applepine"):
    print(value)
else:
    print("sorry, we don't have")