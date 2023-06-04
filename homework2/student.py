from human import Human
class Student(Human):
    def __init__(self, name = "", age =0, height=0.0,group= "", subject= "", grate = 0.0):
        super().__init__(name, age, height)
        self.Group = group
        self.Subject = subject
        self.Grate = grate
    def __str__(self):
        return f"{super().__str__()}\n" \
               f"group: {self.Group}\n" \
               f"subject: {self.Subject}\n" \
               f"grate: {self.Grate}\n"