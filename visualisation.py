import matplotlib.pyplot as plt
class Show:
    def __init__(self,data1,data2):
        self.data1 = data1
        self.semester = [1,2,3,4,5,6,7,8]
        self.data2 = data2

    def math(self):


        math = self.data1.Math

        plt.bar(math, self.semester)
        plt.title("მათემატიკის საშუალო ქულა ყველა სემესტრში")
        plt.xlabel("საშუალო ქულა")
        plt.ylabel("სემესტრი")

        return plt.show()

    def physic(self):


        physic = self.data1.Physics

        plt.bar(physic, self.semester)
        plt.title("ფიზიკის საშუალო ქულა ყველა სემესტრში")
        plt.xlabel("საშუალო ქულა")
        plt.ylabel("სემესტრი")

        return plt.show()

    def chemistry(self):


        chemistry = self.data1.Chemistry

        plt.bar(chemistry, self.semester)
        plt.title("ქიმიის საშუალო ქულა ყველა სემესტრში")
        plt.xlabel("საშუალო ქულა")
        plt.ylabel("სემესტრი")

        return plt.show()

    def biology(self):


        biology = self.data1.Biology

        plt.bar(biology, self.semester)
        plt.title("ბიოლოგიის საშუალო ქულა ყველა სემესტრში")
        plt.xlabel("საშუალო ქულა")
        plt.ylabel("სემესტრი")

        return plt.show()

    def english(self):


        english = self.data1.English

        plt.bar(english, self.semester)
        plt.title("ინგლისურის საშუალო ქულა ყველა სემესტრში")
        plt.xlabel("საშუალო ქულა")
        plt.ylabel("სემესტრი")

        return plt.show()

    def plot(self):
        plt.plot(self.semester,self.data2.values)
        plt.title("საშუალო ქულა სემესტრების მიხედვით")
        plt.xlabel("სემესტრები")
        plt.ylabel("საშუალო ქულა")

        return plt.show()


