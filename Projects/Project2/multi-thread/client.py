from socket import * #import the socket library
HOST = '' # This can be empty as of now or we can pass localhost
PORT = 50008 #server port


# This function is used to request the server for the word to check in the wordlist
def requestServer(client_socket):
    print("--------------------------------------------")
    message = input("\n> Enter the word to check in WordList: ") # input the word to check in wordlist

    # If message is empty, do not send it to the server
    if message == "":
        requestServer(client_socket)
    elif message.lower().strip() == 'quit': #we use exit to terminate the program
        print("Exiting the program. Thank you for using the WordList Server")
        return
    else:
        print("Searching...")

    client_socket.send(message.encode()) # send the message by encoding
    # wait for the response from the server. do not close the connection until the response is received
    
    response = ''
    while True:
        chunk = client_socket.recv(1024).decode()
        if "END_OF_RESPONSE" in chunk:
            response += chunk.replace("END_OF_RESPONSE", "") # remove the END_OF_RESPONSE from the response 
            break
        response += chunk # append the chunk to the response
    
    # response = client_socket.recv(1024).decode() # we receive the response from server and decode it
    print("\nResponse from the server: \n" + response)

    # If the response is not empty, then we can request the server again
    if response != "":
        requestServer(client_socket)

    client_socket.close() # close the connection
        


def checkServerStatus():

    # properly handle the connection. If the server is not available, then we can't request the server
    client_socket = None
    #  A try block is used to catch the exceptions for checking the connection with the server
    try:
        client_socket = socket(AF_INET, SOCK_STREAM) # initialize the client socket
        client_socket.connect((HOST, PORT)) # connect to the server socket port
    except:
        print("Server is offline or not available. Please try again later.")
        return

    # If the server socket is connected, then we can request the server
    if client_socket:
        print("🔗 Connection Established with the server! ") # print the message
        print("Welcome to the WordList Server. Here you can check if the word is available in the wordlist. \nSimply pass `?` in the middle of the word to search all available words with your query")
        requestServer(client_socket) # request the server


#  main function
if __name__ == '__main__':
    checkServerStatus() # check the server status
