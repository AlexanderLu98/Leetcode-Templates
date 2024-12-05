
class Sliding_window_variable_size():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.result = []

    def find_max(self):
        max_sum = 0
        for i in range(self.n):
            max_sum += self.arr[i]
            self.result.append(max_sum)
        return max(self.result)
    
    def find_min(self):
        min_sum = 0
        for i in range(self.n):
            min_sum += self.arr[i]
            self.result.append(min_sum)
        return min(self.result)

if __name__ == "__main__":
    s = Sliding_window_variable_size([1, 2, 3, 1, 4, 5, 2, 3, 6])
    print(s.find_max())
    print(s.find_min())

class SlidingWindowVariableSizeTemplate:
    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def apply_operation(self, min_k, max_k, operation):
        result = []

        # Iterate over all possible window sizes from min_k to max_k
        for k in range(min_k, max_k + 1):
            # Initialize the first window
            window_result = operation(self.data[:k])
            result.append((k, window_result))

            # Slide the window from start to end of the data
            for i in range(k, self.n):
                window_result = operation(self.data[i - k + 1:i + 1])
                result.append((k, window_result))

        return result

# Example usage
if __name__ == "__main__":
    def sum_operation(window):
        return sum(window)

    def concat_operation(window):
        return ''.join(window)

    # For numeric data
    s = SlidingWindowVariableSizeTemplate([1, 2, 3, 1, 4, 5, 2, 3, 6])
    print(s.apply_operation(2, 4, sum_operation))  
    # Output: [(2, 3), (2, 5), (2, 4), (2, 5), (2, 9), (2, 7), (2, 5), (2, 9), (3, 6), (3, 6), (3, 8), (3, 10), (3, 11), (3, 10), (3, 11), (4, 7), (4, 10), (4, 13), (4, 12), (4, 14)]

    # For string data
    s = SlidingWindowVariableSizeTemplate(['a', 'b', 'c', 'd', 'e'])
    print(s.apply_operation(2, 3, concat_operation))  
    # Output: [(2, 'ab'), (2, 'bc'), (2, 'cd'), (2, 'de'), (3, 'abc'), (3, 'bcd'), (3, 'cde')]