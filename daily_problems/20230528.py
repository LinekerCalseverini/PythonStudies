# There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can
# climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if
# X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your
# function to take in X.
def get_all_possible_sequences(possible_values: list,
                               number_of_values: int) -> set:
    if number_of_values != 1:
        all_possible_sequences = set()
        possible_sequences = get_all_possible_sequences(possible_values,
                                                        number_of_values-1)
        for sequence in possible_sequences:
            all_possible_sequences.add(sequence)
            for value in possible_values:
                sequence_copy = list(sequence[:])
                sequence_copy.append(value)
                all_possible_sequences.add(tuple(sequence_copy))
    else:
        all_possible_sequences = set()
        for value in possible_values:
            all_possible_sequences.add(tuple([value]))

    return all_possible_sequences


def get_possible_steps(possible_steps: list, number_steps: int) -> list:
    possible_ways = []
    all_possible_sequences = get_all_possible_sequences(possible_steps,
                                                        number_steps)

    for sequence in all_possible_sequences:
        if sum(sequence) == number_steps:
            possible_ways.append(sequence)

    return possible_ways


possible_steps = [1, 3, 5]
number_steps = 6

all_ways = get_possible_steps(possible_steps, number_steps)
print(f'X: {possible_steps}')
print(f'N: {number_steps}')
for sequence in all_ways:
    print(sequence)
print(f'Max number of ways: {len(all_ways)}')
