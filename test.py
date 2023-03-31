import socket



def hostFn():
    myLH = 1
    myRH = 1
    notmyLH = 1
    notmyRH = 1

    host = input("enter host name: ")  
    if not host:
      host = "127.0.0.1" # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
              yourHand = input("Your hand (L/R): ")
              if yourHand == "L":
                yourHand = myLH
              else:
                yourHand = myRH
              theirHand = input("Their hand (L/R): ")
              if (theirHand == "L"):
                notmyLH = notmyLH + yourHand
              else:
                notmyRH = notmyRH + yourHand

              print(f"their hand:")
              print(f"{notmyLH}\t{notmyRH}\n\n")
              print(f"your hand:")
              print(f"{myLH}\t{myRH}")



              conn.sendall(bytes(str(yourHand), "utf-8"))
              conn.sendall(bytes(theirHand, "utf-8"))

              attack = conn.recv(1024).decode("utf-8") 
              

              direction = conn.recv(1024).decode("utf-8") 
              

              if direction == "L":
                myLH = myLH + int(attack)
              else:
                 myRH = myRH + int(attack)

              print(f"their hand:")
              print(f"{notmyLH}\t{notmyRH}\n\n")
              print(f"your hand:")
              print(f"{myLH}\t{myRH}")
              # out = input("Data to send: ")
              # conn.sendall(bytes(out, "utf-8"))
              # data = conn.recv(1024)
              # print(f"Received {data}")
   

def clientFn():
  myLH = 1
  myRH = 1
  notmyLH = 1
  notmyRH = 1
  host = input("enter host name: ")  # The server's hostname or IP address
  if not host:
    host = "127.0.0.1"

  PORT = 65432  # The port used by the server

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((host, PORT))
      # s.sendall(b"Connected!")
      while True:
        attack = s.recv(1024).decode("utf-8") 

        direction = s.recv(1024).decode("utf-8") 

        if direction == "L":
            myLH = myLH + int(attack)
        else:
           myRH = myRH + int(attack)

        print(f"their hand:")
        print(f"{notmyLH}\t{notmyRH}\n\n")
        print(f"your hand:")
        print(f"{myLH}\t{myRH}")

        yourHand = input("Your hand (L/R): ")
        if yourHand == "L":
          yourHand = myLH
        else:
           yourHand = myRH
        theirHand = input("Their hand (L/R): ")
        if (theirHand == "L"):
           notmyLH = notmyLH + yourHand
        else:
           notmyRH = notmyRH + yourHand
        
        print(f"their hand:")
        print(f"{notmyLH}\t{notmyRH}\n\n")
        print(f"your hand:")
        print(f"{myLH}\t{myRH}")
        s.sendall(bytes(str(yourHand), "utf-8"))
        s.sendall(bytes(theirHand, "utf-8"))



if __name__ == "__main__":
  hosting = input("do you want to host? (Y/N)")
  if hosting == "Y":
      hostFn()
  else:
      clientFn()