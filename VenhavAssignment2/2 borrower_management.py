"borrower management"

class Borrower:
    def __init__(s, name, contact_details, membership_id):
        s.name = name
        s.contact_details = contact_details
        s.membership_id = membership_id

class Library:
    def __init__(s):
        s.borrowers = []

    def add_borrower(s, borrower):
        s.borrowers.append(borrower)

                
    def update_borrower(s, borrower, new_contact_details):
        if borrower in s.borrowers:
            borrower.contact_details = new_contact_details
        else:
            print("Book not found in the library.")
        
    def remove_borrower(s, borrower):
        if borrower in s.borrowers:
            s.borrowers.remove(borrower)
        else:
            print("Borrower not found in the library.")

    def display_borrowers(s):
        for borrower in s.borrowers:
            #print(borrower)
            print(borrower.name, borrower.contact_details, borrower.membership_id)
            

            
lib_obj = Library()
borrow_obj1 = Borrower("Pandu", "pandu@gmail.com", 12345)
borrow_obj2 = Borrower("Hari", "hari@gmail.com", 67890)
 
lib_obj.add_borrower(borrow_obj1) #adding borrower1
lib_obj.add_borrower(borrow_obj2) #adding borrower2

lib_obj.display_borrowers()

lib_obj.update_borrower(borrow_obj1,"jaswanth1847@gmail.com") #updating the Existing-borrower

lib_obj.remove_borrower(borrow_obj2) #removing the Existing-borrower
lib_obj.display_borrowers()
