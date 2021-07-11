# CREATING A VIRTUAL ENVIRONMENT

First we need to install the "pipenv" library:

```shell
pip install pipenv
```

Code to create a virtual environment (After moving to the directory where we need to create the virtual environment):

```shell
virtualenv .
```

Code to activate the virtual environment (Windows : command prompt):

```shell
.\Scripts\activate
```

In GitBash (for Windows):

```shell
source ./Scripts/activate
```

To see packages installed in the virtual environment, execute :

```shell
pip freeze
```

Quitting a virtual environment
