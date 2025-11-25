students_score = {
    101: 87,
    102: 92,
    103: 75
}

def get_score(roll):
    return students_score.get(roll, "Score not found")

def add_score(roll, score):
    students_score[roll] = score
