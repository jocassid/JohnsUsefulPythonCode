
from pytest import raises

from directed_acyclic_graph import DirectedAcyclicGraph


class TestDirectedAcyclicGraph:

    def test_empty_dag(self):

        dag = DirectedAcyclicGraph()

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            dag.check()
        message = "Graph should have at least 2 nodes"
        assert message == str(exec_info.value)

    def test_check_value_not_iterable(self):
        dag = DirectedAcyclicGraph(a=5, b=6)
        with raises(DirectedAcyclicGraph.Error) as exec_info:
            dag.check()
        message = "Error with node a.  5 is not iterable"
        assert message == str(exec_info.value)

    def test_check__target_not_in_graph(self):

        dag = DirectedAcyclicGraph(a=('b',), c=('d',))

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            dag.check()
        message = "Error with node a.  b not found in graph"
        assert message == str(exec_info.value)

    def test_check__graph_has_cycle(self):
        pairs = (
            (1, (2,)),
            (2, (3,)),
            (3, (4, 5)),
            (4, None),
            (5, (2,)),
        )
        dag = DirectedAcyclicGraph(pairs)

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            dag.check()
        message = "Graph is cyclic. 1, 2, 3, 5, 2"
        assert message == str(exec_info.value)

    def test_check__graph_has_no_leaf_nodes(self):

        dag = DirectedAcyclicGraph(
            a=('b',),
            b=('c', 'd'),
            c=None,
            d=('a',),
        )

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            dag.check()
        message = "Graph has no leaf nodes and is cyclic"
        assert str(exec_info.value).startswith(message)

    def test_leaf_nodes(self):

        dag = DirectedAcyclicGraph(
            a=('c',),
            b=('c',),
            c=('d',),
            d=None,
        )

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            leaf_nodes = dag.leaf_nodes
        message = "call check before accessing leaf_nodes"
        assert message == str(exec_info.value)

        dag.check()
        assert {'a', 'b'} == dag.leaf_nodes

    def test_reverse(self):

        dag = DirectedAcyclicGraph(
            a=('c',),
            b=('c',),
            c=('d',),
            d=None,
        )

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            junk = dag.reverse
            del junk
        message = 'call check before accessing reverse'
        assert message == str(exec_info.value)

        dag.check()

        expected = {
            'd': {'c'},
            'c': {'b', 'a'},
            'b': None,
            'a': None,
        }
        actual = dag.reverse
        assert expected == actual

    def test_routes(self):

        dag = DirectedAcyclicGraph(
            a=('c',),
            b=('c',),
            c=('d',),
            d=None,
        )

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            junk = dag.routes_to('a')
        message = 'call check before calling routes_to'
        assert message == str(exec_info.value)
        dag.check()

        with raises(DirectedAcyclicGraph.Error) as exec_info:
            junk = dag.routes_to('e')
        message = 'node e not present in this graph'
        assert message == str(exec_info.value)

        expected = [
            ['a'],
        ]
        actual = dag.routes_to('a')
        assert expected == actual



    def test_shortest_route(self):
        assert False, 'later'
