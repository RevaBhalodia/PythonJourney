# 1
def count_frequency(lst):
    freq = {}

    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq
numbers = [1, 2, 2, 3, 1, 2, 4]
print(count_frequency(numbers))


# 2
def round_prices(products):
    new_dict = {}

    for item, price in products.items():
        rounded_price = ((price + 5) // 10) * 10
        new_dict[item] = rounded_price

    return new_dict
products = {
    "Pen": 12,
    "Notebook": 58,
    "Bag": 243
}

print(round_prices(products))


# 3
def second_highest(students):
    scores = []

    for name, score in students:
        scores.append(score)

    scores = list(set(scores))
    scores.sort(reverse=True)

    second = scores[1]

    for name, score in students:
        if score == second:
            return name
data = [("Alex", 85), ("luke", 92), ("haley", 88), ("manny", 92)]
print(second_highest(data))


# 4
def max_temp_difference(cities):
    max_temp = max(cities.values())
    min_temp = min(cities.values())

    for city, temp in cities.items():
        if temp == max_temp or temp == min_temp:
            print(city)
temps = {
    "Delhi": 42,
    "Mumbai": 35,
    "Shimla": 18,
    "Chennai": 38
}

max_temp_difference(temps)
