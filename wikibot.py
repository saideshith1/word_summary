import wikipedia

def search(name='Microsoft', length=2):
    result = wikipedia.summary(name, sentences=length)
    return result
print(search("Facebook",1))