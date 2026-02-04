# 1
students = {
    "nancy": 75,
    "johnathan": 58,
    "robin": 82,
    "steve": 60
}

for name, marks in students.items():
    if marks > 60:
        print(name)


# 2
prices = {"pen": 10, "book": 40, "bag": 500}

for item in prices:
    prices[item] = prices[item] * 0.8

print(prices)
