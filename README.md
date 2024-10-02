Student Score Analysis and Visualization
Project Overview
This project is designed to analyze and visualize student scores across multiple subjects and semesters. It reads the dataset of student scores from a CSV file, processes the data using the pandas library, and generates visualizations with matplotlib.

Features
Failed Students Identification: Identifies students who scored below 50 in any subject.
Semester-wise Average Scores: Calculates and displays the average scores for each subject across different semesters.
Top Student Finder: Finds the student with the highest average score across all semesters.
Lowest Subject Performance: Identifies the subject with the lowest average score.
Progress Tracker: Tracks and lists students who have improved their scores consistently across semesters.
Visualizations: Generates bar charts for each subject's average score and a line plot showing the overall average score across semesters.
Project Structure
main.py: The main execution file, which reads the CSV file and runs the analysis using Students_Score class and visualizations using Show class.
students_and_subjects.py: Contains the Students_Score class that handles data analysis.
visualisation.py: Contains the Show class that generates visualizations for individual subjects and overall performance.
Dependencies
pandas: For data manipulation and analysis.
matplotlib: For creating visualizations.
Installation
Clone the repository.
Install the required libraries:
pip install pandas matplotlib
Ensure that the dataset (student_scores_random_names.csv) is in the same directory as main.py.
Usage
Run the main.py file to execute the analysis and view results:
python main.py
The program will print the results of various analyses, such as failed students and average scores by semester, and will also display the visualizations in separate windows.
Output
The program will generate an Excel file (students_scores.xlsx) containing the average scores for each subject by semester.
Visualizations include:
Bar charts for each subject’s average score by semester.
A line plot showing the overall average score across semesters.
