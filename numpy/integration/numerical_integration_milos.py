import numpy as np

# delta_x = 0.1


# middle Riemann sum approximation:

def riemann_sum_approx(delta_x, func):
    interval = np.arange(0, np.pi/2, delta_x)
    # n_elements = np.shape(interval)[0]
    # inter_1 = np.zeros(n_elements+1)
    # inter_2 = np.zeros(n_elements+1)
    # inter_1[1:] = interval
    # inter_2[:-1] = interval
    inter_1 = interval[1:]
    inter_2 = interval[:-1]
    # print(inter_1)
    # print(inter_2)
    x_i_prime_vec = np.divide((inter_1 + inter_2), 2)
    # print(x_i_prime_vec)
    
    approx = np.sum(np.sin(x_i_prime_vec)*delta_x)
    return approx


if __name__ == "__main__":
    delta_vec = [1, 0.1, 0.01, 0.001, 0.0001]
    for delta_x in delta_vec:
        approx = riemann_sum_approx(delta_x, np.sin)
        print('Given delta_x={}, the Riemann sum is:{}'.format(delta_x, approx))