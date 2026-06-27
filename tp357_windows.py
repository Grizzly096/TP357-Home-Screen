from bleak import BleakScanner
import asyncio

TARGET = {
    "mac": ["E4:61:74:61:E6:D1", "C3:E5:C1:52:81:2B"],
    "name": "TP357S"
}

DATA = {
    "temperature": None,
    "humidity": None
}

def parse(key, data):
    print(f"parse() called with key=0x{key:04X}, raw_data={list(data)}")
    data = list(data)

    # Sanity check: low byte of key should always be 0xC2 for TP357
    if (key & 0xFF) != 0xC2:
        return None
    if len(data) < 2:
        return None

    # The high byte of the company ID key IS the low byte of temperature!
    temp_low  = (key >> 8) & 0xFF  # e.g. key=0x4CC2 → 0x4C = 76
    temp_high = data[0]            # e.g. 0x01 = 1

    temp_raw = (temp_high << 8) | temp_low  # 0x014C = 332
    temperature = temp_raw / 10.0                  # 33.2°C ✓

    humidity = data[1]                      # 0x34 = 52% ✓

    print(f"parse() -> temp_raw={temp_raw}, temperature={temperature:.1f}, humidity={humidity}")
    return temperature, humidity

def callback(device, advertisement_data):
    # include device name (may be None)
    name = device.name or "unknown"
    print(f"callback() device={device.address} name={name} RSSI={advertisement_data.rssi}")
    if device.address.upper() not in TARGET["mac"] and not name in TARGET["name"]:
        print("  -> not target, ignoring")
        return

    print("  -> target matched, processing manufacturer data")

    for key, data in advertisement_data.manufacturer_data.items():
        print(f"RAW key=0x{key:04X}, data={list(data)}")
        parsed = parse(key, data)
        if parsed:
            temperature, hum = parsed
            print(f"  → temperature={temperature:.1f}°C  HUM={hum}%  RSSI={advertisement_data.rssi}")
            DATA["temperature"] = temperature;
            DATA["humidity"] = hum;
            return
async def start():
    print("start() initializing scanner")
    scanner = BleakScanner(callback)
    print("start() starting scanner")
    await scanner.start()
    print("start() scanner running for 30s")
    await asyncio.sleep(20)
    print("start() stopping scanner")
    await scanner.stop()
    return DATA
