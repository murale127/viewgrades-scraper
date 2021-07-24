# IITM Grades Scraper

An interactive and alternate Command Line visualisation of an IITM student's grades by scraping data from https://www.iitm.ac.in/viewgrades/  
Requires Chrome and can be run on Windows and Linux( also through WSL2)

## Setup

1. Clone the repository onto your system (or download the .zip file and unzip it)
   <pre><code></code></pre>
2. Navigate to the location where you have cloned/downloaded the code on terminal
3. Create virtual environment
   <pre><code>python3 -m venv env</code></pre>
4. Activate virtual environment
   <pre><code>source env/bin/activate</code></pre>
5. To install the neccesary packages
   <pre><code>pip3 install -r requirements.txt</code></pre>
6. To run the code
   <pre><code>python3 PageLogin.py</code></pre>

## Features currently available:

1. Displays your CGPA
2. Accepts a department and give the GPA of the courses offered by that department
3. Plot Credits per stream in bar chart
4. GPA per semester in bar chart
5. Find credits and grade for user input course

# Contribution

Some parts of this code is from [Murale127](https://github.com/murale127/viewgrades-scraper). I have changed the requirement from Firefox to Chrome and added few features from where he stopped.
