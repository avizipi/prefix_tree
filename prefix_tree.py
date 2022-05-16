import json
import random


class PrefixTree:
    def __init__(self):
        self.root = {}
        self.num_of_words = 0
        self.__end_sign = "__end_of_word__"

    def __repr__(self):
        return json.dumps(self.root, indent=4, sort_keys=False)

    def __len__(self) -> int:
        return self.num_of_words

    def insert(self, word: str) -> bool:
        """
        >>> pt = PrefixTree()
        >>> pt.insert('abc')
        True
        >>> print(pt)
        {
            "a": {
                "b": {
                    "c": {
                        "__end_of_word__": null
                    }
                }
            }
        }
        """
        current_node = self.root
        for letter in word:
            try:
                current_node = current_node[letter]
            except KeyError:  # do not exist
                current_node[letter] = {}
                current_node = current_node[letter]
        if self.__end_sign in current_node:
            return False
        else:
            current_node[self.__end_sign] = None
            self.num_of_words = self.num_of_words + 1
            return True

    def contains(self, word: str) -> bool:
        """
        >>> pt = PrefixTree()
        >>> pt.insert('abc')
        True
        >>> print(pt.contains("efg"))
        False
        >>> print(pt.contains("abc"))
        True
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return self.__end_sign in current_node

    def get_random_value(self) -> str:
        """
        >>> pt = PrefixTree()
        >>> pt.insert('abc')
        True
        >>> print(pt.get_random_value())
        abc
        """
        if self.num_of_words == 0:
            return ""
        current_node = self.root
        depth = 1
        letters = [random.choice(list(current_node))]
        if letters[0] == self.__end_sign:
            return ""

        while letters[-1] != self.__end_sign:
            current_node = current_node[letters[-1]]
            letters.append(random.choice(list(current_node)))

        return "".join(letters[0:-1])


class PrefixTree2:
    def __init__(self):
        self.root = {}
        self.num_of_words = 0
        self.__end_sign = "__end_of_word__"

    def __repr__(self):
        return json.dumps(self.root, indent=4, sort_keys=False)

    def __len__(self) -> int:
        return self.num_of_words

    def insert(self, word: str) -> bool:
        """
        >>> pt = PrefixTree2()
        >>> pt.insert('abc')
        True
        >>> print(pt)
        {
            "ab": {
                "c": {
                    "__end_of_word__": null
                }
            }
        }
        """
        current_node = self.root
        for i in range(0, len(word), 2):
            key = word[i:i+2]   # this will not fail if i+2 > len(word)
            try:
                current_node = current_node[key]
            except KeyError:  # do not exist
                current_node[key] = {}
                current_node = current_node[key]
        if self.__end_sign in current_node:
            return False
        else:
            current_node[self.__end_sign] = None
            self.num_of_words = self.num_of_words + 1
            return True

    def contains(self, word: str) -> bool:
        """
        >>> pt = PrefixTree2()
        >>> pt.insert('abc')
        True
        >>> print(pt.contains("efg"))
        False
        >>> print(pt.contains("abc"))
        True
        """
        current_node = self.root
        for i in range(0, len(word), 2):
            key = word[i:i+2]   # this will not fail if i+2 > len(word)
            if key not in current_node:
                return False
            current_node = current_node[key]
        return self.__end_sign in current_node

    def get_random_value(self) -> str:
        """
        >>> pt = PrefixTree2()
        >>> pt.insert('abc')
        True
        >>> print(pt.get_random_value())
        abc
        """
        if self.num_of_words == 0:
            return ""
        current_node = self.root
        depth = 1
        letters = [random.choice(list(current_node))]
        if letters[0] == self.__end_sign:
            return ""

        while letters[-1] != self.__end_sign:
            current_node = current_node[letters[-1]]
            letters.append(random.choice(list(current_node)))

        return "".join(letters[0:-1])