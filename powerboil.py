import sys
import os
import json
from preprocessed_files  import HTML_STRING,readme,extension_html,popupfile,linearRegression,basic_plot
import subprocess
import gitignore
# Colors class
class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible = '\033[08m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan = '\033[96m'
#Directory Selection         
def select_dir():
    while(True):
 
        DIR = list(os.listdir())
        print(colors.red, " 1) Select the directoy you want  to  create your Project \n  2) Press '*' to create a new directory \n 3) To create in Current Directory Press #")
        print(colors.reset)    
        for index, dirs in enumerate(DIR):
            print(colors.purple, "{0}) {1}".format(index, dirs))
            print(colors.reset)
        choice = input()
        if (choice == '*'):
            directory_name = input( "Enter the name of the Directory You want to create")
            print(colors.reset)
            os.mkdir(directory_name)
            return directory_name
            break
        elif choice == '#':
            return os.getcwd()    
        elif int(choice) <= len(DIR) -1 :
            selected_dir = DIR[ int(choice)]
            return select_dir
            break
        elif int(choice) > len(DIR - 1):
            print(colors.red, "Enter a valid Choice \n")
            print(colors.reset)
            continue
# BoilerPlate Code for Django             
def create_django(project_name=None, dir_to_create=None,app_name=None):
    if(dir_to_create == None):
        dir_to_create = select_dir()
        os.chdir(dir_to_create)
    while (True):
        if(project_name ==None):
            print(colors.yellow, " 1) Enter the Project Name \n")
            print(colors.reset)
            project_name = input()
        if (project_name.isspace()):
            print(colors.yellow, "Enter a valid Project Name to continue")
            print(colors.reset)
            continue

        project_name = project_name.strip().lower()
        if(app_name ==None):
            print(colors.yellow,"2) Enter the App Name")
            app_name=input()
            if (app_name.isspace()):
                print(colors.red, "Enter a valid App Name")
                print(colors.reset)
                continue
            
        app_name = app_name.strip().lower()
        try:
            print(colors.bold, colors.blue, "Please Wait Creating Your Awesome Django Project... ")
            print(colors.reset)
            DEVNULL= open(os.devnull,'wb')
            p = subprocess.Popen(['django-admin startproject '+project_name ], stdout=DEVNULL, stderr=subprocess.STDOUT,shell=True)
            output=p.communicate()
            os.chdir(project_name)
            with open("README.md", 'a') as f:
                f.write(readme.format(project_name, project_name, "Django"))
            with open('.gitignore', 'a') as f:
                f.write(gitignore.DJANGO_GIT_IGNORE)
                  
            pr = subprocess.Popen(['django-admin startapp '+ app_name], stdout=DEVNULL, stderr=subprocess.STDOUT,shell=True)
            out = pr.communicate()[0]
            if pr.returncode == 0:
                print(colors.green, "Project Created Succesfully")
                print(colors.reset)
                sys.exit()
                DEVNULL.close()
        except subprocess.CalledProcessError as e:
               if p.returncode != 0:
                   print("It seems you have not Installed Django in Your System do you want  to install and continue[Yes/No]")
                   choice = input()
                   if (not choice.lower() == 'yes'):
                       sys.exit()
                   if (choice.lower() == 'yes'):
                       print(colors.blue, "Installing Django ..")
                       print(colors.reset)
                       p=subprocess.Popen(['pip3 install django'], stdout=DEVNULL, shell=True, stderr=subprocess.STDOUT)
                       output = p.communicate()
                       
                       if p.returncode == 0:
                           print(colors.black, "Django installed Succesfully rerun command to create project")
                           break
                       else:
                            print(colors.cyan,"Couldn't install Django please Try again")
                            print(colors.reset)

                            sys.exit()
                  
#Boiler Plate Code for Flutter                                  
def create_flutter(project_name=None, dir_to_create=None):
    if dir_to_create == None:
        dir_to_create = select_dir()
        os.chdir(dir_to_create)
    while (True):
       if(project_name ==None):
            print(colors.yellow, "Enter Project Name")
            print(colors.reset)
            project_name = input()
            if project_name.isspace():
                print( colors.red,"Please Enter a valid Project Name to continue")
                print(colors.reset)
                continue
       try:
            print(colors.bold, colors.blue, "Please Wait Creating Your Awesome Flutter  Project ..")
            print(colors.reset)
            DEVNULL= open(os.devnull,'wb')
            p = subprocess.Popen(['flutter create '+project_name ], stdout=DEVNULL, stderr=subprocess.STDOUT,shell=True)
            output = p.communicate()
            if p.returncode == 0:
                print(colors.bold, colors.yellow, "Project Created Succesfully !!! ")
                print(colors.reset)
                sys.exit()

       except subprocess.CalledProcessError  as e:
           if p.returncode != 0:
               print(colors.red, colors.bold, "Error ! Couldn't find Flutter in your system please follow this and install and continue   \n https://flutter.dev/docs/get-started/install")
               print(colors.reset)    
               sys.exit()
# BoilerPlate Code for React               
def create_react(project_name=None, dir_to_create=None):
    if dir_to_create == None:
        dir_to_create = select_dir()
        os.chdir(dir_to_create)
    while (True):
        if project_name == None :
            print(colors.yellow, "Enter Project Name")
            print(colors.reset)
            project_name = input()
            if project_name.isspace():
                print( colors.red,"Please Enter a valid Project Name to continue")
                print(colors.reset)
                continue
        try:
                print(colors.bold, colors.blue, "Please Wait Creating Your Awesome React  Project !! ")
                print(colors.reset)
                DEVNULL = open(os.devnull, 'wb')
               
                p = subprocess.Popen(['npx create-react-app ' + project_name ], stdout=DEVNULL, stderr=subprocess.STDOUT,shell=True)
                output = p.communicate()[0]
                if p.returncode == 0:
                    print(colors.bold, colors.yellow, "Project Created Succesfully !!! ")
                    print(colors.reset)
                    sys.exit()

        except subprocess.CalledProcessError  as e:
            if p.returncode != 0:
               print("It seems that 'Node' is not installed in your System Please follow the below link to install \n https://nodejs.org/en/download/ ")
               print(colors.reset)
               sys.exit()
#Boiler Plate Code for Vue
def create_vue(project_name=None, dir_to_create=None):
    if dir_to_create == None:
        dir_to_create = select_dir()
        os.chdir(dir_to_create)
    while (True):
        if project_name ==None:
            print(colors.yellow, "Enter Project Name")
            print(colors.reset)
            project_name = input()
            if project_name.isspace():
                print( colors.red,"Please Enter a valid Project Name to continue")
                print(colors.reset)
                continue
        try:
                print(colors.bold, colors.blue, "Please Wait Creating Your Awesome Vue Project !! ")
                print(colors.reset)
                DEVNULL = open(os.devnull, 'wb')
               
                p = subprocess.Popen(['vue create -b  ' + project_name ], stdout=DEVNULL ,stderr=subprocess.STDOUT,shell=True,stdin=subprocess.PIPE)
                output = p.communicate(input = b'\n')[0]
                if p.returncode == 0:
                    print(colors.bold, colors.yellow, "Project Created Succesfully !!! ")
                    print(colors.reset)
                    sys.exit()

        except subprocess.CalledProcessError  as e:
            if p.returncode != 0:
                if p.returncode != 0:
                   print("It seems you have not Installed Vue  in Your System do you want  to install and continue[Yes/No]")
                   choice = input()
                   if (not choice.lower() == 'yes'):
                       sys.exit()
                   if (choice.lower() == 'yes'):
                       print(colors.blue, "Installing Vue ..")
                       print(colors.reset)
                       p=subprocess.Popen(['npm install -g @vue/cli '], stdout=DEVNULL, shell=True, stderr=subprocess.STDOUT)
                       output = p.communicate()
                       
                       if p.returncode == 0:
                           continue
                       else:
                            print("Couldn't install Vue  please Try again,Install it manually or make sure npm is installed ,Follow the docs to install npm \n https://nodejs.org/en/download/ ")
                            print(colors.reset)
                            sys.exit()
#BoilerPlate Code for HTML            
def create_html(project_name=None, dir_to_create=None):
    if dir_to_create == None:
        dir_to_create = select_dir()
        os.chdir(dir_to_create)
    while (True):
        if project_name ==None:
            print(colors.yellow, "Enter Project Name")
            print(colors.reset)
            project_name = input()
            if project_name.isspace():
                print( colors.red,"Please Enter a valid Project Name to continue")
                print(colors.reset)
                continue
        else:
            print(colors.bold, colors.blue, "Creating Your Awesome HTML Project")
            print(colors.reset)
            try:
                os.makedirs(project_name)
                os.chdir(project_name)
                with open("README.md", 'a') as f:
                    f.write(readme.format(project_name, project_name, "HTML"))

                with open('index.html', 'w') as file:
                    file.write(HTML_STRING.format(project_name.title(),project_name.title()))
                print(colors.bold, colors.yellow, "Project Created Sucessfully")
                print(colors.reset)
                sys.exit()
            except FileExistsError as e:
                print(colors.bold, colors.red, project_name + " already exists please mention a different name ")
                print(colors.reset)
                break
#BoilerPlate Code for Chrome Extension        
def create_extension(project_name=None, dir_to_create=None):
    if dir_to_create == None:
        dir_to_create = select_dir()
        os.chdir(dir_to_create)
    while (True):
        if project_name ==None:
            print(colors.yellow, "Enter Project Name")
            print(colors.reset)
            project_name = input()
            if project_name.isspace():
                print( colors.red,"Please Enter a valid Project Name to continue")
                print(colors.reset)
                continue
        else:
            print(colors.bold, colors.blue, "Creating Your Awesome HTML Project")
            print(colors.reset)
            try:
                os.makedirs(project_name)
                os.chdir(project_name)
                with open("README.md", 'a') as f:
                    f.write(readme.format(project_name, project_name, "Chrome Extension"))

                with open('index.html', 'w') as f:
                    f.write(extension_html.format(project_name.title()))
                with open('popup.js') as f:
                    f.write(popupfile)
                       
                print(colors.bold, colors.yellow, "Project Created Sucessfully")
                print(colors.reset)
                sys.exit()
            except FileExistsError as e:
                print(colors.bold, colors.red, project_name + " already exists please mention a different name ")
                print(colors.reset)
 
                break
#Boiler Plate Code for ML                
def create_ml(project_name=None, dir_to_create=None):
    DEVNULL = open(os.devnull, 'wb')
    if dir_to_create == None:
        dir_to_create = select_dir()
        os.chdir(select_dir)
        print(colors.yellow, "Is the PC setup with all dependencies [Yes/No] ? \n")
        choice = input()
        if choice.lower() == 'Yes' or choice.lower() == 'y':
            print(colors.reset, colors.red, "The following packages will be installed 1) Sci- Kit Learn \n 2) Numpy  \n 3) Matplotlib \n 4)Pandas \n [Yes/No]")
            option = input()
            if option.lower == 'yes' or option.lower() == 'y':
               project_dir= os.mkdir("BoilerML")
               os.chdir(project_dir)
               print(colors.lightgreen, "Installing Numpy ... ")
               print(colors.reset)
               p = subprocess.Popen(['pip3 install numpy'], stdout=DEVNULL, stderr=subprocess.STDOUT, shell=True)
               output = p.communicate()[0]
               if p.returncode == 0:
                   print("Installed Numpy")
               else:
                   print("Unexpected Error occured ,Please try again later")
                   sys.exit()

               p = subprocess.Popen(['pip3 install matplotlib'], stdout=DEVNULL, stderr=subprocess.STDOUT, shell=True)
               output = p.communicate()[0]
               if p.returncode == 0:
                   print("Installed Matplotlib")
               else:
                   print("Unexpected Error occure")
                   sys.exit()
                   p = subprocess.Popen(['pip3 install sklearn'], stdout=DEVNULL, stderr=subprocess.STDOUT, shell=True)
                   output = p.communicate()[0]
                   if p.returncode == 0:
                       print("Installed sucessfully al the Pakcages")
                       print(colors.yellow, "Powerboiling Please wait ....")
                       with open("README.md ", 'a') as f:
                            f.write(readme.format(project_name, project_name, "ML Project"))
                       with open("basic_model.py", 'a') as f:
                             f.write(linearRegression)
                       with open("basic_plot.py") as f:
                            f.write(basic_plot)
def main():
    if len(sys.argv) == 1:
        FRAMEWORKS=['Django','Vue','Flutter','React' ,'HTML','Chrome Extension']
        print(colors.blue, '============PowerBoil ========== \n Boiler Plate codes for the following frameworks')
        print(colors.reset)
        for index, frameworks in enumerate(FRAMEWORKS):
            print(f"{index} ) {frameworks}")

     
        choice = int(input("Enter your Choice"))
        print(colors.reset)

        if (choice == 0):
            create_django()
        elif(choice == 1):
            create_vue()
        elif (choice == 2):
            create_flutter()
        elif (choice == 3):
            create_react()
        elif (choice == 4):
            create_html()
        elif (choice == 5):
            create_extension()    
        else:
            print("Invalid Choice")
            sys.exit()                         
    if (sys.argv[1] == 'django'):
        create_django(project_name=sys.argv[2],dir_to_create=os.getcwd())
    elif sys.argv[1] == 'react':
        create_react(project_name=sys.argv[2],dir_to_create=os.getcwd())
    elif sys.argv[1] == 'flutter':
        create_flutter(project_name=sys.argv[2], dir_to_create=os.getcwd())
    elif sys.argv[1] == 'vue':
        create_vue(project_name=sys.argv[2], dir_to_create=os.getcwd())
    elif sys.argv[1] == 'html':
         create_html(project_name=sys.argv[2], dir_to_create=os.getcwd())
    elif sys.argv[1] == 'extension':
        create_extension(project_name=sys.argv[2],dir_to_create=os.getcwd())     
if __name__ == "__main__":
   main()
       


        
