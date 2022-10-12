class ContactList:

    '''
    Each contact list should store its `contacts` as a list of dictionaries
    The list should be sorted by the contacts' name.
    '''
    contact_lst = []
    
    '''
    The contact list should also have a `name` that distinguishes it, 
    e.g. "School Friends", "Extended Family", or "Work Buddies".
    - containing name and phone number
    '''
    def __init__(self, group, lst):
        self.lst = lst
        self.group = group
        ContactList.contact_lst.append({self.group : self.lst})
    
    
    '''
    should add a new contact to the list, while keeping the list sorted
    '''
    def add_contact(self, contact):
        self.contact = contact
        
        for item in ContactList.contact_lst:
            # print(item)
            if self.group in item.keys():
                # print(self.group.values())
                item[self.group].append(self.contact) 
            
                
            # print(item.keys())    
        
        # ContactList.contact_lst.append({self.group: self.contact})
        
    
    '''
    should remove a contact from the list by name.
    '''
    def remove_contact(self, contact):
        self.contact = contact
        '''
            locate contact in contact_list
            loop through the list of dictionaries
                if key match then remove
        '''
        
        for item in ContactList.contact_lst:
            # print(item)
            if self.group in item.keys():
                for index in range(0, len(item[self.group])-1):
                    if item[self.group][index]["name"] == contact:
                        # del item[self.group][index]["name":contact]
                        print(item[self.group].pop(index))
                        print(item[self.group])
                        # item[self.group].pop(index)
                        # item[self.group][index].remove(contact)
                # print(item[self.group][2]["name"])
                # print(item.values())
         
        
    
    '''
    should accept another contact list as an argument, and then 
    return a new ContactList to indicate all the contacts that 
    appear in both lists (exact same name and phone number).
    '''
    def find_shared_contacts(self,ContactList):
        result = []
        self.lst_compare = ContactList.lst
        # print(self.lst_compare)
        # print(self.lst)
        for i in self.lst_compare:
            if i in self.lst:
                result.append(i)

        return result
    

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My_Friends', friends)
my_work_buddies = ContactList('Work_Buddies', work_buddies)

# test1 = ContactList('friends',friends)



my_work_buddies.add_contact({'name':'Luigi','number':'123-4567'})
my_work_buddies.remove_contact('Alice')

# print(my_friends_list.find_shared_contacts(my_work_buddies))

