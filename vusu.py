# -*- coding:utf-8 -*-
import json
import sys
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
if __name__ == '__main__':
    args = sys.argv
    json_path = args[1]
    vis = visualizer(json_path)
    vis.visualize()