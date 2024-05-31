import subprocess


def get_bluetooth_mac_windows():
    try:
        # getmac komutunu çalıştır ve çıktısını al
        result = subprocess.run(['getmac', '/v', '/fo', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('latin-1', errors='ignore')  # latin-1 kullanarak kodla

        # Bluetooth MAC adresini çıktıdan ayıkla
        for line in output.split('\n'):
            if 'Bluetooth Device' in line:
                next_line = output.split('\n')[output.split('\n').index(line) + 1]
                if 'Physical Address' in next_line:
                    mac_address = next_line.split(': ')[1].strip()
                    return mac_address
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


mac_address = get_bluetooth_mac_windows()
print(f"Bluetooth MAC Address: {mac_address}")

