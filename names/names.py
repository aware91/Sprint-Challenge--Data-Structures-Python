import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure\

class BSTNode:
    def __init__(self, value):
        self.val = value
        self.r = None
        self.l = None
    def insert(self, value):
        if value < self.val:
            if self.l is None:
                self.l = BSTNode(value)
            else:
                self.l.insert(value)
        if value >= self.val:
            if self.r is None:
                self.r = BSTNode(value)
            else:
                self.r.insert(value)
    def contains(self, target):
        if self.val == target:
            return True
        elif target < self.val:
            if self.l and self.l.contains(target):
                return self.l
            else:
                return False
        else:
            if self.r and self.r.contains(target):
                return self.r
            else:
                return False


# Replace the nested for loops below with your improvements
bst = BSTNode("None")
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.