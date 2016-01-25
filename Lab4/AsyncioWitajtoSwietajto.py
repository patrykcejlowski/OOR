import asyncio    #import biblioteki

def hello_world(loop):          #prosta funkcja od 0 do 9 drukuj Hello Swiecie
    for i in range(10):
        print("Hello Swiecie")
    loop.stop()

loop = asyncio.get_event_loop()  #pobierz klase z petla
loop.call_soon(hello_world, loop) # metoda wywolujaca asap nasza funkcje z 1 argumentem , inne tego typu delay or later
loop.run_forever()     #wykonuj tak dlugo, az ktos nie powie zeby sie zatrzymac, odwolanie w metodzie na koncu loop.stop

loop.close()

print("finished babe!")