import enum
import openpyxl
import xlsxwriter
import os


students_avg_scores = {
    'Max': 4.964,
    'Eric': 4.962,
    'Peter': 4.923,
    'Mark': 4.957,
    'Julie': 4.95,
    'Jimmy': 4.973,
    'Felix': 4.937,
    'Vasya': 4.911,
    'Don': 4.936,
    'Zoi': 4.937
}


def make_report_about_top3(students_avg_scores):
    students = {}
    students = sorted(students_avg_scores.items(), key=lambda x: x[1], reverse=True)
    top_students = students[:3]

    path = os.path.abspath(os.path.dirname(__file__))
    dir_save = os.path.join(path, 'data/')

    check_dir = os.path.exists(dir_save)
    if not check_dir:
        os.mkdir(dir_save, mode=0o777)

    file_path = os.path.join(dir_save, 'top3_students.xlsx')
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    for i, student in enumerate(top_students):
        i += 1
        worksheet.write(f'A{str(i)}', student[0])
        worksheet.write(f'B{str(i)}', student[1])
    workbook.close()

    return file_path


if __name__ == '__main__':
    file_path = make_report_about_top3(students_avg_scores)
