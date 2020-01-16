try :
    import json
    from addressBook import addressBook
except ImportError :
    print("importing error")
def adressBookManagement() :
    ad = addressBook()
    #choice = [1,2,3,4,5]
    #for i in range(len(choice)) :
    try :
        input = int(input("press '1' for delet",2-adding,3-sort_case,4-zip_sort,5-modify))
        if input == 1 :
            print(ad.delet_person())
            continue
        elif input == 2 :
            print(ad.add_person()) 
        elif input == 3 :
            print(ad.sort_case())
            continue    
        elif input == 4 :
            print(ad.sort_zip())
            continue
        elif input == 5 :
            print(ad.modify_person())
            continue 
        else :
            print("invalid choice") 
    except ValueError :
        print("check input")             

