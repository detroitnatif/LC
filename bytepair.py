from collections import Counter

def get_pairs(word):
    return [(word[i], word[i + 1]) for i in range(len(word) - 1)]

def bpe(word):
    word = list(word)
    while True:
        pairs = get_pairs(word)
        if not pairs: break
        most_common_pair = Counter(pairs).most_common(1)[0][0]
        word = [word[i] + word[i + 1] if i < len(word) - 1 and (word[i], word[i + 1]) == most_common_pair else word[i] for i in range(len(word)) if i == 0 or (word[i-1], word[i]) != most_common_pair]
        print(" ".join(word))
        if len(word) == 1: break
    return "".join(word)

bpe("mississippi")