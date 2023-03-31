import socket
import player 
host = input("enter host name: ")  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

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

        # Print the player hands
        printPlayerHands(serverPlayer, clinetPlayer)

        # Loop until true
        while True:
            break

