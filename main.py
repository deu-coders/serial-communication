import time
import serial

mode = input('Select mode (sender, receiver): ')

port = 'COM2'
baudrate = 9600
parity = serial.PARITY_ODD

ser = serial.Serial(
    port=port,
    baudrate=baudrate,
    parity=parity,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
)

ser.isOpen()

print(f'Serial port ongoing!!')
print(f'\tPort={port}')
print(f'\tBaudrate={baudrate}')
print(f'\tparity={parity}')
print()

while True:
    if mode == 'sender':
        message = input("나 (exit으로 종료) >> ")

        if message == 'exit':
            ser.close()
            exit()

        ser.write(bytearray(message + '\r\n', 'ascii'))

    elif mode == 'receiver':
        time.sleep(1)

        length = ser.in_waiting()
        if length == 0:
            continue

        print("상대방 >>", ser.read(length).decode('ascii'))

    else:
        print('Invalid mode.')
        break
