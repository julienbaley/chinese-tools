import sys
from collections import Counter
from itertools import groupby
from lib.zhtools.segment import get_vocab
from lib.zhtools.anki import Anki


def print_counter(cnt):
    def grouper(word_count):
        word, count = word_count
        if count >= 1000:
            return str(count - (count % 1000)) + "+"
        elif count >= 100:
            return str(count - (count % 100)) + "+"
        elif count >= 10:
            return str(count - (count % 10)) + "+"
        else:
            return str(count)

    for cnt, word_counts in groupby(cnt.most_common(), key=grouper):
        print(cnt)
        print(sorted((word for word, count in word_counts), key=(lambda x: (len(x), x)), reverse=True))
        print()


def cumul_freq(cnt):
    total_freq = sum(cnt.values())
    l = list()
    acc = 0
    for w, c in cnt.most_common():
        acc += c
        l.append((w, round(100 * acc / total_freq, 2)))


if __name__ == "__main__":
    hsk = set()
    for lvl in range(1,7):
        with open("data/hsk{lvl}".format(lvl=lvl)) as f:
            for line in f:
                hsk.add(line.strip())
    
    with open(sys.argv[1]) as f:
        txt = "\n".join(f.readlines())
        cnt = get_vocab(txt)
        #print(cnt)
        # cnt = Counter(txt.split())

    anki = Anki("/home/julien/.local/share/Anki2/User 1/collection.anki2")
    voc = set(zs for fr, zs, zt, *_ in anki.get_vocab("普通話"))

    for w in voc:
        del cnt[w]

    keys = set(cnt.keys())
    with open("data/cedict.txt") as f:
        #cedict = set(line.split()[1] for line in f if not line.startswith("#"))
        cedict = {line.split()[1]: line[line.find('/'):] for line in f if not line.startswith("#")}
    unknown_keys = keys - set(cedict.keys())
    for w in unknown_keys:
        del cnt[w]

    show_counter = True
    if show_counter:

        hsk_only = True & False
        if hsk_only:
            cnt = Counter({k:v for k,v in cnt.items() if k in hsk})
        print(len(cnt))
        print_counter(cnt)
    else:
        for k,v in cnt.most_common():
            print(k,'\t',cedict[k])

    from random import sample
    if len(cnt) > 10:
        print('\t'.join(sample(cnt.keys(), 10)))

