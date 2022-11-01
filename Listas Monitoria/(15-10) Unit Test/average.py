# function that receiveis a dict of test scores and calculates the average
def average_scores(scores_dict):
    if not isinstance(scores_dict, dict):
        raise TypeError("The input must be a dictionary")
    if len(scores_dict) == 0:
        raise ValueError("The dictionary must not be empty")
    sum = 0
    for score in scores_dict.values():
        sum += score
    return sum / len(scores_dict)