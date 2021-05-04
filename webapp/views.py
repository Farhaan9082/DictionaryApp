from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def home(request):
    return render(request, 'webapp/Page-1.html', {})

def meaning(request):
    word = request.GET.get('word')
    dictionary = PyDictionary()
    mean = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)

    if mean == None:
        word = "Word not found"
        mean = "Meaning :"
    elif 'Noun' in mean.keys():
        mean = "Meaning : {}.".format(mean['Noun'][0])
    elif 'Verb' in mean.keys():
        mean = "Meaning : {}.".format(mean['Verb'][0])
    elif 'Adjective' in mean.keys():
        mean = "Meaning : {}.".format(mean['Adjective'][0])
    else:
        mean = "Meaning : {}.".format(mean['Adverb'][0])
    
    if synonyms == None:
        synonyms = "Synonyms :"
    elif len(synonyms) > 1:
        synonyms = "Synonyms : {}, {}.".format(synonyms[0], synonyms[1])
    else:
        synonyms = "Synonyms : {}.".format(synonyms[0])
    
    if antonyms == None:
        antonyms = "Antonyms :"
    elif len(antonyms) > 1:
        antonyms = "Antonyms : {}, {}.".format(antonyms[0], antonyms[1])
    else:
        antonyms = "Antonyms : {}.".format(antonyms[0])

    return render(request, 'webapp/Page-2.html', {'word': word,'meaning': mean,'synonyms': synonyms,'antonyms': antonyms})