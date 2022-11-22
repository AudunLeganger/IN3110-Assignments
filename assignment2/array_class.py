"""
Array class for assignment 2
"""

class Array:

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
        # Checks if values are homogenous
        if not self.check_homogenous(values):
            raise Exception("Array not homogenous")

        # Check if the values are of valid types
        if not self.check_type_validity(values):
            raise Exception("Array data type not valid")

        # Check that the amount of values corresponds to the shape
        if not self.check_shape_validity(shape, values):
            raise Exception("Array data shape not valid")

        # Set instance attributes
        self.shape = shape
        self.values = []
        for value in values:
            self.values.append(value)


    # Checks for datatype homogeniety
    def check_homogenous(self,values):
        data_type = type(values[0])
        for element in values:
            if data_type is not type(element):
                return False
        self.data_type = type(values[0])
        return True
    
    # Checks for valid data types
    def check_type_validity(self,values):
        data_type = str(self.data_type)
        if data_type == "<class 'int'>" or data_type == "<class 'float'>" or data_type == "<class 'bool'>" or data_type == "<class 'complex'>":
            return True
        return False

    # Checks for shape validity
    def check_shape_validity(self, shape, values):
        prod = 1
        for length in shape:
            prod = prod * length
        return prod == len(values)
    
    # Returns shape of the array object
    def get_shape(self):
        return self.shape
    
    # Returns a formated string displaying the array contents
    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        print_string = "["
        for i in range(len(self.values)-1):
            print_string = print_string + str(self.values[i]) + ", "
        print_string = print_string + str(self.values[-1]) + "]"
        return print_string


    def __getitem__(self, index):
        """Returns whatever data is stored at the given index.
        """
        return self.values[index]


    def perform_scalar_operation(self, other, operator):
        """Performs a mathematical scalar operation on the array, and returns the resulting array object."""
        values = []
        for value in self.values:
            values.append(value)

        if operator == "+":
            for i in range(len(values)):
                values[i] = values[i] + other

        elif operator == "-":
            for i in range(len(values)):
                values[i] = values[i] - other

        elif operator == "*":
            for i in range(len(values)):
                values[i] = values[i] * other
        result_array = Array(self.shape, *values)
        return result_array

        
    def perform_array_operator(self, other, operator):
        """Performs a mathematical array operation on the array, and returns the resulting array object."""
        values = []
        for value in self.values:
            values.append(value)
            
        if operator == "+":
            for i in range(len(values)):
                values[i] = values[i] + other[i]

        elif operator == "-":
            for i in range(len(values)):
                values[i] = values[i] - other[i]

        elif operator == "*":
            for i in range(len(values)):
                values[i] = values[i] * other[i]
        
        result_array = Array(self.shape, *values)
        return result_array

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        # Checks for addition with integers
        if str(type(other)) == "<class 'int'>":
            return self.perform_scalar_operation(other,"+")

        # Checks for data type mismatch
        type_other = str(type(other[0]))
        if type_other != str(self.data_type):
            raise TypeError("Type mismatch.")
        
        # Checks for shape mismatch
        elif other.get_shape() != self.shape:
            raise ValueError("Shape mismatch.")

        # Checks for addition with booleans
        if type_other == "<class 'boolean'>":
            raise TypeError("Not implemented.")
        
        # Checks for element-wise array addition
        elif type_other == "<class 'float'>" or type_other == "<class 'complex'>" or type_other == "<class 'int'>":
            return self.perform_array_operator(other,"+")
        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        # Checks for addition with integers
        if str(type(other)) == "<class 'int'>":
            return self.perform_scalar_operation(other,"-")

        # Checks for data type mismatch
        type_other = str(type(other[0]))
        if type_other != str(self.data_type):
            raise TypeError("Type mismatch.")
        
        # Checks for shape mismatch
        elif other.get_shape() != self.shape:
            raise ValueError("Shape mismatch.")

        # Checks for addition with booleans
        if type_other == "<class 'boolean'>":
            raise TypeError("Not implemented.")
        
        # Checks for element-wise array addition
        elif type_other == "<class 'float'>" or type_other == "<class 'complex'>" or type_other == "<class 'int'>":
            return self.perform_array_operator(other,"-")

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        # 10-Array1
        # return -1 * Array1 + 10
        return (self.__mul__(-1) + other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Checks for addition with integers
        if str(type(other)) == "<class 'int'>":
            return self.perform_scalar_operation(other,"*")

        # Checks for data type mismatch
        type_other = str(type(other[0]))
        if type_other != str(self.data_type):
            raise TypeError("Type mismatch.")
        
        # Checks for shape mismatch
        elif other.get_shape() != self.shape:
            raise ValueError("Shape mismatch.")

        # Checks for addition with booleans
        if type_other == "<class 'boolean'>":
            raise TypeError("Not implemented.")
        
        # Checks for element-wise array addition
        elif type_other == "<class 'float'>" or type_other == "<class 'complex'>" or type_other == "<class 'int'>":
            return self.perform_array_operator(other,"*")

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
