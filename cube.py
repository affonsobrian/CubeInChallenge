from enum import Enum

class Color(Enum):
    BLUE = "B"
    RED = "R"
    GREEN = "G"
    ORANGE = "O"
    YELLOW = "Y"
    WHITE = "W"

class Cube:
    
    def __init__(self):
        self.vector = []
        self._commands = {
            "R": self.R_C,
            "R'": self.R_AC,
            "L": self.L_C,
            "L'": self.L_AC,
            "U": self.U_C,
            "U'": self.U_AC,
            "D": self.D_C,
            "D'": self.D_AC,
            "F": self.F_C,
            "F'": self.F_AC,
            "B": self.B_C,
            "B'": self.B_AC        
        }
        self.set_cube_solved()

    def __str__(self):
        v = self.vector
        saida = ( 
        f"\n      |{v[36]} {v[37]} {v[38]}|\n"
        f"      |{v[39]} {v[40]} {v[41]}|\n"
        f"      |{v[42]} {v[43]} {v[44]}|\n"
        f"|{v[0]} {v[1]} {v[2]}|{v[9]} {v[10]} {v[11]}|{v[18]} {v[19]} {v[20]}|{v[27]} {v[28]} {v[29]}|\n"
        f"|{v[3]} {v[4]} {v[5]}|{v[12]} {v[13]} {v[14]}|{v[21]} {v[22]} {v[23]}|{v[30]} {v[31]} {v[32]}|\n"
        f"|{v[6]} {v[7]} {v[8]}|{v[15]} {v[16]} {v[17]}|{v[24]} {v[25]} {v[26]}|{v[33]} {v[34]} {v[35]}|\n"
        f"      |{v[45]} {v[46]} {v[47]}|\n"
        f"      |{v[48]} {v[49]} {v[50]}|\n"
        f"      |{v[51]} {v[52]} {v[53]}|\n")
        return saida

    def set_cube_solved(self):
        self.vector += [Color.BLUE.value for i in range(9)]
        self.vector += [Color.RED.value for i in range(9)]
        self.vector += [Color.GREEN.value for i in range(9)]
        self.vector += [Color.ORANGE.value for i in range(9)]
        self.vector += [Color.YELLOW.value for i in range(9)]
        self.vector += [Color.WHITE.value for i in range(9)]

        self.vector = [i for i in range(54)]

    def execute_commands(self, entry):
        entry_list = entry.split(' ')
        for value in entry_list:
            self._commands[value]()

    # direita horario
    def R_C(self):    
        # laterais
        aux = self.vector[17], self.vector[14], self.vector[11], self.vector[44], self.vector[41], self.vector[38], self.vector[27], self.vector[30], self.vector[33], self.vector[53], self.vector[50], self.vector[47] 
        self.vector[44], self.vector[41], self.vector[38], self.vector[27], self.vector[30], self.vector[33], self.vector[53], self.vector[50], self.vector[47], self.vector[17], self.vector[14], self.vector[11] = aux
        # eixo
        aux = self.vector[15], self.vector[12], self.vector[9], self.vector[10], self.vector[11], self.vector[14], self.vector[17], self.vector[16]
        self.vector[9], self.vector[10], self.vector[11], self.vector[14], self.vector[17], self.vector[16], self.vector[15], self.vector[12] = aux

    # direita anti-horario
    def R_AC(self):
        for i in range(3):
            self.R_C()

    # esquerda anti-horario
    def L_AC(self):    
        # laterais
        aux = self.vector[6], self.vector[3], self.vector[0], self.vector[36], self.vector[37], self.vector[38], self.vector[20], self.vector[23], self.vector[26], self.vector[53], self.vector[52], self.vector[51] 
        self.vector[36], self.vector[37], self.vector[38], self.vector[20], self.vector[23], self.vector[26], self.vector[53], self.vector[52], self.vector[51], self.vector[6], self.vector[3], self.vector[0] = aux
        # eixo
        aux = self.vector[33], self.vector[34], self.vector[35], self.vector[32], self.vector[29], self.vector[28], self.vector[27], self.vector[30]
        self.vector[35], self.vector[32], self.vector[29], self.vector[28], self.vector[27], self.vector[30], self.vector[33], self.vector[34]  = aux

    # esquerda horario
    def L_C(self):
        for i in range(3):
            self.L_AC()

    # topo horario
    def U_C(self):
        # laterais
        aux = self.vector[2], self.vector[1], self.vector[0], self.vector[29], self.vector[28], self.vector[27], self.vector[20], self.vector[19], self.vector[18], self.vector[11], self.vector[10], self.vector[9]
        self.vector[29], self.vector[28], self.vector[27], self.vector[20], self.vector[19], self.vector[18], self.vector[11], self.vector[10], self.vector[9], self.vector[2], self.vector[1], self.vector[0] = aux
        # eixo
        aux = self.vector[42], self.vector[39], self.vector[36], self.vector[37], self.vector[38], self.vector[41], self.vector[44], self.vector[43]
        self.vector[36], self.vector[37], self.vector[38], self.vector[41], self.vector[44], self.vector[43], self.vector[42], self.vector[39] = aux

    # topo anti-horario
    def U_AC(self):
        for i in range(3):
            self.U_C()

    def D_AC(self):
        for i in range(3):
            self.D_C()

    def D_C(self):
        # laterais
        aux = self.vector[6], self.vector[7], self.vector[8], self.vector[15], self.vector[16], self.vector[17], self.vector[24], self.vector[25], self.vector[26], self.vector[33], self.vector[34], self.vector[35]
        self.vector[15], self.vector[16], self.vector[17], self.vector[24], self.vector[25], self.vector[26], self.vector[33], self.vector[34], self.vector[35], self.vector[6], self.vector[7], self.vector[8] = aux 
        # eixo
        aux = self.vector[45], self.vector[48], self.vector[51], self.vector[52], self.vector[53], self.vector[50], self.vector[47], self.vector[46]
        self.vector[47], self.vector[46], self.vector[45], self.vector[48], self.vector[51], self.vector[52], self.vector[53], self.vector[50] = aux


    def F_C(self):
        # laterais
        aux = self.vector[36], self.vector[39], self.vector[42], self.vector[9], self.vector[12], self.vector[15], self.vector[45], self.vector[48], self.vector[51], self.vector[29], self.vector[32], self.vector[35]
        self.vector[9], self.vector[12], self.vector[15], self.vector[45], self.vector[48], self.vector[51], self.vector[29], self.vector[32], self.vector[35], self.vector[36], self.vector[39], self.vector[42] = aux 
        # eixo
        aux = self.vector[0], self.vector[1], self.vector[2], self.vector[5], self.vector[8], self.vector[7], self.vector[6], self.vector[3]
        self.vector[2], self.vector[5], self.vector[8], self.vector[7], self.vector[6], self.vector[3], self.vector[0], self.vector[1] = aux 

    def F_AC(self):
        for i in range(3):
            self.F_C()
    
    def B_C(self):
        return None
    
    def B_AC(self):
        return None

c = Cube()
print(c)
c.execute_commands("B")
print(c)
