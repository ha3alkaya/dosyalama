#This app for student records.
#Users can be create,search,list or delete student records.

#Copyright (C) <2016>  <Hazal KAYA>

   # This program is free software: you can redistribute it and/or modify
   # it under the terms of the GNU General Public License as published by
   # the Free Software Foundation, either version 3 of the License, or
   # (at your option) any later version.

   # This program is distributed in the hope that it will be useful,
   # but WITHOUT ANY WARRANTY; without even the implied warranty of
   # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   # GNU General Public License for more details.

   # You should have received a copy of the GNU General Public License
   # along with this program.  If not, see <http://www.gnu.org/licenses/>.

text = """
       Please select what do you want:
       (C) - Create a new student record.
       (L) - List student record.
       (D) - Delete student record.
       (S) - Search student records.
       (Q) - Quit.
       """
choice = input(text)
if (choice == "q") or (choice == "Q"):
    print("You want 'Quit'.") 
    exit()
else:
    if (choice == "c") or (choice == "C"):
        print("You want 'Create a new student record'.")
        student_file = open("student_file.txt","a")
        id = input("Enter student's id: ")
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        record = id + " - " + name +" "+ surname 
        student_file.write(record)
        student_file.write("\n")
        student_file.close()
        print("Record successfully created.")
    elif (choice == "L") or (choice == "l"):
        print("You want 'List all record'.")
        student_file = open("student_file.txt","r")
        print(student_file.read())
        print("-"*30)
        student_file.close()
    elif (choice == "S") or (choice == "s"):
        nu = input("You want search an existing record. Please enter something:" )
        student_file = open("student_file.txt","r")
        for line in student_file:
            if nu in line: 
                print(line)
        print("-"*30)
        student_file.close()
    elif (choice == "D") or (choice == "d"):
        nu = input("You want delete an existing record.Please enter student's id: ")
        student_file = open("student_file.txt")
        result = student_file.readlines()
        del result[int(nu)-1]
        student_file.close()
        student_file = open("student_file.txt","w")
        student_file.writelines(result)
        student_file.close()
    else:
        print("Error!!!")
