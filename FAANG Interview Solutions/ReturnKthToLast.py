from LinkedList import LinkedList
def nthToLast(LL, n):
    pointer1 = LL.head
    pointer2 = LL.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))
