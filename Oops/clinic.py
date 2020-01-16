try :
    import json
except ImportError:
    print("importing error")  
class search:
    def __init__(self):
        try:
            f = open("clinic_json.json","r")
            self.data = json.loads(f)
        except FileNotFoundError :
            print("file not found")    
    def search(self): 
        data = self.data
        choice = input("enter choice d-doctor or p-patient")
        if choice == d :
            specilization = input("enter your required specilization")
            for i in data["doctor"] :
                if i["specilization"] == specilization :
                    print("name is",data["name"],"specilise in",data["specilization"],"phone no:".data["phone"],"avaliable at time",data["avaliable"])

