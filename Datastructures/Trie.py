class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.final_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        parent = self.root
        for i in word:
            c_index = ord(i) - ord('a')
            if not parent.children[c_index]: 
                parent.children[c_index] = TrieNode()
            parent = parent.children[c_index]

        parent.final_word = True
    def search(self, word):
        parent = self.root
        for i in word:
            c_index = ord(i) - ord('a')
            if not parent.children[c_index]:
                return False
            parent = parent.children[c_index]

        return parent.final_word


if __name__ == "__main__":
    t1 = Trie()
    t1.insert("hello")
    t1.insert("jaswanth")


    print(t1.search("hello"))
    print(t1.search("jaswan"))
