import os

"""

A file that creates a structured dataset
     data
      |
      |--- train
      |
      |--- test
      |
      |--- validation

"""

def createDatadir(path, parentdir, subdirs):

    os.chdir(path)
    print("The current working directory is {}".format(path))
    #os.chdir(path)
    check_dir = os.path.isdir('./data')
    subfolders = []

    if check_dir == False:
        print("There is no data dir,\ncreating the directories now")
        parent_dir = os.makedirs('data/')
        parent_path = os.chdir('./data')
        #subfolders = []
        if subdirs == 2:
          subfolders.extend(('train', 'test'))
        elif subdirs == 3:
          subfolders.extend(('train', 'test', 'validation'))
        else:
          print("Set a valid number of directories\n2 for train and test set and\n3 for train, test and validation sets")
        for subfolder in subfolders:
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
                created_folders = os.listdir()
        print("The subfolders {} have been created".format(created_folders))
    else:
        print("Data directory exists")



if __name__ == '__main__':
    path = input("Enter the directory path: ")
    parentdir = str(input("What is the name of your parent directory? "))
    subdirs = int(input("How many subdirectories need to create? "))
    createDatadir(path, parentdir, subdirs)