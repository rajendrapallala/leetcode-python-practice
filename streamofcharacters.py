class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    def __str__(self):
        rtnstr = str(self.is_word ) if self.is_word else ""
        #rtnstr = " The word is " + str(self.is_word) + " and children are "
        chld = ""
        for (key, value) in self.children.items():
            chld = chld + "{" + str(key) + " : " + str(value) + "}"
        return str(self.is_word) +"-"+ chld
        
        
class StreamChecker:
    def __init__(self, words):
        self.trie = TrieNode()
        for word in words:
            self.insert(word)
        print(self.trie)
        self.partials = [self.trie]

    def query(self, l):
        new_partials, match = [self.trie], False
        for p in self.partials:
            if l in p.children:
                new_partials.append(p.children[l])
                if p.children[l].is_word:
                    match = True
        self.partials = new_partials
        return match
    
    def insert(self, word):
        curr = self.trie
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True


if __name__ == "__main__":
    a = StreamChecker(["cdd","f","kl","dfkk"])
    print(a.partials)
    print(a.query('c'))
    print(a.query('d'))
    print(a.query('d'))