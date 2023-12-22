import copy

### Functions for reading writing and deleting data file


### Main Menu display and get option
def MainMenu():

    option = input("""=-=-=Main Menu=-=-=
What you like to do?
                   
1 - Load in the saved workout
2 - Create a new workout to save
3 - Edit the existing saved workout
4 - Delete the saved workout""")
    
    valid = InputIntValidation(option,1,4) #check input is valid

    if valid == True:
        return int(option),valid
    else:
        return 0,


### Check for saved file
def CheckFile():
    # first line dictates if default or not. "default" = default, "saved" = been appended to
    with open ("C:/Users/Jackr/OneDrive/Documents/GitHub/Lifting-Detection/BodyTracking/data/data.txt") as f:
        line = f.readline()

    if line.strip() == "default":
            found = False # not found any saved data, default file
    else:
        found == True # file has been edited, not default file

    f.close()

    return found



### Read file into dict from data.txt
def ReadFile():
    exercise_data = [] # store data to here

    with open ("C:/Users/Jackr/OneDrive/Documents/GitHub/Lifting-Detection/BodyTracking/data/data.txt") as f:
        lines = f.readlines() # read line by line
        
    lines.pop(0)
    
    for l in lines:
        values = l.strip().split(',')
        #exercise_data.append(values) # store each exercise separately in 2d array
        exercise_data.append([values[0]] + [int(val) for val in values[1:]])

   # exercise_data.pop(0) # remove "default" line

    return exercise_data



### Display the file array thats been read in from data.txt
def ViewFile(exercise_data):
    data = exercise_data

    print("Exercise  -  Sets , Reps\n------------------------")

    for i in data: # print each exercise line
        print("{} - {} , {}".format(i[0],i[1],i[2]))

    return 0



### Load in and use the data file Once this is called, program will continue to computer vision
def LoadFile(rep_dict,exercise_data):

    for i in exercise_data: #load in array as dict
        rep_dict[i[0]] = [i[1],i[2]]

    #make deep copy of dict
    
    deepDict = copy.deepcopy(rep_dict)
    return rep_dict, deepDict



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


### Check if an input is valid
def InputIntValidation(input, minValue, maxValue):
    valid = False

    try: #attempt to make sure input is an integer
        int(input)
    except:
        print("Invalid Input: Value is not a number")
        return 0
    
    if int(input) >= minValue and int(input) <= maxValue: #check value is within range
        valid = True
    else:
        print("Invalid Input: Value is not within range")

    return valid

def LogCompletedWorkout(workout):
    #log workout as completed in excel
    return 0