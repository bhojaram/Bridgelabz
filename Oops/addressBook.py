try :
    import json
except ImportError :
    print("importing error")
#creating class of addressbook
class addressBook :
    def __init__(self) :
        #passing the json file
        f = open("json.json") 
        #load() use to convert json.. 
        #file to python    
        self.data = json.loads(f) 
    def addRecords(self) :
        try :
            #entering input for dictonary
            first_name = input("enter the first name")
            last_name = input("enter the last name")
            address = input("enter the proper address")
            city = input("enter the city name")
            state = input("enter the state you belong to")
            zip = int(input("enter the zip of area"))
            phone = int(input("enter a valid contact no."))
            #creating dictonary
            dic = {"first_name":first_name,
                   "last_name":last_name,
                  "address":address, 
                  "city":city,
                  "state":state, 
                  "zip":zip,
                  "phone":phone } 
            #creating object of self.data       
            data = self.data
            #and adding to dictonary
            data.append(dic)
        except ValueError :
            print("check for data")             

    def delet_person(self):
        x = input("enter the first name of person to delet")
        #searching for first name
        for i in self.data :
            if x == i["first_name"] :
                #deleting the respective record
                del i["first_name"]
    #adding new person            
    def add_person(self):
        x = input("enter the first name of person to insert")
        for i in self.data :
            #searching for first name
            if x != i["first_name"] :
                #then adding to json file
                f = open("json.json", "a")  
                json.dumps(data,f) 
    def sort_case(self) :
        #accessing record in alphabatic order
        print(json.dumps(f,indent = 7,sort_keys = True ))
    def sort_zip(self) :
        print(json.dumps(f,sort_keys = "zip"))
    def modify_person(self) :
        x = input("enter the first name to modify")
        for i in self.data :
            if x == i["first_name"] :
                f = open("json.json","w")
                json.dumps(data,f)

