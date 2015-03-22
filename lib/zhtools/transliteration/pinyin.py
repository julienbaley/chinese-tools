import re

tone_marks = { "a":"āáǎà",
               "e":"ēéěè",
               "i":"īíǐì",
               "o":"ōóǒò",
               "u":"ūúǔù",
               "ü":"ǖǘǚǜ"}

colour_coding = {   1 : "008000", #"green",
                    2 : "0000FF", #"blue",
                    3 : "800080", #"purple",
                    4 : "FF0000", #"red",
                    5 : "000000"} #"black"

def find_marked_vowel(syllable):
    """Returns the vowel of the syllable that should receive the tone mark.
    
    Rules for tone mark placement can be found at http://www.pinyin.info/rules/where.html
    1. 'a' has priority over all
    2. 'e' comes right after
    3. 'o' receives the mark in ou (not in uo)
    4. in all other cases (which involve glides /w/, /ɥ/ and /j/), the last vowel takes the mark"""
       
    if "a" in syllable:
        return "a"
    elif "e" in syllable:
        return "e"
    elif "ou" in syllable:
        return "o"
    else:
        last_vowel_regex = "(?P<last_vowel>[aeiouü])[^aeiouü]*$"
        return re.search(last_vowel_regex, syllable).group("last_vowel")

def tone_number_to_mark(s, add_colour=False):
    rval = list()
    #segment in syllables
    for syllable in re.split("([a-zA-Zü]{1,6}[1-5])", s):
        if syllable.isalnum():
            try:
                tone = int(syllable[-1])
            except ValueError:
                if syllable[-1] != "r":
                    raise Exception("Malformed pinyin, doesn't have tone number in \"{syl}\"".format(syl=syllable))
            else:
                syllable = syllable[:-1]
                if tone != 5: #tone 5 in unmarked
                    v = find_marked_vowel(syllable)
                    syllable = syllable.replace(v, tone_marks[v][tone-1])
            if add_colour:
                syllable = '<span style="color:#{col}">{syl}</span>'.format(col=colour_coding[tone], syl=syllable)
        rval.append(syllable)
    return "".join(rval)
