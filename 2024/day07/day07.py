import itertools

with open('input.txt', 'r') as file:
    calibrations = []
    for calibration in file.readlines():
        answer, inputs = calibration.strip().split(':')
        input_list = [int(x) for x in inputs.split()]
        calibrations.append([int(answer), input_list])


def day7(calibrations, operators={'*', '+'}):
    sum_of_valid_operations = 0

    #operators = {'*', '+'}

    for calib in calibrations:
#        print(calib)
        answer = calib[0]

        #for oper_iter in itertools.permutations(operators, r=len(calib[1])-1):
        for oper_iter in itertools.product(operators, repeat=len(calib[1])-1):
            #print(oper_iter)
            equation = []
            for idx, x in enumerate(calib[1]):
                equation.append(x)
                if idx < len(oper_iter):
                    equation.append(oper_iter[idx])

            #print(equation)

            if answer == do_left_right_math(equation):
                #print(f"Good {answer}")
                sum_of_valid_operations += answer
                break

    return sum_of_valid_operations

def do_left_right_math(equation):
    result = equation[0]
    for i in range(len(equation)-1):
        # Skip the first
        if i == 0:
            continue

        # Skip numbers
        if i % 2 == 0:
            continue

        next_op = equation[i]
        next_number = equation[i+1]

        if next_op == '*':
            result = result * next_number
        elif next_op == '+':
            result = result + next_number
        elif next_op == '||':
            result = int(str(result)+str(next_number))

    return result

print(f"Part 1: {day7(calibrations)}")
print("Part 2:", day7(calibrations, {'*', '+', '||'}))
