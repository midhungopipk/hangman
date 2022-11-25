from datetime import date

employees = []


class Employee:
    def create_employee(self, n, i, d):
        return dict(name=n, id=i, dob=d, skills=[])

    def add_skill(self, employees, i):
        for e in employees:
            if e["id"] == i:
                skill_name = input("Enter the skill:")
                d = int(input("enter the date of completion"))
                m = int(input("enter the month of completion"))
                y = int(input("enter the year of completion"))
                date_of_completion = date(y, m, d)
                completion_level = int(input("enter the level from 0 to 5:"))

                for s in e["skills"]:
                    if s["skill"] == skill_name:
                        if s["level"] < completion_level:
                            s.update(
                                dict(
                                    skill=skill_name,
                                    date=date_of_completion,
                                    level=completion_level,
                                )
                            )
                            break
                else:
                    e["skills"].append(
                        dict(
                            skill=skill_name,
                            date=date_of_completion,
                            level=completion_level,
                        )
                    )

    def view_all_skills(self, employees, id):
        for e in employees:
            if e["id"] == id:
                print("Skills of {}".format(e["name"]))
                for s in e["skills"]:
                    print(
                        "{} - completed on {} with level of {}".format(
                            s["skill"], s["date"], s["level"]
                        )
                    )

    def exiting(self, x):
        print(x)


print("Welcome....")


def menu():
    print("Enter 1 to add an Employee:")
    print("Enter 2 to list all Employees:")
    print("Enter 3 to add skill to an Employee:")
    print("Enter 4 to display skills of an Employee:")
    print("Enter 5 to exit:")
    choice = int(input("Please enter your choice:"))
    e = Employee()

    if choice == 1:
        name = input("enter the name")
        id = int(input("enter the id"))
        dob = int(input("enter the dob"))
        employee = e.create_employee(name, id, dob)
        employees.append(dict(employee))

    elif choice == 2:
        for i in employees:
            print(i)
    elif choice == 3:
        id = int(input("Enter the id of employee to add skill:"))
        e.add_skill(employees, id)

    elif choice == 4:
        id = int(input("Enter the id of employee to view the skills:"))
        e.view_all_skills(employees, id)

    elif choice == 5:
        e.exiting("Thank you...")
        exit(0)

    menu()


menu()
