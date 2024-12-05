
class Sliding_window_fixed_size:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        self.n = len(arr)
        self.result = []

    def find_max(self):
        max_sum = 0
        for i in range(self.k):
            max_sum += self.arr[i]
        self.result.append(max_sum)

        for i in range(self.k, self.n):
            max_sum += self.arr[i] - self.arr[i - self.k]
            self.result.append(max_sum)

        return max(self.result)
    
    def find_min(self):
        min_sum = 0
        for i in range(self.k):
            min_sum += self.arr[i]
        self.result.append(min_sum)

        for i in range(self.k, self.n):
            min_sum += self.arr[i] - self.arr[i - self.k]
            self.result.append(min_sum)

        return min(self.result)

if __name__ == "__main__":
    s = Sliding_window_fixed_size([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
    print(s.find_max())
    print(s.find_min())


class SlidingWindowFixedSizeTemplate:
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.n = len(data)

    def apply_operation(self, operation):
        result = []

        # Initialize the first window
        window_result = operation(self.data[:self.k])
        result.append(window_result)

        # Slide the window from start to end of the data
        for i in range(self.k, self.n):
            window_result = operation(self.data[i - self.k + 1:i + 1])
            result.append(window_result)

        return result

# Example usage
if __name__ == "__main__":
    def sum_operation(window):
        return sum(window)

    def concat_operation(window):
        return ''.join(window)

    # For numeric data
    s = SlidingWindowFixedSizeTemplate([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
    print(s.apply_operation(sum_operation))  # Output: [6, 6, 8, 10, 11, 10, 11]

    # For string data
    s = SlidingWindowFixedSizeTemplate(['a', 'b', 'c', 'd', 'e'], 2)
    print(s.apply_operation(concat_operation))  # Output: ['ab', 'bc', 'cd', 'de']