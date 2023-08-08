#############################
#CalcBit - calculadora pixel#
#############################
import pyxel

#Padronização dos botões
class Button(object):
    def __init__(self, x:int, y:int, img:int, imgx:int, imgy:int, width:int, height:int, key:None, value:str):
        self.x= x
        self.y= y
        self.img= img
        self.imgx= imgx
        self.imgy= imgy
        self.width= width
        self.height= height
        self.value= value
        self.key= key
        
    def press(self):
        if pyxel.mouse_y > self.y and pyxel.mouse_y < self.y + self.height or pyxel.btnp(self.key):
            if pyxel.mouse_x > self.x and pyxel.mouse_x < self.x + self.width or pyxel.btnp(self.key):
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(self.key):
                    self.img=1
                    return True

        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnr(self.key):
            self.img=0

    def draw(self):
        pyxel.blt(self.x, self.y,self.img, self.imgx, self.imgy, self.width, self.height)

#Calculadora
class Calc:
    def __init__(self):
        #Declarando variaveis
        self.result= ""
        #Numeros
        self.btn0=Button(x=0,y=121,img=0,imgx=0,imgy=96, width=24, height=24, key= pyxel.KEY_KP_0, value= '0')
        self.btn1=Button(x=0,y=97,img=0,imgx=0,imgy=72, width=24, height=24, key= pyxel.KEY_KP_1, value= '1')
        self.btn2=Button(x=24,y=97,img=0,imgx=24,imgy=72, width=24, height=24, key= pyxel.KEY_KP_2, value= '2')
        self.btn3=Button(x=48,y=97,img=0,imgx=48,imgy=72, width=24, height=24, key= pyxel.KEY_KP_3, value= '3')
        self.btn4=Button(x=0,y=73,img=0,imgx=0,imgy=48, width=24, height=24, key= pyxel.KEY_KP_4, value= '4')
        self.btn5=Button(x=24,y=73,img=0,imgx=24,imgy=48, width=24, height=24, key= pyxel.KEY_KP_5, value= '5')
        self.btn6=Button(x=48,y=73,img=0,imgx=48,imgy=48, width=24, height=24, key= pyxel.KEY_KP_6, value= '6')
        self.btn7=Button(x=0,y=49,img=0,imgx=0,imgy=24, width=24, height=24, key= pyxel.KEY_KP_7, value= '7')
        self.btn8=Button(x=24,y=49,img=0,imgx=24,imgy=24, width=24, height=24, key= pyxel.KEY_KP_8, value= '8')
        self.btn9=Button(x=48,y=49,img=0,imgx=48,imgy=24, width=24, height=24, key= pyxel.KEY_KP_9, value= '9')
        #Simbolos/operadores
        self.btnAC=Button(x=72,y=25,img=0,imgx=72,imgy=0, width=24, height=24, key= pyxel.KEY_DELETE, value= '')
        self.btnEqual=Button(x=48,y=121,img=0,imgx=48,imgy=96, width=24, height=24, key= pyxel.KEY_KP_ENTER, value= '')
        self.btnAdd=Button(x=72,y=121,img=0,imgx=72,imgy=96, width=24, height=24, key= pyxel.KEY_KP_PLUS, value= '+')
        self.btnSub=Button(x=72,y=97,img=0,imgx=72,imgy=72, width=24, height=24, key= pyxel.KEY_KP_MINUS, value= '-')
        self.btnMult=Button(x=72,y=73,img=0,imgx=72,imgy=48, width=24, height=24, key= pyxel.KEY_KP_MULTIPLY, value= '*')
        self.btnDiv=Button(x=72,y=49,img=0,imgx=72,imgy=24, width=24, height=24, key= pyxel.KEY_KP_DIVIDE, value= '/')
        self.btnPerc=Button(x=48,y=25,img=0,imgx=48,imgy=0, width=24, height=24, key= pyxel.KEY_PERCENT, value= '%')
        self.btnPoint=Button(x=24,y=121,img=0,imgx=24,imgy=96, width=24, height=24, key= pyxel.KEY_KP_PERIOD , value= '.')
        self.btnParentheses1=Button(x=0,y=25,img=0,imgx=0,imgy=0, width=24, height=24, key= pyxel.KEY_LEFTPAREN, value= '(')
        self.btnParentheses2=Button(x=24,y=25,img=0,imgx=24,imgy=0, width=24, height=24, key= pyxel.KEY_RIGHTPAREN , value= ')')
        #Lista de Botões
        self.btnList=[self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9,
                      self.btnAC, self.btnEqual, self.btnAdd, self.btnSub, self.btnMult, self.btnDiv, self.btnPerc, self.btnPoint, self.btnParentheses1, self.btnParentheses2]
        pyxel.init(96,145, 'CalcBit',quit_key= False)
        pyxel.load('resources/CalcBit.pyxres')
        pyxel.run(self.update, self.draw)
        
    #Método para receber o resultado do calculo inserido
    def getResult(self):
        self.result= eval(self.result)
        
    #Método de verificação de interação a cada quadro
    def update(self):
        for btn in self.btnList:
            if btn.press():
                #Se num1 receber o num maximo
                if len(str(self.result)) < 21:
                    self.result =str(self.result)+str(btn.value)
                #Botão AC
                if btn.key== pyxel.KEY_DELETE:      #if for Butão AC:
                    self.result= ""                 #   apague tudo
                #Botão Igual
                if btn.key== pyxel.KEY_KP_ENTER and len(self.result)!= 0:
                    self.getResult()
        #Botão BACKSPACE
        if pyxel.btnp(pyxel.KEY_BACKSPACE) and len(self.result) > 0:
            self.result= self.result.replace(str(self.result[-1]), "",1)

    #Método para atualização de tela a cada quadro
    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(True)
        #Display da calculadora
        #Tela de saida de dados da calculadora         
        pyxel.rect(5,2,86,20,11)
        pyxel.rectb(5,2,86,20,3)
        pyxel.text(90-len(str(self.result))*4,15,str(self.result),7)
        for btn in self.btnList:
            btn.draw()
        
#verificação da execução direta do módulo
if __name__== "__main__":
    Calc()