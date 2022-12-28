name = input()
new_name = ""
def normalize(name):

    # put your code here
    list = {"é":"e", "ë":"e", "á":"a", "å":"aa", "œ":"oe", "æ" :"ae"}

    for i in range(len(name)):
        global new_name
        if name[i] in list:
            new_name = new_name + list[name[i]]
        else:
            new_name = new_name + name[i]

    return new_name

print(normalize(name))