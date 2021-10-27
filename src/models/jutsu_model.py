class Jutsu():
    jutsu_ranks = ("D","C","B","A","S",)

    def __init__(self, jutsu_name, jutsu_type, jutsu_level, jutsu_damage, chakra_spend) -> None:
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_level = self.jutsu_is_ranked(jutsu_level)
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = self.spended_chakra(chakra_spend)


    def jutsu_is_ranked(self, level):
        if not level.upper() in self.jutsu_ranks:
           return 'Unranked'
        else:
           return level.upper()
        
    def spended_chakra(self, spended_chakr):
        if spended_chakr <= 0:
           return 100
        
