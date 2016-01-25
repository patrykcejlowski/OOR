# *-* Utf-8 *-*
import asyncio

#dwie funkcje

@asyncio.coroutine #zaznaczamy jako wspolbieznosc, daje mozliwosc zatrzymania(zawieszenia) funkcji  i powrotu
def goodbye_world():
    for i in range(10):
        print("Żegnaj okrutny Świecie!")
        yield from asyncio.sleep(1)

@asyncio.coroutine
def hello_world():
    for i in range(10):
        print("Witaj okrutny Świecie!")
        yield from asyncio.sleep(1) #funkcja ustepuje, bez tego sie zapetli i nie ustapi miejsca innym, wraca do loopera
                                    #looper wybiera nastepna
loop = asyncio.get_event_loop()    #tworzymy pętle
hello = asyncio.ensure_future(hello_world())  #zamienia funkcje na zadanie i wrzuca w rejestr, mozna uzyc async ale wymiera
goodbye = asyncio.ensure_future(goodbye_world())
loop.run_forever() #działa w nieskończoność

loop.close()


print("Skonczylimy!")