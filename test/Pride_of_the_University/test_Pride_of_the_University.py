import pytest
import os
from Pride_of_the_University.Pride_of_the_University import make_report_about_top3


class Test_make_report_about_top3():

    def test_make_report_about_top3(self, load_data):
        students_avg_scores = load_data
        file_path = make_report_about_top3(students_avg_scores)
        check_dir = os.path.exists(file_path)
        assert check_dir is True
