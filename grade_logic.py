from PyQt6.QtWidgets import QMainWindow
from gui import *
import csv
import os
class Grades(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        """
        Sets up lists of entry lists to simplify process of showing and hiding
        Used AI to help simplify hiding and showing entry boxes and labels
        :return: None
        """
        super().__init__()
        self.setupUi(self)


        self.__entry = [self.score1_entry, self.score2_entry, self.score3_entry, self.score4_entry]
        self.__label = [self.score1_label, self.score2_label, self.score3_label, self.score4_label]

        [a.hide() for a in self.__entry]
        [a.hide() for a in self.__label]

        self.__click = True

        self.submit.clicked.connect(lambda: self.grade())

    def grade(self) -> None:
        """
        Takes student info checks and unhides # of attempts
        after first submit it will check the scores and write to csv file
        :return: None
        """
        try:
            if self.__click:

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


                for a in range(attempts):
                    self.__entry[a].show()
                    self.__label[a].show()

                self.main_label.setText("Enter scores between 0-100 and submit")
                self.__click = False
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

    def reset(self)-> None:
        """
        Resets all score entry boxes and labels ready for new input
        :return: None
        """
        self.__click = True
        self.student_name.clear()
        self.num_attempts.clear()
        for entry in self.__entry:
            entry.clear()
            entry.hide()
        for label in self.__label:
            label.hide()

