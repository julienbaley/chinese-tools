import os
import subprocess
import tempfile
from collections import Counter
from contextlib import contextmanager
from .is_cjk import is_chinese_word


class change_directory():
    def __init__(self, path):
        self.src = os.getcwd()
        self.dst = path

    def __enter__(self):
        os.chdir(self.dst)

    def __exit__(self, *_):
        os.chdir(self.src)


@contextmanager
def get_filename():
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    yield f.name
    os.remove(f.name)


def segment(txt):
    jars = ":".join(["fudannlp.jar",
                     "lib/commons-cli-1.2.jar",
                     "lib/trove.jar"])

    cls = "edu.fudan.nlp.cn.tag.CWSTagger"

    with get_filename() as fin, get_filename() as fout:
        with open(fin, "w") as g:
            g.write(txt)

        cmd = 'java -classpath {jars} {cls} -f models/seg.m {fin} {fout}'\
              .format(jars=jars, cls=cls, fin=fin, fout=fout)

        with change_directory(os.path.join("third-parties", "fudan")):
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            p.communicate()

        with open(fout) as f:
            for line in f:#.decode("utf-8").strip().splitlines():
                yield line.strip()


def get_vocab(txt):
    cnt = Counter()
    for line in segment(txt):
        cnt.update(filter(is_chinese_word, line.split()))
    return cnt
