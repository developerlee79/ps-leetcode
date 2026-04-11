class Node:
    def __init__(self, value):
        self.value = value
        self.end = False
        self.next = {}

    def insert(self, word: str, index: int):
        if index == len(word):
            self.end = True
            return
        if word[index] not in self.next:
            self.next[word[index]] = Node(word[index])
        self.next[word[index]].insert(word, index + 1)

    def search(self, word: str, index: int) -> bool:
        if index == len(word):
            return self.end
        if word[index] not in self.next:
            return False
        return self.next[word[index]].search(word, index + 1)

    def start_with(self, word: str, index: int) -> bool:
        if index == len(word):
            return True
        if word[index] not in self.next:
            return False
        return self.next[word[index]].start_with(word, index + 1)


class Trie:

    def __init__(self):
        self.node = Node("")

    def insert(self, word: str) -> None:
        if not word:
            return
        self.node.insert(word, 0)

    def search(self, word: str) -> bool:
        if not word:
            return False
        return self.node.search(word, 0)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        return self.node.start_with(prefix, 0)
