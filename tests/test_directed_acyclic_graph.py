#!/usr/bin/env python3

# This file is part of https://github.com/jocassid/JohnsUsefulPythonCode
# This file is in the public domain, be excellent to one another, party on dudes.

from pytest import raises

from directed_acyclic_graph import \
    Graph, \
    GraphError, \
    GraphPath, \
    DirectedAcyclicGraph, \
    Node


class TestNode:

    def test_init(self):
        node = Node('a')
        assert node.label == 'a'
        assert node.next_labels == set()
        assert node.data is None

        node = Node('a', 'b', 'c')
        assert node.label == 'a'
        assert node.next_labels == {'b', 'c'}
        assert node.data is None

        node = Node('a', 'b', 'c', data='foo')
        assert node.label == 'a'
        assert node.next_labels == {'b', 'c'}
        assert node.data == 'foo'


class TestGraphPath:

    def test_init(self):
        with raises(GraphError) as exec_info:
            GraphPath(['a', 'b', 'a'])
        message = "label a already in path"
        assert message == str(exec_info.value)

        graph = GraphPath()
        assert graph == []

        graph = GraphPath(['a', 'b'])
        assert graph == ['a', 'b']

    def test_insert(self):
        graph = Graph(['a'])



class TestGraph:

    def test_init(self):
        assert Graph(Node('a')) == {'a': Node('a')}

        with raises(GraphError) as exec_info:
            Graph(Node('a', 'b'))
        message = 'missing Node with label b'
        assert message == str(exec_info.value)

        graph = Graph(Node('a', 'b'), Node('b'))
        expected = {
            'a': Node('a', 'b'),
            'b': Node('b'),
        }
        assert graph == expected

        with raises(GraphError) as exec_info:
            Graph(
                Node('a'),
                Node('a'),
            )
        message = "Node labeled a already defined"
        assert message == str(exec_info.value)

    def test_validate_label(self):
        graph = Graph(Node('a', 'b'), Node('b'))

        arg_name = 'label1'
        graph.validate_label(arg_name, 'a')

        with raises(GraphError) as exec_info:
            graph.validate_label(arg_name, 'c')
        message = 'label1 c not present in graph'
        assert message == str(exec_info.value)

    def test_get_paths_between__no_branch_graph(self):
        graph = Graph(
            Node('a', 'b'),
            Node('b', 'c'),
            Node('c'),
        )

        with raises(GraphError) as exec_info:
            graph.get_paths_between('a', 'a')
        message = "Labels are identical"
        assert message == str(exec_info.value)

        expected = [['a', 'b']]
        paths = graph.get_paths_between('a', 'b')
        assert expected == paths

        expected = [['a', 'b', 'c']]
        paths = graph.get_paths_between('a', 'c')
        assert expected == paths

    def test_get_paths_between__simple_branch_graph(self):
        graph = Graph(
            Node('a', 'b'),
            Node('b', 'c', 'd'),
            Node('c', 'e'),
            Node('d', 'e'),
            Node('e'),
        )

        expected = sorted([
            ['a', 'b', 'c', 'e'],
            ['a', 'b', 'd', 'e'],
        ])
        actual = sorted(graph.get_paths_between('a', 'e'))
        assert expected == actual

    def test_get_paths_between__cyclic_graph(self):
        graph = Graph(
            Node('a', 'b'),
            Node('b', 'a', 'c'),
            Node('c'),
        )

        assert False, "Warning infinite loop!"





#
# class TestDirectedAcyclicGraph:
#
#     def test_empty_dag(self):
#
#         dag = DirectedAcyclicGraph()
#
#         with raises(GraphError) as exec_info:
#             dag.check()
#         message = "Graph should have at least 2 nodes"
#         assert message == str(exec_info.value)
#
#     def test_check_value_not_iterable(self):
#         dag = DirectedAcyclicGraph(a=5, b=6)
#         with raises(GraphError) as exec_info:
#             dag.check()
#         message = "Error with node a.  5 is not iterable"
#         assert message == str(exec_info.value)
#
#     def test_check__target_not_in_graph(self):
#
#         dag = DirectedAcyclicGraph(a=('b',), c=('d',))
#
#         with raises(GraphError) as exec_info:
#             dag.check()
#         message = "Error with node a.  b not found in graph"
#         assert message == str(exec_info.value)
#
#     def test_check__graph_has_cycle(self):
#         pairs = (
#             (1, (2,)),
#             (2, (3,)),
#             (3, (4, 5)),
#             (4, None),
#             (5, (2,)),
#         )
#         dag = DirectedAcyclicGraph(pairs)
#
#         with raises(GraphError) as exec_info:
#             dag.check()
#         message = "Graph is cyclic. 1, 2, 3, 5, 2"
#         assert message == str(exec_info.value)
#
#     def test_check__graph_has_no_leaf_nodes(self):
#
#         dag = DirectedAcyclicGraph(
#             a=('b',),
#             b=('c', 'd'),
#             c=None,
#             d=('a',),
#         )
#
#         with raises(GraphError) as exec_info:
#             dag.check()
#         message = "Graph has no leaf nodes and is cyclic"
#         assert str(exec_info.value).startswith(message)
#
#     def test_leaf_nodes(self):
#
#         dag = DirectedAcyclicGraph(
#             a=('c',),
#             b=('c',),
#             c=('d',),
#             d=None,
#         )
#
#         with raises(GraphError) as exec_info:
#             leaf_nodes = dag.leaf_nodes
#         message = "call check before accessing leaf_nodes"
#         assert message == str(exec_info.value)
#
#         dag.check()
#         assert {'a', 'b'} == dag.leaf_nodes
#
#     def test_reverse(self):
#
#         dag = DirectedAcyclicGraph(
#             a=('c',),
#             b=('c',),
#             c=('d',),
#             d=None,
#         )
#
#         with raises(GraphError) as exec_info:
#             junk = dag.reverse
#             del junk
#         message = 'call check before accessing reverse'
#         assert message == str(exec_info.value)
#
#         dag.check()
#
#         expected = {
#             'd': {'c'},
#             'c': {'b', 'a'},
#             'b': None,
#             'a': None,
#         }
#         actual = dag.reverse
#         assert expected == actual
#
#     @staticmethod
#     def build_dag():
#         return DirectedAcyclicGraph(
#             a=('c',),
#             b=('c',),
#             c=('d',),
#             d=None,
#         )
#
#     def test_routes_to__not_checked(self):
#         dag = self.build_dag()
#
#         with raises(GraphError) as exec_info:
#             junk = dag.routes_to('a')
#         message = 'call check before calling routes_to'
#         assert message == str(exec_info.value)
#
#     def test_routes_to__node_not_present(self):
#         dag = self.build_dag()
#         dag.check()
#
#         with raises(GraphError) as exec_info:
#             junk = dag.routes_to('e')
#         message = 'node e not present in this graph'
#         assert message == str(exec_info.value)
#
#     def test_routes_to__starting_at_leaf(self):
#         dag = self.build_dag()
#         dag.check()
#
#         expected = [
#             ['a'],
#         ]
#         actual = dag.routes_to('a')
#         assert expected == actual
#
#     def test_routes_to__not_at_leaf(self):
#         dag = self.build_dag()
#         dag.check()
#
#         expected = [
#             ['a', 'c'],
#             ['b', 'c'],
#         ]
#         actual = dag.routes_to('c')
#         assert expected == actual
#
#     def test_shortest_route(self):
#         assert False, 'later'
