import numpy
import threading


class RingBuffer:
    """a basic threadsafe implementation of a ringbuffer.

    For more information on circular buffers and their use cases see:
    https://en.wikipedia.org/wiki/Circular_buffer
    """

    def __init__(self, type, size):
        """initalize a new ringbuffer

        Args:
            type (any numpy type): The type to use for the underlaying numby array
            size (int): The size of the ringbuffer
        """
        self.__type = type
        self.__size = size
        self.__index = 0
        self.__buffer = numpy.empty(shape=size, dtype=type)
        self.__full = False
        self.__lock = threading.Lock()

    def append(self, value):
        """Append a value to the buffer

        Args:
            value (any): the object or value you want to append to the ringbuffer
        """
        self.__lock.acquire()
        self.__buffer[self.__index] = value
        self.__index += 1

        # make sure the buffer actually loops back
        if self.__index < self.__size:
            self.__lock.release()
            return

        self.__index = 0
        self.__full = True
        self.__lock.release()

    def get_buffer_copy(self):
        """get a copy of the entire buffer in a threadsafe manner

        Returns:
            numpy array: a direct copy of the entire buffer
        """
        self.__lock.acquire()
        copy = self.__buffer.copy()
        self.__lock.release()

        return copy

    def get_last_entry(self):
        """get the most recent entry into the ringbuffer or None if there are none

        Returns:
            object: the most recent entry in the ringbuffer
        """
        val = None
        self.__lock.acquire()

        # return None if there are no entries
        if self.__full or self.__index != 0:
            val = self.__buffer[self.__index - 1]
        self.__lock.release()

        return val

    def get_recent_entries(self, count):
        """Get N most recent entries from the ringbuffer in a threadsafe manner.
        Most recent entries first.
        Errors if count is bigger than the size of the buffer.

        Args:
            count (integer): The amount of objects you wish to retrieve

        Returns:
            numpy array: an array containing the entries
        """

        entries = numpy.empty(count, self.__type)

        self.__lock.acquire()
        if count > self.__size:
            raise Exception("count: %s exceeds the size: %s of the ringbuffer." % (count, self.__size))
        read_index = self.__index - 1

        if read_index < 0:
            read_index = self.__size - 1

        for i in range(count):
            entries[i] = self.__buffer[read_index]

            read_index -= 1
            if read_index < 0:
                read_index = self.__size - 1
        self.__lock.release()

        return entries
