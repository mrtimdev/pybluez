import bluetooth

def find_bluetooth_device(device_name):
    print("Searching for Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    
    for addr, name in nearby_devices:
        print(f"Found device {name} with address {addr}")
        if name == device_name:
            print(f"Found target device {name} with address {addr}")
            return addr
    return None

def connect_to_printer(address):
    port = 1  # Bluetooth RFCOMM port
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((address, port))
        print(f"Connected to printer at address {address}")
        return sock
    except bluetooth.btcommon.BluetoothError as err:
        print(f"Failed to connect to printer: {err}")
        return None

def main():
    printer_name = "YourPrinterName"  # Replace with your printer's Bluetooth name
    printer_address = find_bluetooth_device(printer_name)
    
    if printer_address:
        printer_socket = connect_to_printer(printer_address)
        if printer_socket:
            # Send data to the printer
            printer_socket.send("Hello, Printer!")
            printer_socket.close()
    else:
        print("Printer not found.")

if __name__ == "__main__":
    main()
