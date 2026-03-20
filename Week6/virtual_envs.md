**VIRTUAL ENVIRONMENTS**



***WARNING: I am using venv on short for "virtual environment". Sometimes it might not be the case. So you need to read the whole document probably to know the actual meaning of venv in a 	 particular case.***



A **virtual environment** is an isolated space where we:

* Install the **python packages** needed by our project
* This doesn't affect the system's **global** packages, only for just this project
* A **virtual environment** is a directory, usually created inside the project folder for convenience, but it can exist anywhere.
* Certain projects require certain versions of certain packages. To prevent crashes or conflicts with other projects we create these **venv's**.



**Let’s say:**

Project A **->** needs numpy==1.20

Project B **->** needs numpy==1.26



If you install globally:

**->** One will break.



With virtual environments:

**->** Both work perfectly.



**Steps to create one:**

* We go into our project folder.
* Our project folder is the place where all the files related to our project are saved.
* We go into this project folder using the cd command from the terminal. **Eg.** cd Desktop/Project/
* After that in windows we are going to use: **python -m venv name** -> name is the name you give for your virtual environment



**Activating the Virtual Environment:**

* After creating the **venv** we need to activate it.
* To activate the virtual environment use the command:

&#x09;**1.** From your project folder where the virtual environment is and use the command: **name\_of\_your\_venv\\Scripts\\activate**

&#x09;**2.** Once activated, you can see your **(name\_of\_your\_venv)** before any terminal command.

&#x09;**3.** To deactivate just type deactivate.



**Project Workflow:**

* If you were to share the required project folder with your teammate, you needn't transfer the whole **venv**.
* First use the command, **pip freeze > requirements.txt**
* The above command would create a **requirements.txt** file which contains the python packages along with their versions you had used in your project.
* Now all your teammate has to do is\*\*:\*\*

&#x09;**1.** Create a project folder for himself.

&#x09;**2.** Create a **venv** here in the project folder.

&#x09;**3.** Save the **requirements.txt** file in the project folder.

&#x09;**4.** Navigate to the project folder inside the terminal.

&#x09;**5.** Activate the **venv** he has created.

&#x09;**6.** Use the command **pip install -r requirements.txt**

* So after the 6th step, all the required packages along with their correct versions will be downloaded inside his **virtual environment**.



**Best Practice:**
Do not include the virtual environment folder in version control (e.g., GitHub). Add it to your **.gitignore** file.
