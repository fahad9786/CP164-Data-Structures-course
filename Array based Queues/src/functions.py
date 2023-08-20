"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-08"
-------------------------------------------------------
"""

from Queue_array import Queue

def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    
    target = Queue()
    
    
    while(not source1.is_empty() and not source2.is_empty()):
        a = source1.remove()
        b = source2.remove()
        target.insert(a)
        target.insert(b)
        
    while(not source1.is_empty()):
        a = source1.remove()
        target.insert(a)
         
    
    while(not source2.is_empty()):
        b = source2.remove()
        target.insert(b)

    return target


from Priority_Queue_array import Priority_Queue


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    
    ""
    
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while(not source.is_empty()):
        first = source.remove()
        if first < key:
            target1.insert(first)
        else:
            target2.insert(first)
    
 

    return target1, target2
    
    
    
    
    
    
    
    
    