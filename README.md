# Docker Flask Example

## About

This is an MIT licensed Flask Application running on docker





## Prerequirements:






## Up And Running:

### 1) Validations:
Inside the CLI (Git bash for example run these commands)

<b>

```bash
docker --help
```
```bash
docker volume --help
```
```bash
docker-compose --help
```
</b>
If you get any error while running any of these commands, then you
need to fix the problem.  
There are some missing software on your device, 
and you need to install them correctly.






### 2) Create a volume called "the_data_base":


Inside the CLI (Git bash for example run these commands)

<b>

```bash
docker volume create the_data_base
```
</b>

Then validate that the **the_data_base** volume has been created, using
this command
<b>

```bash
docker volume ls
```
</b>

A volume called "**the_data_base**" should appear now.






### 3) cd into project directory:

1. Download the the project form github.
2. Open your CLI (Command Line Interface)
3. cd (Change Directory) into the project directory  
	So that you can execute commands here  
	for more info about how to change directory, 
	watch this video on Youtube:<br><a 
	href="https://www.youtube.com/watch?v=oQc-2gsjgDg">
	Youtube: Git Bash, Bash Basics</a>
4. validate that you are in the correct directory using the command  
	<b>
	
	```bash
	ls
	```
	
	</b>
	
	and now should see a list of file and direcories in this folder  
	It should include **app.py**









