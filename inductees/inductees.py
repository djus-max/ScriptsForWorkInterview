names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names, birthday_years, genders):
    inductees = []
    inaccurate_data = []
    this_year = 2021
    students = zip(names, birthday_years, genders)
    for inductee in students:
        age_difference = this_year - inductee[1] if inductee[1] is not None else 0
        if 18 <= age_difference <= 30 and (inductee[2] == "Male"):
            inductees.append(inductee[0])
        else:
            inaccurate_data.append(inductee[0])

    return inductees, inaccurate_data


if __name__ == '__main__':
    inductees, inaccurate_data = get_inductees(names, birthday_years, genders)
    print(inductees, inaccurate_data)
