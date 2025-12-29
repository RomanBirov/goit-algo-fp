from dataclasses import dataclass
from typing import Optional, Iterable


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class LinkedList:
    def __init__(self, values: Optional[Iterable[int]] = None) -> None:
        self.head: Optional[Node] = None
        if values:
            for v in values:
                self.append(v)

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def to_list(self) -> list[int]:
        result: list[int] = []
        cur = self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result

    def reverse(self) -> None:
        prev: Optional[Node] = None
        cur = self.head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        self.head = prev

    def sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        mid = self._get_middle(head)
        right_head = mid.next
        mid.next = None

        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(right_head)

        return self._merge_two_sorted_nodes(left_sorted, right_sorted)

    def _get_middle(self, head: Node) -> Node:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def _merge_two_sorted_nodes(
        a: Optional[Node], b: Optional[Node]
    ) -> Optional[Node]:
        dummy = Node(0)
        tail = dummy

        while a and b:
            if a.value <= b.value:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        return dummy.next


def merge_sorted_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    merged = LinkedList()
    merged.head = LinkedList._merge_two_sorted_nodes(l1.head, l2.head)
    return merged


if __name__ == "__main__":
    ll = LinkedList([3, 1, 5, 2, 4])
    print("Original:", ll.to_list())

    ll.reverse()
    print("Reversed:", ll.to_list())

    ll.sort()
    print("Sorted:", ll.to_list())

    a = LinkedList([1, 3, 5, 7])
    b = LinkedList([2, 4, 6, 8])
    merged = merge_sorted_lists(a, b)
    print("Merged:", merged.to_list())
