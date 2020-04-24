#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
 
class player:
    scorerate=0
    shootpro=0
    keeperpro=0
    name=''
    def __init__(self,scorerate,shootpro,keeperpro,name):
        self.name = name
        self.scorerate = scorerate
        self.shootpro=shootpro
        self.keeperpro=keeperpro
       
class team:
    name=''
    getpro=0
    playerlist=[]
    def __init__(self,getpro,playerlist,name):
        self.name = name
        self.getpro=getpro
        self.playerlist=playerlist

class match:
    time=0
    thisscoreh=0
    thisscorea=0
    allscoreh=0
    allscorea=0
    penscoreh=0
    penscorea=0
    def __init__(self,teamh,teama,lastscoreh,lastscorea):
        self.teamh = teamh
        self.teama= teama
        self.lastscoreh=lastscoreh
        self.lastscorea=lastscorea
        self.allscoreh=lastscoreh
        self.allscorea=lastscorea
    def scoreh(self):
        self.thisscoreh+=1
        self.allscoreh+=1
        if self.allscoreh==self.allscorea:
            # 客场进球
            if self.lastscoreh==self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+",这样90分钟结束会有加时赛！")
            if self.lastscoreh>self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+"但是"+self.teamh.name+"客场进球领先！")
            if self.lastscoreh<self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+"但是"+self.teama.name+"客场进球领先！")
        else:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea))
            
    def scorea(self):
        self.thisscorea+=1
        self.allscorea+=1
        if self.allscoreh==self.allscorea:
            # 客场进球
            if self.lastscoreh==self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+",这样90分钟结束会有加时赛！")
            if self.lastscoreh>self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+"但是"+self.teamh.name+"客场进球领先！")
            if self.lastscoreh<self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+"但是"+self.teama.name+"客场进球领先！")
        else:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea))

    def scoreh120(self):
        self.thisscoreh+=1
        self.allscoreh+=1
        if self.allscoreh==self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea)+"这样的比分维持下去的话，迎接他们的是残酷的点球大战！")    
        else:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name)    
   
    def scorea120(self):
        self.thisscorea+=1
        self.allscorea+=1
        if self.allscoreh==self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea)+"这样的比分维持下去的话，迎接他们的是残酷的点球大战！")    
        else:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea))    

    def judge90(self):
        if self.allscoreh==self.allscorea:
            # 客场进球
            if self.lastscoreh==self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+",这样90分钟结束会有加时赛！")
                self.vs120()
                return
            if self.lastscoreh>self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+"但是"+self.teamh.name+"客场进球领先，取得胜利！")
            if self.lastscoreh<self.thisscorea:
                print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+"但是"+self.teama.name+"客场进球领先，取得胜利！")
        if self.allscoreh>self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea)+"，"+self.teamh.name+"胜利！")
        if self.allscoreh<self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea)+"，"+self.teama.name+"胜利！")
    def judge120(self):
        if self.allscoreh==self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分平,"+str(self.allscoreh)+":"+str(self.allscorea)+",接下来是点球大战！")
            self.vspen() 
            return           
        if self.allscoreh>self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea)+"，"+self.teamh.name+"胜利！")
        if self.allscoreh<self.allscorea:
            print("本场比分"+self.teamh.name+str(self.thisscoreh)+":"+str(self.thisscorea)+self.teama.name+"，目前总比分为"+str(self.allscoreh)+":"+str(self.allscorea)+"，"+self.teama.name+"胜利！")
    def vspen(self):
        i=1
        ii=10
        while True:
            if i>5:
                self.kick(ii)
                i+=1
                ii-=1
                if self.judgepen()==1:
                    return
            if i==5:
                self.kick(ii)
                i+=1
                ii-=1
                if self.judgepen()==1:
                    return
            if i<5:
                self.kick(ii)
                i+=1
                ii-=1
            if ii==0:
                ii=10
    def kick(self,ii):
        hp=random.randint(0,9999)
        ap=random.randint(0,9999)
        if hp<self.teamh.playerlist[ii].scorerate*150:
            print(self.teamh.playerlist[ii].name+"罚中！")
            self.penscoreh+=1
        else:
            print(self.teamh.playerlist[ii].name+"点球被扑出！")

        if ap<self.teama.playerlist[ii].scorerate*150:
            print(self.teama.playerlist[ii].name+"罚中！")
            self.penscorea+=1
        else:
            print(self.teama.playerlist[ii].name+"点球被扑出！")

        print("目前比分"+str(self.penscoreh)+":"+str(self.penscorea)+"!")
    def judgepen(self):
        if self.penscoreh==self.penscorea:
            print("点球大战继续！")
            return 0
        if self.penscoreh>self.penscorea:
            print("比赛结束！"+self.teamh.name+"取胜!")
            return 1
        if self.penscoreh<self.penscorea:
            print("比赛结束！"+self.teama.name+"取胜!")
            return 1
    def vs90(self):
        for time in range(0,91):
            if random.randint(0,99)<60:
                # something happens
                if random.randint(0,99)<=self.teamh.getpro:
                    whichplayer=self.teamh.playerlist[random.randint(0,10)]
                    shootposs=random.randint(0,9999)
                    if shootposs<=whichplayer.shootpro*100:
                        # readyshoot
                        anotherplayer=self.teama.playerlist[random.randint(1,7)]
                        defendposs=random.randint(0,9999)
                        if defendposs>=anotherplayer.keeperpro*100:
                            # shoot keeper
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teama.playerlist[0].keeperpro*100:
                            # score
                                print("球进啦！"+str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门得手，"+self.teama.playerlist[0].name+"扑救不及！")
                                self.scoreh()
                            else:
                                # save by keeper
                                print(str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门,但却被"+self.teama.playerlist[0].name+"神勇化解。")
                        else:
                            # anotherplayer
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teama.playerlist[0].keeperpro*500:
                            # longscore
                                print("球进啦！"+str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",晃开空间远射,"+self.teama.playerlist[0].name+"鞭长莫及。")
                                self.scoreh()
                            else:
                                # tackle
                                print(str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"突破进入禁区，但被"+anotherplayer.name+"抢断。")
                    
                    # else:
                    #     print(str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"大力远射，飞上看台")

                else:
                    whichplayer=self.teama.playerlist[random.randint(0,10)]
                    shootposs=random.randint(0,9999)
                    if shootposs<=whichplayer.shootpro*100:
                        # readyshoot
                        anotherplayer=self.teamh.playerlist[random.randint(1,7)]
                        defendposs=random.randint(0,9999)
                        if defendposs>=anotherplayer.keeperpro*100:
                            # shoot keeper
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teamh.playerlist[0].keeperpro*100:
                            # score
                                print("球进啦！"+str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门得手，"+self.teamh.playerlist[0].name+"扑救不及！")
                                self.scorea()
                            else:
                                # save by keeper
                                print(str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门,但却被"+self.teamh.playerlist[0].name+"神勇化解。")
                        else:
                            # anotherplayer
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teamh.playerlist[0].keeperpro*500:
                            # longscore
                                print("球进啦！"+str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",晃开空间远射,"+self.teamh.playerlist[0].name+"鞭长莫及。")
                                self.scorea()
                            else:
                                # tackle
                                print(str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"突破进入禁区，但被"+anotherplayer.name+"抢断。")
                    
                    # else:
                    #     print(str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"大力远射，但是效果不佳飞上看台")
        self.judge90()
    
    def vs120(self):
        for time in range(90,120):
            if random.randint(0,99)<40:
                # something happens
                if random.randint(0,99)<=self.teamh.getpro:
                    whichplayer=self.teamh.playerlist[random.randint(0,10)]
                    shootposs=random.randint(0,9999)
                    if shootposs<=whichplayer.shootpro*100:
                        # readyshoot
                        anotherplayer=self.teama.playerlist[random.randint(1,7)]
                        defendposs=random.randint(0,9999)
                        if defendposs>=anotherplayer.keeperpro*100:
                            # shoot keeper
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teama.playerlist[0].keeperpro*100:
                            # score
                                print("球进啦！"+str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门得手，"+self.teama.playerlist[0].name+"扑救不及！")
                                self.scoreh120()
                            else:
                                # save by keeper
                                print(str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门,但却被"+self.teama.playerlist[0].name+"神勇化解。")
                        else:
                            # anotherplayer
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teama.playerlist[0].keeperpro*150:
                            # longscore
                                print("球进啦！"+str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",晃开空间远射,"+self.teama.playerlist[0].name+"鞭长莫及。")
                                self.scoreh120()
                            else:
                                # tackle
                                print(str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"突破进入禁区，但被"+anotherplayer.name+"抢断。")
                    
                    # else:
                        # print(str(time)+"分钟，"+self.teamh.name+"得到机会，"+whichplayer.name+"大力远射，飞上看台")

                else:
                    whichplayer=self.teama.playerlist[random.randint(0,10)]
                    shootposs=random.randint(0,9999)
                    if shootposs<=whichplayer.shootpro*100:
                        # readyshoot
                        anotherplayer=self.teamh.playerlist[random.randint(1,7)]
                        defendposs=random.randint(0,9999)
                        if defendposs>=anotherplayer.keeperpro*100:
                            # shoot keeper
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teamh.playerlist[0].keeperpro*100:
                            # score
                                print("球进啦！"+str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门得手，"+self.teamh.playerlist[0].name+"扑救不及！")
                                self.scorea120()
                            else:
                                # save by keeper
                                print(str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",进入禁区射门,但却被"+self.teamh.playerlist[0].name+"神勇化解。")
                        else:
                            # anotherplayer
                            scoreposs=random.randint(0,9999)
                            if scoreposs>=self.teamh.playerlist[0].keeperpro*150:
                            # longscore
                                print("球进啦！"+str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"过掉了"+anotherplayer.name+",晃开空间远射,"+self.teamh.playerlist[0].name+"鞭长莫及。")
                                self.scorea120()
                            else:
                                # tackle
                                print(str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"突破进入禁区，但被"+anotherplayer.name+"抢断。")
                    
                    # else:
                        # print(str(time)+"分钟，"+self.teama.name+"得到机会，"+whichplayer.name+"大力远射，但是效果不佳飞上看台")
        
        self.judge120()        




def Main():
    ph={}
    pa={}
    ph[0]=player(0.01,0.01,65,'纳瓦斯')
    ph[1]=player(3,10,30,'科雷尔')
    ph[2]=player(7,2,50,'蒂亚戈席尔瓦')
    ph[3]=player(1,5,21,'金彭贝')
    ph[4]=player(5,5,30,'贝尔纳特')
    ph[5]=player(3,3,60,'格耶')
    ph[6]=player(6,20,40,'马尔基尼奥斯')
    ph[7]=player(3,7,23,'帕雷德斯')
    ph[8]=player(20,33,6,'迪马利亚')
    ph[9]=player(40,40,2,'姆巴佩')
    ph[10]=player(50,60,2,'内马尔')

    pa[0]=player(0.01,0.01,60,'布尔基')
    pa[1]=player(1,7,30,'扎家杜')
    pa[2]=player(2,3,50,'胡梅尔斯')
    pa[3]=player(3,9,45,'皮实切克')
    pa[4]=player(6,10,25,'格雷罗')
    pa[5]=player(8,15,30,'维特塞尔')
    pa[6]=player(10,26,30,'埃木雷詹')
    pa[7]=player(8,10,25,'阿什拉夫')
    pa[8]=player(30,30,3,'索尔根阿扎尔')
    pa[9]=player(60,60,2,'哈兰德')
    pa[10]=player(40,40,1,'桑乔')

    # ph[0]=player(0.01,0.01,60,'Neuer')
    # ph[1]=player(3,17,15,'帕瓦尔')
    # ph[2]=player(2,3,23,'Boateng')
    # ph[3]=player(3,9,25,'Alaba')
    # ph[4]=player(6,10,25,'Davis')
    # ph[5]=player(8,15,25,'基米希')
    # ph[6]=player(10,26,20,'Thiago')
    # ph[7]=player(20,20,6,'格纳布里')
    # ph[8]=player(30,20,3,'Muller')
    # ph[9]=player(10,15,2,'Coutinho')
    # ph[10]=player(10,50,1,'齐尔科泽')

    # pa[0]=player(0.01,0.01,71,'Kepa')
    # pa[1]=player(13,10,40,'Azplicueta')
    # pa[2]=player(15,10,43,'Rudiger')
    # pa[3]=player(13,8,32,'Zouma')
    # pa[4]=player(20,10,31,'Emerson')
    # pa[5]=player(30,13,30,'Gilmor')
    # pa[6]=player(35,40,36,'Barkley')
    # pa[7]=player(30,15,30,'Cheek')
    # pa[8]=player(80,80,17,'Willian')
    # pa[9]=player(60,70,15,'Giroud')
    # pa[10]=player(60,60,20,'Pedro')
    
    liv=team(55,ph,'巴黎圣日尔曼')
    atm=team(45,pa,'多特蒙德')

    match0=match(liv,atm,1,2)
    match0.vs90()



if __name__=='__main__':
    Main()