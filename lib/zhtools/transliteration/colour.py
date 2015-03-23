import re

colour_coding = {   0 : "000000", #"black"
                    1 : "008000", #"green",
                    2 : "0000FF", #"blue",
                    3 : "800080", #"purple",
                    4 : "FF0000", #"red",
                    5 : "000000"} #"black"

def apply_colour(s, tone):
    return '<span style="color:#{col}">{txt}</span>'.format(col=colour_coding[tone], txt=s)

def strip_colour(s, colour=None):
    if colour is None:
        for colour in range(5):
            s = strip_colour(s, colour)
    else:
        regex = apply_colour("([^<]+)", colour)
        s = re.sub(regex, r"\1", s)
    return s

def copy_colour(src, dest):
    colours = re.findall("({tag}){nontag}({tag})".format(tag="<[^>]+>", nontag="[^<]+"), src)
    return "".join(["".join([start, char, end]) for (start, end), char in zip(colours, dest)])

def minimize_colour(s):
    #remove black
    s = strip_colour(s, 0)
    
    #factorize identical consecutive tags
    old_s = ""
    while old_s != s:
        old_s = s
        s = re.sub(r"({tag})({nontag})({tag})\1({nontag})\3".format(tag="<[^>]+>", nontag="[^<]+"), r"\1\2\4\3", s)
    
    return s
