from collections import defaultdict

def find_ladders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    layer = {beginWord: [[beginWord]]}

    while layer:
        new_layer = defaultdict(list)

        for word in layer:
            if word == endWord:
                return layer[word]

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        for path in layer[word]:
                            new_layer[new_word].append(path + [new_word])

        wordSet -= set(new_layer.keys())
        layer = new_layer

    return []
# Example
print(find_ladders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]