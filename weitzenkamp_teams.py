class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)
    
    def __contains__(self, member):
        return member in self.__myTeam
    
    def __iter__(self):
        return iter(self.__myTeam)


def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))
    
    print('Tim' in classmates)
        #check if Tim is part of classmates
    print('Sam' in classmates)
        #check if Sam is part of classmates
#user is just seeing if John is in "classmates" - interface, the program is running __contains__ function in the background - impl

    for members in classmates:
        print (members)
#user just needs a simple for loop here, but without the __iter__ function, it will not run becuase class is not iterable without it. 

    print('__len__' in dir(classmates))
        #checks if __len__ exists in classmates
main()