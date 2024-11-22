# Process Mining Application
This is a desktop application made for the software engineering course, 
# How to set up the project
Due to the project having a dependency on the [pm4py-dcr](https://github.com/paul-cvp/pm4py-dcr/tree/8ffdc7a3598ac8942d02ecb5802695ea7655eb60) 
repository, you will need to add the ``--recursive`` option to the clone command to also clone that
submodule:
```bash
git clone https://github.com/MiniBossDK/process-mining-application.git
```
Then, in the root of the cloned repository use the following command:
```bash
git submodule update --init --recursive
```

In the cloned repository, you will also need to create a [python
virtual environment](https://docs.python.org/3/library/venv.html). To create a new
virtual environment for the project you can write the following command in the root of cloned
repository:
```bash
python -m venv processminingapp
```
Then use activate that virtual environment with the following commands:

**For Linux and macOS**
```bash
source processminingapp/bin/activate
```

**For Windows in cmd**

```bash
venv\Scripts\activate.bat
```
**For Windows in PowerShell**
```bash
venv\Scripts\Activate.ps1
```

After the setup and activation of the virtual environment, you will need
to install the required packages for the project. There are both packages required
by this project and the pm4py-dcr project. 

To install the packages required by this project use the following command in the root of the project:
```bash
pip install -r requirements.txt
```
Then, to install the packages required by pm4py-dcr use the following commands in the root of the project:
```bash
cd pm4py-dcr/
pip install .
```
Everything should now be set up, and you will now be able to run the application.

# How to run the program
To run the program, simply type the following command in the root of the project:
```bash
python main.py
```