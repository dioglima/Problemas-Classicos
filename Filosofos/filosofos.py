from random import uniform
import threading
from time import sleep

NUM_FILOSOFOS = 5
pratos = [0, 0, 0, 0, 0]

hashi = [threading.Semaphore(1) for i in range(NUM_FILOSOFOS)]


def filosofo(id):
    while True:
        print(f"Filosofo {id} esta pensando \n")

        sleep(uniform(5, 10))

        print(f"Filosofo {id} esta com fome \n")
        pegar_hashi(id)

        print(f"Filosofo {id} esta comendo. \n")
        sleep(uniform(5, 15))

        print(f"Filosofo {id} terminou de comer. \n ")
        colocar_hashi(id)

        pratos[id] += 1
        print(pratos)


def pegar_hashi(id):
    hashi_esquerda = id
    hashi_direita = (id + 1) % NUM_FILOSOFOS

    hashi[hashi_esquerda].acquire()
    hashi[hashi_direita].acquire()


def colocar_hashi(id):
    hashi_esquerda = id
    hashi_direita = (id + 1) % NUM_FILOSOFOS

    hashi[hashi_esquerda].release()
    hashi[hashi_direita].release()


filosofos = []
for i in range(NUM_FILOSOFOS):
    filosofo_thread = threading.Thread(target=filosofo, args=(i,))
    filosofo_thread.start()
    filosofos.append(filosofo_thread)


for filosofo_thread in filosofos:
    filosofo_thread.join()
