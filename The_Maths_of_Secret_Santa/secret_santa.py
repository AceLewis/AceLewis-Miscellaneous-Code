import random
import numpy as np
import matplotlib.pyplot as plt


def random_picking(num_of_people):
    "Returns if the random shuffling was successful"
    list_1 = np.arange(num_of_people)
    list_2 = np.random.permutation(num_of_people)
    return not np.any(list_1 == list_2)


def percentage_bad_rand(num_of_people, num_of_times):
    "Estimates the percentage of successful draws"
    times = 0
    for _ in range(num_of_times):
        times += random_picking(num_of_people)
    return times/num_of_times


def percentage_in_range(function_to_use, num_to, num_of_times):
    "Return the percentage of a successful draws for every number in the range"
    number_list = []
    for num in range(2, num_to+1):
        number_list.append(function_to_use(num, num_of_times))
    return list(range(2, num_to+1)), number_list


num_list, num_percent_est = percentage_in_range(percentage_bad_rand, 10, 300000)

# Plot the data
plt.figure()
plt.plot(num_list, num_percent_est)
plt.title('Estimated percentage of a sucessful draws')
plt.xlabel('Number of people in draw')
plt.ylabel('Percentage that the draw will be successful')
plt.savefig("Estimated_percentage_of_successful.png")
plt.savefig("Estimated_percentage_of_successful.svg")
plt.close()


limit_when_large = num_percent_est[-1]
print('The estimated percentage of bad draws for many people is {:.3%}'.format(limit_when_large))

# Now lets use maths, the much more elegant and computationally less expensive way.

def the_maths_way(num_of_people, *unused):
    "Use maths and not brute force to find the percentage of a sucessful draw"
    return np.sum([((-1)**(x))/(np.math.factorial(x)) for x in range(0, num_of_people+1)])


num_list, num_percent = percentage_in_range(the_maths_way, 10, 0)

# Plot the data
plt.figure()
plt.plot(num_list, num_percent)
plt.title('Actual percentage of a sucessful draws')
plt.xlabel('Number of people in draw')
plt.ylabel('Percentage that the draw will be successful')
plt.savefig("Actual_percentage_of_successful.png")
plt.savefig("Actual_percentage_of_successful.svg")
plt.close()

# The limit of the summation for the percentage of successful draws is 1/e
print('The actual percentage of successful draws tends to {:.3%}'.format(1/np.exp(1)))
