
from collections import OrderedDict


class DirectedAcyclicGraph(OrderedDict):
    """There's a graph module in the standard library for Python 3.9+, but
    until we upgrade the servers here we are."""

    class Error(RuntimeError):
        pass

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
            raise self.Error('Graph should have at least 2 nodes')

        self._leaf_nodes = set(self.keys())
        self.visited_nodes = set()

        for node, dest_nodes in self.items():

            if dest_nodes is None:
                continue

            if not hasattr(dest_nodes, '__iter__'):
                raise self.Error(
                    f"Error with node {node}.  {dest_nodes} is not iterable"
                )

            for item in dest_nodes:
                if item not in self:
                    raise self.Error(
                        f"Error with node {node}.  {item} not found in graph"
                    )

                if item in self._leaf_nodes:
                    self._leaf_nodes.remove(item)

        if not self._leaf_nodes:
            raise self.Error(f"Graph has no leaf nodes and is cyclic.")

        for leaf_node in self._leaf_nodes:
            self.visited_nodes = set()
            path = self._check_node(leaf_node)
            if path:
                path = ", ".join(str(n) for n in path)
                raise self.Error(f"Graph is cyclic. {path}")
        self.needs_check = False

        # done checking, lets free up some memory
        self.unvisited_nodes = None
        self.visited_nodes = None

    @property
    def leaf_nodes(self):
        if self.needs_check:
            raise self.Error(
                "call check before accessing leaf_nodes"
            )
        return self._leaf_nodes

    @property
    def reverse(self):
        if self.needs_check:
            raise self.Error(
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
            raise self.Error(
                "call check before calling routes_to"
            )

        if node not in self:
            raise self.Error(
                f"node {node} not present in this graph"
            )

        reverse = self._reverse or self.reverse
        print(reverse)

        routes = []
        while
        next_nodes = reverse[node]


        return routes



