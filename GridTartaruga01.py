
# coding: utf-8

# <h1> Grid da tartaruga
# 

# In[1]:


import pygame
clock = pygame.time.Clock()


# In[2]:


class Coisa:
    
    def __init__(self,estado = None):
        self.estado = estado
        
    def __repr__(self):
        #representação do objeto na forma de string
        return '<{}>'.format(getattr(self, '__name__',self.__class__.__name__))
    
    def mostraEstado(self):
        return str(self.estado)
    
    def vivo(self):
        return hasattr(self, 'vivo') and self.vivo
    


# In[3]:


class Agente(Coisa):
    
    def __init__(self,estado = None, funcaoAgente = None):
        super().__init__(estado)
        if funcaoAgente == None:
            def funcaoAgente(*entradas):
                return "Ação Default"
        self.funcaoAgente = funcaoAgente
        self.historicoPercepcoes = []
        self.x = 2*128
        self.y = 3*128
        
    def percepcao(self):
        entrada = input("Entre com dados ")# percepções
        self.historicoPercepcoes.append(eval(entrada))
            
    def movimentacao(self,px,py):
        print (px,py)
        self.x = px*128
        self.y = py*128
        
    def saida(self):
        return self.funcaoAgente(self.historicoPercepcoes)


# In[4]:


class Tartaruga(Agente):
    def __init__(self,estadoInicial = None, funcaoAgente = None):
        super().__init__(estadoInicial,funcaoAgente)
        self.img = pygame.image.load('Tartaruga.png')

        


# In[5]:


class bloco(Coisa):
    def __init__(self,estado = None,px = 0, py = 0):
        super().__init__(estado)
        self.img = pygame.Surface([128,128])
        self.img.fill((0,0,255))
        self.x = px*128
        self.y = py*128
    
          
        
    


# In[6]:


class Minhoca(Coisa):
    def __init__(self,estado = None,px = 0, py = 0):
        super().__init__(estado)
        self.img = pygame.image.load('Minhoca.png')
        self.x = px*128
        self.y = py*128


# In[7]:


class Ambiente:
    
    def __init__(self,estadoInicial = None):
        self.estado = estadoInicial
        self.objetosNoAmbiente = []
        self.agentes = []
        
    def percepcao(self,agente):
        # Define as percepções do agente
        return None
    
    def adicionaAgente(self,agente):
        self.agentes.append(agente)
        
    def adicionaObjeto(self,obj):
        self.objetosNoAmbiente.append(obj)
        
        


# In[8]:


class ReinoAnimal(Ambiente):
    def __init__(self,estadoInicial):
        super().__init__(estadoInicial)
        pygame.init()
        self.tempo=0
        self.fim = False

    def executaAmbiente(self):
        self.tela = pygame.display.set_mode((768,640),0,8)
        pygame.display.set_caption('Grid da Tartaruga')
        self.aux = 0                
        pygame.display.update()#AT elementos no display
        while not self.fim:
            self.aux +=1
            self.planoDeFundo()
            for i in range(len(self.objetosNoAmbiente)):
                self.tela.blit(self.objetosNoAmbiente[i].img,(self.objetosNoAmbiente[i].x, self.objetosNoAmbiente[i].y))
            self.tela.blit(self.agentes[0].img,(self.agentes[0].x, self.agentes[0].y))
            if self.aux== 100:
                self.aux=0
                if self.tempo <3:

                    self.px,self.py = self.agentes[0].funcaoAgente(self.tempo)
                    self.agentes[0].movimentacao(self.px,self.py)

                    self.tempo+=1
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fim = True
            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()
                    
                    
    def planoDeFundo(self):
        self.tela.fill((250,250,250))
        for x in range(0,768,128):
            pygame.draw.line(self.tela, (255,0,0), (x,0), (x,640))
        for y in range(0,640,128):
            pygame.draw.line(self.tela, (255,0,0), (0,y), (768,y))
            

        
        

  


# In[9]:


def deslocamendoParaExibi(t):
    #fucao criada somente para simular a saida de coordenadas para um deslocamento
    if t <3 :
        Coordenadas = [[2,2],[2,1],[1,1]]
        return Coordenadas[t][0], Coordenadas[t][1]


# In[10]:


a = ReinoAnimal([])


# In[11]:


t = Tartaruga([],deslocamendoParaExibi)


# In[12]:


a.adicionaAgente(t)


# In[13]:


b1 = bloco(0,4,2)


# In[14]:


b2 = bloco(0,4,3)


# In[15]:


m = Minhoca(0,5,2)


# In[16]:


a.adicionaObjeto(b1)


# In[17]:


a.adicionaObjeto(b2)


# In[18]:


a.adicionaObjeto(m)


# In[19]:


a.executaAmbiente()

