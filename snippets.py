# Code snippets used to solve the problem

# First step, lets get the file names
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕


def fetch_filenames(path='data'):
    return glob.glob('{}/*.in'.format(path))


def calculate_slices(file_path):
    print(file_path)


input_files = fetch_filenames()
for file_path in input_files:
    calculate_slices(file_path)

# Second step, lets get the contents of the files
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕


def get_file_content(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        second_line = f.readline()

    # We can get the len of the pizza list if we need the number of available pizzas
    max_slices = list(map(int, first_line.split()))[0]

    # Create the pizza list by reading the file
    pizza_list = list(map(int, second_line.split()))

    print('Max slices={}'.format(max_slices))
    print('Num of pizzas={}'.format(len(pizza_list)))

    return max_slices, pizza_list


def calculate_slices(file_path):
    print('processing file: {}'.format(file_path))
    max_slices, pizza_list = get_file_content(file_path)


# Third step, lets start processing the pizza_list
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕


# Since there are multiple orders, we will save the best in a list and replace it any time we find a better one
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕


def find_best_order(max_slices, pizza_list):

    best_order = []  # To store the best solution
    current_order = []  # To store the current solutionn

    return best_order


def calculate_slices(file_path):
    print('processing file: {}'.format(file_path))
    max_slices, pizza_list = get_file_content(file_path)
    best_order = find_best_order(max_slices, pizza_list)


# Great, now lets start trying to find the best pizzs order!
# We know we need to loop over the list in reverse, so lets code that out first!
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕

def find_best_order(max_slices, pizza_list):

    best_order = []  # To store the best solution
    current_order = []  # To store the current solutionn

    start_index = len(pizza_list) - 1

    for i in range(start_index, -1, -1):  # Used to traverse from end to start of the pizza_list
        print(pizza_list[i])

    return best_order

# Now we are cooking with gas, lets find the first order we can make just using the values in reverse!
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕


def find_best_order(max_slices, pizza_list):

    best_order = []  # To store the best solution
    current_order = []  # To store the current solution

    start_index = len(pizza_list) - 1

    slices_sum = 0 # Sum of slices

    for i in range(start_index, -1, -1):  # Used to traverse from end to start of the pizza_list

        temp_sum = slices_sum + pizza_list[i]

        # If the temporary sum is equal to target that means a perfect solution is found
        if (temp_sum == max_slices):
            slices_sum = temp_sum
            current_order.append({
                'index': i,
                'value': pizza_list[i]
            })
            break  # Go to return solution

        if (temp_sum > max_slices):  # If the temporary sum is greater than max_slices
            continue  # Try next value

        if (temp_sum < max_slices):  # The temporary sum is less than max_slices
            slices_sum = temp_sum
            current_order.append({
                'index': i,
                'value': pizza_list[i]
            })
            continue


    best_order = current_order

    return best_order


def calculate_slices(file_path):
    print('processing file: {}'.format(file_path))
    max_slices, pizza_list = get_file_content(file_path)
    best_order = find_best_order(max_slices, pizza_list)
    print('Max slices:')
    print(sum(pizza['value'] for pizza in best_order))


# Awesome, we can solve a solution to the problem. 
# Now lets save it to a file so we are sure we wont run out of time trying to get a higher max number of slices
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕

def save_order(pizzas, file_path):
    order = ""
    for pizza in pizzas:
        order = order + str(pizza['index']) + " "
    
    print('Saving order')
    print(order)

    with open(file_path.replace('.in', '.out'), 'w') as f:
        f.write(str(len(pizzas)) + "\n")
        f.write(order)


def calculate_slices(file_path):
    print('processing file: {}'.format(file_path))
    max_slices, pizza_list = get_file_content(file_path)
    best_order = find_best_order(max_slices, pizza_list)
    print('Max slices:')
    print(sum(pizza['value'] for pizza in best_order))

    save_order(best_order, file_path)

# Looks like we got some of the boilerplating out of the way
# We are going to take the solution that inspired this repo, but
# How do you think we can find the best order?
# 🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕

def find_best_order(max_slices, pizza_list):

    best_order = []  # To store the best solution
    current_order = []  # To store the current solutionn

    start_index = len(pizza_list)

    max_sum = 0  # Stores the maximum sum found
    slices_sum = 0  # Sum of slices

    order_count = 0

    # If first element of current_order becomes 0 that means solution generating is finished

    while((len(current_order) > 0 and current_order[0].get('index', -1) != 0) or len(current_order) == 0):

        order_count = order_count + 1
        print("Attempting order={}".format(order_count))
        start_index = start_index - 1

        # Used to traverse from end to start of the pizza_list
        for i in range(start_index, -1, -1):

            temp_sum = slices_sum + pizza_list[i]

            # If the temporary sum is equal to target that means a perfect solution is found
            if (temp_sum == max_slices):
                slices_sum = temp_sum
                current_order.append({
                    'index': i,
                    'value': pizza_list[i]
                })
                break  # Go to return solution

            if (temp_sum > max_slices):  # If the temporary sum is greater than max_slices
                continue  # Try next value

            if (temp_sum < max_slices):  # The temporary sum is less than max_slices
                slices_sum = temp_sum
                current_order.append({
                    'index': i,
                    'value': pizza_list[i]
                })
                continue

        # If we found a better order
        if (max_sum < slices_sum):
            print('Found better order')
            max_sum = slices_sum

            # Cast it to a list becaus of reference issue
            best_order = list(current_order)

        # If we found a perfect order
        if (max_sum == max_slices):
            break

        # Lets keep processing
        if(len(current_order) != 0):
            last_pizza = current_order.pop()
            slices_sum = slices_sum - \
                last_pizza['value']  # Subtract it from sum
            start_index = last_pizza['index']  # set the index

        if(len(current_order) == 0 and (start_index == 0)):  # If there are no more possible orders
            break

    return best_order