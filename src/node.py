class Node:
    def __init__(self, value, count=0, children={}) -> None:
        self.value: str = value
        self.count: int = count
        self.children: dict[str, Node] = children

    def add_child(self, child) -> None:
        self.children[child.value] = child

    def __str__(self) -> str:
        return f"({self.value} [{self.count}])"
