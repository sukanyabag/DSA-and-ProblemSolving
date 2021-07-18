#CREATION OF TRIE -  time complexity = O(1), space complexity = O(1)

class TrieNode:
    def __init__(self):
        self.children = {} # dict because we build links between children -> children
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    #INSERTION IN TRIE- time complexity = O(m), space complexity = O(m), m = len of word
    def insertString(self, word):
        currNode = self.root
        # check if the char to be inserted exists (if yes, don't insert) or not (insert)
        for i in word:
            ch = i
            node = currNode.children.get(ch)
            if node == None:
                #if node doesn't exist, create newnode
                node = TrieNode()
                currNode.children.update({ch : node})
            currNode = node
        currNode.endOfString = True
        print("Successfully inserted the character in Trie!")

    #SEARCHING IN TRIE- time complexity = O(m), space complexity = O(1), m = len of word
    def searchString(self, word):
        currNode = self.root
        for i in word:
            node = currNode.children.get(i)
            if node == None:
                return False
            currNode = node

        if currNode.endOfString == True:
            return "The string exists in the trie!"
        else:
            return "The string doesn't exist in the trie!"
#DELETING IN TRIE - time complexity = O(m), space complexity = O(1), m = len of word
def deleteString(root, word, index):
    ch = word[index]
    currNode = root.children.get(ch)
    canCurrNodebeDeleted = False

    #1st case - some other prefix of str matches the one we will delete
    if len(currNode.children) > 1:
        deleteString(currNode, word, index+1)
        return False

    #2nd case - the entire str to be deleted is a prefix of another str
    if index == len(word)-1:
        if len(currNode.children) >= 1:
            currNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    #3rd case - other str is a prefix of the str we want to delete
    if currNode.endOfString == True:
        deleteString(currNode, word, index+1)
        return False

    #4th case - none of the nodes depends on this str
    canCurrNodebeDeleted = deleteString(currNode, word, index+1)
    if canCurrNodebeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

#WE USE DELETESTR METHOD OUTSIDE TRIE CLASS BECAUSE, TRIE SHOULD NOT BE MODIFIED

newTrie = Trie()
newTrie.insertString("Gilf")
newTrie.insertString("Gilfoyle")
deleteString(newTrie.root, "Gilfo",0)
print(newTrie.searchString("Gilfo")) 

