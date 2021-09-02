# Cole seu código aqui
from src.models.ninja_model import Ninja


class Jounin(Ninja):
    ninja_level = "Jounin"

    def __init__(self, name, clan, village, proficiency={"taijutsu": 0, "ninjutsu": 0, "genjutsu": 0}, is_in_mission=False):

        super().__init__(name, clan, village, ninja_level="Jounin", jutsu_list=[
        ], health_pool=100, chakra_pool=100, concious=True)

        self.name = name
        self.clan = clan
        self.village = village
        self.proficiency = proficiency
        self.is_in_mission = is_in_mission

    def list_best_proficiency(self):
        ninjutsu = self.proficiency["ninjutsu"]
        taijutsu = self.proficiency["taijutsu"]
        genjutsu = self.proficiency["genjutsu"]

        if ninjutsu > taijutsu and ninjutsu > genjutsu:
            return f"{self.name} demonstra maior proficiência em ninjutsu"
        elif taijutsu > ninjutsu and taijutsu > genjutsu:
            return f"{self.name} demonstra maior proficiência em taijutsu"
        elif genjutsu > ninjutsu and genjutsu > taijutsu:
            return f"{self.name} demonstra maior proficiência em genjutsu"

    def start_mission(self):
        if self.is_in_mission is True:
            return f"O ninja {self.name} {self.clan} já está em uma missão"
        elif self.is_in_mission is False:
            self.is_in_mission = True
            return f"O ninja {self.name} {self.clan} saiu em missão"

    def return_from_mission(self):
        if self.is_in_mission is True:
            self.is_in_mission = False
            return f"O ninja {self.name} {self.clan} retornou em segurança da missão"
        else:
            return f"O ninja {self.name} {self.clan} não está em nenhuma missão no momento"


kakashi = Jounin("Kakashi", "Hatake", "Konoha")
print(kakashi.ninja_level)
