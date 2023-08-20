"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-01-24"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while(len(source) != 0):
    #copy the value on to top of stack and the pop it from the stack until
    # the stack is empty 
        stack.push(source.pop())
        
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    while(not stack.is_empty()):
        # fillking rarget
        # taking the last value and popping and then adding it to a new  list
        # then then next value moves down the old value
        target.insert(0,stack.pop())
        
        
    
    
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    # test to see if functtions work
    
    if not source.is_empty():
        source.push()
        source.pop()
        source.peek()
        
        
        
        
        
        
        
    # queues area now
        
        
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0 :
        queue.insert(source.pop(0))
    return 
    
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    while len(queue) > 0 :
        value = (queue.remove())
        target.append(value)
        
    

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    # test insert
    print("inserted value of queue", q.insert(5))
    
    print("is queue empty", q.is_empty())
    
    print("the length is" , len(q))
    
    print("peek: ", q.peek())
    
    
    while not q.is_empty():
        value = q.remove()
        print("Removed", value)
    

    return
    
    
    
    
    
    
    
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while (len(source) != 0):
        value = source.pop(0)
        pq.insert(value)
    

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while(not pq.is_empty()):
        value = pq.remove()
        target.append(value)
    

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    
    
    
    
    # figure out if it is empty or not
    if pq.is_empty() == True:
        print("good")
    else:
        print("bad")
        
   
    # insert list in pq
    # if the length r equal all is good
    for i in a:
        pq.insert(i)
    if len(pq) == len(a):
        print("good")
    else: 
        print("bad")
        
        
        
    # checking lengths agian for length functions see if works
    if (len(a) == len(pq)):
        print("good")
    else:
        print("bad")
        
    
    # seeing if 
    if ( pq.peek()  == max(a) ):
        print("good")
    else:
        print("bad")

    while not pq.is_empty():
        pq.remove()
        
    if pq.is_empty() == True:
        print("good")

    
    return 


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    while(len(source) > 0):
        llist.append(source.pop(0))
    
    
    
    

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    ---
    """
    while not llist.is_empty():
        target.append(llist.pop(0))
        

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    
        
    if lst.is_empty():
        print("True")
        
    for i in source:
        lst.append(i)
    
    if not lst.is_empty():
        print("True")
        
    lst.insert(0, 0)
    
    if lst.count(0) == 1:
        print("True")
        
    print("index should be 0:", lst.index(0))
        
    print("value should be 0:", lst.find(0))
    
    print("max should be 5:", lst.max())
    
    print("this would remove the one", lst.remove(0))
    
    print("min should be 1: ", lst.min())

    
        
    return







        
        
    