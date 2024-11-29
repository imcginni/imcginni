"""SYST/CYSE-130 Exam2
Author: Ian McGinnis
"""
import csv
criteria = {"A+":[97,103], "A":[94,96], "A-":[90,93],
            "B+":[86,89], "B":[83,85], "B-":[80,82],
            "C+":[76,79], "C":[73,75], "C-":[70,72],
            "D":[60,69], "F":[0,59]}


def calc_total(student) -> int:
    """Given a student record this function shall
    calculate and RETURN the students total score as follows:
        1. Take the sum of the highest 6 CX scores
        2. Take the sum of the highest 5 QZ scores
        3. Take the sum of the highest 2 EX scores
        4. Take the sum of all the HW scores
        5. Multiply the CX total by a factor of 1.67
        6. Multiply the QZ total by a factor of 0.3
        7. Take a sum of the resulting category totals
        8. Round the prior sum and return this value"""
    cx= list(map(float, student[3:13]))
    qz= list(map(float, student[16:23]))
    ex= list(map(float, student[-2:]))
    hw= list(map(float, student[13:16]))

    cx_t=sum(sorted(cx,reverse=True)[:6])
    qz_t=sum(sorted(qz,reverse=True)[:6])
    ex_t=sum(sorted(ex,reverse=True)[:6])
    hw_t=sum(hw)

    cx_t*=1.67
    qz_t*=0.3
    total=cx_t+qz_t+ex_t+hw_t
    return round(total)


def calc_grade(total) -> str:
    """Given a total score i.e. an integer
    between 0-100 calculate and RETURN a string grade
    based on the course grade criteria i.e.
        97-100 = A+  94-96 = A	90-93 = A-,
        86-89 = B+	 83-85 = B	80-82 = B-
        76-79 = C+	 73-75 = C	70-72 = C-,
        60-69 = D	 0-59 = F"""
    for grade,(lower,upper) in criteria.items():
        if lower <= total <= upper:
            return grade


def print_results(first, last, *other):
    """Given a student's first name and last and an arbitrary
    number of other data most likely to be their scores
    print the given inputs following the format:
        1. first and last name inputs must be at least 15
           characters and left aligned
        2. All other inputs must be at least 7 characters
            and left aligned"""
    name=f"{first:<15} {last:<15}"
    other_s=" ".join(f"{str(data):<7}" for data in other)
    print(name + other_s)

fieldW=10
header = ["FistName", "LastName", "Total", "Grade"]
print("".join(field.center(fieldW) for field in header))
if __name__ == "__main__":
    with open("data/student_data.csv", newline='') as studfile:
        reader = csv.reader(studfile)
        students = list(reader)
    for stud in students[1:]:
        first = stud[1]
        last = stud[2]
        total = calc_total(stud)
        grade = calc_grade(total)
        print(f"{first:<{fieldW}}{last:<{fieldW}}{total:<{fieldW}}{grade:<{fieldW}}")



