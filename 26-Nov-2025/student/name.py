students_name = {
    101: "Vishwajeet Kumar",
    102: "Raja Kumar",
    103: "Vinod Kumar Thakur"
}


def get_name(roll):
    return students_name.get(roll, "Name not found")

def add_name(roll, name):
    students_name[roll] = name
