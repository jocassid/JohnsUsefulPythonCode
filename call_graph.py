#!/usr/bin/env python3

from cmd import Cmd
from json import loads, dumps


from graph import Graph, Node


def requires_current_node(func):
    def foo(self, arg):
        if not self.current_node:
            print(f"current node not specified")
            return False
        return func(self, arg)
    return foo


class CallGraph(Cmd):

    prompt = '(): '

    def __init__(self):
        super().__init__()
        self.current_node = None
        self.graph = Graph()

    def do_node(self, arg_str):
        """set current node"""
        if not arg_str:
            print(f"missing argument")
            return False
        node = self.graph.get(arg_str)
        if not node:
            node = Node(arg_str)
            self.graph[node.label] = node
        self.current_node = node
        self.prompt = f"({node.label}): "

    def do_save(self, args):
        """save call graph to file"""
        if not args:
            print("missing filename")
            return False
        temp = {k: v.to_dict() for k, v in self.graph.items()}
        with open(args, 'w') as out_file:
            out_file.write(dumps(temp))

    def do_load(self, arg_str):
        """load graph from .json file"""
        if not arg_str:
            print('missing filename')
            return False
        self.current_node = None
        self.graph = Graph()
        with open(arg_str, 'r') as in_file:
            temp_dict = loads(in_file.read())
            for label, node_data in temp_dict.items():
                node = Node.from_dict(node_data)
                self.graph[label] = node

    def do_print(self, arg_str):
        """print call graph"""
        for label in sorted(self.graph.keys()):
            print(f"{label}:")
            node = self.graph[label]
            for next_node in sorted(node.next_labels):
                print(f"  - {next_node}")
            print()

    @requires_current_node
    def do_usage(self, usage_location):
        """Add usage of node"""
        if not usage_location:
            print(f"no usage location specified")
            return False
        usage_node = self.graph.get(usage_location)
        if not usage_node:
            usage_node = Node(usage_location)
            self.graph[usage_location] = usage_node
        usage_node.next_labels.add(self.current_node.label)

    @requires_current_node
    def do_call(self, call_str):
        """Add call from current node"""
        if not call_str:
            print(f"no call specified")
            return False
        called_node = self.graph.get(call_str)
        if not called_node:
            called_node = Node(call_str)
            self.graph[call_str] = called_node
        self.current_node.next_labels.add(call_str)

    def do_exit(self, arg):
        """exit call_graph"""
        print("Exiting")
        return True


if __name__ == '__main__':
    call_graph = CallGraph()
    call_graph.cmdloop()
