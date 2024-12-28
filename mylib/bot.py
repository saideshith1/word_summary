import wikipedia
def search(name, sentences):
    result = wikipedia.summary(name, sentences=sentences)
    return result