f = open("10-Les_miserables.txt", "r")
wordset = []
for data in f:
    data_parsed = data.strip()
    if data_parsed == "":
        continue
    else:
        data_parsed = data_parsed.replace(".", "").replace("\"", "").replace("?", "").replace("!", "").replace(",",
                                                                                                               "").replace(
            ":", "").replace("(", "").replace(")", "").replace("-", " ").replace("'s", "").replace("'",
                                                                                                   "").upper().split(
            " ")
        wordset += data_parsed

wordcount = {}
wordpercent = {}
fullcount = 0

for word in wordset:
    fullcount += 1
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

sortcount = sorted(wordcount.values())[::-1]
sortword = sorted(wordcount, key=wordcount.__getitem__)[::-1]

print(sortcount)
print(sortword)

i = 0

for word in sortword:
    print("%s\t\t%s\t%f" % (word, sortcount[i], sortcount[i] / fullcount * 100))
    i += 1
