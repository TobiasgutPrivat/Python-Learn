import numpy as np

my_array = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(my_array[0])
print(my_array[:,-1])
print(my_array[:2,1])

def percentArray(array):
    sum = np.sum(array)
    new = array / sum
    return new

class ArrayAnalyzer:
    def __init__(self, array):
        self.array = array

    def get_boolean_array(self):
        return self.array > 5

    def get_percent_array(self):
        return percentArray(self.array)
    
analyzer = ArrayAnalyzer(my_array)
print(analyzer.get_boolean_array())
print(analyzer.get_percent_array())

assert np.isclose(np.sum(analyzer.get_percent_array()), 1), "The sum of the percent array should be 1"