import sys
from lib.zhtools.segment import get_vocab
from lib.zhtools.anki import Anki


def cumul_freq(cnt):
    total_freq = sum(cnt.values())
    l = list()
    acc = 0
    for w, c in cnt.most_common():
        acc += c
        l.append((w, round(100 * acc / total_freq, 2)))
    return l


with open(sys.argv[1]) as f:
    txt = "\n".join(f.readlines())
    cnt = get_vocab(txt)
    print(cnt)

anki = Anki("/home/julien/Documents/Anki/User 1/collection.anki2")
voc = set(zs for zs, zt, *_ in anki.get_vocab("普通話"))
print(voc)
print(len(voc))


for lvl in [1, 2, 3]:
    with open("data/hsk{lvl}".format(lvl=lvl)) as f:
        for line in f:
            voc.add(line.strip())

for w in voc:
    del cnt[w]

keys = set(cnt.keys())
with open("data/cedict.txt") as f:
    cedict = set(line.split()[1] for line in f if not line.startswith("#"))
unknown_keys = keys - cedict
for w in unknown_keys:
    del cnt[w]

print(len(cnt))
print(cnt)
