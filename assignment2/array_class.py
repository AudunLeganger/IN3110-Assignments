"""
Array class for assignment 2
"""

class Array:
    from itertools import chain
    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        # Check if the values are of valid types
        # Check that the amount of values corresponds to the shape
        # Set instance attributes
        if not self.is_homogenous(values):
            raise ValueError("Array parameters are not of same data type")
        if not self.is_valid_type(values):
            raise TypeError("Array parameters are not of supported data type (int/float/complex/bool)")
        if not self.is_valid_shape(shape, values):
            raise ValueError("Array dimensions do not match value count")
        
        self.shape = shape
        self.values = self.make_data_structure(shape,values)
        
    
    def is_homogenous(self, values):
        '''Returns True if elements of array are of same type. If not, returns False'''
        data_type = type(values[0])
        for value in values:
            if data_type != type(value):
                return False
        return True

    def is_valid_type(self, values):
        valid_types = [type(1), type(1.0), type(True), type(complex(1,1))]
        if type(values[0] in valid_types):
            return True
        return False
    
    def is_valid_shape(self, shape, values):
        '''Returns true if the number of elements resulting from shape is equal to the number of elements in values'''
        elements_shape = 1
        for entry in shape:
            elements_shape = elements_shape * entry

        if elements_shape == len(values):
            return True
        return False
    
    def make_data_structure(self,shape,values):
        '''Iterates through the arguments in "shape", and calls on make_nested_list accordingly
        Returns:
            list: nested list containing the data in values as specified by the dimensions in "shape"'''
        cur_values = list(values)
        for i in range(len(shape)-1, 0, -1):
            cur_length = shape[i]
            cur_values = self.make_nested_list(cur_length,cur_values)
        return cur_values
    
    def make_nested_list(self, list_length, values):
        '''Groups list elements of list "values" in new list of length "list_length"
        Retruns:
            list: list containing nested lists'''
        iterations = int((len(values)/list_length))
        nested_list = []
        for i in range(iterations):
            new_element = values[i*list_length : (i*list_length + list_length)]
            nested_list.append(new_element)
        return nested_list


    def flat_array(self):
        """Flattens the N-dimensional array of values into a 1-dimensional array.
        Returns:
            list: flat list of array values.
        """
        flat_array = self._array
        for _ in range(len(self.shape[1:])):
            flat_array = list(chain(*flat_array))
        return flat_array

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        pass

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented

        pass

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        pass

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        pass

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        pass

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        pass

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        pass

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        pass
