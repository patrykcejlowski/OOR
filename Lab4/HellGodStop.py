# *-* Utf-8 *-*
import asyncio
import sys

#dwie funkcje

@asyncio.coroutine
def goodbye_world():
    for i in range(10):
        print("Żegnaj okrutny Świecie!")
        yield from asyncio.sleep(1)

@asyncio.coroutine
def hello_world():
    for i in range(10):
        print("Witaj okrutny Świecie!")
        yield from asyncio.sleep(1)

def wait_input(loop, tasks):
    print("Zatrzymuje")
    for t in tasks():
        t.cancel()
    loop.stop()
loop = asyncio.get_event_loop()
hello = asyncio.ensure_future(hello_world())
goodbye = asyncio.ensure_future(goodbye_world())

print("Wcisnij dowolny przycisk, aby zatrzymać...")
loop.add_reader(sys.stdin, wait_input, loop, [hello, goodbye])

loop.run_forever()

loop.close()


print("Skonczylimy!")