import sys
import os

# Dynamically adds the project root (Python-DSA) to Python's module search path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Data_Structures.Binary_trees.Heaps import Min_heap
from Data_Structures.Binary_trees.Binary_tree import Binary_tree

'''Huffman Coding -- Huffman Coding is a greedy algorithm used for lossless data compression. 
It assigns variable-length binary codes to characters based on their frequency ,
shorter codes for more frequent characters and longer codes for less frequent ones. 
This minimizes the overall number of bits required for encoding'''

class Node():
    def __init__(self, freq, code = '', key = ''):
        self.data = freq
        self.code = code
        self.key = key
        self.left = None
        self.right = None

    def __lt__(self, other):  # Less than
        return self.data < other.data

    def __gt__(self, other):  # Greater Than
        return self.data > other.data

bt = Binary_tree()
def weighted_external_path_length(root):    #O(n)
    if not root or bt.is_leaf(root):
        return 0
    return root.data + weighted_external_path_length(root.left) + weighted_external_path_length(root.right)

def set_codes(root):    #O(n)
    if root:
        if root.left:
            root.left.code = root.code + '0'
            set_codes(root.left)
        if root.right:
            root.right.code = root.code + '1'
            set_codes(root.right)

def get_codes(root,codes):  #O(n)
    if root:
        if bt.is_leaf(root):
            codes[root.key] = root.code
        get_codes(root.left, codes)
        get_codes(root.right, codes)


#Time Complexity -- O(nlogn)
def Huffman_coding(Text):
    Text = Text.strip()
    Map = dict()
    for ch in Text: #O(n)
        if ch in Map:
            Map[ch] += 1
        else:
            Map[ch] = 1
    n = len(Map.keys())
    heap = Min_heap([Node(count, key = key) for key, count in Map.items()]) #O(n)
    for _ in range(n-1):    #O(nlogn)
        left = heap.extract_min()   #O(logn)
        right = heap.extract_min()  #O(logn)
        root = Node(left.data + right.data)
        root.left = left
        root.right = right
        heap.insert_key(root)   #O(logn)
        
    wept = weighted_external_path_length(root)
    set_codes(root)
    codes = dict()
    get_codes(root,codes)
    return wept, codes

