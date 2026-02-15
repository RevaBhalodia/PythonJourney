def word_count(sentence):
    sentence = sentence.lower()          
    words = sentence.split()             
    
    count_dict = {}
    
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
            
    return count_dict

text = "Python is fun and python is easy"
print(word_count(text))
