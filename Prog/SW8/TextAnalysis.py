def NumberOfFirstPersonSingularPronouns(text: str) -> int:
    """Counts the number of first-person singular pronouns (I, me, my) in a given text."""
    return text.count("I") + text.count("me") + text.count("my")

def NumberOfWords(text: str) -> int:
    """Computes the number of words in a given text."""
    return len(text.split())

def WordsPerSentence(text: str) -> float:
    """Computes the average number of words in a sentence for a given text."""
    return NumberOfWords(text) / len(text.split("."))

def GenderDetection(text: str) -> str:
    """Assumes if the author of the text is male or female, based on the number of first-person singular pronouns."""
    documentLength = NumberOfWords(text)
    firstPersonSingularPronouns = NumberOfFirstPersonSingularPronouns(text)
    if firstPersonSingularPronouns < 0.08 * documentLength: #0.08 is an estimated value
        return "male"
    else:
        return "female"
    
text = input("Enter text: ")
print()
print("Number of first person singular pronouns:", NumberOfFirstPersonSingularPronouns(text))
print("Number of Words:", NumberOfWords(text))
print("Words per sentence:", WordsPerSentence(text))
print("Assumed Gender:", GenderDetection(text))
# Examples (ChatGPT):
# Female
# Hey there! 😊 Just wanted to check in and see how everything's going with you. I know things have been pretty hectic lately, and sometimes it’s hard to keep up with everything.Honestly, I’m trying to stay on top of my own list of things to do, but you know how it goes… one minute you’re all organized, and the next, it’s like chaos has somehow spread across the week! 😅 But I’m actually trying this new method where I write down just three “must-do” tasks each day, and it’s been helping a lot. Baby steps, right?Anyway, let me know if there’s anything I can do to help with whatever you’re up to, or if you just want to chat. It’s nice to connect when everything else feels a little overwhelming.Take care and talk soon!
# male
# Hey! Just checking in to see how things are going. I know it’s been a busy stretch, and sometimes it’s a lot to handle.I’m trying to keep my own stuff organized, too, but you know how it goes… One second you’re on top of things, and the next, it’s like everything needs your attention at once. I’ve started sticking to a top-three list for the day — just the main things to get done — and it’s actually been working pretty well.Anyway, if there’s anything I can help with or if you just want to catch up, let me know. Always good to connect when things get a little crazy.
