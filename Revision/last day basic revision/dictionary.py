# question 1
def tuple_list_to_dict(tuples_list):
    result = {}
    for key, value in tuples_list:
        result[key] = value
    return result
data = [("apple", 2), ("banana", 3)]
print(tuple_list_to_dict(data))


# question 2
def word_count(sentence):
    words = sentence.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count
sentence = "python is easy and python is powerful"
print(word_count(sentence))



