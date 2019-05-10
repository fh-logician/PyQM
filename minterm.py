class Minterm:
    """An object to hold information about a minterm when using the Quine-McCluskey Algorithm
    """

    def __init__(self, values, value):
        self._values = values
        self._value = value
        self._used = False

        self._values.sort()
    
    def __str__(self):
        values = ", ".join([str(value) for value in self._values])
        return f"m({values}) = {self._value}"
    
    def __eq__(self, minterm):

        if type(minterm) != Minterm:
            return False

        return (
            self._value == minterm._value and
            self._values == minterm._values
        )
    
    def get_values(self):
        """Returns all the implicants that this minterm covers.
        """
        return self._values
    
    def get_value(self):
        """Returns the bit values ('-010', '1010', etc.) for this minterm.
        """
        return self._value
    
    def use(self):
        """Keeps track of when this minterm is "used" in a comparison.
        """
        self._used = True
    
    def used(self):
        """Returns whether or not this minterm was used.
        """
        return self._used
    
    def combine(self, minterm):
        """Combines this minterm with the specified minterm if possible.
        """

        # Check if this minterm is the same as the one trying to be combined with
        if self._value == minterm._value or self._values == minterm._values:
            return None
        
        # Keep track of the amount of difference between the value of the minterm
        #   and also keep track of the resulting string
        diff = 0
        result = ""

        # Iterate through all the bit values
        for char in range(len(self._value)):

            # Check if this minterm and the combined minterm have a bit difference
            if self._value[char] != minterm._value[char]:
                diff += 1
                result += "-"
            
            # There is no difference
            else:
                result += self._value[char]
            
            # The difference is greater than 1, these minterms cannot be combined
            if diff > 1:
                return None
        
        return Minterm(self._values + minterm._values, result)
