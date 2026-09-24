from module import Datetime_module,Mathematical_module,Random_module,File_Operation,uuid_module

print("--------------------------------")
print("Welcome to Multi-Utility Toolkit")
print("--------------------------------")

while(True):
    print()
    print("Choose an option:")
    print("1.Datetime and Time Operations")
    print("2.Mathematical Operations")
    print("3.Random Data Generation")
    print("4.Generate Unique Identifiers(UUID)")
    print("5.File Operations(Custom Module)")
    print("6.Explore Module Attributes(dir())")
    print("7.Exit")
    choice=int(input("Enter your choice:"))

    match(choice):
       
        case 1:
            while(True):
                print()
                print("1.Display current date and time")
                print("2.Calculate the difference between two dates/times")
                print("3.Format date into custom format")
                print("4.stopwatch")
                print("5.Countdown Timer")
                print("6.Back to Main Menu\n")
                choice=int(input("Enter your choice:"))
                
                match(choice):
                   
                    case 1:
                        Datetime_module.display_current_datetime()

                    case 2:
                        Datetime_module.calculate_date_difference()
                     
                    case 3:
                        Datetime_module.format_date()

                    case 4:
                        Datetime_module.stopwatch()

                    case 5:
                        Datetime_module.countdown_timer()
                          
                    case 6:
                        print("Moving back to Main menu\n")
                        break

                    case _:
                        print("Invalide choice!")
       
        case 2:
            while(True):
                print()
                print("1.Calculate the Factorial")
                print("2.Solve Compound Interset")
                print("3.Trigonometric Calculations")
                print("4.Area of Geometric Shapes")
                print("5.Back to Main Menu\n")
                choice=int(input("Enter your choice:"))
                
                match(choice):

                    case 1:
                        Mathematical_module.calculate_factorial()
                        
                    case 2:
                        Mathematical_module.compound_interest()
                        
                    case 3:
                        Mathematical_module.trigonometric_calculations()
                        
                    case 4:
                        Mathematical_module.geometric_areas()
                       
                    case 5:
                        print("Moving back to Main menu\n")
                        break

                    case _:
                        print("Invalide choice!")
       
        case 3:
            while(True):
                print()
                print("1.Generate Random Number")
                print("2.Generate Random List")
                print("3.Create Random Password")
                print("4.Generate Random OTP")
                print("5.Back to Main Menu\n")
                choice=int(input("Enter your choice:"))
                
                match(choice):
                    
                    case 1:
                        Random_module.generate_random_number()
                        
                    case 2:
                        Random_module.generate_random_list()
                        
                    case 3:
                        Random_module.create_random_password()
                        
                    case 4:
                        Random_module.generate_random_otp()
                       
                    case 5:
                        print("Moving back to Main menu\n")
                        break

                    case _:
                        print("Invalide choice!")
       
        case 4:
            while(True):
                print("1.Generate uuid4")
                print("2.Generate uuid3")
                print("3.Generate uuid5")
                print("4.Back to Main Menu\n")
                choice=int(input("Enter your choice:"))
                
                match(choice):
                    
                    case 1:
                        uuid_module.generate_uuid4()
                                
                    case 2:
                        uuid_module.generate_uuid3()
                             
                    case 3:
                        uuid_module.generate_uuid5()
                          
                    case 4:
                        print("Moving back to main menu")
                        break
         
            print("-------------------------------------------------")
            
        case 5:
            while(True):
                print()
                print("1.Create a new file")
                print("2.Write to a file")
                print("3.Read from a file")
                print("4.Append to a file")
                print("5.Back to Main Menu\n")
                choice=int(input("Enter your choice:"))
                
                match(choice):
                    
                    case 1:
                       File_Operation.create_file() 
                       print("-------------------------------------------")    
                   
                    case 2:
                         File_Operation.write_file()
                         print("-------------------------------------------")
                    
                    case 3:
                        File_Operation.read_file() 
                        print("-------------------------------------------")
                   
                    case 4:
                       File_Operation.append_file() 
                       print("---------------------------------------------")
                    
                    case 5:
                        print("Moving back to Main menu\n")
                        break

                    case _:
                        print("Invalide choice!")

        case 6:
            print("Explore Module Attributes:")
            module_name=input("Enter module to explore:")
            module = __import__(module_name)
            print(f"Available Attributes in {module_name} module are:")
            print(dir((module)))
            print("----------------------------------------------------")

        case 7:
            print("----------------------------------------------")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("----------------------------------------------")
            break

        case _:
             print("Invalide choice!")
             print("Please choose Between 1-7")
