text = input()
words = text.split()
for word in range(len(words)):
    # finish the code here
    if words[word].startswith("https://") or  words[word].startswith("http://") or words[word].lower().startswith("www."):
        print(words[word])