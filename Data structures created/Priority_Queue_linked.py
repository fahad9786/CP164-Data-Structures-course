"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2020-11-02"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        
        if self._front is None:
            node = _PQ_Node(value, None)
            self._front = node
            self._rear = node
        elif value < self._front._value:
            node = _PQ_Node(value, self._front)
            self._front = node
        elif value >= self._rear._value:
            node = _PQ_Node(value, None)
            self._rear._next = node
            self._rear = node
        else:
            prev = None
            curr = self._front
    
            while value >= curr._value:
                prev = curr
                curr = curr._next
    
            node = _PQ_Node(value, curr)
            prev._next = node
        
        self._count += 1
        return
            
    

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"


        # Your code here
        
        value = deepcopy(self._front._value)
        # your code here
        if self._count == 1:
            self._front = None 
            self._rear = None 
            self._count -= 1
            
        else:
            self._front = self._front._next
            self._count -= 1
        
        return (value)
    

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"


        # Your code here
        
        
        value = deepcopy(self._front._value)
        return value
        
        
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """

        # Your code here
        target1 = Priority_Queue()
        target2 = Priority_Queue()
        
        x = 1
        while self._front is not None:
            x += 1
            if x % 2 == 0:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
                
           
        
        
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """

        # Your code here
        target1 = Priority_Queue()
        target2 = Priority_Queue()
            
        while self._front is not None and self._front._value < key:
            target1._move_front_to_rear(self)
        
        while self._front is not None:
            target2._move_front_to_rear(self)
            
        return target1, target2
 
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        x = 1
        while source1._front is not None and source2._front is not None:
            x += 1
            if x % 2 == 0:
                self._move_front_to_rear(source1)
            else:
                self._move_front_to_rear(source2)
        if source1._front is not None:
            self._append_queue(source1)
            
        if(source2._front is not None):
            self._append_queue(source2)
                
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"


        # Your code here
        node1 = source._front
        if self._front is None:
            self._front = node1
        else:
            self._rear._next = node1
            
        
        self._count = source._count + self._count
        self._rear = source._rear  
        source._front = None 
        source._rear = None 
        source._count = 0
        
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"


        # Your code here
        
        # your code here
        node1 = source._front
        
        source._count -= 1
        source._front = source._front._next
        
        if source._front is None: 
            source._rear = None 


        if self._rear is None:
            self._front = node1 
        
        else: 
            self._rear._next = node1
        
        node1._next = None
        self._count += 1
        self._rear = node1
            
            
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next