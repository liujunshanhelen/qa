import json
import uuid
import graphviz
import vusu as jv
import json
import sys
json_path = 'test.json'
vis = jv.visualizer(json_path)
vis.visualize()
#定义节点类
class Node(object):
    def __init__(self, data):
        self.parent=data
        self.child_1=[]
        self.child_2=[]
        self.isnull=1
        self.child_1.append(getPlan(self.parent))
        self.child_1.append((getPlan(self.child_1[0][0])))
        self.child_2.append(getPlan(self.child_1[0][1]))

class visualizer(object):
    def __init__(self, jsonfile):
        with open(jsonfile, 'r') as f:
            meta = json.load(f)
            self.json = meta
        self.tree = ''
    def _print(self, s):
        self.tree += '\n'
        self.tree += s
        print(s)
    def _visualize(self, var, level, from_list=False):
        if 'keys' in dir(var):
            if from_list:
                s = ' ' * level + '|- hoge ' + '\t:\t' + str(type(var)).split('\'')[1]
                self._print(s)
                level += 1
            for key,value in var.items():
                s = ' ' * level + '|-' + key + '\t:\t' + str(type(var[key])).split('\'')[1]
                self._print(s)
                self._visualize(var[key], level + 1)
            self._print('')

        elif 'list' == str(type(var)).split('\'')[1]:
            self._visualize(var[0], level + 1, from_list=True)

        elif from_list:
            s = ' ' * level + '|- hoge ' + '\t:\t' + str(type(var)).split('\'')[1]
            self._print(s)
    def visualize(self, var_direct=None):
        self.tree = ''

        if var_direct is None:
            s = 'json'
            self._print(s)
            self._visualize(self.json, 0)
        else:
            s = 'var\t:\t' + str(type(var_direct)).split('\'')[1]
            self._print(s)
            self._visualize(var_direct, 0)
#递归获取Plan节点
def getPlan(data):
    for key ,values  in data.items():
        if(key=='Plans'):
           return values


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('test.json') as f:
        data = json.load(f)
    a=data[0].get('Plan')
    tree=Node(a)
    args = sys.argv
    json_path = args[1]
    vis = visualizer(json_path)
    vis.visualize()

    '''
    s = graphviz.Digraph('structs', filename='structs_revisited.gv',
                         node_attr={'shape': 'record'})
    for key ,values  in tree.parent.items():
        s.node('struct1', '<f0> left|<f1> middle|<f2> right')
        str='%s %s'%(key,values)
        s.node('struct1', 'str')
        


import json

from pyecharts import options as opts
from pyecharts.charts import Tree

with open("test.json", "r", encoding="utf-8") as f:
    j = json.load(f)
c = (
    Tree()
    .add("", [j], collapse_interval=2, orient="RL")
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree"))
    .render("tree_right_left.html")
)
'''


















