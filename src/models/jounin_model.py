from ninja_model import Ninja

class Jounin(Ninja):
    ninja_level = 'Jounin'

    def __init__(self, name, clan, village, proficiency, is_in_mission=False) -> None:
        super().__init__(name, clan, village)
        self.proficiency = proficiency
        self.is_in_mission = is_in_mission

    
    def list_best_proficiency(self):
        proficiency = max(self.proficiency, key=self.proficiency.get)
        return f'{self.name} demonstra maior proficiência em {proficiency}'


    def start_mission(self):
        if self.is_in_mission:
            return f'O ninja {self.name} {self.clan} já está em uma missão'

        self.is_in_mission = True
        return f'O ninja {self.name} {self.clan} saiu em missão'
        
    
    def return_from_mission(self):
        if not self.is_in_mission:
            return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'
        
        self.is_in_mission = False
        return f'O ninja {self.name} {self.clan} retornou em segurança da missão'