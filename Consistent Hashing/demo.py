"""Demo script for ConsistentHashRing usage."""

from consistent_hash_ring import ConsistentHashRing


def main() -> None:
    ring = ConsistentHashRing(replicas=5)
    for node in ("node-a", "node-b", "node-c"):
        ring.addNode(node)

    keys = ["alpha", "beta", "gamma", "delta"]
    for key in keys:
        node = ring.getNode(key)
        print(f"{key} -> {node}")

    ring.removeNode("node-b")
    print("After removing node-b:")
    for key in keys:
        node = ring.getNode(key)
        print(f"{key} -> {node}")


if __name__ == "__main__":
    main()
