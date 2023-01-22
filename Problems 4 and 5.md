# In-Your-Interface

Problems 1-3 are answered within the python file attached to this repository. 

4. The interface what is visible to the user and what the user interacts with. The implementation is the "meat and potatoes" behind the program, all
  of the code and details are what makes up implementation. The only changes that will be visible to the user are those changes made that affect the 
  interface itself. The implementation is what actually carries out the actions, while the interface just defines what objects can do.

5. For local storage devices, I would create a class called Local.
  This would look something like this: (very simple example)
    class Local(self):
      def __init__(self, documents):
        self.myLocalStorage = documents
      def __len__(self):
         return len(self.__myLocalStorage)
   From this local class, we could have child classes of "USB" and "hard drive" that would inherit many of the properties of the local class.
   The interface would allow a user to decide where to store their documents. The implementation is all the code that is hidden from the user, such as the
   __len__ function above. The user can call "print(len(myUSBStorage))" from the child class, USB, and be able to see how many documents or data are 
   currently stored there. The user is not being exposed to any of the actual code above, the implementation, by the interface allows them to see what
   they need, the total number of documents currently stored there. 

