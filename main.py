def orders_array(array):
    ordered_array = []
    ordered_array.append(int(array[0]))

    del array[0]

    for i in array:
        actual_number = int(i)
        j = len(ordered_array)
        k = 0
        while k < j:
            temp_pos = -999
            if actual_number < ordered_array[k]:
                temp_pos = k
                k = j + 1
            k += 1

        if temp_pos != -999:
            ordered_array.insert(temp_pos, actual_number)
        else:
            ordered_array.append(actual_number)
    return ordered_array

def missing_array_number(array):
    i = 0
    while i < len(array) - 1:
        if array[i] + 1 != array[i + 1]:
            return array[i] + 1
        i += 1
    return array[len(array) - 1] + 1

def main():
    print("How many arrays do you want to order?")
    num_inputs = input()
    count = 0

    while count < int(num_inputs):
        print("Input the array in the following format: [number, number, number]")
        ordered_array = orders_array(input()[1:-1].split(','))
        missing_number = missing_array_number(ordered_array)
        print(missing_number)
        count += 1

main()
