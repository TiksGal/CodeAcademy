import urllib3
import base64
import shlex
import subprocess
import os
import time


class Launch:

    Scan = {"The Number and Question": "The Answer"}
    Type = ("LinuxOS", "MacOS (Not)", "WindowsOS (Not)", "AndroidOS (Not)")
    TypeOption = [0, 0, 0, 0]
    Inventory = {}

    def __init__(self):
        self.OperationName = "Configuration Check of the Operating System"
        self.OperationDescription = "Functionality for checking the Configuration, which were defined in the " \
                                       "Documentation of the Specific Platform."
        # self.http = urllib3.PoolManager()

    def options(self):
        print("Loaded Operation: " + str(self.OperationName))
        print("Available Scan Options:")

        for item in self.Type:
            print("\t" + item)

    def SetOptions(self):
        print("\tSelect OS for the Scan:")
        i = 0
        for item in self.Type:
            value = input("Do You want to Scan the " + item + "? (y/n)")
            if value == "y" or value == "Y":
                self.TypeOption[i] = 1
            else:
                self.TypeOption[i] = 0
            del value
            i += 1

    def OperationStart(self):
        # need specify for which OS Configuration Scan gonna be performed
        self.options()
        value = input("Do You want to Scan only first Option? (y/n)")
        if value == "y" or value == "Y":
            self.TypeOption[-1] = 1
        else:
            self.SetOptions()
        del value

        # Scan type: by selected OS and defined Custom Configuration in this One File
        # LinuxOS - developed by Linus Torvalds and Companies which using it as open sourced product
        # MacOS - developed by Apple Company
        # WindowsOS - developed by Microsoft Company
        # AndroidOS - developed by Google and Companies which using it as open sourced product
        print("Current time: " + str(time.ctime()))
        time.sleep(1)

        i = 0
        for item in self.Type:
            if item.find("LinuxOS") and self.TypeOption[i] == 1:
                print("LinuxOS Scan commence:")
                self.LinuxOSScan()
            elif item.find("MacOS") and self.TypeOption[i] == 1:
                print("MacOS Scan commence:")
                self.MacOSScan()
            elif item.find("WindowsOS") and self.TypeOption[i] == 1:
                print("WindowsOS Scan commence:")
                self.WindowsOSScan()
            elif item.find("AndroidOS") and self.TypeOption[i] == 1:
                print("AndroidOS Scan commence:")
                self.AndroidOSScan()
            else:
                pass
            i += 1

    def LinuxOSScan(self):
	    
	    print('')
	    print("OS prod information:")
	    print(os.system('uname -a'))
	    
	    #
	    # TODO. Specific OS Distribution
	    # has possibility to have different Configuration Options
	    #
	    #
	    # Checking OS privileges of the Current User
	    #
	    
	    print('')
	    y = 1
	    var_user = ''
	    var_output = ''
	    
	    print("--- Initial actual information ---")
	    print("No:" + str(y) + " Q. Does for the following commands Administrative Access are Given?")
	    
	    try:
	    	var_user = subprocess.check_output(['whoami'])
	    except subprocess.CalledProcessError as error:
	    	print('Error No: ' + str(y))
	    
	    user = str(var_user)
	    
	    try:
	    	var_output = subprocess.check_output(['groups', user])
	    except subprocess.CalledProcessError as error:
	    	print('Error No: ' + str(y))
	    
	    if 'sudo' in var_output:
	    	self.Scan["No:" + str(y) + ". Does for checking the Configuration Administrative Access are Given?"] = \
	    'Everything seems right.'
	    	print("No:" + str(y) + " A. Everything seems right.")
	    elif 'root' in var_output:
	    	self.Scan["No:" + str(y) + ". Does for checking the Configuration Administrative Access are Given?"] = \
	    'It gonna work.'
	    	print("No:" + str(y) + " A. It gonna work.")
	    else:
	    	self.Scan["No:" + str(y) + ". Does for checking the Configuration Administrative Access are Given?"] = \
	    	'No.'
	    	print("No:" + str(y) + " A. No.")
	    
	    del var_user, var_output
	    
	    #
	    # Checking Situation with the Users and Groups of the Operation System
	    #
	    
	    print('')
	    y += 1
	    var_output = ''
	    var_error = ''

	    print("No:" + str(y) + " Q. Does exists accounts with empty password field?")
	    
	    try:
	    	result = subprocess.run(
	    	['awk', '-F:', '''($2 == "") { print $1 "does not have password" }''', '/etc/shadow'], capture_output=True, text=True
	    )
	    except subprocess.CalledProcessError as error:
	    	print('Error No: ' + str(y))
	    	print(error)
	    	print(result.stderr)
	    

	    var_output = result.stdout
	    
	    if self.checkValueInData("Permission denied", var_output) != '-1':
	    	self.Scan["No:" + str(y) + ". Does the User have permission to access the Shadow file (Linux)?"] = 'This User does not have Super User access privileges.'
	    	print("No:" + str(y) + " A. This User does not have Super User access privileges.")
	    else:	    
		    if not var_output:
			    self.eveScan["No:" + str(y) + ". Does exists accounts with empty password field?"] = 'All accounts has the passwords and without empty fields.'
			    print("No:" + str(y) + " A. All accounts has the passwords.")
		    else:
			    self.eveScan["No:" + str(y) + ". Does exists accounts with empty password field?"] = 'Need to check for passwordless accounts.'
			    print("No:" + str(y) + " A. Need to check for passwordless accounts.")
			    
	    del var_output
	    
	    #
	    # Checking for specific known applications
	    #
	    
	    print('')
	    y += 1
	    var_output = ''
	    var_operation = ''
	    list_operations = ("H", "LI", "L")
	    
	    print("--- Checking Application Settings ---")
	    
	    """
	    " 1st value of @var eveInventory is mean for choosing the Operation:
	    " Codename:
	    " H - Help
	    " LI - Launch and return Output Only
	    " L - Launch
	    """
	    
	    self.Inventory["apparmor module is loaded."] = ("L", "apparmor_status")
	    self.Inventory["OpenSSL"] = ("LI", "openssl version")
	    self.Inventory["nmap.org"] = ("H", "nmap", "nmap.ncat", "nmap.nping")

	    for key, value in self.Inventory.items():
	    	var_operation = value[0]
	    	i = -1
	    	for val in value:
	    		i = i + 1
	    		
	    		if i != 0 and var_operation == "H":
	    			try:
	    				result = subprocess.run(
	    				[val, '-h'], capture_output=True, text=True
	    				)
	    			except subprocess.CalledProcessError as error:
	    				print('Error No: ' + str(y))
	    				print(error)
	    				print(result.stderr)
	    			
	    			data_rev = self.checkValueInData(key, result.stdout)
	    			
	    			if data_rev < 0:
	    				self.Scan["No:" + str(y) + ". Does the app " + str(val) + " installed ?"] = str(val) + ' does not Present.'
	    				print("No:" + str(y) + " A. " + str(val) + " does not present in the OS.")
	    			else:
	    				self.Scan["No:" + str(y) + ". Does the app " + str(val) + " installed ?"] = str(val) + ' is Present.'
	    				print("No:" + str(y) + " A. " + str(val) + " is present in the OS.")
	    		
	    		if i != 0 and var_operation == "L":
	    			try:
	    				result = subprocess.run(
	    				[val], capture_output=True, text=True
	    				)
	    			except subprocess.CalledProcessError as error:
	    				print('Error No: ' + str(y))
	    				print(error)
	    				print(result.stderr)
	    			
	    			data_rev = self.checkValueInData(key, result.stdout)
	    			
	    			if data_rev < 0:
	    				self.Scan["No:" + str(y) + ". Does the app " + str(val) + " installed ?"] = str(val) + ' does not Present.'
	    				print("No:" + str(y) + " A. " + str(val) + " does not present in the OS.")
	    			else:
	    				self.Scan["No:" + str(y) + ". Does the app " + str(val) + " installed ?"] = str(val) + ' is Present.'
	    				print("No:" + str(y) + " A. " + str(val) + " is present in the OS.")
	    				print(result.stdout)
	    		
	    		if i != 0 and var_operation == "LI":
	    			try:
	    				var_output = subprocess.check_output([val, 'version'])
	    			except subprocess.CalledProcessError as error:
	    				print('Error No: ' + str(y))
	    				print(error)
	    				print(result.stderr)
	    			
	    			print(var_output)
	    			

	    del var_output, var_operation, list_operations


    def MacOSScan(self):
        print("Currently Not Available.")

    def WindowsOSScan(self):
        print("Currently Not Available.")

    def AndroidOSScan(self):
        print("Currently Not Available.")

    def checkValueInData(self, value, data):
        return data.find(value)
        
    
obj = Launch()

obj.OperationStart()