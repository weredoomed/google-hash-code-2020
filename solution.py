import glob


def fetch_filenames(path='data'):
    return glob.glob('{}/*.in'.format(path))


def get_file_content(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        second_line = f.readline()

    # Assign parameters
    # We can get the len of the pizza list if we need the number of available pizzas
    max_slices = list(map(int, first_line.split()))[0]

    # Create the pizza list by reading the file
    pizza_list = list(map(int, second_line.split()))

    print('Max slices={}'.format(max_slices))
    print('Num pizzas={}'.format(len(pizza_list)))

    return max_slices, pizza_list


def find_best_order(max_slices, pizza_list):

    best_order = []  # To store the best solution
    current_order = []  # To store the current solutionn

    start_index = len(pizza_list)

    max_sum = 0  # Stores the maximum sum found
    slices_sum = 0  # Sum of slices

    order_count = 0

    # If first element of currentIndexList becomes 0 that means solution generating is finished

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


if __name__ == '__main__':
    input_files = fetch_filenames()
    for file_path in input_files:
        calculate_slices(file_path)
