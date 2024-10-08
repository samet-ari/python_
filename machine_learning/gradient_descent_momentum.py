"""
Implementation of gradient descent algorithm using momentum for minimizing cost of a linear hypothesis
function.
"""
import numpy as np

# List of input, output pairs
train_data = (
    ((5, 2, 3), 15),
    ((6, 5, 9), 25),
    ((11, 12, 13), 41),
    ((1, 1, 1), 8),
    ((11, 12, 13), 41),
)
test_data = (((515, 22, 13), 555), ((61, 35, 49), 150))
parameter_vector = [2, 4, 1, 5]
m = len(train_data)
LEARNING_RATE = 0.009
MOMENTUM = 0.9

# Initialize velocity (for momentum)
velocity = [0] * len(parameter_vector)

def _error(example_no, data_set="train"):
    """
    Calculate the error (difference between predicted and actual output) for a given example.
    Args:
        example_no (int): Index of the example in the dataset.
        data_set (str): The dataset to use, either "train" or "test". 
    Returns:
        float: The difference between the predicted output and the actual output.
    """
    return calculate_hypothesis_value(example_no, data_set) - output(example_no, data_set)


def _hypothesis_value(data_input_tuple):
    """
    Compute the hypothesis value (predicted output) for a given input tuple.
    Args:
        data_input_tuple (tuple): The input tuple (features) for the example.
    Returns:
        float: The hypothesis value for the given input.
    """
    hyp_val = 0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    return hyp_val


def output(example_no, data_set):
    """
    Retrieve the actual output (label) for a given example from the specified dataset.
    Args:
        example_no (int): Index of the example in the dataset.
        data_set (str): The dataset to use, either "train" or "test".
    Returns:
        int: The actual output value for the specified example.
    """
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]
    return None


def calculate_hypothesis_value(example_no, data_set):
    """
    Calculate the hypothesis value (predicted output) for a given example.
    Args:
        example_no (int): Index of the example in the dataset.
        data_set (str): The dataset to use, either "train" or "test".
    Returns:
        float: The hypothesis value for the specified example.
    """
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set == "test":
        return _hypothesis_value(test_data[example_no][0])
    return None


def summation_of_cost_derivative(index, end=m):
    """
    Calculate the summation of the cost derivative for a given index.
    Args:
        index (int): The index of the parameter for which the derivative is calculated.
        end (int): The number of examples to consider (defaults to the size of the training set).
    Returns:
        float: The summation of the cost derivatives for the given parameter.
    """
    summation_value = 0
    for i in range(end):
        if index == -1:
            summation_value += _error(i)
        else:
            summation_value += _error(i) * train_data[i][0][index]
    return summation_value


def get_cost_derivative(index):
    """
    Compute the cost derivative with respect to a parameter.
    Args:
        index (int): The index of the parameter.
    Returns:
        float: The cost derivative for the specified parameter.
    """
    return summation_of_cost_derivative(index, m) / m


def run_gradient_descent_with_momentum():
    """
    Run gradient descent with momentum to minimize the cost function.
    This function updates the parameter vector using velocity and the learning rate.
    """
    global parameter_vector, velocity
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    iteration = 0
    while True:
        iteration += 1
        temp_parameter_vector = [0] * len(parameter_vector)
        for i in range(len(parameter_vector)):
            cost_derivative = get_cost_derivative(i - 1)
            velocity[i] = MOMENTUM * velocity[i] + cost_derivative
            temp_parameter_vector[i] = parameter_vector[i] - LEARNING_RATE * velocity[i]
        
        if np.allclose(parameter_vector, temp_parameter_vector, atol=absolute_error_limit, rtol=relative_error_limit):
            break
        parameter_vector = temp_parameter_vector
    print(f"Number of iterations: {iteration}")


def test_gradient_descent():
    """
    Test the trained model on the test dataset and print actual vs predicted outputs.
    """
    for i in range(len(test_data)):
        print(f"Actual output value: {output(i, 'test')}")
        print(f"Hypothesis output: {calculate_hypothesis_value(i, 'test')}")

if __name__ == "__main__":
    run_gradient_descent_with_momentum()
    print("\nTesting gradient descent with momentum for a linear hypothesis function.\n")
    test_gradient_descent()