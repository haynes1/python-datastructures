import linkedlist as ll

L = ll.LinkedList()

# n0 = ll.ListNode(0)
# n1 = ll.ListNode(1)
# n2 = ll.ListNode(2)
# n3 = ll.ListNode(3)
# n4 = ll.ListNode(4)

L.append(0)
L.append(1)
L.append(2)
L.append(3)
L.append(4)

print "traverse 1"
L.traverse1()

print "\n\n"

print "traverse 2"
L.traverse2()