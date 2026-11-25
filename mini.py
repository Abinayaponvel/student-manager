import json
class Students:
    def __init__(self, name, marks, age=None):
        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100")

        self.name = name
        self.marks = marks
        self.age = age

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}, Marks:{self.marks}"

def find_student(all_students, name):
        
    for s in all_students:
        if s.name.lower() == name.lower():
            return s
    return None

def avg_marks(all_students):
    if len(all_students) == 0:
        return 0

    total = 0

    for s in all_students:
        total += s.marks

    return total / len(all_students)

def delete(all_students,name):
    for s in all_students:
        if s.name.lower() == name.lower():
            all_students.remove(s)
            return True
    return False


def high(all_students):
    if not all_students:
        return None
    else:
        top_student = all_students[0]
    for s in all_students:
        if s.marks > top_student.marks:
            top_student = s
    return top_student

def load_students(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        return []

    all_students =  []

    for d in data:
        try:
            student = Students(
                name=d["name"],
                marks=d["marks"],
                age=d.get("age")
            )

            all_students.append(student)

        except (KeyError, ValueError) as e:
            print("Skipping bad record:", d, "-", e)

    return all_students

def save_students(all_students, filename):
    data = []

    for s in all_students:
        data.append({
            "name": s.name,
            "marks": s.marks,
            "age": s.age
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
def main():
    all_students = load_students("students.json")
    while True:
        print("\n===== Student Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Student")
        print("4. Show average marks")
        print("5. delete a student")
        print("6. Top student")
        print("7. Save & Exit")

    
        choice = input("Enter choice: ")
    

        if "1" == choice:
            try:
            
                name = input("Enter name: ")
                marks = int(input("Enter marks: "))
                age = int(input("Enter age: "))

                student=Students(name,marks,age)
                all_students.append(student)

            
                print("Student added successfully")
            
            except ValueError:
                print(e)
           

        elif "2" == choice:
            if not all_students:
                print("No students Yet")
            else:
                for s in all_students:
                    print(s)

        elif "3" == choice:
            name=input("Enter name: ").strip()
            student = find_student(all_students, name)
            if student:
                print("Student found:", student)
            else:
                print("Student not found.")

        elif "4" == choice:
            avg_mark = avg_marks(all_students)
            print("The average mark of all students is: " ,avg_mark)

        elif "5" == choice:
            name=input("Enter name: ")
            student = delete(all_students, name)
            if student:
                print("Student deleted successfully:")
            else:
                print("Student not found.")

        elif "6" == choice:
        
            student = high(all_students)
            print("The Top student is", student)

        elif "7" == choice:
        
            save_students(all_students, "students.json")
            print("Saved")
            print("Good bye")
        
            break
        
if __name__ == "__main__":
    main()
           
    
        
        
    
        
        
        
        
        
        
