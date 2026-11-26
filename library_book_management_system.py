#q1
#BOOK INFORMATION AND DATA STUCTURE
name="WINGS OF INFORMATION"
book=["Mazha","Pathumma de Aatinkutty","Nizhal","Beerbahutty","Mugam"]
categories=("Fiction","Commady","Thrillar")
status={"Mazha":"A","Nizhal":"A","Beerbahutty":"N","Pathumma de Aatinkutty":"N","Mugam":"A"}
no_book=[status["Beerbahutty"],status["Mazha"],status["Mugam"],status["Nizhal"],status["Pathumma de Aatinkutty"]]
borro=["Beerbahutty","Pathumma de Aatinkutty"]
av_books=["Mazha","Nizhal","Mugam"]
# print("Library Details",":","\n","Library Name : ",name,"\n","Library Opening Time : ","8:00 AM to 8:00 PM","\n","Available Books: ",len(no_book),"\n","Books are : ",book,"\n","All Book Categorys: ","\n",book[0],":",categories[0],"\n",book[1],":",categories[1],"\n",book[2],":",categories[2],"\n",book[3],":",categories[0],"\n",book[4],":",categories[0])
# print("Number of Available Books : ",len(no_book))
# print("Number of Borrowed Book: ",len(borro))


#output
# Library Details : 
#  Library Name :  WINGS OF INFORMATION 
#  Library Opening Time :  8:00 AM to 8:00 PM 
#  Available Books:  5 
#  Books are :  ['Mazha', 'Pathumma de Aatinkutty', 'Nizhal', 'Beerbahutty', 'Mugam'] 
#  All Book Categorys:  
#  Mazha : Fiction 
#  Pathumma de Aatinkutty : Commady 
#  Nizhal : Thrillar 
#  Beerbahutty : Fiction 
#  Mugam : Fiction
# Number of Available Books :  5
# Number of Borrowed Book:  2


#2
#BORROWING RULES
# age=int(input("enter your age: "))
available_books=['Mazha', 'Pathumma de aatinkutty', 'Nizhal', 'Beerbahutty', 'Mugam']
# book=input("Enter book name : ").capitalize()
# print("User can maximum borro 3 books onlyyy.. ")
# print("Books can borro only 18 years old users.. ")
# if book==available_books[0] and age>=18:
#     print("Book is Available. You can borro")
# elif book==available_books[1] and age>=18:
#     print("Book is Available. You can borro")
# elif book==available_books[2] and age>=18:
#     print("Book is Available. You can borro")
# elif book==available_books[3] and age>=18:
#     print("Book is Available. You can borro")
# elif book==available_books[4] and age>=18:
#     print("Book is Available. You can borro")
    
# else:
#     print("Not Available")
#     print("ensuare that you are above 18 years olde")



#output
# enter your age: 10
# Enter book name : mazha
# User can maximum borro 3 books onlyyy.. 
# Books can borro only 18 years old users.. 
# Not Available
# ensuare that you are above 18 years olde


# enter your age: 21
# Enter book name : nizhal
# User can maximum borro 3 books onlyyy.. 
# Books can borro only 18 years old users.. 
# Book is Available. You can borro




#3
#Library Menu

# available_books=['Mazha', 'Pathumma de aatinkutty', 'Nizhal', 'Beerbahutty', 'Mugam']
# for available_books in range(available_books[-1]):
#     print(available_books)


#4
#FUNCTIONS

def display_books(self):
    print(available_books)
def borrow_book(self):
    
    user=input("enter book name: ")
    if user==available_books[0]:
        print("you can borror this Book")
    elif user==available_books[1]:
        print("you can borror this Book")
    elif user==available_books[2]:
        print("you can borror this Book")
    elif user==available_books[3]:
        print("you can borror this Book")
    elif user==available_books[4]:
        print("you can borror this Book")
        available_books.remove(user)
def return_book(self):
    #self.return_option=return_option
    return_option=input("enter the return book name: ")
    available_books.append(return_option)
def display_avilable_books(self):
    print(available_books)

displaybooks=display_books()
borrowbook=borrow_book()
returnbook=return_book()
displayavilablebooks=display_avilable_books()