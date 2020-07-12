import csv, os
import shutil
from tempfile import NamedTemporaryFile

class students:

    def displayOptions(self,Menu):

        for index , option in enumerate(Menu,start=1):
            print(f"\t{index}.{option.upper()}")
        
        option = int(input("\n---Please Choose Your Option----::\t"))
        return option


    def welcome(self):
        print("\n\n----------Welcome To Our IT Academy----------\n")
        users = ['New Student','Enrolled Student']  
        Option=self.displayOptions(users)

        if Option ==1:
            self.newStudent()
            
        elif Option == 2:
            self.enrolledStudent()
            
        else:
            print("\tPlease Choose Valid Option!!\n")
    

    def newStudent(self):
        newStudentOption = ['Enquiry','Register']
        option=self.displayOptions(newStudentOption)
        self.enquiry() if option == 1 else self.register() 
    
    def enrolledStudent(self):
        enrolledStudentOption = ['Profile','Display All','Update','Leave','Completion']
        option = self.displayOptions(enrolledStudentOption)
        if option ==1:
            self.profile()
            
        elif option ==2:
            self.showAll()
            
        elif option == 3:
            self.updateInfo()
            
        elif option == 4:
            self.deleteInfo()
        elif option ==5:
            self.complete()
            pass

        else:
            print("Invalid Option!!")


    def profile(self):
        name = input("\t\nEnter Name::")
        Id = int(input("\t\nEnter your ID::"))
        with open('Student.csv') as student:
            fileread = csv.DictReader(student)
            for row in fileread:
                if row['Name'] == name and int(row['ID'])== Id:
                    print(f"\t\nName::{row['Name']}\nAddress::{row['Address']}\nCourse::{row['Course']}")
                    break
            else:
                print("Student Not Registered")
        self.restart()

    def showAll(self):
        with open('Student.csv') as student:
            fileread = csv.DictReader(student)
            print("\n\tID\t|  Name\t|  Address\t|  Course\t|  Paid\t|  Remaining ")
            for row in fileread:
                print(f"\n\t{row['ID']}\t   {row['Name']}\t   {row['Address']}\t\t   {row['Course']}\t   {row['Payment']}\t   {int(row['Registration Fee'])-int(row['Payment'])}\t ")
        self.restart()


    def enquiry(self):
        with open('course.csv') as course:
            fileread = csv.DictReader(course)
            print("\n\tName\t|  Duration\t|  Fee\t|  Remark\t")
            for row in fileread:
                print(f"\n\t{row['Name']}\t   {row['Duration']}\t   {row['Fee']}\t   {row['Remark']}")
        print("\n Interested? Book Your Course")
        response = input("\n\tEnter 'Y' for Yes or 'N' for No::")
        if response.lower() == 'y':
            self.register() 
        else:
            self.restart()


    def register(self):
        print(">>>>>> Registration <<<<<<")
        std_id = int(input("Enter ID:"))
        std_name = input("\nEnter Your Name:")
        std_address = input("\nEnter Your Address:")
        std_course = input("\nEnter course name you want to enroll:")
        flag = False
        with open('course.csv','r') as course:
            reader = csv.reader(course)
            for row in reader:
                if (row[0].lower() or row[0].title()) == std_course:
                    flag = True
                    break
            else:
                print("Invalid course!!")
                flag = False     
        if flag == True:     
            registration_option =['Partial Payment','Full Payment']
            option = self.displayOptions(registration_option)
            if option == 1:
                payment= 10000
            else :
                payment= 20000
            fieldname = ['ID','Name','Address','Course','Registration Fee','Payment','Remark']
            
            if os.path.exists('Student.csv') == False:
                with open('Student.csv','w',newline='') as student:   
                            
                    filewrite = csv.DictWriter(student,fieldnames=fieldname)
                    filewrite.writeheader()
                    filewrite.writerow({'ID':std_id,'Name':std_name,'Address':std_address,'Course':std_course,'Registration Fee':20000,'Payment':payment,'Remark':registration_option[option-1]})
                    
            else:
                with open('Student.csv','a',newline='') as student:
                    filewrite = csv.DictWriter(student,fieldnames=fieldname)
                    filewrite.writerow({'ID':std_id,'Name':std_name,'Address':std_address,'Course':std_course,'Registration Fee':20000,'Payment':payment,'Remark':registration_option[option-1]})

            print("\t\n<<<Registration Succeed>>>")
        
        else:
            print("\t\n<<<Registration Failed!!>>>")
        
        self.restart()

    def updateInfo(self):
        fieldname = ['ID','Name','Address','Course','Registration Fee','Payment','Remark']
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        name =input("Enter name::")
        Id =int(input("Enter student ID::"))
        with open('Student.csv','r') as upfile,tempfile:
            reader = csv.DictReader(upfile,fieldnames=fieldname)
            writer = csv.DictWriter(tempfile,fieldnames=fieldname)
            for row in reader:
                if row['Name'] == name and int(row['ID']) == Id:
                    print(f"{row['Name']}\t{row['Course']}\t{row['Payment']}\t{int(row['Registration Fee'])-int(row['Payment'])}  'Due Amount'")
                    print("--Successfully Updated student payment info--")
                    if int(row['Payment'])!=int(row['Registration Fee']):
                        payment = 20000
                    else:
                        payment = row['Payment']

                    row = {'ID':row['ID'],'Name':row['Name'],'Address':row['Address'],'Course':row['Course'],'Registration Fee':row['Registration Fee'],'Payment':payment,'Remark':'Full Payment'}
                writer.writerow(row)
        
        shutil.move(tempfile.name, 'Student.csv')

    def deleteInfo(self):
        fieldname = ['ID','Name','Address','Course','Registration Fee','Payment','Remark']
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        click = input("Do you want to leave the course ?[Y/N]::")
        if click.lower()  == 'y':
            name =input("Enter Student's Name::")
            Id =int(input("Enter Student's ID::"))
            with open('Student.csv','r') as upfile,tempfile:
                reader = csv.DictReader(upfile,fieldnames=fieldname)
                writer = csv.DictWriter(tempfile,fieldnames=fieldname)
                for row in reader:
                    if row['Name'] == name and int(row['ID']) == Id:
                        print(f"{row['Name']}\t{row['Course']}\t{row['Payment']}\t")
                        continue
                    else:
                        row = {'ID':row['ID'],'Name':row['Name'],'Address':row['Address'],'Course':row['Course'],'Registration Fee':row['Registration Fee'],'Payment':row['Payment'],'Remark':row['Remark']}
                    writer.writerow(row)
            
            shutil.move(tempfile.name, 'Student.csv')
            print(">>>Successfully Deleted<<<")
            self.restart()
        else:
            self.restart()



    def complete(self):
        fieldname = ['ID','Name','Address','Course','Registration Fee','Payment','Remark']
        # fieldnameAppended = ['ID','Name','Address','Course','Registration Fee','Payment','Remark']

        tempfile = NamedTemporaryFile(mode='w', delete=False)
        finish=input("Have your Course Completed?[Y/N]::")

        if finish.lower() =='y':
            name =input("Enter Your Name::")
            Id =int(input("Enter Your ID::"))
            with open('Student.csv','r') as upfile,tempfile:
                reader = csv.DictReader(upfile,fieldnames=fieldname)
                writer = csv.DictWriter(tempfile,fieldnames=fieldname)
                for row in reader:
                    if row['Name'] == name and int(row['ID']) == Id:
                        print(f"{row['Name']}\t{row['Course']}\t{row['Payment']}\t")
                        row = {'ID':row['ID'],'Name':row['Name'],'Address':row['Address'],'Course':row['Course'],'Registration Fee':row['Registration Fee'],'Payment':'Returned','Remark':'Completed'}
                        print(f"Your payment is {row['Payment']}\t")
                    else:
                        # print("Invalid Student Name or ID")
                        row = {'ID':row['ID'],'Name':row['Name'],'Address':row['Address'],'Course':row['Course'],'Registration Fee':row['Registration Fee'],'Payment':row['Payment'],'Remark':row['Remark']}
                    writer.writerow(row)

            shutil.move(tempfile.name, 'Student.csv')
            print("Congratulation!! Your Course Completed Successfully")
            self.restart()
        else:
            self.restart()

    def restart(self):
        run=input("\nDo you want to continue [Y/N]?")
        if run.lower() == 'y':
            self.welcome()
        



# if __init__ =='__main()__':
s = students()
s.welcome()
