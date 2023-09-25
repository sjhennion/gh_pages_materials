from usocket import socket
from machine import Pin,SPI
import network
import time
import utime

led = Pin(25, Pin.OUT)

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)

    print('Client')
    nic.ifconfig('dhcp')
    
    print('IP address :', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    
def client_loop():
    print("Attempt Loopback client Connect")

    s = socket()
    utime.sleep_ms(4000)
	# Connect to PC
    s.connect(('192.168.1.100', 5000)) #Destination IP Address

    s.send('1')

    start_time = time.ticks_ms() 
    print("Loopback client Connect!")
    for x in range(999):
        data = s.recv(16)
        print(data.decode('utf-8'))
        if data != 'NULL':
            data_int = int(data) + 1
            s.send(str(data_int))
    end_time = time.ticks_ms() 

    print("Total time: ", time.ticks_diff(end_time, start_time))

        
def main():
    # Client blinks three times slow
    for y in range(3):
        led.value(1)
        utime.sleep_ms(500)
        led.value(0)
        utime.sleep_ms(500)

    w5x00_init()
    
    client_loop()

if __name__ == "__main__":
    main()
