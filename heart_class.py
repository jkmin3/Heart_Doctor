# This is my class for my data for patients with heart disease
# I made this so that all types of data can be entered
# There are also simple functions as well

class Heart:
    all_patients = []
    heart_disease = []
    no_heart_disease = []
    male_patients = []
    female_patients = []

    def __init__(self, patient, age, sex, has_disease, chest_pain_type='', resting_bp=0, cholesterol=0, fasting_bs=0,
                 resting_ecg='', max_hr=0, exercise_angina='', old_peak=0, st_slope=''):
        self.patient = patient
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_bp = resting_bp
        self.cholesterol = cholesterol
        self.fasting_bs = fasting_bs
        self.resting_ecg = resting_ecg
        self.max_hr = max_hr
        self.exercise_angina = exercise_angina
        self.old_peak = old_peak
        self.st_slope = st_slope
        self.has_disease = has_disease
        self.all_patients.append(self)
        if self.has_disease == '0':
            self.no_heart_disease.append(self)
        else:
            self.heart_disease.append(self)
        if self.sex == 'M':
            self.male_patients.append(self)
        else:
            self.female_patients.append(self)

    def add_age(self, age):
        self.age += age

    def change_sex(self, sex):
        self.sex = sex

    def change_max_hr(self, max_hr):
        self.max_hr = max_hr

    @staticmethod
    def bar_graph(csv, group, num, title, save):
        import pandas as pd
        df = pd.read_csv(csv)
        pt = df.groupby([group]).mean()
        chart = pt[num].plot(kind='bar', fontsize=8, rot=360, title=title)
        return chart.get_figure().savefig(save)

    @staticmethod
    def scatter(csv, x, y, title, save):
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.read_csv(csv)
        fig, axes = plt.subplots(nrows=1, ncols=1)
        axes.scatter(df[x], df[y])
        axes.set_title(title, fontsize=12)
        plt.xlabel(x)
        plt.ylabel(y)
        return plt.savefig(save)

    @staticmethod
    def chart(csv, chart, x, y, title, color):
        import pandas as pd
        df = pd.read_csv(csv)
        chart.plot(df[x], df[y], label=title, color=color)
        chart.set_title(title, fontsize=12)

    @staticmethod
    def make_histogram(csv, chart, elements):
        import pandas as pd
        df = pd.read_csv(csv)
        low = min(df[elements])
        high = max(df[elements])
        bins = high - low + 1

        chart.hist(df[elements], bins=bins)
        chart.set_title(elements, fontsize=12)

    @classmethod
    def heart_disease_patients(cls):
        return cls.heart_disease

    @classmethod
    def no_heart_disease_patients(cls):
        return cls.no_heart_disease

    @classmethod
    def patients(cls):
        return cls.all_patients

    @classmethod
    def males(cls):
        return cls.male_patients

    @classmethod
    def females(cls):
        return cls.female_patients

    @staticmethod
    def average_num(patients):
        total = 0
        for patient in patients:
            total += float(patient)
        return total / len(patients)

    @staticmethod
    def counter(patients):
        from collections import Counter
        return Counter(patients)
