# =========================================
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
# Solution written by: Juan Ortiz
# Time complexity for solution: O(n)
# ========================================

wordBank = ['apple', 'dog', 'deer', 'deal', 'damp', 'eel']

def autocomplete(word):
    chars = len(word)
    return [w for w in wordBank if w[:chars] == word]

query = 'de'
print(autocomplete(query))
