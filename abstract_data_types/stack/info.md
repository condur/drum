# Stack 

A stack is an ordered list in which insertion and deletion are done al one end, called top. The last clement inserted is the first one to be deleted. Hence, il is called the Last in First out (LIPO) or First in Last out (FILO) list).

Special names arc given to the two chanitcs that can be made to a stack. When an element is inserted in a stack, the concept is called _push_, and when an element is removed from the stack, the concept is called _pop_. Trying to pop out an empty stack is called _underflow_ and trying to push an clement in a full stack is called _overflow_.

## The following operations make a stack an ADT. For simplicity, assume the data is an integer type.

__Main stack operations__
• Push (int data): Inserts _data_ onto stack.
• int Pop(): Removes and returns the last inserted clement from the :>tack. 

__Auxiliary stack operations__
• int Top(): Returns the last inserted element without removing it.
• int Size(): Returns the number of elements stored in the stack.
• int isEmptyStack(): Indicates whether any clements an: stored in the stuck or not.
• int isFullStack(): Indicates whether the stack is full or not.
