students_performance = {
    101: "Excellent",
    102: "Outstanding",
    103: "Good"
}

def get_performance(roll):
    return students_performance.get(roll, "Performance not found")

def add_performance(roll, performance):
    students_performance[roll] = performance
