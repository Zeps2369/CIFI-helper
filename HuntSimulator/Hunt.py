import math
import random


class enemy:
    def __init__(self):
        self.name = "Enemy"
        self.maxHp = 0
        self.hp = self.maxHp
        self.atk = 0
        self.hpRegen = 0
        self.critChance = 0
        self.critDmg = 0
        self.atkSpeed = 0
        self.dmgReduction = 0
        self.evadeChance = 0

    class hound:
        def __init__(self):
            self.name = "Hound"
            self.maxHp = 9
            self.hp = self.maxHp
            self.atk = 2.5
            self.hpRegen = 0.08
            self.critChance = 0.0322
            self.critDmg = 1.21
            self.atkSpeed = 4.53
            self.dmgReduction = 1
            self.evadeChance = 0

        def stageUpdate(self, stage):
            self.maxHp += 4*stage
            self.atk += 0.7*stage
            self.hpRegen = 0.08*stage-1
            self.critChance += 0.0004*stage
            self.critDmg += 0.008*stage
            self.atkSpeed -= 0.006*stage

        def enemyAtk(self):
            rand = random.random()
            if rand <= self.critChance:
                return self.atk + self.critDmg * self.atk
            else:
                return self.atk

    class drone:
        def __init__(self):
            self.name = "Drone"
            self.maxHp = 12
            self.atk = 2.5
            self.hpRegen = 0.1
            self.critChance = 1.5
            self.critDmg = 1.5
            self.attSpeed = 2
            self.dmgReduction = 1
            self.evadeChance = 0


class hunter:
    class borge:
        def __init__(self):
            self.name = "Borge"
            self.maxHp = 749
            self.hp = self.maxHp
            self.atk = 96.05
            self.hpRegen = 3.90
            self.critChance = 0.152
            self.critDmg = 1.62
            self.atkSpeed = 4.29
            self.dmgReduction = 0.4293
            self.evadeChance = 0.1052
            self.effectChance = 0.25
            self.lifeSteal = 0
            self.lootMultiplier = 1
            self.missingHpRegen = 0
            self.cleave = True

        def hunterAtk(self):
            rand = random.random()
            if rand <= self.critChance:
                return self.atk + self.critDmg * self.atk
            else:
                return self.atk

    class ozzy:
        def __init__(self):
            self.name = "Ozzy"
            self.maxHp = 12
            self.atk = 2.5
            self.hpRegen = 0.1
            self.critChance = 1.5
            self.critDmg = 1.5
            self.attSpeed = 2
            self.dmgReduction = 1
            self.evadeChance = 0


class borgeTalents:
    class attributes:
        class soulOfAres:
            def __init__(self):
                self.name = "Soul of Ares"
                self.level = 0
                self.maxLevel = 999
                self.hpMultiplier = 1.01
                self.atkMultiplier = 1.002
                self.lvlCost = 1

        class essenceOfYlith:
            def __init__(self):
                self.name = "Essence of Ylith"
                self.level = 0
                self.maxLevel = 999
                self.hpRegenMultiplier = 1.0075
                self.hpRegenAddition = 0.03
                self.lvlCost = 1

        class spartanLineage:
            def __init__(self):
                self.name = "Spartan Lineage"
                self.level = 0
                self.maxLevel = 5
                self.dmgReductionMultiplier = 1.015
                self.lvlCost = 2

        class timelessMastery:
            def __init__(self):
                self.name = "Timeless Mastery"
                self.level = 0
                self.maxLevel = 5
                self.lootMultiplier = 1.14
                self.lvlCost = 3

        class bookOfBaal:
            def __init__(self):
                self.name = "Book of Baal"
                self.level = 0
                self.maxLevel = 6
                self.lifeSteal = 0.011
                self.lvlCost = 3

        class superiorSensors:
            def __init__(self):
                self.name = "Superior Sensors"
                self.level = 0
                self.maxLevel = 5
                self.evadeChance = 0.016
                self.effectChance = 0.012
                self.lvlCost = 2

        class helltouchBarrier:
            def __init__(self):
                self.name = "Helltouch Barrier"
                self.level = 0
                self.maxLevel = 10
                self.dmgReflect = 0.08
                self.lvlCost = 2

        class lifedrainInhaler:
            def __init__(self):
                self.name = "Lifedrain Inhaler"
                self.level = 0
                self.maxLevel = 10
                self.missingHpRgn = 0.008
                self.lvlCost = 3

        class explosivePunches:
            def __init__(self):
                self.name = "Explosive Punches"
                self.level = 0
                self.maxLevel = 5
                self.critChance = 0.044
                self.critDmg = 0.008
                self.lvlCost = 3


# TODO make enemies a variable instead of a class


if __name__ == "__main__":
    pass
