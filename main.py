import pandas as pd
from students_and_subjects import Students_Score
from visualisation import Show

def main():

    data = pd.read_csv('student_scores_random_names.csv')
    df =pd.DataFrame(data)
    st = Students_Score(df)


    print("სტუდენტები, რომლებიც რომელიმე საგანში ჩაიჭრნენ: ")
    for student in st.failed_students():
        print(student)
    print("-----------------------------------------------")

    print("თითოეული საგნის საშუალო ქულა სემესტრების მიხედვით :")
    print(st.mean_each_semester())
    print("-----------------------------------------------")


    print(st.find_student_with_most_average_score())
    print("-----------------------------------------------")

    print(st.find_subject_with_less_avg_score())
    st.new_dataframe()
    st.progress_in_scores()
    print("-----------------------------------------------")

    print("სტუდენტები, რომლებმაც გააუმჯობესეს ქულები:")
    for student in st.progress_in_scores():
        print(student)

    visual = Show(st.mean_each_semester(),st.average_by_semester())


    visual.math()
    visual.physic()
    visual.chemistry()
    visual.biology()
    visual.english()
    visual.plot()

if __name__ == '__main__':
    main()