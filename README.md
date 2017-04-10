# Graph-Theory
A repo containing some of the lecture and labs for this module


## Project specification 
The following document contains the instructions for Project 2017 for Graph Theory. The project will be worth 50% of your mark for this module. You are required to prototype a Neo4j database for use in a timetabling system for GMIT. The database should store information about student groups, classrooms, lecturers, and work hours – just like the current timetabling system in use at GMIT.  

### Minimum Viable Project
The minimum standard for this project is a GitHub repository containing a write-up detailing the design of the database and how it should be used, and an example Neo4j database with this design. The document should clearly state what data needs to be stored in a timetabling system, and how that data is to be represented in your database. This means that you must clearly specify the design choices you have made as to what data are represented as nodes, relationships, labels, relationship types and properties. It should also specify and give examples of Cypher queries for adding, changing, retreiving and deleting data. Your example database should contain data from GMIT.

A better project will be organised, with extensive comments and expla- nations. The architecture of the system will be well conceived, and example queries for optimsing timetables will be provided.

### Submissions
GitHub must be used to manage the development of the software. Your GitHub repository will form the main submission of the project. You must submit the URL of your GitHub repository for this project using the link on the course Moodle page before the deadline. You can do this at any time, as the last commit before the deadline will be used as your submission for this project.  

### Graph Theory Project 2017
Any submission that does not have a full and incremental git history with informative commit messages over the course of the project work will be accorded a proportionate mark. It is expected that your repository will have at least tens of commits, with each commit relating to a reasonably small unit of work. In the last week of term, or at any other time, you may be asked by the lecturer to explain the contents of your git repository. While it is encouraged that students will engage in peer learning, all software that is contained in your submission must have been written by you yourself. You can show this by having a long incremental commit history and by being able to explain your code.

## Project Information 
### Accuiring Data  
Acquiring some for the data for the database such as the rooms in GMIT can be quite a long task if manually typed. I aim to build a webscrape in python that will scrape the page and gather the rooms.

#### Nodes and databse structure
The database will have a structure. similar to the following:

| Name     | Type |  Labels (If applicable) | Properties (if applicable) |
|----------		|------|-------------------------|----------------------------|
| Room     		| Node |                         |                            |
| Lecturer 		| Node |                         |                            |
| Module   		| Node |                         |                            |
| Group/Class   	| Node |                         |                            |
| Course   		| Node |                         |                            |
| Time   			| Node |                         |                            |
