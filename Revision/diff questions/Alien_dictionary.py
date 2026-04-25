from collections import defaultdict, deque

def alien_order(words):
    adj = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    queue = deque([c for c in indegree if indegree[c] == 0])
    result = ""

    while queue:
        char = queue.popleft()
        result += char

        for neighbor in adj[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(indegree) else ""

# Example
print(alien_order(["wrt","wrf","er","ett","rftt"]))
# Output: "wertf"