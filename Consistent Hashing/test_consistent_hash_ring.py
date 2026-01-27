import threading
import unittest

from consistent_hash_ring import ConsistentHashRing


class TestConsistentHashRing(unittest.TestCase):
    def test_empty_ring_returns_none(self) -> None:
        ring = ConsistentHashRing()
        self.assertIsNone(ring.getNode("alpha"))

    def test_add_nodes_then_get_node_returns_one_of_them(self) -> None:
        ring = ConsistentHashRing(replicas=10)
        nodes = {"node-a", "node-b", "node-c"}
        for node in nodes:
            ring.addNode(node)
        self.assertIn(ring.getNode("alpha"), nodes)
        self.assertIn(ring.getNode("beta"), nodes)

    def test_add_same_node_twice_idempotent(self) -> None:
        ring = ConsistentHashRing(replicas=5)
        ring.addNode("node-a")
        size_before = len(ring._positions)
        ring.addNode("node-a")
        size_after = len(ring._positions)
        self.assertEqual(size_before, size_after)

    def test_remove_missing_node_no_op(self) -> None:
        ring = ConsistentHashRing()
        ring.addNode("node-a")
        size_before = len(ring._positions)
        ring.removeNode("node-missing")
        size_after = len(ring._positions)
        self.assertEqual(size_before, size_after)

    def test_remove_existing_node(self) -> None:
        ring = ConsistentHashRing(replicas=10)
        ring.addNode("node-a")
        ring.addNode("node-b")
        ring.removeNode("node-a")
        for key in ["alpha", "beta", "gamma", "delta"]:
            self.assertNotEqual(ring.getNode(key), "node-a")

    def test_concurrency_stress(self) -> None:
        ring = ConsistentHashRing(replicas=20)
        ring.addNode("node-a")
        ring.addNode("node-b")
        stop_event = threading.Event()
        errors = []

        def reader() -> None:
            try:
                while not stop_event.is_set():
                    ring.getNode("alpha")
                    ring.getNode("beta")
            except Exception as exc:
                errors.append(exc)

        def writer() -> None:
            try:
                for _ in range(200):
                    ring.addNode("node-c")
                    ring.removeNode("node-c")
            except Exception as exc:  # pragma: no cover - testing concurrency safety
                errors.append(exc)

        readers = [threading.Thread(target=reader) for _ in range(5)]
        writer_thread = threading.Thread(target=writer)
        for thread in readers:
            thread.start()
        writer_thread.start()
        writer_thread.join()
        stop_event.set()
        for thread in readers:
            thread.join()

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
