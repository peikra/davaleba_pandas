import pandas as pd



class Students_Score:
    def __init__(self,data):
        self.data = data


    def failed_students(self):
        failed_students = self.data[(self.data['Math']<50) |
                      (self.data['Physics'] < 50) |
                      (self.data['Chemistry'] < 50) |
                      (self.data['Biology']<50) |
                      (self.data['English'] < 50)
        ]
        failed_students_list = failed_students['Student'].unique()

        return failed_students_list

    def mean_each_semester(self):
        average = self.data.groupby('Semester')[['Math','Physics','Chemistry','Biology','English']].mean()

        return average

    def find_student_with_most_average_score(self):
        self.data['average'] = self.data[['Math','Physics','Chemistry','Biology','English']].mean(axis=1)
        student_average = self.data.groupby('Student')['average'].mean()

        max_score = student_average.max()
        top = student_average[student_average==max_score]


        return f"ყველა სემესტრსა და საგანში ყველაზე მაღალი საშუალო ქულა აქვს: {top}"
    def find_subject_with_less_avg_score(self):
        average = self.data.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
        l = average.min()
        subject = l.idxmin()
        return f"ყველაზე დაბალი საშუალო ქულა არის: {l.min()}, საგანი:{subject}"

    def new_dataframe(self):
        data = self.mean_each_semester().reset_index(drop=True)
        data.index = data.index + 1
        pd.DataFrame(data)


        return data.to_excel('students_scores.xlsx')

    def progress_in_scores(self):

        average_scores = self.data.groupby(['Semester','Student'])[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean().reset_index()
        average_scores['Overall Average'] = average_scores[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
        pivot = average_scores.pivot(index = 'Student', columns= 'Semester', values= 'Overall Average' )

        progressed_students = []
        for student in pivot.index:
            scores = pivot.loc[student].dropna()
            if all(scores[i] < scores[j] for i,j in zip(scores.index[:-1],scores.index[1:])):
                progressed_students.append(student)

        return progressed_students

    def average_by_semester(self):
        average = self.data.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
        average['overall average'] = average.mean(axis=1)

        return average['overall average']












