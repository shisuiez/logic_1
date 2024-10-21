def exam_average_score(*scores):
    return sum(scores) / len(scores)

average_score = exam_average_score(85, 90, 78, 92)
print(average_score)
