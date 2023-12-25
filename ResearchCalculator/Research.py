import json


class Research:
    def __init__(self, name, start_cost, rp_multiplier, level, growth_exponent, max_level):
        self.name = name
        self.start_cost = start_cost
        self.rp_multiplier = rp_multiplier
        self.level = level
        self.growth_exponent = growth_exponent
        self.max_level = max_level

    def update_level(self):
        self.level += 1

    def calculate_actual_cost(self):
        return self.start_cost * (self.growth_exponent ** (self.level - 1))

    def calculate_static_research_time(self, user_info, rp_gain):
        # Calculate the time it takes to complete a research
        # formula = start_cost * (growth_exponent ** (level - 1)) / rp_gain
        study_count_required = self.start_cost * \
            (self.growth_exponent ** (self.level - 1)) / rp_gain

        return (((study_count_required / user_info.studies_pr_study) * user_info.ticks_pr_study) / user_info.tocks) * user_info.tick_speed

    def calculate_dynamic_research_time(self, user_info, rp_gain):
        rp_gained = 0
        tick = 0
        while rp_gained < self.calculate_actual_cost():
            rp_gained += rp_gain
            tick += 1
        return tick * user_info.tick_speed


class UserInfo:

    def __init__(self, tick_speed, tocks, ticks_pr_study, studies_pr_study):
        self.tick_speed = tick_speed
        self.tocks = tocks
        self.ticks_pr_study = ticks_pr_study
        self.studies_pr_study = studies_pr_study


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
    for item in data:
        try:
            user_info.append(UserInfo(
                item['tick_speed'], item['tocks'], item['ticks_pr_study'], item['studies_pr_study']))
        except Exception as e:
            print(f"Error creating Research object: {e}")

    return user_info


# Usage
researches = load_researches_from_json(
    'ResearchCalculator/Data/reseaches_pre_ouro.json')

user_info = load_user_info_from_json(
    'ResearchCalculator/Data/user_info.json')

rp_gain = int(input("RP gain: "))

time = researches[0].calculate_research_time(user_info[0], rp_gain)
print(f"Time to complete {researches[0].name}: {time} seconds")


def update_research_level_json(researches, file_path):
    # Update the level of a research in the json file
    with open(file_path, 'w') as f:
        f.write(json.dumps(researches, default=lambda x: x.__dict__))


def update_user_info_json(user_info, file_path):
    # Update the level of a research in the json file
    with open(file_path, 'w') as f:
        f.write(json.dumps(user_info, default=lambda x: x.__dict__))
