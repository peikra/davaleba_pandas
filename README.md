# 📊 Student Score Analysis and Visualization

## 🎯 Project Overview

This project provides a detailed analysis and visualization of student scores across multiple subjects and semesters. Using the **pandas** library for data manipulation and **matplotlib** for generating visualizations, the project helps identify trends in student performance and visualize them effectively.

---

## 🛠️ Features

- **📉 Failed Students Identification**: List students who scored below 50 in any subject.
- **📊 Semester-wise Average Scores**: Calculate and display the average score for each subject across all semesters.
- **🏆 Top Student Finder**: Identify the student with the highest average score across all subjects and semesters.
- **📉 Lowest Subject Performance**: Find the subject with the lowest average score across semesters.
- **📈 Progress Tracker**: Track students who have shown consistent improvement across semesters.
- **📊 Visualizations**: Generate bar charts for each subject and a line plot for overall performance across semesters.

---

## 🏗️ Project Structure
├── main.py # Main execution file ├── students_and_subjects.py # Contains Students_Score class for analysis ├── visualisation.py # Contains Show class for visualizing data ├── student_scores_random_names.csv # Dataset (CSV file) └── README.md # Project documentation

---

## 🧰 Requirements

Make sure to install the following libraries:

- **pandas**: Data manipulation and analysis.
- **matplotlib**: Plotting and visualization.

Install them by running:

```bash
pip install pandas matplotlib
## 🚀 Usage
Clone this repository:
git clone https://github.com/your-username/your-repo-name.git
Navigate to the project directory and ensure the dataset (student_scores_random_names.csv) is in the same directory as main.py.
## 📝 Outputs
Excel Export: The program generates an Excel file (students_scores.xlsx) with average scores for each subject by semester.
Visualizations:
Bar charts for each subject’s average score by semester.
Line plot showing the overall average score across semesters.


