try :
    #catching exception
    import json
except ImportError:
    print("importing error")  
class Search:
    def search(self):
            choice = input("enter choice d-doctor or p-patient :")
            if choice == 'd' :
                try:
                    f = open("/home/user/Bridgelabz/Oops/clinicManagement/clinic_json.json","r")
                    data_key = json.load(f)
                    print(data_key["doctor"])
                except FileNotFoundError :
                    print("file not found")
                
                #searching for specilization 
                #in doctor.. dictonary
                specilization = input("enter your required specilization :")
                for data in data_key["doctor"] :
                    if data["specilization"] == specilization :
                        print("doctor",data["name"],data["specilization"],data["phone"],data["avaliable"])
                    else:
                        #if doctor not found..
                        #then add new doctor
                        print("not found ..so add docor datails")    
                        name = input("enter doctor name to add :")   
                        spl = input("enter the specilization") 
                        phone = int(input("enter the phone :"))
                        ava = input("enter avaliable time")
                        #fetching details
                        di = {"name":name,
                            "specilization" :spl,"phone":phone,
                            "avaliable": ava
                            }
                        #appending data to dictnary      
                        data1 = data_key
                        data1["doctor"].append(di)    
                        f = open("/home/user/Bridgelabz/Oops/clinicManagement/clinic_json.json","w")
                        json.dump(data1,f)
            elif choice == 'p' :
                try:
                    f = open("/home/user/Bridgelabz/Oops/clinicManagement/clinic_json.json","r")
                    data_key = json.load(f)
                    print(data_key["patient"])
                except FileNotFoundError :
                    print("file not found")
                #taking id & searching for patient
                id = int(input("enter the id of patient "))
                for data in data_key["patient"] :
                    if data["id"] == id :
                        #printing patient details
                        print("patient",data["name"],data["add"],data["phone"],data["gender"])
                    else:
                        #adding new patient if not present
                        name = input("enter address of patient")
                        id = int(input("enter the id"))
                        address =  input("enter name of patient")
                        phone =  int(input("enter phone no. of patient"))
                        gender =  input("enter gender of patient")
                        #addind data to dictonary
                        di= {"name" :name,
                                 "id":id,
                                 "add":address,
                                 "phone":phone,
                                 "gender":gender 
                            }
                        data1 = data_key 
                        #appending data to dictonary   
                        data1["patient"].append(di)
                        print(data_key["patient"])
                        f = open("/home/user/Bridgelabz/Oops/clinicManagement/clinic_json.json","w")
                        json.dump(data1,f)

            else :
                print("you chose wrong choice")
s= Search()
s.search()
