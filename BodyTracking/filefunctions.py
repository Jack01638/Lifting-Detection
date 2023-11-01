### Functions for reading writing and deleting data file


### Check for saved file
def CheckFile():
    # first line dictates if default or not. "default" = default, "saved" = been appended to
    with open ("./data/data.txt") as f:
        lines = f.readline()

    if lines.strip() == "default":
            found = False # not found any saved data, default file
    else:
        found == True # file has been edited, not default file

    f.close()

    return found



### Read file into dict from data.txt
def ReadFile():
    #read line by line:
        # store each line in 2d array
        # [1 if exercise being used,exercise name, total sets - 1, total reps]
    return 0 # return array with file data



### Display the file array thats been read in from data.txt
def ViewFile():
    # only view if been read in
    # print list in following format:
    '''
    Exercise Name - Sets + 1 / Reps
    ---------------------------
    Bicep Curl - 10 / 12
    Row - 8 / 15
    '''
    return 0 # keep returning 0 as nothing needs to be returned



### Load in and use the data file
def LoadFile():
    # using array from ReadFile(), load each exercuse into the dictinary
    # make sure this function is called before we make a deep copy, or make a new deep copy of the new one after so ensure rep_dict_info is correct
    return 0



### Edit data file
def EditFile():
    # only call if confirmed file exists
    # call ViewFile() to show data
    # while still editing:
        # select which element in array (the exercise) you want to edit
            # print old data for this exercise
            # enter value to change sets to
            # enter value to change reps to
            # change entry in the array
            # print confirmed new data for this exercise
        # call ViewFile()
    # confirm to save these changes to file (cannot be undone)
    # save array to data.txt and overwrite old data
    return 0



### Delete saved file
def DeleteFile():
    # only do if file is made
    # ViewFile()
    # confirm deltetion
    # set data.txt to empty sets/reps
    return 0