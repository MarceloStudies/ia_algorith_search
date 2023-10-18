
import random as rd
import numpy as np

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, 
                valor2=None, anterior=None, proximo=None):
        # controle da árvore de busca
        self.pai       = pai
        # indica o nó do grafo
        self.estado    = estado
        # função de avaliação f(n) do método
        self.valor1    = valor1        
        # custo do caminho da origem até o nó atual
        self.valor2    = valor2     
        # controle da lista encadeada
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):
    
    def custo_uniforme(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      
    
    def greedy(self, inicio, fim):
        
        ind_f = nos.index(fim) 
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")

                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = h[ind_f][ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      


    def a_estrela(self, inicio, fim):
        
        ind_f = nos.index(fim)
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 + h[ind_f][ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"

    def aia_estrela(self, inicio, fim, limite):
        
        ind_f = nos.index(fim)
        while True:
            lim_exc = []
            l1 = lista()
            l2 = lista()
            visitado = []
            
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            #print("Limite: ",limite)
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == fim:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                    #print("Cópia da árvore:\n",l2.exibeLista())
                    #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
    
                    return caminho, atual.valor2
            
                ind = nos.index(atual.estado)
                for novo in grafo[ind]:
                    
                    ind1 = nos.index(novo[0])
                    
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[1]  # custo do caminho
                    v1 = v2 + h[ind_f][ind1] # f2(n)
    
                    if v1<=limite:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo[0]:
                                if visitado[j][1]<=v2:
                                    flag1 = False
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(novo[0], v1 , v2, atual)
                            l2.inserePos_X(novo[0], v1, v2, atual)
                            if flag2:
                                linha = []
                                linha.append(novo[0])
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
            limite = sum(lim_exc)/len(lim_exc)
                    
        return "Caminho não encontrado"
    
def gera_H(n):
    aux = busca()
    h = np.zeros((n,n),int)
    i = 0
    for no_origem in nos:
        j = 0
        for no_destino in nos:
            if no_origem != no_destino:
                cam, v  = aux.custo_uniforme(no_origem, no_destino)
                h[i][j] = v*rd.uniform(0,1)
            j += 1
        i += 1
    return h

nos = ["QUEST1","QUEST2","QUEST3","QUEST4","QUEST5",
       "QUEST6","QUEST7","QUEST8","QUEST9","QUEST10","QUEST11",
       "QUEST12","QUEST13","QUEST14","QUEST15","QUEST16",
       "QUEST17","QUEST18","QUEST19","QUEST20"]

grafo = [[["QUEST20",7.5], ["QUEST17",11.8], ["QUEST16",1.40]],
         [["QUEST18",8.5], ["QUEST14",1.01], ["QUEST7",9.0],["QUEST6",21.1]], 
         [["QUEST15",14.6], ["QUEST14",13.8], ["QUEST4",12.0]], 
         [["QUEST11",7.5], ["QUEST3",1.20]], 
         [["QUEST8",8.6]],
         [["QUEST16",9.9], ["QUEST2",2.11]], 
         [["QUEST2",9.0]], 
         [["QUEST18",9.8], ["QUEST5",8.6]], 
         [["QUEST19",9.2], ["QUEST12",8.7]],
         [["QUEST17",11.1],["QUEST11",7.0]], 
         [["QUEST10",7.0], ["QUEST4",7.5]], 
         [["QUEST9",8.7]], 
         [["QUEST20",7.1], ["QUEST16",15.1]],
         [["QUEST15",9.7], ["QUEST3",13.8], ["QUEST2",10.1]], 
         [["QUEST16",8.0], ["QUEST14",9.7], ["QUEST3",14.6]], 
         [["QUEST15",8.0], ["QUEST13",1.51], ["QUEST6",9.9], ["QUEST1",14.0]], 
         [["QUEST10",11.1], ["QUEST1",11.8]],
         [["QUEST19",14.2], ["QUEST8",9.8], ["QUEST2",8.5]], 
         [["QUEST18",14.2], ["QUEST9",9.2]], 
         [["QUEST13",7.1], ["QUEST1",7.5]]
        ]
# HEURISTICA SERVE SOMENTE PARA DESTINO QUEST2
sol = busca()
caminho = []
# gera a matriz de heurística
h = gera_H(len(nos))




def gerarAmbiente(inicio, final, tipo, limit):
    inicio = inicio.upper()
    final  = final.upper()
    if (tipo == 1):
        caminho, custo = sol.custo_uniforme(inicio,final)
        algoritimo = "custo_uniforme"
        
    if (tipo == 2):
        caminho, custo = sol.greedy(inicio,final)
        algoritimo = "greedy"

    if (tipo == 3):
        caminho, custo = sol.a_estrela(inicio,final)
        algoritimo = "A_estrela"

    if (tipo == 4):
        limite = limit
        caminho, custo = sol.aia_estrela(inicio,final,limite)
        algoritimo = "Aia_estrela"

    resposta_json = {
        "caminho": caminho[::-1],
        "custo": custo,
        "algoritimo": algoritimo
    }
    return resposta_json



