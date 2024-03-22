from socket import *
HOST = ''
PORT = 50008 #server port



def requestServer():
    client_socket = socket(AF_INET, SOCK_STREAM) # initialize
    client_socket.connect((HOST, PORT)) # connect to the server socket port 

    message = input("Enter the word to Check in WordList: ")

    while message.lower().strip() != 'quit': #we use exit to terminate the program
        client_socket.send(message.encode()) # send the message by encoding

        response = client_socket.recv(1024).decode() # we receive the response from server and decode it

        print("Response from the server: " + response) # response result 

        message = input("Enter the word to Check in WordList: ")

    client_socket.close() # close the connection



if __name__ == '__main__':
    requestServer()

