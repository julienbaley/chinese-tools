import sys
from lib.zhtools.cedict import CEdict
from lib.zhtools.transliteration.colour import strip_colour


def get_hsk():
    hsk = dict()
    for lvl in range(1, 7):
        with open("data/hsk{lvl}".format(lvl=lvl)) as f:
            for line in f:
                word = line.strip()
                if word not in hsk:
                    hsk[word] = "hsk{lvl}".format(lvl=lvl)
    return hsk


if __name__ == "__main__":
    cedict = CEdict(colour=True)
    hsk = get_hsk()
    filename = sys.argv[1]
    while True:
        word = input("({f})=> ".format(f=filename)).strip()
        try:
            entries = cedict[word]
        except KeyError:
            print("Unknown word")
            continue
        else:
            if len(entries) > 1:
                for i, e in enumerate(entries):
                    print(i, "\t", e)
                choice = int(input("Which? [0-{n}] ".format(n=len(entries)-1)))
            else:
                choice = 0
            e = entries[choice]
            lvl = hsk.get(strip_colour(e.simp), "")
            defs = input("Definition? ")
            with open(filename, "a") as g:
                g.write("\t".join([e.simp, e.trad, e.pinyin, defs, lvl])
                        + "\n")
