class Jutsu():
    jutsu_ranks = ("D","C","B","A","S",)

    def __init__(self, jutsu_name, jutsu_type, jutsu_level, jutsu_damage, chakra_spend) -> None:
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_level = jutsu_level
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = chakra_spend
        self.jutsu_is_ranked()
        self.spended_chakra()


    def jutsu_is_ranked(self):
        if not self.jutsu_level.upper() in self.jutsu_ranks:
            self.jutsu_level = 'Unranked'
        else:
            self.jutsu_level = self.jutsu_level.upper()
        
    def spended_chakra(self):
        if self.chakra_spend <= 0:
            self.chakra_spend = 100
        
