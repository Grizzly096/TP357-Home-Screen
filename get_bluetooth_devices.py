import asyncio
from bleak import BleakScanner

def main():
    scan()

async def scan():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(scan())