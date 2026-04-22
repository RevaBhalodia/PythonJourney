from collections import Counter
import re

def summarize(text):
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    sentences = text.split('.')
    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.lower().split():
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
    return '. '.join(summary)

text = "Python is great. Python is easy to learn. It is widely used. Many developers love Python."
print(summarize(text))