class User:
    """ An class to demonstrate simple objects"""
    def __init__(self,id,full_name,dob):
        self.id=id
        self.name=full_name
        self.dob=dob
    
    def namid(self):
        """ A method to return NAME  & ID """
        return [self.id,self.name]

#initialize objects      
user1 = User("001","Praketa Saxena","01/12/1992")
#get name and id 
print(user1.namid())