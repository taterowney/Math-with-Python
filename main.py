import random

STATISTIC = 0.15
#as a PROPORTION of results

COMPARISON = '<'

PROBABILITY_SUCCESS = 0.3333

SAMPLE_SIZE = 27

NUM_REPETITIONS = 1000

def findPvalue(statistic, probability_success, sample_size, comparison, num_repetitions = 1000):
    replications = 0
    for i in range(num_repetitions):
        total_successes = 0
        for j in range(sample_size):
            if random.random() <= probability_success:
                total_successes += 1
        if eval('(total_successes/sample_size)'+comparison+'statistic'):
            replications += 1
    return replications/num_repetitions

def is_significant(statistic, probability_success, sample_size, comparison, num_repetitions=1000, threshold=0.05):
    p_value = findPvalue(statistic, probability_success, sample_size, comparison, num_repetitions=num_repetitions)
    if p_value <= threshold:
        return "This result is significant! (p value = %s)"% p_value
    else:
        return "Guess you're gonna have to find something else to study... (p value = %s)"% p_value

if __name__ == '__main__':
    print(is_significant(STATISTIC, PROBABILITY_SUCCESS, SAMPLE_SIZE, comparison=COMPARISON))