## About The Project
<!-- add a screenshot here of the project -->

This project is trying to automate the menial tasks during a competitive programming competition. During a competition, we do not want to have to think about where we are creating our solution files, and we don't want to have to copy our template solution files before we start on solving a problem. 

This project will help you by:
- Creating a directory for every problem during the contest.
-  Copying in your template solution files.
-  Copying in your compilation bash script.
-  Copying the example input test cases.
-  Copying the example output test cases.

## Getting Started
### Setup


First clone the git repository
```bash
git clone https://github.com/AnonymousMorris/codeforce_template_generator.git
```

### Usage
Make a new directory for you competitive programming
```bash
mkdir codeforces
cd codeforces
```
Run init to set up all the directories and structures
```bash
cf init
```
To generate the files for a new contests
```bash
cd contests
cf new codeforces_contest_url
```
To generate the files for a new problem
```bash
cd problems
cf new codeforces_problem_url
```
## Customizing the setup
The template codes are stored in the skeleton directory along with the build bash script and stress testing scripts. 

### To use your own template: 
1. Put your templates into the corresponding location in the skeleton directory.
2. Then edit the config.json to the match the name of the new template code you would like to use. 
