from random import choice

id_count = -1

class Athlete():
    def __init__(self, name):
        global id_count
        id_count += 1   # Auto increment ID
        self.id = id_count
        self.name = name
        self.dumbbell = 0
        self.practicing = False

    def __str__(self):
        cor = '\033[32;m' if self.practicing else '\033[36;m'
        id = f'0{self.id}' if 0 <= self.id < 10 else f'{self.id}'
        return f'{cor}{id} - {self.name:<21}| Carga: {self.dumbbell}kgs \033[38;m'
    

    def practice(self, weight_rack):
        """
        Função para pegar o halter do rack e começar o exercício.

        :param weight_rack: dicionário com os halteres enumerados
        """
        avlb_dmbl = [place for place, dumbbell in weight_rack.items() if dumbbell>0]
        if not avlb_dmbl:
            print('Exercício cancelado. Nenhum peso disponível')
            return 0

        place_chosen = choice(avlb_dmbl)
        self.dumbbell = weight_rack[place_chosen]
        weight_rack[place_chosen] = 0
        self.practicing = True

        print(f'{self.name:<20} pegou o halter {self.dumbbell}kgs [{place_chosen}]')    ###
        return 1


class Reactive(Athlete):
    def __init__(self, name): Athlete.__init__(self, name)
    def rest(self, weight_rack):
        """
        Função para guardar o halter no rack, de maneira desorganizada, e terminar o exercício.

        :param weight_rack: dicionário com os halteres enumerados
        """
        avlb_place = [place for place, dumbbell in weight_rack.items() if dumbbell == 0]
        
        if not avlb_place:
            print('Descanso cancelado. Nenhum lugar disponível no rack')
            return 0
        
        place_chosen = choice(avlb_place)
        weight_rack[place_chosen] = self.dumbbell
        self.dumbbell = 0
        self.practicing = False

        print(f'{self.name:<20} devolveu o halter {weight_rack[place_chosen]}kgs [{place_chosen}]')    ###
        return 1


class Proactive(Athlete):
    def __init__(self, name): Athlete.__init__(self, name)
    def rest(self, weight_rack):
        """
        Função para guardar o halter no rack, de maneira organizada, e terminar o exercício.

        :param weight_rack: dicionário com os halteres enumerados
        """
        avlb_place = [place for place, dumbbell in weight_rack.items() if dumbbell == 0]
        
        if not avlb_place:
            print('Descanso cancelado. Nenhum lugar disponível no rack')
            return 0
        elif weight_rack[self.dumbbell] == 0: place_chosen = self.dumbbell
        else: place_chosen = choice(avlb_place)
        
        weight_rack[place_chosen] = self.dumbbell
        self.dumbbell = 0
        self.practicing = False

        print(f'{self.name:<20} devolveu o halter {weight_rack[place_chosen]}kgs [{place_chosen}]')    ###
        return 1

