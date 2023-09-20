from usocket import socket
from machine import Pin,SPI
import network
import time

is_server=False

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)

    if is_server: 
        #Server
        nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    else:
        #Client
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
    conn, addr = s.accept()
    print("Connect to:", conn, "address:", addr) 
    print("Loopback server Open!")
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL':
            conn.send(data)

def client_loop():
    print("Attempt Loopback client Connect!")

    s = socket()
    s.connect(s.getaddrinfo('192.168.1.20', 5000)) #Destination IP Address
    
    s.send(1)

    print("Loopback client Connect!")
    while True:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data+1)
        
def main():
    w5x00_init()
    
    if is_server:
        ###TCP SERVER###
        server_loop()
    else:
        ###TCP CLIENT###
        client_loop()

if __name__ == "__main__":
    main()