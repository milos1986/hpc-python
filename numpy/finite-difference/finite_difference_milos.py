import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# Evaluate numerically the derivative of sin in this [0, pi/2] interval (excluding the 
# end points) using the above formula. Try to avoid for loops. Compare the
# result to function cos in the same interval.
x_i = np.arange(0, np.pi/2, step=0.1)  # 
x_i = x_i[1:-1]  # exclude end points
x_i
delta_x = 0.1
# 

# func = np.sin()
def finite_difference_dif(x_i, func, delta_x=0.1):
    print('Input data: ', x_i)
    df = np.divide((func(x_i + delta_x) - func(x_i - delta_x)), 2 * delta_x)
    print('Approx. diff is: ', df)
    cos_val = np.cos(x_i)
    # PLOTTING
    fig1, ax1 = plt.subplots()
    ax1.plot(x_i, df, label='dif({})'.format(str(func)))
    ax1.plot(x_i, cos_val, label='{} of x_i'.format('cosine'))
    ax1.set_title("Approx derivative of {}, given x_i".format(str(func)))
    ax1.set_xlabel("x_i")
    plt.legend()
    plt.savefig('diff_of_'+str(func))

    print("Mean squared difference:")
    print(np.sqrt(np.sum((df - cos_val)**2)))


    return df

if __name__ == "__main__":
    
    df_sin = finite_difference_dif(x_i, np.sin, 0.1)
    # # plot the cos func in the same, x_i interval:
    # fig2, ax2 = plt.subplots()
    # ax2.plot(x_i, np.cos(x_i), label='cos(x_i)')
    # ax2.set_title("cos of x_i interval")
    # ax2.set_xlabel("x_i")
    # plt.legend()
    # plt.savefig('cos of x_i interval'))