from tkinter import simpledialog, messagebox
import json
from tracemalloc import start
from turtle import update
import tkinter as tk
from tkinter import simpledialog


class Research:
    def __init__(self, name, start_cost, rp_multiplier, level, growth_exponent, max_level):
        self.name = name
        self.start_cost = start_cost
        self.rp_multiplier = rp_multiplier
        self.level = level
        self.growth_exponent = growth_exponent
        self.max_level = max_level


class UserInfo:

    def __init__(self, tick_speed, tocks, ticks_pr_study, study_multiplier):
        self.tick_speed = tick_speed
        self.tocks = tocks
        self.ticks_pr_study = ticks_pr_study
        self.study_multiplier = study_multiplier


def load_researches_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    researches = []
    # Assuming 'researches' is the key in your JSON file
    for item in data:
        try:
            researches.append(Research(
                item['name'], item['start_cost'], item['rp_multiplier'], item['level'], item['growth_exponent'], item['max_level']))
        except Exception as e:
            print(f"Error creating Research object: {e}")

    return researches


def load_user_info_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    user_info = []
    # Assuming 'researches' is the key in your JSON file
    for item in data['user_info']:
        try:
            user_info.append(UserInfo(
                item['tick_speed'], item['tocks'], item['ticks_pr_study'], item['study_multiplier']))
        except Exception as e:
            print(f"Error creating Research object: {e}")

    return user_info


# Usage
researches = load_researches_from_json(
    'ResearchCalculator/Data/reseaches_pre_ouro.json')

user_info = load_user_info_from_json(
    'ResearchCalculator/Data/user_info.json')

for research in researches:
    print(research.__dict__)
#
# for user_info in user_info:
#    print(user_info.__dict__)

rp_gain = int(input("RP gain: "))


def calculate_research_time(start_cost, growth_exponent, level, tick_speed, tocks, ticks_pr_study, study_multiplier, rp_gain):
    # Calculate the time it takes to complete a research
    # formula = start_cost * (growth_exponent ** (level - 1)) / rp_gain
    study_count_required = start_cost * \
        (growth_exponent ** (level - 1)) / rp_gain

    return (((study_count_required / study_multiplier) * ticks_pr_study) / tocks) * tick_speed


time = calculate_research_time(researches[0].start_cost, researches[0].growth_exponent, researches[0].level,
                               user_info[0].tick_speed, user_info[0].tocks, user_info[0].ticks_pr_study, user_info[0].study_multiplier, rp_gain)
print(f"Time to complete {researches[0].name}: {time} seconds")


def update_research_level_json(researches, file_path):
    # Update the level of a research in the json file
    with open(file_path, 'w') as f:
        f.write(json.dumps(researches, default=lambda x: x.__dict__))


def update_user_info_json(user_info, file_path):
    # Update the level of a research in the json file
    with open(file_path, 'w') as f:
        f.write(json.dumps(user_info, default=lambda x: x.__dict__))


def update_research_level(researches, research_name):
    # Update the level of a research
    for research in researches:
        if research.name == research_name:
            if research.level < research.max_level:
                research.level += 1
                return research

    return None


class UserInfoForm(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Set User Info")

        self.tick_speed_var = tk.StringVar()
        self.tocks_var = tk.StringVar()
        self.ticks_pr_study_var = tk.StringVar()
        self.study_multiplier_var = tk.StringVar()

        tk.Label(self, text="Tick Speed:").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.tick_speed_var).grid(row=0, column=1)

        tk.Label(self, text="Tocks:").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.tocks_var).grid(row=1, column=1)

        tk.Label(self, text="Ticks per Study:").grid(row=2, column=0)
        tk.Entry(self, textvariable=self.ticks_pr_study_var).grid(
            row=2, column=1)

        tk.Label(self, text="Study Multiplier:").grid(row=3, column=0)
        tk.Entry(self, textvariable=self.study_multiplier_var).grid(
            row=3, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(
            row=4, column=0, columnspan=2)

    def submit(self):
        self.result = UserInfo(
            int(self.tick_speed_var.get()),
            int(self.tocks_var.get()),
            int(self.ticks_pr_study_var.get()),
            int(self.study_multiplier_var.get())
        )
        self.destroy()


class ResearchForm(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Add New Research")

        self.name_var = tk.StringVar()
        self.start_cost_var = tk.StringVar()
        self.rp_multiplier_var = tk.StringVar()
        self.level_var = tk.StringVar()
        self.growth_exponent_var = tk.StringVar()
        self.max_level_var = tk.StringVar()

        tk.Label(self, text="Name:").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self, text="Start Cost:").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.start_cost_var).grid(row=1, column=1)

        tk.Label(self, text="RP Multiplier:").grid(row=2, column=0)
        tk.Entry(self, textvariable=self.rp_multiplier_var).grid(
            row=2, column=1)

        tk.Label(self, text="Level:").grid(row=3, column=0)
        tk.Entry(self, textvariable=self.level_var).grid(row=3, column=1)

        tk.Label(self, text="Growth Exponent:").grid(row=4, column=0)
        tk.Entry(self, textvariable=self.growth_exponent_var).grid(
            row=4, column=1)

        tk.Label(self, text="Max Level:").grid(row=5, column=0)
        tk.Entry(self, textvariable=self.max_level_var).grid(row=5, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(
            row=6, column=0, columnspan=2)

    def submit(self):
        self.result = Research(
            self.name_var.get(),
            int(self.start_cost_var.get()),
            int(self.rp_multiplier_var.get()),
            int(self.level_var.get()),
            int(self.growth_exponent_var.get()),
            int(self.max_level_var.get())
        )
        self.destroy()


def main():
    root = tk.Tk()
    root.withdraw()

    user_info_form = UserInfoForm(root)
    root.wait_window(user_info_form)
    user_info = user_info_form.result
    update_user_info_json(
        [user_info], 'ResearchCalculator/Data/user_info.json')

    while True:
        if messagebox.askyesno("Question", "Do you want to add a new research?"):
            research_form = ResearchForm(root)
            root.wait_window(research_form)
            research = research_form.result
            researches = load_researches_from_json(
                'ResearchCalculator/Data/reseaches_pre_ouro.json')
            researches.append(research)
            update_research_level_json(
                researches, 'ResearchCalculator/Data/reseaches_pre_ouro.json')
        else:
            break

    root.mainloop()


if __name__ == "__main__":
    main()
