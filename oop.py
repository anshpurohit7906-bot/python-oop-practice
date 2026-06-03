import numpy as np

class ArrayMath:
    def __init__(self, initial_list):
        self.numbers = np.array(initial_list)
        
        if not np.issubdtype(self.numbers.dtype, np.number):
            raise ValueError("All elements must be numbers!")

    def add_to_all(self, value):
        self.numbers = self.numbers + value

    def multiply(self, factor):
        self.numbers = self.numbers * factor

    def filter_greater_than(self, threshold):
        self.numbers = self.numbers[self.numbers > threshold]


class DataMatrix:
    def __init__(self, initial_grid):
        self.matrix = np.array(initial_grid)

    def get_column(self, col_index):
        return self.matrix[:, col_index]

    def get_row_sum(self, row_index):
        return np.sum(self.matrix[row_index, :])

    def scale_matrix(self, factor):
        self.matrix = self.matrix * factor

    def get_anomalies(self, threshold):
        return self.matrix[self.matrix > threshold]


# --- LOCAL VERIFICATION RUN ---
if __name__ == "__main__":
    print("--- Testing ArrayMath Safeguard ---")
    try:
        bad_box = ArrayMath(["Apple", "Banana"])
    except ValueError as e:
        print("Safeguard caught error successfully:", e)

    print("\n--- Testing DataMatrix Matrix Operations ---")
    grid = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    server_data = DataMatrix(grid)
    
    print("Column 1 Slicing:", server_data.get_column(1))
    print("Row 1 Aggregation Sum:", server_data.get_row_sum(1))
    print("Matrix Anomalies (>50):", server_data.get_anomalies(50))