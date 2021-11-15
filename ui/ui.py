import pygame
from constants import width, height

def translate(value, min1, max1, min2, max2):
    return min2 + (max2-min2)*((value-min1)/(max1-min1))

class Button:
    def __init__(self, text, position = (width-230, 400) , w = 100, h= 50, border=0, color = (0, 0, 0), borderColor = (0, 0, 0)):
        self.text = text
        self.position = position
        self.w = w
        self.h = h
        self.border = border
        self.temp = color
        self.color = color
        self.borderColor = borderColor
        self.font = 'freesansbold.ttf'
        self.fontSize = 25
        self.textColor = (255, 255, 255)
        self.state = False
        self.action = None
        self.clicked = False

    def HandleMouse(self,mouseClicked, HoverColor = (50, 120, 140)):
        m = pygame.mouse.get_pos()
        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                if mouseClicked :
                    self.color = (200, 200, 200)
                    if self.action == None and mouseClicked == True:
                        self.state = not self.state
            else:
                self.color = self.temp
        else:
            self.color = self.temp


    def Render(self, screen, mouseClicked, checker=True):
        if checker:
            self.HandleMouse(mouseClicked)
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        if self.border > 0:
            pygame.draw.rect(screen, self.borderColor, pygame.Rect(self.position[0] - self.border//2, self.position[1] - self.border//2, self.w + self.border, self.h + self.border))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

        screen.blit(text, textRect)

class Panel:
    def __init__(self, position = (width-400, 90), w= 385, h= 800, color=(2, 3, 12), alpha=100):
        self.position = position
        self.w = w
        self.h = h
        self.color = color
        self.alpha = alpha

    def Render(self, screen):
        s = pygame.Surface((self.w, self.h))
        s.set_alpha(self.alpha)
        s.fill(self.color)
        screen.blit(s, (self.position[0], self.position[1]))
        #pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

class ToggleButton:
    def __init__(self, position= ((width-200, 400)), w = 30, h=30, state=False, color=(20, 40, 50), activeColor=(240, 140, 200)):
        self.position = position
        self.w = w
        self.h = h
        self.clicked = False
        self.state = state
        self.temp = (activeColor, color)
        self.activeColor = activeColor
        self.color = color

    def HandleMouse(self, HoverColor = (50, 120, 140)):
        m = pygame.mouse.get_pos()

        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                self.activeColor = HoverColor
                if pygame.mouse.get_pressed()[0]:
                    self.color = (255, 255, 255)
                if self.clicked:
                    self.state = not self.state
            else:
                self.color = self.temp[1]
                self.activeColor =self.temp[0]
        else:
            self.color = self.temp[1]
            self.activeColor =self.temp[0]

    def Render(self, screen, clicked):
        self.HandleMouse()
        self.clicked = clicked
        if self.state == True:
            pygame.draw.rect(screen, self.activeColor, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        return self.state

class TextUI:
    def __init__(self,text, position, fontColor, anchor='center'):
        self.position = position
        self.text = text
        self.font = 'freesansbold.ttf'
        self.anchor = anchor
        self.fontSize = 18
        self.fontColor = fontColor
    def Render(self, screen):
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.fontColor)
        textRect = text.get_rect()
        setattr(textRect, self.anchor, self.position)
        #textRect.center = (self.position[0], self.position[1])
        screen.blit(text, textRect)

class DigitInput:
    def __init__(self,startingValue, position = (width-320, 100), w= 300, h= 600, color=(8, 3, 12)):
        self.position = position
        self.text = str(startingValue)
        self.fontColor = (255, 255, 255)
        self.fontSize = 18
        self.font = 'freesansbold.ttf'
        self.w = w
        self.h = h
        self.color = color
        self.value  = int(self.text)
        self.hoverEnter = False

    def Check(self, backspace,val):

        if self.hoverEnter == True:
            if backspace == True:

                if len(str(self.value)) <= 0 or len(str(self.value))-1 <= 0:
                    self.value = 0
                else:
                    self.value = int(str(self.value)[:-1])

            else:
                if self.text.isdigit():
                    self.value = int(str(self.value) + str(self.text))
                else:
                    for el in self.text:
                        if el.isdigit() != True:
                            self.text = self.text.replace(el, "")
        backspace == False
        self.text = ""

    def updateText(self, val, pressed):
        m = pygame.mouse.get_pos()
        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.hoverEnter = True
                if pressed == True:
                    self.text += val
            else:
                self.hoverEnter = False
                val = ""
        else:
            self.hoverEnter = False
            val = ""


    def Render(self, screen, val, backspace, pressed):
        self.updateText(val, pressed)
        self.Check(backspace, val)
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(str(self.value), True, self.fontColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        screen.blit(text, textRect)

class Slider:
    def __init__(self,x, y, val, min1, max1, length, h, max=500):
        self.value = val
        self.x = x
        self.y = y
        self.h = h
        self.min1 = min1
        self.max1 = max1
        self.length = length
        self.lineColor = (20, 10, 20)
        self.rectradius = 10
        self.temp_radius = self.rectradius
        self.rectColor = (255, 255, 255)
        self.v = 0.2
        self.temp = self.lineColor
        self.max = max

    def Calculate(self, val):
        self.v = translate(val, 0, self.length, 0, 1)
        self.value = self.v * self.max

    def HandleMouse(self):
        mx, my = pygame.mouse.get_pos()

        if mx >= self.x and mx <= self.x + self.length:
            if my >= self.y and my <= self.y + self.h:
                self.rectradius = 15
                if pygame.mouse.get_pressed()[0]:
                    self.Calculate(mx - self.x)
            else:
                self.lineColor = self.temp
                self.rectradius = self.temp_radius
        else:
            self.lineColor = self.temp
            self.rectradius = self.temp_radius

    def Render(self,screen):
        self.HandleMouse()
        pygame.draw.rect(screen, self.lineColor, pygame.Rect(self.x, self.y, self.length, self.h))
        x = int((self.v * self.length) + self.x)
        pygame.draw.rect(screen, self.rectColor, pygame.Rect(self.x, self.y, int( self.v * self.length), self.h))
        pygame.draw.circle(screen, (130, 213, 151), (x, self.y + (self.rectradius//2)), self.rectradius)
        return self.value



## Don't Mind the code below it's an absolute mess 🍝
class DropDownButton:
    def __init__(self, text="Select", position = (width-230, 400) , w = 100, h= 50, children_size=2, border=0, color = (0, 0, 0), borderColor = (0, 0, 0)):
        self.text = text
        self.position = position
        self.w = w
        self.h = h
        self.border = border
        self.temp = color
        self.color = color
        self.children_size = children_size
        self.childs = []
        for i in range(self.children_size):
            button = Button("button " +str(i), (position[0], position[1] + h + h*i+  2), w, h, border, color, borderColor)
            self.childs.append(button)
        self.borderColor = borderColor
        self.font = 'freesansbold.ttf'
        self.fontSize = 25
        self.textColor = (255, 255, 255)
        self.state = False
        self.action = None
        self.selected = False
        self.folded = False
        self.currentIndex = None

    def updateChildren(self, value):
        self.children_size = value
        for i in range(self.children_size):
            button = Button("button " +str(i), (self.position[0], self.position[1] + h + h*i+  2), self.w, self.h, 0, self.border, self.color, self.borderColor)
            self.childs.append(button)

    def HandleMouse(self,mouseClicked, HoverColor = (50, 120, 140)):
        if self.folded == False:
            m = pygame.mouse.get_pos()
            if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
                if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                    self.color = HoverColor
                    if mouseClicked == True:
                        self.folded = not self.folded
                        self.color = (200, 200, 200)
                        if self.action == None and mouseClicked == True:
                            self.state = not self.state
                else:
                    self.color = self.temp
            else:
                self.color = self.temp
        else:
            m = pygame.mouse.get_pos()
            if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
                if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                    self.color = HoverColor
                    if mouseClicked == True:
                        self.folded = not self.folded
                        self.color = (200, 200, 200)
                        if self.action == None and mouseClicked == True:
                            self.state = not self.state
                else:
                    self.color = self.temp
            else:
                self.color = self.temp
            for child in self.childs:
                m = pygame.mouse.get_pos()
                if m[0] >= child.position[0] and m[0] <= child.position[0] + child.w:
                    if m[1] >= child.position[1] and m[1] <= child.position[1] + child.h:
                        child.color = HoverColor
                        if mouseClicked==True:
                            child.color = (200, 200, 200)
                            self.text = child.text
                            self.currentIndex = self.childs.index(child)
                            self.folded = not self.folded
                            if child.action == None and mouseClicked == True:
                                child.state = not child.state
                    else:
                        child.color = child.temp
                else:
                    child.color = child.temp


    def Render(self, screen, mouseClicked, checker = True):
        if checker:
            self.HandleMouse(mouseClicked)
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        if self.border > 0:
            pygame.draw.rect(screen, self.borderColor, pygame.Rect(self.position[0] - self.border//2, self.position[1] - self.border//2, self.w + self.border, self.h + self.border))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

        screen.blit(text, textRect)
        if self.folded == True:
            for child in self.childs:
                child.Render(screen, mouseClicked, False)
