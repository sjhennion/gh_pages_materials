from usocket import socket
from machine import Pin,SPI
import network
import time
import utime

is_server=False
led = Pin(25, Pin.OUT)

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)

    if is_server: 
        nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    else:
        nic.ifconfig(('192.168.1.21','255.255.255.0','192.168.1.1','8.8.8.8'))
    
    print('IP address :', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    
def server_loop(): 
    s = socket()
    s.bind(('192.168.1.20', 5000)) #Source IP Address
    s.listen(5)
    
    print("TEST server")
    led.value(1)
    conn, addr = s.accept()
    print("Connect to:", conn, "address:", addr) 
    print("Loopback server Open!")
    while True:
        data = conn.recv(2048)
        # Server blinks three times fast on each data reception
        for x in range(3):
            led.value(1)
            utime.sleep_ms(50)
            led.value(0)
            utime.sleep_ms(50)
        print(data.decode('utf-8'))
        if data != 'NULL':
            conn.send(data)

def client_loop():
    print("Attempt Loopback client Connect!")

    s = socket()
    s.connect(('192.168.1.20', 5000)) #Destination IP Address
    
    s.send('1')

    print("Loopback client Connect!")
    while True:
        data = s.recv(2048)
        # Client blinks on off slow on data reception
        print(data.decode('utf-8'))
        if data != 'NULL' :
            led.value(1)
            utime.sleep_ms(500)
            led.value(0)
            utime.sleep_ms(500)
            data_int = int(data) + 1
            s.send(str(data_int))
        
def main():
    # Server blinks twice fast, three separate times
    if is_server:
        for x in range(3):
            for y in range(2):
                led.value(1)
                utime.sleep_ms(50)
                led.value(0)
                utime.sleep_ms(50)
            time.sleep(1)
    # Client blinks three times slow
    else:
        for y in range(3):
            led.value(1)
            utime.sleep_ms(500)
            led.value(0)
            utime.sleep_ms(500)

    w5x00_init()
    
    if is_server:
        server_loop()
    else:
        client_loop()

if __name__ == "__main__":
    main()
