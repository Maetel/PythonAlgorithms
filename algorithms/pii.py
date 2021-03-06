#파이썬 알고리즘 인터뷰
import re #p151
import collections #p151

def p148(logs):
    #로그파일 재정렬
    copied = logs[:]
    def is_digit(x):
        return x.split()[1].isdigit()
    digits, letters = [], []
    for elem in copied:
        if is_digit(elem):
            digits.append(elem)
        else:
            letters.append(elem)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
    #return copied

def p148_test():
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(p148(logs))

def p151(paragraph, banned):
    def my_solution():
        def cleanse(sentence):
            return [word for word in re.sub('[^\w]', ' ', sentence).lower().split()]
        paragraph = cleanse(paragraph)
        #가장 흔한 단어
        counts = {}
        max_word = None
        for word in paragraph:
            banned_found = False
            for banned_word in banned:
                if word == banned_word:
                    banned_found = True
                    break
            if banned_found:
                continue
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        
        def most_frequent_key(dict):
            li = [k for k,v in sorted(dict.items(), key = lambda item:item[1])]
            return li[-1]
    
        return most_frequent_key(counts)
    
    def book_solution():
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        return collections.Counter(words).most_common(1)[0][0]
    #my_solution()
    return book_solution()


def p151_test():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    result = p151(paragraph, banned)
    print(result)

def p153(words):
    #애너그램
    def groupified(word):
        return "".join(sorted(list(word)))

    groupped = {}
    for word in words:
        id = groupified(word)
        if id in groupped.keys():
            groupped[id].append(word)
        else:
            groupped[id] = [word]
    return [value for value in groupped.values()]

def p153_test():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = p153(words)
    print(result)

if __name__ == "__main__":
    #p148_test()
    #p151_test()
    p153_test()