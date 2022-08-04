#!/usr/bin/env python3

# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

from collections import OrderedDict


class GraphError(RuntimeError):
    pass


class Node:
    def __init__(self, label, next_nodes):
        if not hasattr(label, '__hash__'):
            raise GraphError(f"label {label!r} isn't hashable")
        self.label = label
        self.next_nodes = set(next_nodes)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self.label != other.label:
            return False
        return self.next_nodes == other.next_nodes

    def to_dict(self):
        return {
            'label': self.label,
            'next_nodes': list(self.next_nodes),
        }

    @staticmethod
    def from_dict(temp_dict):
        node = Node(temp_dict.get('label'))
        for next_node in temp_dict.get('next_nodes', []):
            node.next_nodes.add(next_node)
        return node


class Graph(dict):

    def __init__(self, *nodes):
        kwargs = {n.label: n for n in nodes}
        super().__init__(**kwargs)
        self.checked = self.check()

    def check(self):
        all_labels = set(self.keys())
        for label, node in self.items():
            for next_node in node.next_nodes:
            pass
        return False

    def validate_label(self, arg_name, label):
        if label in self:
            return
        raise GraphError(f"{arg_name} {label} not present in graph")

    def get_paths_between(self, label1, label2, visited_labels=None):

        self.validate_label('label1', label1)
        self.validate_label('label2', label2)

        node1 = self[label1]
        next_nodes = node1.next_nodes
        if not next_nodes:
            return []

        if label2 in next_nodes:
            return [[label1, label2]]

        if not visited_labels:
            visited_labels = set()
        visited_labels.add(label1)

        paths_out = []
        for label in next_nodes:
            if label in visited_labels:
                continue
            paths = self.get_paths_between(label, label2)
            if not paths:
                continue
            for path in paths:
                path.insert(0, label1)
                paths_out.append(path)
        return paths_out


class DirectedAcyclicGraph(Graph):
    """There's a graph module in the standard library for Python 3.9+, but
    until we upgrade the servers here we are."""

    def __init__(self, iterable_or_mapping=None, **kwargs):
        if iterable_or_mapping:
            super().__init__(iterable_or_mapping, **kwargs)
        else:
            super().__init__(**kwargs)

        self.needs_check = True
        self._leaf_nodes = None
        self.unvisited_nodes = None
        self.visited_nodes = None
        self._reverse = None

    def _check_node(self, node):
        if node in self.visited_nodes:
            return [node]

        self.visited_nodes.add(node)
        if self.unvisited_nodes and node in self.unvisited_nodes:
            self.unvisited_nodes.remove(node)

        for child_node in (self[node] or []):
            path = self._check_node(child_node)
            if not path:
                continue
            path.insert(0, node)
            return path

    def check(self):
        if len(self) < 2:
            raise GraphError('Graph should have at least 2 nodes')

        self._leaf_nodes = set(self.keys())
        self.visited_nodes = set()

        for node, dest_nodes in self.items():

            if dest_nodes is None:
                continue

            if not hasattr(dest_nodes, '__iter__'):
                raise GraphError(
                    f"Error with node {node}.  {dest_nodes} is not iterable"
                )

            for item in dest_nodes:
                if item not in self:
                    raise GraphError(
                        f"Error with node {node}.  {item} not found in graph"
                    )

                if item in self._leaf_nodes:
                    self._leaf_nodes.remove(item)

        if not self._leaf_nodes:
            raise GraphError(f"Graph has no leaf nodes and is cyclic.")

        for leaf_node in self._leaf_nodes:
            self.visited_nodes = set()
            path = self._check_node(leaf_node)
            if path:
                path = ", ".join(str(n) for n in path)
                raise GraphError(f"Graph is cyclic. {path}")
        self.needs_check = False

        # done checking, lets free up some memory
        self.unvisited_nodes = None
        self.visited_nodes = None

    @property
    def leaf_nodes(self):
        if self.needs_check:
            raise GraphError(
                "call check before accessing leaf_nodes"
            )
        return self._leaf_nodes

    @property
    def reverse(self):
        if self.needs_check:
            raise GraphError(
                "call check before accessing reverse"
            )

        self._reverse = {}
        for key, values in self.items():
            if values is None:
                continue

            for value in values:
                if value not in self._reverse:
                    self._reverse[value] = {key}
                    continue
                self._reverse[value].add(key)

        missing_keys = set(self.keys()) - set(self._reverse)
        for key in missing_keys:
            self._reverse[key] = None

        return self._reverse

    def routes_to(self, node):
        if self.needs_check:
            raise GraphError(
                "call check before calling routes_to"
            )

        if node not in self:
            raise GraphError(
                f"node {node} not present in this graph"
            )

        reverse = self._reverse or self.reverse
        print(reverse)

        active_routes = [[node]]
        routes = []
        i = 0
        while len(active_routes) > 0:
            i += 1
            if i > 3:
                break

            temp_active_routes = active_routes
            active_routes = []

            j = 0
            for route in temp_active_routes:
                j += 1
                if j > 3:
                    break

                last_node = route[-1]
                next_nodes = reverse[last_node]
                print(
                    "route={} last_node={} next_nodes={}".format(
                        route,
                        last_node,
                        next_nodes,
                    )
                )

                if next_nodes is None:
                    routes.append(route)
                    continue

                if len(next_nodes) == 1:
                    route.insert(0, next_nodes.pop())
                    active_routes.append(route)
                    continue

                for next_node in next_nodes:
                    temp_route = route.copy()
                    temp_route.insert(0, next_node)
                    active_routes.append(temp_route)

            print("At bottom of loop")
            print(f"   active_routes {active_routes}")
            print(f"   routes {routes}")

        return routes



