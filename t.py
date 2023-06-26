import socket
from time import sleep

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 8080))
    s.listen(10)
    print('listening . . . ')
    conn, addr = s.accept()
    while True: 
        print(addr,'conected ')
        with open('received_file.txt', 'w') as f:
            data = conn.recv(1024)
            s = data.decode('utf-8')
            print('saved ')
            f.write(s)
        sleep(30)

