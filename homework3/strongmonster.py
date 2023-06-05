from monster import Monster
class Monster:
    def __init__(self, name = "", age =0, height=0.0,group= ""):
        super().__init__(name, age, height)
        self.Group = group
    def __str__(self):
        return f"{super().__str__()}\n" \
               f"group: {self.Group}\n" \