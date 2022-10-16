# chess_colab_2022

A simple chess graphical application collaborate with cohorts

## To run the game

If you have the game installed and the virtual environment activated, then you can run 

```shell
$ python3 -m chess
```

anywhere in your filesystem. If you don't have the game installed, you must ```cd``` to the project directory and run the above command.

## How to set up the development environment using terminal

To set up the development environment from the command line, do the following steps in terminal:

```shell
$ cd ~/path/to/project/chess_colab_2022
$ python -m venv .venv
```

You only need to follow these steps once.

## How to activate your virtual development environment in terminal

Activate your virtual environment with:

- on UNIX-like:
  
```shell
$ source .venv/bin/activate
```

- on Windows

```shell
.venv\Scripts\activate
```	
	
Do this before you start working on or installing the project to make sure only the correct packages are installed.

## To do a temporary editable development install

After you have made a few code changes and you are ready to run your code, run 

```shell
$ pip install --editable .
```

once to do a temporary editable development install. You do not need to rerun this if you edit Python source files. You only need to rerun it if you make changes to the build system.

Now you have access to your package as if it was installed in .venv

## To run unit tests

To run unit tests, simply ensure that the virtual environment is activated and run 

```shell
$ pytest
```

in the root project directory.
