"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    for value in values:
        # Compute hash value
        hash_value = hash(value)

        # Map hash value to a slot in the hash table
        slot = hash_value % slots

        # Print the hash value, slot number, and value
        print("{:8d} {:4d} {}".format(hash_value, slot, value))
    
    return