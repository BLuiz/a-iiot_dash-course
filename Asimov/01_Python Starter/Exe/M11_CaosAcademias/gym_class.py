
class Gym:
    def __init__(self, lighter, heavier):
        self.weight_rack = {value: value for value in range(lighter, heavier+1, 2)}
        self.athletes = list()
    def __str__(self):
        txt = str()
        places = str()
        dumbbells = str()
        for p, d in self.weight_rack.items():
            dumbbells   += f' {d}kg '
            places      += f' [{p}] '
        txt = f"{dumbbells}\n{places}"
        return txt
    def __del__(self): print('O caos destruiu a academia')
    
    def show_athletes(self):
        for athlete_info in self.athletes:
            print(athlete_info)

