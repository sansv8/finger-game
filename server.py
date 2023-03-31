import socket
from player import *
host = input("enter host name: ")  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
waiting = False

# Handle action 
def handleAttack(yourHand, theirHand, player1, player2):
    # If hand is L
    if yourHand == "L":
        yourHand = 0
    else:
        yourHand = 1
    # If action is A
    if theirHand == "L":
        player1.attack(yourHand, player2.rightH)
    else:
        # If
        player1.attack(yourHand, player2.leftH)

# Handel Split
def handleSplit(hand, player):
    # If hand is L
    if hand == "L":
        hand = 0
    else:
        hand = 1
    
    # Split hand 
    player.split(hand)
    
# Print player hands
def printPlayerHands(player1, player2):
    print(f"Their hand:")
    print(f"{player2.leftH.fingers}\t{player2.rightH.fingers}\n\n")
    print(f"Your hand:")
    print(f"{player1.leftH.fingers}\t{player1.rightH.fingers}")

# Check win condition
def playerLoss(player):
    # If both fingers are 0
    if(player.leftH.fingers == 0 and player.rightH.fingers == 0):
        # Return true
        return True
    
    # Otherwise, return false
    return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        # Intiailize players
        serverPlayer = player(True, True)
        clinetPlayer = player(True, True)

        # Loop until true
        while True:
            # Print the player hands
            printPlayerHands(serverPlayer, clinetPlayer)

            # If state is waiting
            if waiting:
                # Print waiting
                print("Waiting...")

                # Wait for action 
                mode = conn.recv(1024).decode("utf-8")
                
                # If mode is a 
                if(mode == "A"):
                    # Get yourHand
                    yourHand = conn.recv(1024).decode("utf-8")

                    # Get their hand
                    theirHand = conn.recv(1024).decode("utf-8")

                    # Recieve the action
                    handleAttack(yourHand, theirHand, serverPlayer, clinetPlayer)
                # Otherwise if mode is s
                if(mode == "S"):
                    # Get hand to pslit
                    hand = conn.recv(1024).decode("utf-8")

                    # Handle split
                    handleSplit(hand, clinetPlayer)
            
                # Check if player has loss
                if(playerLoss(serverPlayer)):
                    # print you loss
                    print("You Loss")

                    # Break loop 
                    break

                # Change mode to waiting
                waiting = False

            # Otherwise, if waiting is false
            else:
                # Get mode from user
                yourMode = input("Attack or Split? (A/S)")
                conn.sendall(bytes(yourMode, "utf-8"))

                # If mode is "A"
                if(yourMode == "A"):
                    # Get hand to attack
                    handToAttack = input("What hand to attack? (L/R)")
                    conn.sendall(bytes(handToAttack, "utf-8"))

                    # Get hand to attack with
                    yourHand = input("Hand to attack with? (L/R)")
                    conn.sendall(bytes(yourHand, "utf-8"))

                    # Do attack
                    handleAttack(yourHand, handToAttack, clinetPlayer, serverPlayer)
                # If mode is "S"
                else:
                    # Get hand to split
                    handToSplit = input("Hand to split? (L/R)")
                    conn.send(bytes(handToSplit, "utf-8"))

                # Check if client player loss
                if(playerLoss(clinetPlayer)):
                    # Print you won 
                    print("You won")

                    # Break
                    break

                # Set waiting to be true
                waiting = True
                
                


