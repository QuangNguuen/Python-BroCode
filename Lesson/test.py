#
#  Ben's Grade Calculator (Winter 2025)
#
#  Enter the grades that you have received / expect to receive to compute
#  your overall course grade.  The calculator implements the grading rules
#  found on the course information sheet, including replacing lower midterm
#  exam grades with higher final exam grades and enforcing the minimum exam
#  grade requirements.  A+ grades are treated as 4.3 grade points within the
#  course.
#

# The grade point value of each letter grade entered by the user.
GP = {
    "A+": 4.3, "A": 4, "A-": 3.7,
    "B+": 3.3, "B": 3, "B-": 2.7,
    "C+": 2.3, "C": 2, "C-": 1.7,
    "D+": 1.3, "D": 1, "F": 0,
}

# The minimum number of gradepoints that must be earned in the course to
# achieve a particular letter grade.  A+ needs to be reduced from 4.3 because
# there is no way to achieve an A+ on the exercises.
CUTS = {
    "A+": 4.27, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0,
}

# How many exercises and midterms are there?
NUM_EXERCISES = 7
NUM_MIDTERMS = 2

# What is the weight of each assessment?
WEIGHTS = {
    "Exercise 1": 1, "Exercise 2": 1, "Exercise 3": 1,
    "Exercise 4": 1, "Exercise 5": 1, "Exercise 6": 1,
    "Exercise 7": 1,
    "Assignment 1": 7.25, "Assignment 2": 7.25,
    "Assignment 3": 7.25, "Assignment 4": 7.25,
    "Midterm 1": 15, "Midterm 2": 15,
    "Final Exam": 35,
}


#
# Return "a" or "an" depending on whether or not the next word starts with
# a vowel.
# @param next_word the word that will appear immediately after "a" or "an"
# @return "a" or "an"
#
def an(next_word):
    if len(next_word) == 0:
        return "a"
    if (next_word[0].upper() == "A" or next_word[0].upper == "E" or
            next_word[0].upper() == "I" or next_word[0].upper == "O" or
            next_word[0].upper() == "U"):
        return "an"
    return "a"


#
# Load any grades that were saved during the previous run of the program.
# @return a dictionary where the keys are assessments and the values are the
# loaded grades.
#
def loadPreviousGrades():
    #
    # Load the previous grades from the file.
    #
    grades = {}
    try:
        inf = open("_prev_grades.txt", "r")

        for assessment in WEIGHTS:
            grades[assessment] = inf.readline().rstrip()

        inf.close()
    except IOError:
        # Ignore an error if one occurred.
        pass

    #
    # Ensure that the dictionary doesn't include any invalid entries.  Any
    # assessments that have an invalid letter grade are removed from the
    # dictionary.
    #
    invalid = []
    for assessment in grades:
        if grades[assessment] not in GP:
            invalid.append(assessment)
    for assessment in invalid:
        grades.pop(assessment)

    return grades


#
#  Save all of the grades to a file so that they can be used in a subsequent
#  run of the program without being re-entered.
#  @param grades the dictionary of grades to save
#
def saveGrades(grades):
    try:
        outf = open("_prev_grades.txt", "w")
        for assessment in grades:
            print(grades[assessment], file=outf)
        outf.close()
    except IOError:
        print("Failed to save the grades for a future run.")
        return


#
#  Read the grades from the user.
#  @return the entered grades
#
def readGrades():
    # Load any previously saved grades.
    grades = loadPreviousGrades()

    # Read each grade from the user.
    for assessment in WEIGHTS:
        # A blank line will use whatever grade was entered the last time the
        # program executed.
        if assessment in grades:
            prev_grade = grades[assessment]
            prev_message = f" (blank for {prev_grade})"
        else:
            prev_grade = ""
            prev_message = ""

        # Read the input from the user and ensure that it was valid.
        grade = input(f"Enter your grade for {assessment}{prev_message}: ")
        grade = grade.upper()
        if grade == "":
            grade = prev_grade
        while grade not in GP:
            print("That wasn't a valid letter grade.  Try again...")
            grade = input(f"Enter your grade for {assessment}{prev_message}: ")
            grade = grade.upper()

        # Store the grade that was entered.
        grades[assessment] = grade

    # Return the entered grades.
    return grades


#
#  Remove the exercise with the lowest score for the grades dictionary.
#  @param grades a dictionary of grades which is modified by this function
#
def dropLowestExercise(grades):
    # Construct a list of valid letter grades from least worst to best.
    letters = list(GP.keys())
    letters.reverse()

    # Loop through the letter grades from worst to best until an exercise
    # grade has been dropped.
    removed = False
    while len(letters) > 0 and removed == False:
        # Consider the first letter in letters.
        current_letter = letters.pop(0)

        # Compare the current letter grade to each of the exercise grades and
        # drop the first match.
        i = 0
        while i < NUM_EXERCISES and removed == False:
            # Drop the current exercise if its grade matches current_letter.
            if grades[f"Exercise {i + 1}"] == current_letter:
                grades.pop(f"Exercise {i + 1}")
                removed = True
                removed_number = i + 1

            # Move to the next exercise.
            i = i + 1

    # Report which grade was dropped.
    print(f"\nThe lowest exercise grade was {an(current_letter)} "
        f"{current_letter} on Exercise {removed_number}.  "
        "It has been dropped.")


#
# Replace any lower midterm exam grades with a higher final exam grade.
#
def replaceMidterms(grades):
    # Construct a list of valid letter grades from least worst to best.
    letters = list(GP.keys())
    letters.reverse()

    for i in range(1, NUM_MIDTERMS + 1):
        # If the final exam grade is better than the midterm exam grade...
        if letters.index(grades["Final Exam"]) > letters.index(grades[f"Midterm {i}"]):
            # Replace the midterm exam grade with the final exam grade.
            print(f"\nReplacing the {grades[f'Midterm {i}']} on Midterm {i} "
                f"with a {grades['Final Exam']} from the Final Exam.")
            grades[f"Midterm {i}"] = grades["Final Exam"]


#
# Compute the grade point value for the course.
# @param grades the grades earned / projected to be earned by the student
# @return the grade points earned for the course without enforcing the C- or D
# exam requirements
#
def computeGP(grades):
    gp = 0
    for assessment in grades:
        gp = gp + GP[grades[assessment]] * WEIGHTS[assessment]

    return gp / 100


#
# Identify the letter grade that corresponds to a number of grade points.
# @param gpa the number of grade points for which the letter grade is computed
#
def computeLetterGrade(gpa):
    # Construct a list of valid letter grades from least worst to best.
    letters = list(GP.keys())
    letters.reverse()

    # Find the best letter grade that has a cut-off at or below the number of
    # grade points provided.
    for letter in letters:
        if gpa >= CUTS[letter]:
            retval = letter

    return retval


#
# Report if the course grade will be lowered due to failing to achieve a
# C- weighted average across the midterm and final exams.
# @param grades the grades earned by the student.
#
def enforceCMinus(grades, letter):
    gp = computeGP(grades)

    # If the student has a C- or better then verify that they have a C- exam
    # average.
    if gp >= CUTS["C-"]:
        # Compute their grade point average on the exams.
        exam_average = 0
        exam_weights = 0
        for i in range(1, NUM_MIDTERMS + 1):
            exam_average = exam_average + GP[grades[f"Midterm {i}"]] * WEIGHTS[f"Midterm {i}"]
            exam_weights = exam_weights + WEIGHTS[f"Midterm {i}"]

        exam_average = exam_average + GP[grades["Final Exam"]] * WEIGHTS["Final Exam"]
        exam_weights = exam_weights + WEIGHTS["Final Exam"]

        exam_gp = exam_average / exam_weights

        # If the exam GPA is below C- (1.7) then report that the course grade
        # will be lowered.
        if exam_gp < GP["C-"]:
            print(f"\nYour exam average was {exam_gp:.3f}.  This is below "
                f"{GP['C-']} which is required to earn\n"
                "a C- or better in the course.  As a result, your course "
                "grade has been\n"
                "lowered to D+.")
            return "D+"

    # Return the original letter grade if this rule did not apply.
    return letter


#
# Report if the course grade will be lowered due to failing to achieve either
# a D or better on both midterm exams, or a D or better on the final exam.
# @param grades the grades earned by the student.
#
def enforceD(grades, letter):
    gp = computeGP(grades)

    # If the student has a D or better then verify that they have either Ds or
    # better on both midterm exams, or a D or better on the final exam.
    if gp >= CUTS["D"]:
        final_ok = grades["Final Exam"] != "F"
        midterms_ok = True
        for i in range(1, NUM_MIDTERMS + 1):
            if grades[f"Midterm {i}"] == "F":
                midterms_ok = False

        # Report that the grade will be lowered if they have neither achieved
        # a D or better on both midterm exams, nor achieved a D or better on
        # the final exam.
        if not midterms_ok and not final_ok:
            print("\nYou failed to achieve a D or better on both midterm "
                "exams or a D or better on the final\n"
                "exam.  As a result, your course grade has been lowered "
                "to F.")
            return "F"

    # Return the original letter grade if this rule did not apply.
    return letter


def main():
    # Read the grades from the user and save the entered grades so that it's
    # easier to enter the grades the next time the program is run.
    grades = readGrades()
    saveGrades(grades)

    # Modify the grades in ways that benefit the student (drop the lowest
    # exercise and replace lower midterm exam grades with higher final exam
    # grades).
    dropLowestExercise(grades)
    replaceMidterms(grades)

    # Compute the number of grade points earned in the course and the associated
    # letter grade.
    gp = computeGP(grades)
    letter = computeLetterGrade(gp)
    print(f"\nYour computed grade point value is {gp}.  That's {an(letter)} {letter}.")

    # Enforce the exam performance rules.
    letter = enforceCMinus(grades, letter)
    letter = enforceD(grades, letter)

    # Report the overall course grade that will be recorded.
    print("\nThe grades that you entered will result in a course grade of",
        f"{letter}.")


# Call the main function.
main()