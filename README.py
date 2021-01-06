# import _tkinter
import time#use for history,sleep
print("!!!WELCOME TO THE LIBRARY!!!\n\n\n")

while 1:#making loop
    class library:#class

        pass#no variable

        @staticmethod#our method for if person is new

        def user_choice_new(user_value):
            """USER IS NEW PERSON """
            if user_value=="n" or user_value=="N":
                name=input("ENTER YOUR USERNAME ")#user name
                GENDER=input("ENTER GENDER ")#user gender
                USER_PASSWORD=input("YOUR PASSWORD:- ")#user password
                print("PLEASE WAIT MAKING PROFILE.....")
                time.sleep(2)
                users_data=open(f"C://Users//HP//Desktop//DON'T OPEN//LIBRARY_MINI_PROJECT//all user detail//{name}-{USER_PASSWORD}.txt","w")
                users_data.write("USER NAME:-"+name+"\n")#writing name
                users_data.write("USER GENDER:-"+GENDER+"\n")#gender
                users_data.write("USER PASSWORD:-"+str(USER_PASSWORD)+"\n")#writhing password
                user_history=open(f"C://Users//HP//Desktop//DON'T OPEN//LIBRARY_MINI_PROJECT//ALL USER HISTORY//{name}-{USER_PASSWORD}.txt","w")
                user_history.close()
                print("PLEASE REMEMBER YOUR USERNAME AND PASSWORD FOR LATER")
                # import importlib
                # importlib.reload(importlib)
        @staticmethod#method for adding
        def user_choice_add(users_value):
            """IN THIS USER WANT TO ADD BOOK """
            if users_value == "A" or users_value == "a":
                try:#errror handling
                    if_user_name=input("ENTER YOUR USERNAME ")#taking password and name from user
                    if_user_add = input("ENTER YOUR PASSWORD ")
                    print("PLEASE WAIT CHECKING PASSWORD.....")
                    time.sleep(2)
                    user_id = open(f"C://Users//HP//Desktop//DON'T OPEN//LIBRARY_MINI_PROJECT//all user detail//{if_user_name}-{if_user_add}.txt")
                    user_id.close()
                    print("WELCOME!!")
                    print("NOTE:-YOU CAN WRITE ONLY SEVEN LINES")
                    time.sleep(2)
                    print("WRITE YOUR BOOK BELOW:-")
                    time.sleep(1)
                    user_add1 = input("")
                    user_add2 = input("")
                    user_add3 = input("")
                    user_add4 = input("")
                    user_add5 = input("")
                    user_add6 = input("")
                    user_add7 = input("")
                    time.sleep(1)
                    print("ENTER THE NAME FOR YOUR BOOK BELOW:-")
                    user_book_name = input("ENTER HERE ")
                    ALL_BOOKS_NAME = open("ALL_BOOKS_NAME.txt", "a")
                    ALL_BOOKS_NAME.write("\n" + user_book_name)
                    user_book = open(
                        f"C://Users//HP//Desktop//DON'T OPEN//LIBRARY_MINI_PROJECT//all user's books//{user_book_name}.txt","w")
                    user_book.write(user_add1 + "\n")
                    user_book.write(user_add2 + "\n")
                    user_book.write(user_add3 + "\n")
                    user_book.write(user_add4 + "\n")
                    user_book.write(user_add5 + "\n")
                    user_book.write(user_add6 + "\n")
                    user_book.write(user_add7 + "\n")
                    user_history = open(
                        f"C://Users//HP//Desktop//DON'T OPEN//LIBRARY_MINI_PROJECT//ALL USER HISTORY//{if_user_name}-{if_user_add}.txt","a")
                    named_tuple = time.localtime()  # get struct_time
                    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                    user_history.write(f"\nHISTORY:-\nAT{time_string}\nBOOK ADDED:-{user_book_name}\n")

                except:#if it give error than
                    print("WRONG PASSWORD")
                    print("NO PROFILE FOUND")
                    exit()

        @staticmethod
        def user_choice_want(users_value_):
            """IN THIS METHOD USER WANT A BOOK"""
            if users_value_ == "W" or users_value_ == "w":
                try:
                    if_user_nam=input("ENTER YOUR USERNAME ")
                    if_user_ad = input("ENTER YOUR PASSWORD ")
                    user_id = open(f"C:\\Users\\HP\\Desktop\\DON'T OPEN\\LIBRARY_MINI_PROJECT\\all user detail\\{if_user_nam}-{if_user_ad}.txt")
                    user_id.close()
                    print("WELCOME!!")
                except:
                    print("NO PROFILE FOUND")
                    exit()

                print("CHOOSE 1 BOOK GIVEN BELOW:-")
                time.sleep(2)
                user_want_a_book=open("ALL_BOOKS_NAME.txt","r")
                print(user_want_a_book.read())
                try:
                    choice = input("ENTER THE BOOK NAME ")
                    print("YOUR BOOK IS BELOW:-")
                    time.sleep(1)
                    user_book=open(f"C:\\Users\\HP\\Desktop\\DON'T OPEN\\LIBRARY_MINI_PROJECT\\all user's books\\{choice}.txt","r")
                    st=user_book.read()
                    print(st)
                    # deleted_file=open("ALL_DELTED_FILES.txt","w")
                    # deleted_file.write(st+"\n")
                    user_detail_in_txt=open(f"C:\\Users\\HP\\Desktop\\DON'T OPEN\\LIBRARY_MINI_PROJECT\\ALL USER HISTORY\\{if_user_nam}-{if_user_ad}.txt","a")
                    # time.localtime()
                    # user_detail_in_txt.write("history:-"+"\n")
                    named_tuple = time.localtime()  # get struct_time
                    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                    # print(time_string)
                    user_detail_in_txt.write(f"\nHISTORY:-\nAT {time_string}\nBOOK READ:-{choice}\n ")
                except:
                    print("SORRY! THIS BOOK IS NOT AVAILABLE")
        @staticmethod
        def user_choice_history(user_value):
            if user_value=="h" or user_value=="H":
                name=input("ENTER USERNAME ")
                password=input("ENTER PASSWORD ")
                print("PLEASE WAIT CHECKING PASSWORD.....")
                time.sleep(2)
                try:
                    Open=open(f"C:\\Users\\HP\\Desktop\\DON'T OPEN\\LIBRARY_MINI_PROJECT\\all user detail\\{name}-{password}.txt")
                    Open.close()
                except:
                    print("NO PROFILE FOUND")
                    exit()
                print("YOUR HISTORY:-")
                print("PLEASE WAIT.....\n\n\n\n")
                time.sleep(2)
                try:
                    OPEN=open(f"C:\\Users\\HP\\Desktop\\DON'T OPEN\\LIBRARY_MINI_PROJECT\\ALL USER HISTORY\\{name}-{password}.txt","r")
                    print(OPEN.read())
                    OPEN.close()
                except:
                    print("NO PROFILE FOUND ")
        # @staticmethod
        # def user_choice_not(user_value):
        #     if user_value!="n" or user_value!="N" or user_value!="h" or user_value!="H" or user_value!="A" or user_value!="a" or user_value!="w" or user_value!="W":
        #         print("PLEASE WRITE LETTER THAT IS IN BRACKET")

    user = library()
    print("NOTE:- IF YOU ARE A NEW PERSON THAN YOU HAVE TO ENTER(n) AFTER 3 SEC THANKS")
    print("PLEASE WAIT.....")
    time.sleep(3)
    users_value = input("ENTER WANT (w), ADD (a) , NEW PERSON (n) , history (h) ")
    print("PLEASE WAIT.....")
    time.sleep(3)
    # user.user_choice_not(users_value)
    user.user_choice_want(users_value)
    user.user_choice_add(users_value)
    user.user_choice_new(users_value)
    user.user_choice_history(users_value)
