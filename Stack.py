from typing import Any, Optional

class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["Node"] = None


class Stack:
    def __init__(self):
        self.top: Optional["Node"] = None
        self._size: int = 0

    def empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:  
        return self._size

    def push(self, data: Any) -> None:
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1
        
    def pop(self) -> Any:
        if self.empty():
            raise IndexError("Pilha vazia")
        assert self.top is not None
        node = self.top
        self.top = self.top.next
        self._size -= 1
        return node.data

    def peek(self) -> Optional[Node]:
        if self.empty():
            raise IndexError("Pilha vazia")
        return self.top

    def exclude(self, num=1) -> None:
        for _ in range(num):
            if self.empty():
                raise IndexError("Pilha vazia")
            self.pop()

    def __repr__(self) -> str:
        if self.empty():
            raise IndexError("Pilha vazia")

        resp = ""  
        node = self.top 

        while(node): 
            resp += str(node.data) + "\n" 
            node = node.next 
        return resp
