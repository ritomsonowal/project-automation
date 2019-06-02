# project-automation
Automate the steps involved in initialising a new project

## CONFIGURATION:
1. Depending on which shell you are using modify either **~/.bashrc** or **~/.zshrc** file. If you don’t have any idea about this, just go for the **~/.bashrc** file.

2. Add the following line of code to **~/.bashrc**or **~/.zshrc** and save it
```bash
source ~/dev/projects/project-automation/source/.commands.sh
```
3. Edit source/config.py and add your GitHub username to the file and other modify other values as necessary. And you're set to go...

## HOW TO USE:
forge [ project-name ]

Missing *argument* will throw error.

**Example**
```bash
forge Mjolnir
```
## EXTRAS:
If you are using **HTTPS** to add repos you might be asked for credentials as an initial commit is made on initialising the repo.

To avoid this simply go to **init.sh** and change the **HTTPS** link to **SSH** one.
