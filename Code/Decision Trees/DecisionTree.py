import numpy as np
import pandas as pd

class Node:


    def __init__(self, ids=None,children=[], entropy=0, depth=0):
        self.ids=ids # index data
        self.entropy = entropy  # entropy node
        self.depth = depth  # depth node
        self.children = children  # list child nodes
        self.order = None  # values
        self.label = None  # label node if it is leaf
        self.split_attribute = None  # which attribute is chosen, it non-leaf

    def set_properties(self, split_attribute, order):
        self.split_attribute = split_attribute
        self.order = order

    def set_label(self, label):
        self.label = label

def entropy(freq):
    freq_0=freq[np.array(freq).nonzero()[0]]
    prob_0 = freq_0 /(freq_0.sum())
    return -np.sum(prob_0 * np.log2(prob_0))

class Tree :


    def __init__(self, max_depth=10,min_samples=2, min_gain=1e-4):
        self.N=0
        self.root = None
        self.max_depth = max_depth #Maximum depth of the tree, if a node has a depth greater
                                    # than the maximum depth of the tree. That node will be considered leaf.
        self.min_gain = min_gain  #if at some node, the entropy division does not reduce the informationgain
                                   # too much, we can stop it early."min gain" :minimum threshold
        self.min_samples=min_samples  # Minimum number of data points in 1 node.

    def fit(self, x, y):
        self.x=x
        self.y=y
        self.N=x.count()[0]
        ids = range(self.N)
        self.root = Node(ids=ids, entropy=self._entropy(ids), depth=0)

        Queue =[self.root]
        while Queue:
            node = Queue.pop()
            if node.depth< self.max_depth or node.entropy <self.min_gain:
                node.children=self.split(node)
                if not node.children: #leaf Node
                     self._set_label(node)
                Queue +=  node.children
            else :
                self._set_label(node)

    # Function of calculating frequency
    def most_freq(self,List):
        count = 0
        nb = List[0]
        for i in List:
            curr_freq = List.count(i)
            if (curr_freq > count):
                count = curr_freq
                nb = i
        return nb

    #The output function of a node:
    def _set_label(self,node):
        y_ids =[i +1 for i in node.ids]
        a= np.array(self.y[y_ids]).tolist()
        node.set_label(self.most_freq(a))

    #Entropy of 1 node :
    def _entropy(self,ids):
    # Calculate entropy of a node with index ids
        if len(ids) == 0: return 0
        ids = [i+1 for i in ids ]
        freq=np.array(self.y[ids].value_counts())
        return entropy(freq)

    # This function returns the list of children of "node".
    def split (self,node):
        ids = node.ids
        best_gain = 0 # Save the best gain information
        best_split = [] #
        best_atribute = None #
        order = None
        data=self.x.iloc[ids,:]
        #Loopattributes:
        for i ,att in enumerate (list(self.x)):
            splits=[]
            val_att=self.x.iloc[ids,i].unique().tolist()
            for val in val_att :
                id=data.index[data[att]==val].tolist()
                splits.append([j-1 for j in id ]) # list index of properties
            # don't split if a node has too small number of points
            if min(map(len, splits)) < self.min_samples: continue

            HxS=0
            for split in splits :
                HxS=+(len(split)/self.N)*self._entropy(split)
            #ig of 1 att:
            ig= node.entropy-HxS
            if ig <= self.min_gain:continue
            if ig > best_gain:
                best_gain=ig
                best_split=splits
                best_atribute=att
                order=val_att
        node.set_properties(best_atribute,order)
        child_nodes = [Node(ids=split,entropy=self._entropy(split), depth=node.depth + 1)
                       for split in best_split]
        return child_nodes

    #The function tests this model
    def test (self,data):
        npoints = data.count()[0]
        labels = [None]*npoints

        for n in range(npoints):
            x = data.iloc[n, :]
            node = self.root
            while node.children:
                node = node.children[node.order.index(x[node.split_attribute])]
            labels[n] = node.label
            return labels

#Calculate the accuracy of the model
def correct_ratio (list_class,y_test):
    ids = len(y_test)
    cout=0
    for i in range(ids) :
        if list_class[i] != y_test[i]:
            cout =cout+1
        else :continue

    return (len(y_test)-cout)/len(y_test) *100

# main():
#data train
df = pd.read_csv("weather.csv")
x_train = df.iloc[:, :-1]
y_train = df.iloc[:, -1]
#data test
x_test = df.iloc[:5, :-1]
y_test = df.iloc[:5, -1]
#
tree = Tree(max_depth=3, min_samples=2)
tree.fit(x_train, y_train)

print("Output of model:", tree.test(x_test))
print("Actual results", y_test.tolist())
print("The exact ratio of the Multinomial NB algorithm is:",
         correct_ratio(tree.test(x_test),y_test.tolist()), "%")