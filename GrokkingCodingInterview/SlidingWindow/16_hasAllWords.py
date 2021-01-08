from collections import defaultdict
from collections import Counter
import math
def do(strings,words):
    result_idx=[]
    freq = Counter(words)
    words_count = len(words)
    word_length = len(words[0])
    for i in range(len(strings)-word_length*words_count+1):
        words_seen={}
        for j in range(words_count):
            
            next_idx = i+j*word_length
            word = strings[next_idx:next_idx+word_length]
            
            if word not in freq:
                break
            
            if word not in words_seen:
                words_seen[word]=0
            words_seen[word]+=1

            if words_seen[word]>freq.get(word,0):
                break
            
            if j+1==words_count:
                result_idx.append(i)
    return result_idx
print(do("catfoxandfoxandfoxcat", ["cat","fox"]))
