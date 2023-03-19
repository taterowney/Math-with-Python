import numpy as np
import math

from data import raw, target

data_full = np.array([line.split('\t') for line in raw.splitlines()])

data = data_full[1:, 1:]

bool_array = data == 'Y'

# for line in range(len(data)):
#     for col in range(len(data[line])):
#         if data[line][col].lower() == 'y':
#             data[line][col] = 1
#         elif data[line][col].lower() == 'n':
#             data[line][col] = 0
#         else:
#             data[line][col] = float(data[line][col])

column_names = data_full[0, 1:]
row_names = data_full[1:, 0]

depth = 2

prev_split = [row_names]

def try_split(col, to_split):
    ret = [[], []]
    for val in to_split:
        if bool_array[list(row_names).index(val), col]:
            ret[0].append(val)
        else:
            ret[1].append(val)
    return ret

def get_loss(split):
    loss = 0
    for group in range(len(split)):
        for element in split[group]:
            if element not in target[group]:
                loss += 1
    return 1/(1+math.e**(-loss)) - 0.5


for layer in range(depth):
    new_split = []
    for node in range(len(prev_split)):
        best_split = None
        best_loss = 1
        best_split_name = column_names[0]
        for attempt in range(len(column_names)):
            test_split = try_split(attempt, prev_split[node])
            if get_loss(test_split) < best_loss:
                best_loss = get_loss(test_split)
                best_split = test_split
                best_split_name = column_names[attempt]
        print(f"Best split for {prev_split[node]} is {best_split_name} with loss {best_loss}")
        new_split += best_split
    prev_split = new_split
    print("\n")

category1 = []
category2 = []
for i in range(len(prev_split)):
    if i % 2 == 0:
        category1 += prev_split[i]
    else:
        category2 += prev_split[i]

print(f"Loss for training data: {get_loss([category1, category2])}")