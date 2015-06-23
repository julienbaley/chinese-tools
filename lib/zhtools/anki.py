import json
import re
import sqlite3
from contextlib import contextmanager


def strip_html(s):
    return re.sub(r"<[^<]*?>", "", s)


@contextmanager
def connect(filename):
    conn = sqlite3.connect("file:{path}?mode=ro".format(path=filename),
                           uri=True)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


class Anki:
    def __init__(self, filename):
        self.filename = filename

    def get_deck_ids(self, deck_name, subdecks=True):
        with connect(self.filename) as conn:
            c = conn.execute('select decks from col')

            for did, dval in json.loads(next(c)["decks"]).items():
                if subdecks:
                    name_matches = dval["name"].startswith(deck_name)
                else:
                    name_matches = dval["name"] == deck_name
                if name_matches:
                    yield did

    def get_vocab(self, deck_name, subdecks=True):
        dids = self.get_deck_ids(deck_name, subdecks)
        where_clause = " or ".join("did=={}".format(did) for did in dids)
        query = "select distinct nid, flds from notes \
                 join cards on notes.id == cards.nid \
                 where {clause}"\
                    .format(clause=where_clause)
        with connect(self.filename) as conn:
            for (nid, fields) in conn.execute(query):
                yield strip_html(fields).split(chr(0x001f))
