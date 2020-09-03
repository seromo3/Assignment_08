#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# SRomo, 2020-Sep-01, created file, added CD class
# SRomo, 2020-Sep-02, adjusted save, load, and show functions, added error handling
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        intId: (int) with CD ID
        strTitle: (string) with the title of the CD
        strArtist: (string) with the artist of the CD
    methods:
        __str__: returns formatting of properties

    """
    # --- Constructor --- #
    def __init__(self, cdID, ttl, art):
        self.__intID = cdID
        self.__strTitle = ttl
        self.__strArtist = art
    
    
    # --- Properties --- #
    @property
    def intID(self):
        return self.__intID
    
    @intID.setter
    def intID(self, value):
        self.intID = value
    
    @property
    def strTitle(self):
        return self.__strTitle
    
    @strTitle.setter
    def strTitle(self, value):
        self.strTitle = value
    
    @property
    def strArtist(self):
        return self.__strArtist
    
    @strArtist.setter
    def strArtist(self, value):
        self.strArtist = value
    
    # --- Method --- #
    def __str__(self):
        return ('{}, {}, {}'.format(self.intID, self.strTitle, self.strArtist))

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name, table):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        
        try:
            with open(file_name, 'r') as objFile:
                for row in objFile:
                    data = row.strip().split(',')
                    objCD = CD(data[0],data[1],data[2])
                    table.append(objCD)
                print('Your data was loaded!\n')
        except FileNotFoundError:
            print('The file doesn\'t exist. No data could be loaded.\n')
        except:
            print('Something else went wrong.\n')
        
    
    @staticmethod
    def save_inventory(file_name, table):
        """Function to write data from the table to a file
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns: 
            None
        """
        
        try:
            with open(file_name, 'w') as objFile:
                for obj in table:
                    data = (str(obj.intID) + ',' + str(obj.strTitle) + ',' + str(obj.strArtist) + '\n')
                    objFile.write(data)
                print('Your data was saved to the file!')
        except FileNotFoundError:
            print('The file doesn\'t exist. No data could be saved.\n')
        except:
            print('Something else went wrong.\n')
        
        
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Show inventory from file\n[a] Add CD to inventory')
        print('[i] Display Current Inventory\n[s] Save Inventory to file\n[x] exit\n')
        
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

        
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in table:
            print('{}\t{} (by:{})'.format(obj.intID,obj.strTitle,obj.strArtist))
        print('======================================\n')

    @staticmethod
    def add_cd():
        """Allows user to add a CD
        
        Args:
            strID: user input for CD ID
            strTitle: CD title
            strArtist: artist name
            
        Returns:
            intID, strTitle, strArtist
        
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        intID = int(strID)
        return intID, strTitle, strArtist
    

# -- Main Body of Script -- #
FileIO.load_inventory(strFileName, lstOfCDObjects) # Read in the currently saved inventory from txt file

while True:
    IO.print_menu() # Display Menu to user 
    strChoice = IO.menu_choice() # Get user choice

    if strChoice == 'x': # process exit request
        break
    
    if strChoice == 'l': # process load inventory from file
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Do you want to continue? [y/n] ')
        if strYesNo.lower() == 'y':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'a': # process add a CD
        intID, strTitle, strArtist = IO.add_cd() # User input for new ID, CD Title and Artist
        
        objCD = CD(intID, strTitle, strArtist) # Instantiate object
        
        lstOfCDObjects.append(objCD) # Append object to list
        
        IO.show_inventory(lstOfCDObjects) # Display inventory
        continue  
    
    elif strChoice == 'i': # process display current inventory
        IO.show_inventory(lstOfCDObjects)
        continue  
    
    elif strChoice == 's': # process save inventory to txt file
        IO.show_inventory(lstOfCDObjects) # Display current inventory and ask user for confirmation to save
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
