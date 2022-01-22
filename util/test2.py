#!/usr/bin/env python3 
import asyncio
import time
from contextlib import suppress
import signal
from concurrent.futures import CancelledError

run_inner = False

# There are two concurrent outer loops that run forever.

# The first just runs on its own.
async def outer_long_one():
    while True:
        print("Outer long one")
        await asyncio.sleep(5)

# The second runs and checks a queue for new work to do
async def outer_long_two():
    global run_inner

    while True:
        print("Outer long two")
        if run_inner:
            run_inner = False
            await run_inner_funcs()
        await asyncio.sleep(0.5)

# When the 2nd outer loop is triggered (when run_inner is true)
# It runs a setup function that prepares and launches 3 async processes
async def run_inner_funcs():
    print("Setting up inner funcs")
    loop = asyncio.get_running_loop()

    long = asyncio.ensure_future(inner_long())
    one_two = asyncio.gather(inner_short_one(),inner_short_two())
    await one_two
    long.cancel()

# The first process should keep running as long as the other two are running.
# The length of the other two cannot be determined
async def inner_long():
    while True:
        print("\tInner long")
        await asyncio.sleep(1)

# The other two functions are relatively quick - under a minute of wall time
# But they might be 5 seconds and might be 45 seconds
async def inner_short_one():
    print("\tInner short one")
    await asyncio.sleep(5)
    print("\tInner short one (2)")

# The other two functions are relatively quick - under a minute of wall time
# But they might be 5 seconds and might be 45 seconds
async def inner_short_two():
    print("\tInner short two")
    await asyncio.sleep(2)
    print("\tInner short two (2)")


# The script should handle SIGINT gracefully to do final cleanup
def shutdownfunc(signo,stackframe):
    for t in asyncio.all_tasks():
        t.cancel()

    print("Shutting down with " + str(signo))

# And it should handle SIGUSR1, which sets the run_inner variable and allows outer_long_two to call the inner funcs.
def siguserfunc(signo,stackframe):
    print("Sig usr1 func")
    global run_inner
    run_inner = True

async def main():
    try: 
        await asyncio.gather(asyncio.shield(outer_long_one()),asyncio.shield(outer_long_two()))
    except asyncio.exceptions.CancelledError:
        # Exception will be thrown when we cancel in sigterm/sigint
        pass

# Set up signal handlers
signal.signal(signal.SIGINT,shutdownfunc)
signal.signal(signal.SIGTERM,shutdownfunc)
signal.signal(signal.SIGUSR1,siguserfunc)

asyncio.run(main())
