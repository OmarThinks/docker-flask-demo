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











