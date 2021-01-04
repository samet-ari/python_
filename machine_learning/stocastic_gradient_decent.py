"""
Implementation of stocastic gradient decent algorithm for minimizing cost
of a Mean Square Error function [MSE]
"""
import numpy as np

"""
function looks like y = w_0 + w_1 * x [For a single Feature[Column]]
"""
def Generate_data(seed, takeout=0.7):

    total_no = 100
    np.random.seed(seed)
    X_linear = 2 * np.random.randn(total_no, 1)
    y_linear = 4 - 10 * X_linear + np.random.randn(total_no, 1)
    _data = np.c_[X_linear, y_linear]

    bias_column = np.ones(total_no)
    data_modified = np.c_[bias_column, _data]

    amount = int(total_no * 0.7)
    train_data, test_data = data_modified[:amount, :], data_modified[amount: , :]

    np.random.shuffle(train_data)
    np.random.shuffle(test_data)

    return (train_data, test_data)

def _output_val(record_no: int, data_set: np.ndarray) -> np.ndarray:
    """
    param record_no: data point no. in data_set
    param data_set: dataset in which record 's output needed
    return : output for that specific data point value 
    """
    return data_set[record_no, -1]

def mse_error(record_no, data_set, param_vec):
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    error = np.power(_calc_hypothesis_val(record_no, data_set, param_vec) - _output_val(
        record_no, data_set), 2)

    return error * 0.5 

def _calc_hypothesis_val(record_no, data_set, param_vec):
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    data_set = data_set.reshape(-1, n)
    hypothesis_val = np.dot(data_set[record_no, :], param_vec)
    return hypothesis_val

def _calc_gradient(data, output, param_vec):
    """
    """
    x_index_transpose = np.transpose(data)

    result = np.dot(x_index_transpose, np.dot(data, param_vec) - output)
    return result

def stocastic_gradient_decent(data_set, param_vec, seed=1907, epochs=50):
    """
    """
    np.random.seed(seed)
    np.random.shuffle(data_set)
    X = data_set[:, :n]
    y = data_set[:, -1].reshape(-1, 1)
    
    for _ in range(epochs):
        for _ in range(m):
            random_index = np.random.randint(m)
            x_i = X[random_index: random_index + 1]
            y_i = y[random_index: random_index + 1]
            gradient = _calc_gradient(x_i , y_i, param_vec)
            param_vec -= LEARNING_RATE * gradient
            break
    
    return param_vec


train_data, test_data = Generate_data(0)

m = train_data.shape[0]
n = train_data.shape[1] - 1

parameter_vector = np.random.randn(n, 1)
LEARNING_RATE = 0.1

if __name__ == '__main__':
    print('Testing Stocastic Gradient Descent...')
    parameter_vector = stocastic_gradient_decent(train_data, parameter_vector, epochs=100)
    print('Converged.')
    print('Done..')
    error = mse_error(1, test_data, parameter_vector)
    print(error)
    print(parameter_vector)
