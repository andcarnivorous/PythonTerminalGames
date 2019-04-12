from nltk import pos_tag, word_tokenize
    
def yodinator(text):

    text = word_tokenize(text)

    tagged = pos_tag(text)

    verbs = ("MD", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "RB", "RBR", "RBS")

    adverbs = ("RB", "RBR", "RBS")

    first_half = []

    second_half = []


    for t in range(0, len(tagged)):
        if tagged[t][1] in verbs and not tagged[t+1][1] in verbs:

            first_half.extend(tagged[:t+1])
            second_half.extend(tagged[t+1:])
            break
        

        elif tagged[t][1] in verbs and tagged[t+1][1] in verbs:
            first_half.extend(tagged[:t+1])
            second_half.extend(tagged[t+1:])
            break        

    added = second_half + first_half

    sentence = [item[0] for item in added if item[0] not in (".",",")]
    
    if "?" in sentence:
        sentence.append(sentence.pop(sentence.index("?")))
    
    sentence = " ".join(sentence)
    
    return sentence
