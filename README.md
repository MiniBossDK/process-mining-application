# Process Mining Application
This is a desktop application made for the software engineering course, [02369 Software Processes and Patterns](https://kurser.dtu.dk/course/02369). 
The desktop application makes use of [PySide6](https://doc.qt.io/qtforpython-6/) for the front-end and uses the [pm4py-dcr](https://github.com/paul-cvp/pm4py-dcr/tree/8ffdc7a3598ac8942d02ecb5802695ea7655eb60) 
as a backend dependency for most of the process mining features.

The goal of this application is to make process mining with pm4py-dcr more accessible for people
without any programming experience. 
## How to set up the project
First clone the project:
```bash
git clone https://github.com/MiniBossDK/process-mining-application.git
```
Due to the project having a dependency on the [pm4py-dcr](https://github.com/paul-cvp/pm4py-dcr/tree/8ffdc7a3598ac8942d02ecb5802695ea7655eb60) 
repository, you will also need to use the following command in the root of the cloned repository:
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

## How to run the program
To run the program, simply type the following command in the root of the project:
```bash
python main.py
```

## How to run tests
To run the cucumber tests run the following command in the root of the
project after the installation of the required packages:
```bash
behave
```