from PyQt6.QtWidgets import QMainWindow
from gui import *
import csv
import os
class Grades(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.score1_label.hide()
        self.score2_label.hide()
        self.score3_label.hide()
        self.score4_label.hide()

        self.score1_entry.hide()
        self.score2_entry.hide()
        self.score3_entry.hide()
        self.score4_entry.hide()

        self.click = True

        self.submit.clicked.connect(lambda: self.grade())

    def grade(self):

        try:
            if self.click:

                name = self.student_name.text().strip()
                attempts = self.num_attempts.text().strip()

                if name == "":
                    return self.main_label.setText("Please enter name")
                if attempts == "":
                    return self.main_label.setText("Please enter number of attempts")
                attempts = int(attempts)
                for letter in name:
                    if not (letter.isalpha() or letter.isspace()):
                        return self.main_label.setText("Please enter letters in name box")


                if not 1<= attempts <=4:
                    return self.main_label.setText("Please enter number in range 1-4")

                entry = [self.score1_entry, self.score2_entry, self.score3_entry, self.score4_entry]
                label = [self.score1_label, self.score2_label, self.score3_label, self.score4_label]

                for a in range(attempts):       #used Ai  to simplify showing entry boxes and labels
                    entry[a].show()
                    label[a].show()

                self.main_label.setText("Enter scores between 0-100 and submit")
                self.click = False
            else:
                name = self.student_name.text().strip()
                grade_list = [self.score1_entry.text().strip(), self.score2_entry.text().strip(), self.score3_entry.text().strip(), self.score4_entry.text().strip()]

                final_score = []

                for num in grade_list:
                    try:
                        val = int(num)
                        if 0 <= val <= 100:
                            final_score.append(val)
                        else:
                            final_score.append(0)
                    except ValueError:
                        final_score.append(0)


                best_grade = max(final_score, default = 0)

                header = ["Student Name", "Best grade", "Score 1", "Score 2", "Score 3", "Score 4"]

                row = [name, best_grade] + final_score
                check_file = os.path.isfile("grade.csv")

                with open("grade.csv", "a", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    if not check_file:
                        writer.writerow(header)
                    writer.writerow(row)

                self.main_label.setText(f"Grades submitted for {name}" )

                self.reset()
        except ValueError:
            return self.main_label.setText("Please enter number 1-4")

    def reset(self):
        self.click = True
        self.student_name.clear()
        self.num_attempts.clear()
        for entry in [self.score1_entry, self.score2_entry, self.score3_entry, self.score4_entry]:
            entry.clear()
            entry.hide()
        for label in [self.score1_label, self.score2_label, self.score3_label, self.score4_label]:
            label.hide()

