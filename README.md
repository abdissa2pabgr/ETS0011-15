close()
This method is used to close an open file. Once closed, it can't be read or written until reopened.

detach()
This is used on a buffered stream (like TextIOWrapper) to separate the underlying binary buffer from the text wrapper. After detaching, the original stream becomes unusable.

fileno()
Returns the file descriptor (an integer) of the file. This only works with real files (not in-memory streams).

flush()
This method flushes the internal buffer, writing all buffered content to the file. It's useful when you want to make sure everything is written out to the file system immediately.

isatty()
Returns True if the file is connected to a terminal device (like the console). For files, it usually returns False.

read()
Reads the entire content of the file (or up to a given number of characters).

