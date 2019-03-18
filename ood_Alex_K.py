"""
Problem Statement:

Design the class structure for a keyword-based document search engine.
Requirements
- A document consists of an integer ID, a title, and a body.
- A keyword search consists of a short set of tokens (<= ~10) and should return
  the documents which contain the highest number of occurrences
  of the given tokens.
- Function for adding new documents without a given list of stop-words.
  (Stop-words are the same for all documents)
- Function for querying given a string and returning the top n documents.
- Support multiple backends for document storage - e.g. an in-memory
  data store which can't hold a ton of data but is convenient for
  development and testing, and a Postgres database which would be used
  in production.
- Provide an example of how the search engine would be used with some
  short dummy documents.


Loose Criteria:
- Concrete classes for Document and SearchEngine.
- Abstract class for DataStore with concrete classes for the different backends.
- SearchEngine encapsulates the search-specific logic (tokenizing, stop-words, getting top n)
- DataStore implementations encapsulate the storage-specific logic
    - store documents easily retrievable by id.
    - store an inverted-index of keywords pointing to document ids.
- SearchEngine calls the DataStore methods the same way regardless of the backend.
- Recognizes that the DataStore methods could be wildly different based on the implementation.
- DataStore and stop words injected into SearchEngine.
- Postgres connection or connection parameters injected into the SearchEngine.
- Uses idiomatic language constructs, e.g.:
    - @dataclass for the Document class
    - defaultdict for the inverted index
- Recognizes the need/uses efficient algos and data structures, e.g.:
    - hashmap for storing documents and ids
    - inverted index stores the ids, not the full documents
    - partial sort for the _top_n method
- Uses dummy/partially-implemented functions where appropriate.

Follow-up topics:
- Schema, indexing, and queries in postgres database.
- Partial sort implementation.
- How to handle queries that consist entirely of stop-words
- How to parallelize
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Iterator, Set, Dict

DEFAULT_STOP_WORDS = frozenset({"a", "an", "and", "the"})


@dataclass()
class Document:
    id: int
    title: str
    body: str


class DataStore(object):

    def insert(self, token: str, doc: Document):
        ...

    def get_ids(self, token: str) -> Iterator[Document]:
        ...

    def get_doc(self, id: int) -> Document:
        ...


class InMemoryDataStore(DataStore):

    def __init__(self):
        self._id_to_doc: Dict[int, Document] = dict()
        self._token_to_doc_ids: Dict[str, Iterator[int]] = defaultdict(list)

    def insert(self, token: str, doc: Document):
        self._id_to_doc[doc.id] = doc
        self._token_to_doc_ids[token] = doc.id

    def get_ids(self, token: str) -> Iterator[int]:
        return self._token_to_doc_ids[token]

    def get_doc(self, id: int) -> Document:
        return self._id_to_doc[id]


class PostgresDataStore(DataStore):

    def __init__(self, conn):
        ...


class SearchEngine(object):

    def __init__(self, data_store: DataStore, stop_words: Set[str] = DEFAULT_STOP_WORDS):
        self.data_store = data_store
        self.stop_words = stop_words

    def _tokenize_and_filter(self, text: Iterator[str]) -> Iterator[str]:
        ...

    def _top_n(self, items: List[int], n: int) -> List[int]:
        ...

    def insert(self, doc: Document):
        for text in (doc.body, doc.title):
            for token in self._tokenize_and_filter(text):
                self.data_store.insert(token, doc)

    def search(self, keywords: Iterator[str], n: int) -> Iterator[Document]:  # TODO: overload the type.
        candidate_ids = list()
        for token in self._tokenize_and_filter(keywords):
            candidate_ids += datastore.get_ids(token)
        top_ids = self._top_n(candidate_ids, n)
        return map(self.data_store.get_doc, top_ids)


if __name__ == "__main__":
    with ... as pgconn:
        datastore = PostgresDataStore(pgconn)
        google = SearchEngine(datastore)
        docs = [
            Document(1, "cat", "The cat utility reads files sequentially..."),
            Document(2, "grep", "The grep utility searches any given input files..."),
            Document(3, "sed", "The sed utility reads the specified files,,,")
        ]
        _ = [google.insert(d) for d in docs]
        for doc in google.search("utility that reads files", 2):
            print(doc.id, doc.title)
