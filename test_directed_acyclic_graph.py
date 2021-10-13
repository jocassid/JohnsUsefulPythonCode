
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

        dag = DirectedAcyclicGraph(a=('b'), c=('d',))

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
        assert False, "finish later"


