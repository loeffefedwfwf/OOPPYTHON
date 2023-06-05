class Monster:
    def __init__(self, name = "", age =0, height=0.0):
        self.Name = name
        self.Age = age
        self.Height = height
    def __str__(self):
        return f"name: {self.Name}\n" \
               f"age: {self.Age}\n" \
               f"height: {self.Height}"
