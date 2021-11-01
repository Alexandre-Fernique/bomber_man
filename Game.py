# -*- coding: cp1252 -*-
import pygame._view
import pygame
import random
pygame.init()
choix=[
["1xxxxxxxxxxxxxx",
"xjj    m    jjx",
"xjxmx xmx xmxjx",
"x mmm mmm mmm x",
"x xmx xmx xmx x",
"x      m      x",
"x xmx xmx xmx x",
"xmmmmmmmmmmmmmx",
"x xmx xmx xmx x",
"x      m      x",
"x xmx xmx xmx x",
"x mmm mmm mmm x",
"xjxmx xmx xmxjx",
"xjj    m    jjx",
"xxxxxxxxxxxxxxx"],
["2xxxxxxxxxxxxxx",
"xjj    m    jjx",
"xjx x xmx x xjx",
"x  mmmmmmmmm  x",
"x xox xmx xmx x",
"x  m   m   m  x",
"x xmx xmx xmx x",
"xmmmmmmmmmmmmmx",
"x xmx xmx xmx x",
"x  m   m   m  x",
"x xmx xmx xmx x",
"x  mmmmmmmmm  x",
"xjx x xmx x xjx",
"xjj    m    jjx",
"xxxxxxxxxxxxxxx"],
["3xxxxxxxxxxxxxx",
"xjj         jjx",
"xjx x x x x xjx",
"x             x",
"x x x x x x x x",
"x             x",
"x x x x x x x x",
"x             x",
"x x x x x x x x",
"x             x",
"x x x x x x x x",
"x             x",
"xjx x x x x xjx",
"xjj         jjx",
"xxxxxxxxxxxxxxx"]]
liste_gene=["4xxxxxxxxxxxxxx",
"xjj         jjx",
"xjx x x x x xjx",
"x             x",
"x x x x x x x x",
"x             x",
"x x x x x x x x",
"x             x",
"x x x x x x x x",
"x             x",
"x x x x x x x x",
"x             x",
"xjx x x x x xjx",
"xjj         jjx",
"xxxxxxxxxxxxxxx"]
def generer_liste(liste):
##    Fonction prenant en paramètre une liste qui retourne une liste avec des
##    lettres o génerer aléatoirement à la place des espaces 
    new_list=[]
    chaine=""
    for ligne in liste:
        if chaine!="":
            new_list.append(chaine)
        chaine=""
        for lettre in ligne:
            if lettre==" ":
                if 1==random.randint(0,1):
                    chaine+="m"
                else:
                    chaine+=" "
            elif lettre=="4":
                chaine+="4"
            elif lettre!=" ":
                chaine+="x"
    return new_list
choix.append(generer_liste(liste_gene))
def generer(liste,mur_list=pygame.sprite.Group(),Coord=54):
##    Fonction prenant en paramètre une liste, créant une liste d'objet contenant murs
##    en fonction de la liste et la retournant
    x=-1
    y=-1
    for ligne in liste:
        x=-1
        y+=1
        for valeur in ligne:
            x+=1
            if valeur=="m":
                mur_list.add(mur(x*Coord,y*Coord))
    print('Génération du monde réussi niveau '+liste[0][0])
    return mur_list

def gagner(name="",image=""):
##    Fonction affichant les paramatres entrer (une image, un texte)
    screen.blit(image,(300,200))
    Surf_texte=font.render(name+" a gagner!",1,(0,0,0))
    screen.blit(Surf_texte,(400,250))
    
class mur(pygame.sprite.Sprite):
##    Class des murs destructibles
    def __init__(self,posX,posY):
        super(mur,self).__init__()
        self.image=pygame.image.load("Images/Images Divers/blocindu.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
    def update(self,bonus_list=pygame.sprite.Group()):
##        création de bonus
        if random.randint(0,1)==1:
            bonus_list.add(bonus(self.rect.x,self.rect.y,random.randint(1,3)))
class bonus(pygame.sprite.Sprite):
##    Class des Bonus
    def __init__(self,posX,posY,valeur):
        super(bonus,self).__init__()
        if valeur==3:
            self.valeur="MaxBombe"
            self.image=pygame.image.load("Images/Images Divers/Maxbombe.png").convert_alpha()
            self.rect=self.image.get_rect()
        elif valeur==1:
            self.valeur="Range"
            self.image=pygame.image.load("Images/Images Divers/Explosionbonus.png").convert_alpha()
            self.rect=self.image.get_rect()
        else:
            self.valeur="vitesse"
            self.image=pygame.image.load("Images/Images Divers/Vitessebonus.png").convert_alpha()
            self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
    def update(self,perso_list,bonus_list):
##        Collison bonus joueur
        if pygame.sprite.spritecollideany(self,perso_list)!=None:
            Perso_prit=pygame.sprite.spritecollideany(self,perso_list)
            if self.valeur=="MaxBombe":
                Perso_prit.Nbmaxbombe+=1
                print("Max Bombe")
            if self.valeur=="Range":
                Perso_prit.Range+=1
                print("range")
            if self.valeur=="vitesse":
                Perso_prit.vitesse*=0.90
                print("vitesse")
            bonus_list.remove(self)
class bombe(pygame.sprite.Sprite):
##    Class des bombes
    def __init__(self,posX,posY,Vitesse=1,Range=2,perso=pygame.sprite.Sprite):
        super(bombe,self).__init__()
        self.image=pygame.image.load("Images/Images Divers/bombe.png").convert_alpha()
        self.image2=pygame.image.load("Images/Images Divers/bombe2.png").convert_alpha()
        self.image3=pygame.image.load("Images/Images Divers/bombe3.png").convert_alpha()
        self.image4=pygame.image.load("Images/Images Divers/bombe4.png").convert_alpha()
        self.image5=pygame.image.load("Images/Images Divers/bombe5.png").convert_alpha()
        self.image6=pygame.image.load("Images/Images Divers/bombe6.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
        self.a=0
        self.Vitesse=Vitesse
        self.Range=Range
        self.poseur=perso
        self.son=pygame.mixer.Sound("Sound/poudre.wav")
        self.son.play()
    def update(self,bombe_list=pygame.sprite.Group(),explosion_list=pygame.sprite.Group(),Coord=54,mur_list=pygame.sprite.Group()):
##        Fonction gérant l'actualisaion de la class bombe et la création de l'explosion
        self.a+=1
        if self.a==int(60*1/2*self.Vitesse):
            self.image=self.image2
        if self.a==int(60*1*self.Vitesse):
            self.image=self.image3
        if self.a==int(60*3/2*self.Vitesse):
            self.image=self.image4
        if self.a==int(60*2*self.Vitesse):
            self.image=self.image5
        if self.a==int(60*5/2*self.Vitesse):
            self.son.stop()
            self.image=self.image6
        if self.a==int(3*60*self.Vitesse):
            sonExplosion=pygame.mixer.Sound("Sound/explosion.ogg")
            sonExplosion.play()
            self.a=0
            bombe_list.remove(self)
            self.poseur.Nbbombeposer-=1
            for c in range(0,-self.Range,-1):
                b=0
                if 0<c*Coord+self.rect.y and b*Coord+self.rect.x!=Coord*2 and b*Coord+self.rect.x!=Coord*4 and b*Coord+self.rect.x!=Coord*6 and b*Coord+self.rect.x!=Coord*8 and b*Coord+self.rect.x!=Coord*10 and b*Coord+self.rect.x!=Coord*12:
                    Explosion=explosion(b*Coord+self.rect.x,c*Coord+self.rect.y)
                    if pygame.sprite.spritecollideany(Explosion,mur_list)==None:
                        explosion_list.add(Explosion)
                    else:
                        mur_detruit=pygame.sprite.spritecollideany(Explosion,mur_list)
                        mur_detruit.update(bonus_list)
                        mur_list.remove(mur_detruit)
                        explosion_list.add(Explosion)
                        break
            for c in range(0,self.Range):
                b=0
                if Coord*14>c*Coord+self.rect.y and b*Coord+self.rect.x!=Coord*2 and b*Coord+self.rect.x!=Coord*4 and b*Coord+self.rect.x!=Coord*6 and b*Coord+self.rect.x!=Coord*8 and b*Coord+self.rect.x!=Coord*10 and b*Coord+self.rect.x!=Coord*12:
                    Explosion=explosion(b*Coord+self.rect.x,c*Coord+self.rect.y)
                    if pygame.sprite.spritecollideany(Explosion,mur_list)==None:
                        explosion_list.add(Explosion)
                    else:
                        mur_detruit=pygame.sprite.spritecollideany(Explosion,mur_list)
                        mur_detruit.update(bonus_list)
                        mur_list.remove(mur_detruit)
                        explosion_list.add(Explosion)
                        break
            for b in range(0,-self.Range,-1):
                c=0
                if 0<b*Coord+self.rect.x and c*Coord+self.rect.y!=Coord*2 and c*Coord+self.rect.y!=Coord*4 and c*Coord+self.rect.y!=Coord*6 and c*Coord+self.rect.y!=Coord*8 and c*Coord+self.rect.y!=Coord*10 and c*Coord+self.rect.y!=Coord*12:
                    Explosion=explosion(b*Coord+self.rect.x,c*Coord+self.rect.y)
                    if pygame.sprite.spritecollideany(Explosion,mur_list)==None:
                        explosion_list.add(Explosion)
                    else:
                        mur_detruit=pygame.sprite.spritecollideany(Explosion,mur_list)
                        mur_detruit.update(bonus_list)
                        mur_list.remove(mur_detruit)
                        explosion_list.add(Explosion)
                        break
            for b in range(0,self.Range):
                c=0
                if Coord*14>b*Coord+self.rect.x and c*Coord+self.rect.y!=Coord*2 and c*Coord+self.rect.y!=Coord*4 and c*Coord+self.rect.y!=Coord*6 and c*Coord+self.rect.y!=Coord*8 and c*Coord+self.rect.y!=Coord*10 and c*Coord+self.rect.y!=Coord*12:
                    Explosion=explosion(b*Coord+self.rect.x,c*Coord+self.rect.y)
                    if pygame.sprite.spritecollideany(Explosion,mur_list)==None:
                        explosion_list.add(Explosion)
                    else:
                        mur_detruit=pygame.sprite.spritecollideany(Explosion,mur_list)
                        mur_detruit.update(bonus_list)
                        mur_list.remove(mur_detruit)
                        explosion_list.add(Explosion)
                        break
class explosion(pygame.sprite.Sprite):
##    Class des explosions
    def __init__(self,posX,posY):
        super(explosion,self).__init__()
        self.image=pygame.image.load("Images/Images Divers/explosion.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
        self.a=0
        self.sonmort=pygame.mixer.Sound("Sound/mort.ogg")
    def update(self,perso=pygame.sprite.Group(),explosion_list=pygame.sprite.Group(),mort=pygame.sprite.Group()):
##        contact joueur explosions
        self.a+=1
        if self.a==60:
            explosion_list.remove(self)
        collision_list=pygame.sprite.spritecollide(self,perso,False,None)
        for perso_mort in collision_list:
            if perso_mort.vie>0 and perso_mort.immunite==0:
                self.sonmort.play()
                perso_mort.vie-=1
                perso_mort.immunite=60
            if perso_mort.vie==0:
                perso_mort.remove(perso_list)
                perso_mort.poser=False
                if Ghost_mode==True:
                    perso_mort.alive=False
                    perso_mort.poser=True
                    perso_mort.vitesse=1
                    perso_mort.Range=3
                    perso_mort.Nbmaxbombe=3
                    if perso_mort.direction==0:
                        perso_mort.image=perso_mort.droitemort
                    if perso_mort.direction==1:
                        perso_mort.image=perso_mort.hautmort
                    if perso_mort.direction==2:
                        perso_mort.image=perso_mort.gauchemort
                    if perso_mort.direction==3:
                        perso_mort.image=perso_mort.basmort
                    mort.add(perso_mort)
class perso(pygame.sprite.Sprite):
##    Class des perso
    def __init__(self,gauche,droite,haut,bas,X,Y):
        super(perso,self).__init__()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.droite = pygame.image.load(droite).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        self.gauchemort = pygame.image.load("Images/Images Perso/persomortgauche.png").convert_alpha()
        self.droitemort = pygame.image.load("Images/Images Perso/persomortdroite.png").convert_alpha()
        self.hautmort = pygame.image.load("Images/Images Perso/persomorthaut.png").convert_alpha()
        self.basmort = pygame.image.load("Images/Images Perso/persomortbas.png").convert_alpha()
        self.image=self.droite
        self.rect=self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.vie=3
        self.direction=0
        self.poser=True
        self.alive=True
        self.immunite=0
        self.vitesse=1
        self.Range=2
        self.Nbmaxbombe=1
        self.Nbbombeposer=0
        self.compteur=0
    def deplace(self,direction,Coord,mur_list):
##        Fonction gérant le déplacement des joueurs
        if self.alive==True:
            if direction=="haut":
                self.image,self.direction=self.haut,1
                if Coord<self.rect.y and self.rect.x!=Coord*2 and self.rect.x!=Coord*4 and self.rect.x!=Coord*6 and self.rect.x!=Coord*8 and self.rect.x!=Coord*10 and self.rect.x!=Coord*12:
                    self.rect.y-=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None:
                        self.rect.y+=Coord
            if direction=="bas":
                self.image,self.direction=self.bas,3
                if Coord*13>self.rect.y and self.rect.x!=Coord*2 and self.rect.x!=Coord*4 and self.rect.x!=Coord*6 and self.rect.x!=Coord*8 and self.rect.x!=Coord*10 and self.rect.x!=Coord*12:
                    self.rect.y+=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None:
                        self.rect.y-=Coord
            if direction=="gauche" :
                self.image,self.direction=self.gauche,2
                if Coord<self.rect.x and self.rect.y!=Coord*2 and self.rect.y!=Coord*4 and self.rect.y!=Coord*6 and self.rect.y!=Coord*8 and self.rect.y!=Coord*10 and self.rect.y!=Coord*12:
                    self.rect.x-=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None:
                        self.rect.x+=Coord
            if direction=="droite":
                self.image,self.direction=self.droite,0
                if Coord*13>self.rect.x  and self.rect.y!=Coord*2 and self.rect.y!=Coord*4 and self.rect.y!=Coord*6 and self.rect.y!=Coord*8 and self.rect.y!=Coord*10 and self.rect.y!=Coord*12:
                    self.rect.x+=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None:
                        self.rect.x-=Coord
        if self.alive==False:
            if direction=="haut":
                self.image=self.hautmort
                if Coord<self.rect.y and self.rect.x!=Coord*2 and self.rect.x!=Coord*4 and self.rect.x!=Coord*6 and self.rect.x!=Coord*8 and self.rect.x!=Coord*10 and self.rect.x!=Coord*12:
                    self.rect.y-=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None and Ghost_move==False:
                        self.rect.y+=Coord
            if direction=="bas":
                self.image=self.basmort
                if Coord*13>self.rect.y and self.rect.x!=Coord*2 and self.rect.x!=Coord*4 and self.rect.x!=Coord*6 and self.rect.x!=Coord*8 and self.rect.x!=Coord*10 and self.rect.x!=Coord*12:
                    self.rect.y+=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None and Ghost_move==False:
                        self.rect.y-=Coord
            if direction=="gauche" :
                self.image=self.gauchemort
                if Coord<self.rect.x and self.rect.y!=Coord*2 and self.rect.y!=Coord*4 and self.rect.y!=Coord*6 and self.rect.y!=Coord*8 and self.rect.y!=Coord*10 and self.rect.y!=Coord*12:
                    self.rect.x-=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None and Ghost_move==False:
                        self.rect.x+=Coord
            if direction=="droite":
                self.image=self.droitemort
                if Coord*13>self.rect.x  and self.rect.y!=Coord*2 and self.rect.y!=Coord*4 and self.rect.y!=Coord*6 and self.rect.y!=Coord*8 and self.rect.y!=Coord*10 and self.rect.y!=Coord*12:
                    self.rect.x+=Coord
                    if pygame.sprite.spritecollideany(self,mur_list)!=None and Ghost_move==False:
                        self.rect.x-=Coord
    def update(self):
##        actualisation de l'imunité du joueur
        if self.immunite>0:
            self.immunite-=1
def Button(evt,x,y,xmax,ymax,Entrer=False):
##    gestion de l'activation du boutton
    if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and evt.pos[0] > x and evt.pos[1] > y and evt.pos[0] < xmax and evt.pos[1] < ymax:
        sonclick.play()
        return True
    if evt.type==pygame.KEYDOWN and evt.key==pygame.K_RETURN and Entrer:
        sonclick.play()
        return True
def Buttonskin(x,y,xmax,ymax,pasenfichier="",enfichier="",texte=""):
##    gestion de l'animation du boutton
    xmouse,ymouse=pygame.mouse.get_pos()
    Surf_texte=font.render(texte,1,(0,0,0))
    if xmouse > x and ymouse > y and xmouse < xmax and ymouse < ymax:
        image= pygame.image.load(enfichier).convert_alpha()
        screen.blit(image,(x,y+4))
        screen.blit(Surf_texte,(x+95+int(-len(texte)*10/2),y+4+6))
    else :
        image= pygame.image.load(pasenfichier).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(x+95+int(-len(texte)*10/2),y+6))
def Mapskin(x,y,xmax,ymax,valeurmap,Map,fichier="",fichierselec="",texte="",alea=0):
##    gestion de l'animation des maps
    if valeurmap==Map and not type(fichierselec)is tuple:
        Surf_texte=font.render(texte,1,(255,201,14))
        image= pygame.image.load(fichierselec).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(x+54+int(-len(texte)*10/2),ymax+10))
    elif valeurmap!=Map and not type(fichier)is tuple:
        Surf_texte=font.render(texte,1,(0,0,0))
        image= pygame.image.load(fichier).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(x+54+int(-len(texte)*10/2),ymax+10))
    elif valeurmap==Map and type(fichierselec)is tuple:
        Surf_texte=font.render(texte,1,(255,201,14))
        image= pygame.image.load(fichierselec[alea]).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(x+54+int(-len(texte)*10/2),ymax+10))
    else:
        Surf_texte=font.render(texte,1,(0,0,0))
        image= pygame.image.load(fichier[alea]).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(x+54+int(-len(texte)*10/2),ymax+10))
def Buttoncroixskin(x,y,xmax,ymax,etat,imageoui,imagenon,texte="",Ghost_mode=True,nonchoiximage=""):
##    gestion de l'animation des carré de séléction
    Surf_texte=font.render(texte,1,(0,0,0))
    if etat and Ghost_mode:
        image= pygame.image.load(imageoui).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(xmax,y))
    if not etat and Ghost_mode:
        image= pygame.image.load(imagenon).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(xmax,y))
    if not Ghost_mode:
        image= pygame.image.load(nonchoiximage).convert_alpha()
        screen.blit(image,(x,y))
        screen.blit(Surf_texte,(xmax,y))
def Saisi(event,texte):
##    gestion de la saisides nom
    if event.type==pygame.KEYDOWN and (event.key==pygame.K_SPACE or event.key == pygame.K_BACKSPACE or event.unicode.isalpha()):
        if texte[-1]=="_":
            texte=texte[:-1]
        if event.key == pygame.K_SPACE and len(texte)<21:
            texte=texte+" "+"_"
            if len(texte)==22:
                texte=texte[:-1]
        elif event.unicode.isalpha()and len(texte)<21:
            texte=texte+event.unicode+"_"
            if len(texte)==22:
                texte=texte[:-1]
        if  event.key == pygame.K_BACKSPACE:
                texte = texte[:-1]+"_"
    return texte

#constant
Jeux=True
continu=True
menu=True
menu_principal=True
instruction=True
Coord=54
Ghost_mode=False
Ghost_move=False
win=True
Longueur=810
click=0
Map=0
name1,name2,name3,name4="Joueur 1","Joueur 2","Joueur 3","Joueur 4"
# fenêtre
screen=pygame.display.set_mode((1110,810))
pygame.display.set_caption("Bomber Game")
pygame.display.set_icon(pygame.image.load("Images/Images Divers/icone.png").convert())
clock=pygame.time.Clock()
#image,son,ecriture,
ecriture="big_noodle_titling_oblique.ttf"
font=pygame.font.Font(ecriture, 30)

Musique=pygame.mixer.Sound("Sound/tetris.ogg")
print(Musique.get_volume())
sonclick=pygame.mixer.Sound("Sound/Click.ogg")
winimage=pygame.image.load("Images/Images Divers/Win.png").convert_alpha()
menu_nom=pygame.image.load("Images/Images Divers/Nom.png").convert_alpha()
menuprincipal=pygame.image.load("Images/Images Divers/Menuprincipal.png").convert_alpha()
fond = pygame.image.load("Images/Images Divers/MapFinal.png").convert()
Menu = pygame.image.load("Images/Images Divers/Menu.png").convert()
Croixmenu= pygame.image.load("Images/Images Divers/Croixmenu.png").convert_alpha()
perso1menu=pygame.image.load("Images/Images Perso/perso1menu.png").convert_alpha()
perso2menu=pygame.image.load("Images/Images Perso/perso2menu.png").convert_alpha()
perso3menu=pygame.image.load("Images/Images Perso/perso3menu.png").convert_alpha()
perso4menu=pygame.image.load("Images/Images Perso/perso4menu.png").convert_alpha()
ghostmenu=pygame.image.load("Images/Images Perso/persomortmenu.png").convert_alpha()
#list explosion joueur et bombe

Bombe1,Bombe2,Bombe3,Bombe4=pygame.sprite.Sprite,pygame.sprite.Sprite,pygame.sprite.Sprite,pygame.sprite.Sprite
mort_list=pygame.sprite.Group()
explosion_list=pygame.sprite.Group()
bombe_list=pygame.sprite.Group()
bonus_list=pygame.sprite.Group()
mur_list=pygame.sprite.Group()


while continu:
##    menu principal
    while menu_principal:
        screen.blit(menuprincipal,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Jeux=False
                continu=False
                menu=False
                menu_principal=False
                win=False
                instruction=False
            if Button(event,460,300,460+190,300+49,True):
##                jouer
                menu_principal=False
                menu=True
                Jeux=True
                instruction=False
            if Button(event,460,500,460+190,500+49):
##                quitter
                Jeux=False
                continu=False
                menu=False
                menu_principal=False
                win=False
                instruction=False
            if Button(event,460,400,460+190,400+49):
##                instruction
                instruction=True
                menu_principal=False
        Buttonskin(460,300,460+190,300+49,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Play")
        Buttonskin(460,400,460+190,400+49,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Instruction")
        Buttonskin(460,500,460+190,500+49,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Quitter")
        clock.tick(60)
        pygame.display.flip()
##instruction
    while instruction:
        screen.blit(winimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Jeux=False
                continu=False
                menu=False
                menu_principal=False
                win=False
                instruction=False
            if Button(event,890,730,1079,810):
##                Retour
                menu_principal=True
                menu=False
                continu=True
                instruction=False
                Jeux=False
                win=False
            if Button(event,31,730,190,810):
##                quitter
                Jeux=False
                continu=False
                menu_principal=False
                menu=False
                instruction=False
                win=False
            if Button(event,460,730,650,810,True):
##              jouer
                Jeux=True
                instruction=False
                menu=True
        Buttonskin(890,730,1079,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Retour")
        Buttonskin(31,730,190,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Quitter")
        Buttonskin(460,730,650,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Jouer")
        
        Instruction=font.render("Bomber Game est un jeu à 4 joueurs où le principe est d'être le dernier survivant.",1,(0,0,0))
        screen.blit(Instruction,(10,10))
        Instruction2=font.render("Chaque personnage peut poser une bombe pour tuer son ennemi et peut détruire des murs destructibles pour",1,(0,0,0))
        screen.blit(Instruction2,(10,40))
        Instruction3=font.render("récuperer des bonus.",1,(0,0,0))
        screen.blit(Instruction3,(10,70))
        Instruction4=font.render("Ces bonus apportent un avantage au joueur comme baisser la vitesse d'explosion, la portée de l'explosion",1,(0,0,0))
        screen.blit(Instruction4,(10,100))
        Instruction5=font.render("ou encore la possibilité de poser plus de bombe.",1,(0,0,0))
        screen.blit(Instruction5,(10,130))
        Instruction6=font.render(name1+" pour se déplacer Z Q S D et poser une bombe A",1,(0,0,0))
        screen.blit(Instruction6,(10,190))
        Instruction7=font.render(name2+" pour se déplacer avec les fleches directionelles et poser une bombe CTRL droit",1,(0,0,0))
        screen.blit(Instruction7,(10,220))
        Instruction8=font.render(name3+" pour se déplacer I J K L et poser une bombe M",1,(0,0,0))
        screen.blit(Instruction8,(10,250))
        Instruction9=font.render(name4+" pour se déplacer 4 5 6 8(Numpad)et poser une bombe +(Numpad) ",1,(0,0,0))
        screen.blit(Instruction9,(10,280))
        clock.tick(60)
        pygame.display.flip()
    pygame.key.set_repeat(100,50)
    alea=random.randint(0,2)
    temps=0
##    Second menu
    while menu:
        screen.blit(menu_nom,(0,0))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Jeux=False
                continu=False
                menu=False
                menu_principal=False
                win=False
            if Button(event,892,726,1079,810,True):
##                continuer
                menu=False
                if click==2 and name2[-1]=="_":
                    name2=name2[:-1]
                elif click==3 and name3[-1]=="_":
                    name3=name3[:-1]
                elif click==4 and name4[-1]=="_":
                    name4=name4[:-1]
                elif click==1 and name1[-1]=="_":
                    name1=name1[:-1]
            if Button(event,50,100,158,208):
                Map=0
            if Button(event,200,100,308,208):
                Map=1
            if Button(event,50,300,158,408):
                Map=2
            if Button(event,200,300,308,408):
                Map=3
            if Button(event,100,500,290,549):
##                map aléatoire
                Map=random.randint(0,3)
            if Button(event,31,726,190+31,810):
##                retour
                menu=False
                Jeux=False
                menu_principal=True
                win=False
            if Button(event,900,300,938,336):
                Ghost_mode=not Ghost_mode
            if Button(event,900,400,938,436) and Ghost_mode:
                Ghost_move=not Ghost_move
##                Pour empecher de faire réapparaitre le tiret
            if Button(event,555,114,855,149)and click!=1:
                if click==2 and name2[-1]=="_":
                    name2=name2[:-1]
                elif click==3 and name3[-1]=="_":
                    name3=name3[:-1]
                elif click==4 and name4[-1]=="_":
                    name4=name4[:-1]
                click=1
                if len(name1)<21:
                    name1+="_"
            if Button(event,555,296,855,331)and click!=2:
                if click==1 and name1[-1]=="_":
                    name1=name1[:-1]
                elif click==3 and name3[-1]=="_":
                    name3=name3[:-1]
                elif click==4 and name4[-1]=="_":
                    name4=name4[:-1]
                click=2
                if len(name2)<21:
                    name2+="_"
            if Button(event,555,481,855,516)and click!=3:
                if click==1 and name1[-1]=="_":
                    name1=name1[:-1]
                elif click==2 and name2[-1]=="_":
                    name2=name2[:-1]
                elif click==4 and name4[-1]=="_":
                    name4=name4[:-1]
                click=3
                if len(name3)<21:
                    name3+="_"
            if Button(event,555,662,855,697)and click!=4:
                if click==1 and name1[-1]=="_":
                    name1=name1[:-1]
                elif click==2 and name2[-1]=="_":
                    name2=name2[:-1]
                elif click==3 and name3[-1]=="_":
                    name3=name3[:-1]
                click=4
                if len(name4)<21:
                    name4+="_"
                    
            if click==1:
                name1=Saisi(event,name1)
            if click==2:
                name2=Saisi(event,name2)
            if click==3:
                name3=Saisi(event,name3)
            if click==4:
                name4=Saisi(event,name4)
                
        Mapskin(50,100,158,208,0,Map,"Images/Images Divers/Map1.png","Images/Images Divers/Map1selec.png","Map 1")
        Mapskin(200,100,308,208,1,Map,"Images/Images Divers/Map2.png","Images/Images Divers/Map2selec.png","Map 2")
        Mapskin(50,300,158,408,2,Map,"Images/Images Divers/Map3.png","Images/Images Divers/Map3selec.png","Map 3")
        Mapskin(200,300,308,408,3,Map,("Images/Images Divers/Map4.png","Images/Images Divers/Map4bis.png","Images/Images Divers/Map4ter.png"),("Images/Images Divers/Map4selec.png","Images/Images Divers/Map4bisselec.png","Images/Images Divers/Map4terselec.png"),"Map 4",alea)
        Buttoncroixskin(900,300,938,336,Ghost_mode,"Images/Images Divers/Check.png","Images/Images Divers/nonCheck.png","Ghost mode")
        Buttoncroixskin(900,400,938,436,Ghost_move,"Images/Images Divers/Check.png","Images/Images Divers/nonCheck.png","Ghost move",Ghost_mode,"Images/Images Divers/Checkvide.png")
        Buttonskin(100,500,290,549,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Aléatoire")
        Buttonskin(890,730,1079,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Continuer")
        Buttonskin(31,726,190,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Retour")
        text1=font.render(name1,1,(0,0,0))
        text2=font.render(name2,1,(0,0,0))
        text3=font.render(name3,1,(0,0,0))
        text4=font.render(name4,1,(0,0,0))
        screen.blit(text1,(560,117))
        screen.blit(text2,(560,298))
        screen.blit(text3,(560,483))
        screen.blit(text4,(560,663))
        if temps==60:
            temps=0
            alea=random.randint(0,2)
        temps+=1
        clock.tick(60)
        pygame.display.flip()
    pygame.key.set_repeat()
    Musique.play(-1)
    if Jeux:
        mur_list=generer(choix[Map])
    perso1=perso("Images/Images Perso/perso1gauche.png","Images/Images Perso/perso1droite.png","Images/Images Perso/perso1haut.png","Images/Images Perso/perso1bas.png",Coord,Coord)
    perso2=perso("Images/Images Perso/perso2gauche.png","Images/Images Perso/perso2droite.png","Images/Images Perso/perso2haut.png","Images/Images Perso/perso2bas.png",Coord*13,Coord*13)
    perso3=perso("Images/Images Perso/perso3gauche.png","Images/Images Perso/perso3droite.png","Images/Images Perso/perso3haut.png","Images/Images Perso/perso3bas.png",Coord*13,Coord)
    perso4=perso("Images/Images Perso/perso4gauche.png","Images/Images Perso/perso4droite.png","Images/Images Perso/perso4haut.png","Images/Images Perso/perso4bas.png",Coord,Coord*13)
    perso_list=pygame.sprite.Group()
    perso_list.add(perso1,perso2,perso3,perso4)
##    Jeux
    while Jeux:
        screen.blit(fond,(0,0))
        screen.blit(Menu,(810,0))
        for event in pygame.event.get():
            ##Quitter
            if event.type==pygame.QUIT:
                Jeux=False
                continu=False
                menu_principal=False
                menu=False
                win=False
            ##Triche
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_F1:
                    perso_list.remove(perso2,perso3,perso4)
                if event.key==pygame.K_F2:
                    perso_list.remove(perso1,perso3,perso4)
                if event.key==pygame.K_F3:
                    perso_list.remove(perso2,perso1,perso4)
                if event.key==pygame.K_F4:
                    perso_list.remove(perso2,perso3,perso1)
                if event.key==pygame.K_F7:
                    mur_list.empty()
                    mur_list=generer(choix[0])
                if event.key==pygame.K_F8:
                    mur_list.empty()
                    mur_list=generer(choix[1])
                if event.key==pygame.K_F9:
                    mur_list.empty()
                    mur_list=generer(choix[2])
                if event.key==pygame.K_F10:
                    mur_list.empty()
                    mur_list=generer(generer_liste(liste_gene))

                if event.key==pygame.K_PAGEDOWN:
                    Musique.set_volume(Musique.get_volume()-0.1)
                if event.key==pygame.K_PAGEUP:
                    Musique.set_volume(Musique.get_volume()+0.1)
        ##            deplacement des joueur
                if event.key==pygame.K_UP :
                    perso2.deplace("haut",Coord,mur_list)
                if event.key==pygame.K_DOWN:
                    perso2.deplace("bas",Coord,mur_list)
                if event.key==pygame.K_LEFT:
                    perso2.deplace("gauche",Coord,mur_list)
                if event.key==pygame.K_RIGHT:
                    perso2.deplace("droite",Coord,mur_list)
                if event.key==pygame.K_w:
                    perso1.deplace("haut",Coord,mur_list)
                if event.key==pygame.K_s:
                    perso1.deplace("bas",Coord,mur_list)
                if event.key==pygame.K_a:
                    perso1.deplace("gauche",Coord,mur_list)
                if event.key==pygame.K_d:
                    perso1.deplace("droite",Coord,mur_list)
                if event.key==pygame.K_i:
                    perso3.deplace("haut",Coord,mur_list)
                if event.key==pygame.K_k:
                    perso3.deplace("bas",Coord,mur_list)
                if event.key==pygame.K_j:
                    perso3.deplace("gauche",Coord,mur_list)
                if event.key==pygame.K_l:
                    perso3.deplace("droite",Coord,mur_list)
                if event.key==pygame.K_KP8:
                    perso4.deplace("haut",Coord,mur_list)
                if event.key==pygame.K_KP5:
                    perso4.deplace("bas",Coord,mur_list)
                if event.key==pygame.K_KP4:
                    perso4.deplace("gauche",Coord,mur_list)
                if event.key==pygame.K_KP6:
                    perso4.deplace("droite",Coord,mur_list)
    ##            apparition des bombes
                if  event.key==pygame.K_q and perso1.poser==True and perso1.Nbmaxbombe>perso1.Nbbombeposer and pygame.sprite.spritecollideany(perso1,mur_list)==None:
                    Bombe1=bombe(perso1.rect.x,perso1.rect.y,perso1.vitesse,perso1.Range,perso1)
                    bombe_list.add(Bombe1)
                    perso1.Nbbombeposer+=1
                if event.key==pygame.K_RCTRL and perso2.poser==True and perso2.Nbmaxbombe>perso2.Nbbombeposer and pygame.sprite.spritecollideany(perso2,mur_list)==None:
                    Bombe2=bombe(perso2.rect.x,perso2.rect.y,perso2.vitesse,perso2.Range,perso2)
                    bombe_list.add(Bombe2)
                    perso2.Nbbombeposer+=1
                if event.key==pygame.K_SEMICOLON and perso3.poser==True and perso3.Nbmaxbombe>perso3.Nbbombeposer and pygame.sprite.spritecollideany(perso3,mur_list)==None:
                    Bombe3=bombe(perso3.rect.x,perso3.rect.y,perso3.vitesse,perso3.Range,perso3)
                    bombe_list.add(Bombe3)
                    perso3.Nbbombeposer+=1
                if event.key==pygame.K_KP_PLUS and perso4.poser==True and perso4.Nbmaxbombe>perso4.Nbbombeposer and pygame.sprite.spritecollideany(perso4,mur_list)==None:
                    Bombe4=bombe(perso4.rect.x,perso4.rect.y,perso4.vitesse,perso4.Range,perso4)
                    bombe_list.add(Bombe4)
                    perso4.Nbbombeposer+=1
##        update des objets
        bombe_list.update(bombe_list,explosion_list,Coord,mur_list)
        explosion_list.update(perso_list,explosion_list,mort_list)
        perso_list.update()
        bonus_list.update(perso_list,bonus_list)
##        affichage des objets
        bombe_list.draw(screen)
        mur_list.draw(screen)
        mort_list.draw(screen)
        bonus_list.draw(screen)
        explosion_list.draw(screen)
        perso_list.draw(screen)
##        affichage score
        vie1=font.render(str(perso1.vie),1,(0,0,0))
        vitess1=font.render(str(round(perso1.vitesse*3,1)),1,(0,0,0))
        bombemax1=font.render(str(perso1.Nbmaxbombe),1,(0,0,0))
        rangebomb1=font.render(str(perso1.Range),1,(0,0,0))
        
        vie2=font.render(str(perso2.vie),1,(0,0,0))
        vitess2=font.render(str(round(perso2.vitesse*3,1)),1,(0,0,0))
        bombemax2=font.render(str(perso2.Nbmaxbombe),1,(0,0,0))
        rangebomb2=font.render(str(perso2.Range),1,(0,0,0))
        
        vie3=font.render(str(perso3.vie),1,(0,0,0))
        vitess3=font.render(str(round(perso3.vitesse*3,1)),1,(0,0,0))
        bombemax3=font.render(str(perso3.Nbmaxbombe),1,(0,0,0))
        rangebomb3=font.render(str(perso3.Range),1,(0,0,0))
        
        vie4=font.render(str(perso4.vie),1,(0,0,0))
        vitess4=font.render(str(round(perso4.vitesse*3,1)),1,(0,0,0))
        bombemax4=font.render(str(perso4.Nbmaxbombe),1,(0,0,0))
        rangebomb4=font.render(str(perso4.Range),1,(0,0,0))
        
        text1=font.render(name1,1,(0,0,0))
        text2=font.render(name2,1,(0,0,0))
        text3=font.render(name3,1,(0,0,0))
        text4=font.render(name4,1,(0,0,0))
        
        screen.blit(perso1menu,(Longueur,50))
        screen.blit(perso2menu,(Longueur,250))
        screen.blit(perso3menu,(Longueur,450))
        screen.blit(perso4menu,(Longueur,650))
        if not perso_list.has(perso1) and not Ghost_mode:
            screen.blit(Croixmenu,(Longueur,50))
        if not perso_list.has(perso2) and not Ghost_mode:
            screen.blit(Croixmenu,(Longueur,250))
        if not perso_list.has(perso3) and not Ghost_mode:
            screen.blit(Croixmenu,(Longueur,450))
        if not perso_list.has(perso4) and not Ghost_mode:
            screen.blit(Croixmenu,(Longueur,650))
            
        if  mort_list.has(perso1) and Ghost_mode:
            screen.blit(ghostmenu,(Longueur,50))
        if  mort_list.has(perso2) and Ghost_mode:
            screen.blit(ghostmenu,(Longueur,250))
        if  mort_list.has(perso3) and Ghost_mode:
            screen.blit(ghostmenu,(Longueur,450))
        if  mort_list.has(perso4) and Ghost_mode:
            screen.blit(ghostmenu,(Longueur,650))

        screen.blit(text1,(Longueur+150-int(len(name1)/2)*11,10))
        screen.blit(text2,(Longueur+150-int(len(name2)/2)*11,210))
        screen.blit(text3,(Longueur+150-int(len(name3)/2)*11,410))
        screen.blit(text4,(Longueur+150-int(len(name4)/2)*11,610))
        
        screen.blit(vie1,(Longueur+177,67))
        screen.blit(vitess1,(Longueur+263,141))
        screen.blit(bombemax1,(Longueur+172,141))
        screen.blit(rangebomb1,(Longueur+265,67))

        screen.blit(vie2,(Longueur+177,267))
        screen.blit(vitess2,(Longueur+263,341))
        screen.blit(bombemax2,(Longueur+172,341))
        screen.blit(rangebomb2,(Longueur+265,267))
        
        screen.blit(vie3,(Longueur+177,467))
        screen.blit(vitess3,(Longueur+263,541))
        screen.blit(bombemax3,(Longueur+172,541))
        screen.blit(rangebomb3,(Longueur+265,467))

        screen.blit(vie4,(Longueur+177,667))
        screen.blit(vitess4,(Longueur+263,741))
        screen.blit(bombemax4,(Longueur+172,741))
        screen.blit(rangebomb4,(Longueur+265,667))

        clock.tick(60)
        pygame.display.flip()
        if len(perso_list)==1 or len(perso_list)==0:
            Jeux=False
            win=True
    Musique.stop()
##    Menu victoire
    mur_list.empty()
    explosion_list.empty()
    bombe_list.empty()
    bonus_list.empty()
    while win:
        screen.blit(winimage,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Jeux=False
                continu=False
                menu_principal=False
                menu=False
                win=False
            if Button(event,890,730,1079,810):
##                retour menu
                win=False
                menu_principal=True
                menu=True
                continu=True
            if Button(event,31,730,190,810):
##                quitter
                Jeux=False
                continu=False
                menu_principal=False
                menu=False
                win=False
            if Button(event,460,730,650,810,True):
##                ressayer
                win=False
                Jeux=True
        Buttonskin(890,730,1079,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Retour menu")
        Buttonskin(31,730,190,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Quitter")
        Buttonskin(460,730,650,810,"Images/Images Divers/button.png","Images/Images Divers/buttonenfonce.png","Ressayer") 
        if perso_list.has(perso1):
            gagner(name1,perso1menu)
        elif perso_list.has(perso2):
            gagner(name2,perso2menu)
        elif perso_list.has(perso3):
            gagner(name3,perso3menu)
        elif perso_list.has(perso4):
            gagner(name4,perso4menu)
        clock.tick(60)
        pygame.display.flip()
a=0
while a<30:
    a+=1
    clock.tick(60)
pygame.quit()
