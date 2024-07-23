import pyxel

class Button:
    def __init__(self, x, y, img, imgx, imgy, width, height, key, value):
        self.x = x
        self.y = y
        self.img = img
        self.imgx = imgx
        self.imgy = imgy
        self.width = width
        self.height = height
        self.key = key
        self.value = value

    def press(self):
        """Avalia se o botão foi pressionado."""
        if (pyxel.btnp(self.key) or
            self.y < pyxel.mouse_y < self.y + self.height):
            
            if (pyxel.btnp(self.key) or
                self.x < pyxel.mouse_x < self.x + self.width):
                
                if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or
                    pyxel.btnp(self.key)):
                    self.img = 1
                    return True

        if (pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) or
            pyxel.btnr(self.key)):
            self.img = 0

    def draw(self):
        """Desenha o botão na tela."""
        pyxel.blt(self.x, self.y, self.img, self.imgx, self.imgy, self.width, self.height)

class Calc:
    def __init__(self):
        self.result = ""
        # Numeros
        self.btn0 = Button(0, 121, 0, 0, 96, 24, 24, pyxel.KEY_KP_0, '0')
        self.btn1 = Button(0, 97, 0, 0, 72, 24, 24, pyxel.KEY_KP_1, '1')
        self.btn2 = Button(24, 97, 0, 24, 72, 24, 24, pyxel.KEY_KP_2, '2')
        self.btn3 = Button(48, 97, 0, 48, 72, 24, 24, pyxel.KEY_KP_3, '3')
        self.btn4 = Button(0, 73, 0, 0, 48, 24, 24, pyxel.KEY_KP_4, '4')
        self.btn5 = Button(24, 73, 0, 24, 48, 24, 24, pyxel.KEY_KP_5, '5')
        self.btn6 = Button(48, 73, 0, 48, 48, 24, 24, pyxel.KEY_KP_6, '6')
        self.btn7 = Button(0, 49, 0, 0, 24, 24, 24, pyxel.KEY_KP_7, '7')
        self.btn8 = Button(24, 49, 0, 24, 24, 24, 24, pyxel.KEY_KP_8, '8')
        self.btn9 = Button(48, 49, 0, 48, 24, 24, 24, pyxel.KEY_KP_9, '9')
        
        # Simbolos/operadores
        self.btnAC = Button(72, 25, 0, 72, 0, 24, 24, pyxel.KEY_DELETE, '')
        self.btnEqual = Button(48, 121, 0, 48, 96, 24, 24, pyxel.KEY_KP_ENTER, '')
        self.btnAdd = Button(72, 121, 0, 72, 96, 24, 24, pyxel.KEY_KP_PLUS, '+')
        self.btnSub = Button(72, 97, 0, 72, 72, 24, 24, pyxel.KEY_KP_MINUS, '-')
        self.btnMult = Button(72, 73, 0, 72, 48, 24, 24, pyxel.KEY_KP_MULTIPLY, '*')
        self.btnDiv = Button(72, 49, 0, 72, 24, 24, 24, pyxel.KEY_KP_DIVIDE, '/')
        self.btnPerc = Button(48, 25, 0, 48, 0, 24, 24, pyxel.KEY_PERCENT, '%')
        self.btnPoint = Button(24, 121, 0, 24, 96, 24, 24, pyxel.KEY_KP_PERIOD, '.')
        self.btnParentheses1 = Button(0, 25, 0, 0, 0, 24, 24, pyxel.KEY_LEFTPAREN, '(')
        self.btnParentheses2 = Button(24, 25, 0, 24, 0, 24, 24, pyxel.KEY_RIGHTPAREN, ')')
        
        # Lista de Botões
        self.btnList = [
            self.btn0, self.btn1, self.btn2, self.btn3, self.btn4,
            self.btn5, self.btn6, self.btn7, self.btn8, self.btn9,
            self.btnAC, self.btnEqual, self.btnAdd, self.btnSub,
            self.btnMult, self.btnDiv, self.btnPerc, self.btnPoint,
            self.btnParentheses1, self.btnParentheses2
        ]
        
        pyxel.init(96, 145, 'CalcBit')
        pyxel.load('assets/Calcbit.pyxres')
        pyxel.run(self.update, self.draw)

    def getResult(self):
        """Avalia a expressão matemática no resultado."""
        self.result = eval(self.result)
        
    def update(self):
        """Atualiza a lógica da calculadora."""
        for btn in self.btnList:
            if btn.press():
                if len(str(self.result)) < 21:
                    self.result = str(self.result) + str(btn.value)

                if btn.key == pyxel.KEY_DELETE:
                    self.result = self.result[:-len(self.result)]

                if (btn.key == pyxel.KEY_KP_ENTER and
                        len(self.result) != 0):
                    try:
                        self.getResult()
                    except: 
                        self.result = self.result[:-len(self.result)]

        if (pyxel.btnp(pyxel.KEY_BACKSPACE) and
                len(self.result) > 0):
            self.result = self.result[:-1]

    def draw(self):
        """Desenha a interface do jogo/calculadora."""
        pyxel.cls(0)
        pyxel.mouse(True) 
        pyxel.rect(5, 2, 86, 20, 11)
        pyxel.rectb(5, 2, 86, 20, 3)
        
        TXT_WIDTH = len(str(self.result)) * pyxel.FONT_WIDTH
        pyxel.text(90 - TXT_WIDTH, 15, str(self.result), 7)
        for btn in self.btnList:
            btn.draw()

if __name__ == "__main__":
    Calc()
