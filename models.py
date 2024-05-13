# python3 model.py (cmd add. edit, delete list)
from pydantic import BaseModel
import sys


class Person(BaseModel):
    name: str
    age: int
    salary: float


class Db(BaseModel):
    persons: list[Person]


db = Db(persons=[])


def init():
    global db
    file = open("database.json", "r")

    jasonstring = file.read()
    db = Db.model_validate_json(jasonstring)


def save():
    global db
    file = open("database.json", "w")
    db_json = db.model_dump_json()
    file.write(db_json)


def main():
    init()
    arg = sys.argv
    if len(arg) == 1:
        print("you should pass one paramenter")
        exit(1)

    cmd = arg[1]

    if cmd == "add":
        name = input("name:")
        age = int(input("age:"))
        salary = float(input("salary:"))
        person = Person(name=name, age=age, salary=salary)
        db.persons.append(person)
        save()
    elif cmd == "edit":
        name = input("write the name to be edited ")
        for i, person in enumerate(db.persons):
            if person.name == name:
                person.name = input(f"write the new name for {person.name} ")
                person.age = int(input(f"write the new age for {person.age} "))
                person.salary = float(
                    input(f"write the new salary for {person.salary} ")
                )
                save()

        else:
            print(f"{name} was  not found , use list to see all tha name in the list")
    elif cmd == "delete":
        name = input("name:")
        to_delete = None
        for i, person in enumerate(db.persons):
            if person.name == name:
                to_delete = i
                break

        if to_delete is not None:
            del db.persons[to_delete]
            save()
            print(f"deleted:{name}")
        else:
            print("name not found")

    elif cmd == "list":
        for person in db.persons:
            print(person.name)

    elif cmd == "help":
        print("welcome to persons 1000!")
        print("use one of the cmds: add, edit, delete, list")
    else:
        print("invalid cmd, should be add, edit, delete, list")
        exit(1)


if __name__ == "__main__":
    main()
