close()
This method is used to close an open file. Once closed, it can't be read or written until reopened.

detach()
This is used on a buffered stream (like TextIOWrapper) to separate the underlying binary buffer from the text wrapper. After detaching, the original stream becomes unusable.

fileno()
Returns the file descriptor (an integer) of the file. This only works with real files (not in-memory streams).