import json


class Research:
    def __init__(self, name, start_cost, rp_multiplier, level, growth_exponent, max_level):
        self.name = name
        self.start_cost = start_cost
        self.rp_multiplier = rp_multiplier
        self.level = level
        self.growth_exponent = growth_exponent
        self.max_level = max_level
        self.amount = start_cost * (growth_exponent ** (level - 1))

    def remove_rp(self, rp_gain):
        self.amount -= rp_gain

    def update_level(self):
        if self.level < self.max_level:
            self.level += 1
            if self.level == self.max_level:
                self.amount = 0

    def update_amount(self):
        self.amount = self.start_cost * \
            (self.growth_exponent ** (self.level - 1))


research = Research("test", 100, 1.1, 1, 1.1, 10)


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


def update_research_level_json(researches, file_path):
    # Update the level of a research in the json file
    with open(file_path, 'w') as f:
        f.write(json.dumps(researches, default=lambda x: x.__dict__))


def update_user_info_json(user_info, file_path):
    # Update the level of a research in the json file
    with open(file_path, 'w') as f:
        f.write(json.dumps(user_info, default=lambda x: x.__dict__))


def main():
    pass


if __name__ == "__main__":
    main()
