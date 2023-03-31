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
              # YOUR TURN
              yourMode = input("Attack or Split? (A/S)")
              
              if yourMode == "A":
                yourHand = input("Your hand (L/R): ")
                if yourHand == "L":
                  yourHand = myLH
                else:
                  yourHand = myRH
                theirHand = input("Their hand (L/R): ")
                if (theirHand == "L"):
                  notmyLH = notmyLH + yourHand
                  if notmyLH >= 5:
                    notmyLH = notmyLH - 5
                else:
                  notmyRH = notmyRH + yourHand
                  if notmyRH >= 5:
                    notmyRH = notmyRH - 5

                print(f"their hand:")
                print(f"{notmyLH}\t{notmyRH}\n\n")
                print(f"your hand:")
                print(f"{myLH}\t{myRH}\n")

                if (not notmyLH and not notmyRH):
                  conn.sendall(bytes("W", "utf-8"))
                  print("YOU WIN!!!!!!")
                  return 0
                conn.sendall(bytes(str(yourMode), "utf-8"))
                conn.sendall(bytes(str(yourHand), "utf-8"))
                conn.sendall(bytes(str(theirHand), "utf-8"))

              else:
                fingerSum = myLH + myRH
                toLeft = int(input("amount to go to left hand: ") )
                myLH = toLeft
                myRH = fingerSum - toLeft

                print(f"their hand:")
                print(f"{notmyLH}\t{notmyRH}\n\n")
                print(f"your hand:")
                print(f"{myLH}\t{myRH}\n")

                conn.sendall(bytes(str(yourMode), "utf-8"))
                conn.sendall(bytes(str(myLH), "utf-8"))
                conn.sendall(bytes(str(myRH), "utf-8"))

              # THEIR TURN
              mode = conn.recv(1024).decode("utf-8")
              if mode == "W":
                myLH = 0
                myRH = 0
                print(f"their hand:")
                print(f"{notmyLH}\t{notmyRH}\n\n")
                print(f"your hand:")
                print(f"{myLH}\t{myRH}\n")
                print("YOU LOSE")
                return 0
              
              if mode == "A":
                attack = conn.recv(1024).decode("utf-8") 


                direction = conn.recv(1024).decode("utf-8") 


                if direction == "L":
                  myLH = myLH + int(attack)
                  if myLH >= 5:
                    myLH = myLH - 5
                else:
                  myRH = myRH + int(attack)
                  if myRH >= 5:
                    myRH = myRH - 5
              else:
                notmyLH = int(conn.recv(1024).decode("utf-8") )

                notmyRH = int(conn.recv(1024).decode("utf-8") )


              print(f"their hand:")
              print(f"{notmyLH}\t{notmyRH}\n\n")
              print(f"your hand:")
              print(f"{myLH}\t{myRH}\n")



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
        # THEIR TURN
        mode = s.recv(1024).decode("utf-8")
        
        if mode == "W":
          myLH = 0
          myRH = 0
          print(f"their hand:")
          print(f"{notmyLH}\t{notmyRH}\n\n")
          print(f"your hand:")
          print(f"{myLH}\t{myRH}\n")
          print("YOU LOSE")
          return 0

        if mode == "A":
          attack = s.recv(1024).decode("utf-8") 

          direction = s.recv(1024).decode("utf-8") 

          if direction == "L":
              myLH = myLH + int(attack)
              if myLH >= 5:
                myLH = myLH - 5
          else:
            myRH = myRH + int(attack)
            if myRH >= 5:
                myRH = myRH - 5

          
        else :
          notmyLH = int(s.recv(1024).decode("utf-8") )

          notmyRH = int(s.recv(1024).decode("utf-8") )

        print(f"their hand:")
        print(f"{notmyLH}\t{notmyRH}\n\n")
        print(f"your hand:")
        print(f"{myLH}\t{myRH}\n")


        # YOUR TURN

        yourMode = input("Attack or Split? (A/S)")
        
        if yourMode == "A":
          yourHand = input("Your hand (L/R): ")
          if yourHand == "L":
            yourHand = myLH
          else:
            yourHand = myRH
          theirHand = input("Their hand (L/R): ")
          if (theirHand == "L"):
            notmyLH = notmyLH + yourHand
            if notmyLH >= 5:
              notmyLH = notmyLH - 5
          else:
            notmyRH = notmyRH + yourHand
            if notmyRH >= 5:
              notmyRH = notmyRH - 5
          
          print(f"their hand:")
          print(f"{notmyLH}\t{notmyRH}\n\n")
          print(f"your hand:")
          print(f"{myLH}\t{myRH}\n")

          if (not notmyLH and not notmyRH):
            s.sendall(bytes("W", "utf-8"))
            print("YOU WIN!!!!!!")
            return 0
          
          s.sendall(bytes(yourMode, "utf-8"))
          s.sendall(bytes(str(yourHand), "utf-8"))
          s.sendall(bytes(theirHand, "utf-8"))
        
        else:
          fingerSum = myLH + myRH
          toLeft = int(input("amount to go to left hand: ") )
          myLH = toLeft
          myRH = fingerSum - toLeft

          print(f"their hand:")
          print(f"{notmyLH}\t{notmyRH}\n\n")
          print(f"your hand:")
          print(f"{myLH}\t{myRH}\n")

          s.sendall(bytes(yourMode, "utf-8"))
          s.sendall(bytes(myLH, "utf-8"))
          s.sendall(bytes(myRH, "utf-8"))




if __name__ == "__main__":
  hosting = input("do you want to host? (Y/N)")
  if hosting == "Y":
      hostFn()
  else:
      clientFn()