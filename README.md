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

### Outline 
This project will be a representation of a timetabling system for the GMIT Software development course and some of the Digital Media course also.
The idea of the project is to create a timetabling layout in a Graph Database that can possibly be scaled to include other courses in the college.


My project has 3 aims :

+ Fully represent a timetable system for the Software course.
+ Extend this system to include some of the Digital media course.
+ Attempt to conceive a design that both makes sense and can be scaled to other courses.

### Accuiring Data  
Acquiring some for the data for the database such as the rooms in GMIT can be quite a long task if manually typed. I aim to build a webscrape in python that will scrape the page and gather the rooms.

The webscraping I built acomplishes the task through the use of the lxml library for python.
To do the scrape I downloaded a local copy of the timetable webpage and used lxml to find the list of rooms by the xpath. Once I had this list and stripped all HTML content from it, I began to parse it to extract info into its own columns. 
What I was left with was less than 40 lines and gives an output of a CSV file which I could then load into NEO4j. To see how please visit this [wiki page](https://github.com/FlashGordon95/Graph-Theory/wiki/Acquiring-Data)

#### Nodes and database structure
The database will have a structure. similar to the following:

| Name     | Type |   Properties (if applicable) |
|----------		|------|----------------------------|
| Room     		| Node | roomName; capacity; campus |
| Lecturer 		| Node | lecturer;                           |
| Module   		| Node | module;	course/courses;                           |
| Year   			| Node |     course;           |
| Course   		| Node |  course                       |


#### Wiki User Guide
This repo and its contents is explained a good bit in the Wiki guide.
Here are a few links to get you started.  
  
| Name          | Type     |                           Labels (If applicable)                         |
|---------------|----------|:------------------------------------------------------------------------:|
| What is Neo4j | Internal | [link](https://github.com/FlashGordon95/Graph-Theory/wiki/What-is-Neo4j) |
| Installation  | Interal  | [link](https://github.com/FlashGordon95/Graph-Theory/wiki/Installation)  |
|Creating Nodes  | Interal  | [link](https://github.com/FlashGordon95/Graph-Theory/wiki/Creating-Nodes)  |
| Relationships  | Interal  | [link](https://github.com/FlashGordon95/Graph-Theory/wiki/Relationships)  |
