from socket import *                     # get socket constructor and constants
import time
import string
import _thread as thread

myHost = ''    # server machine, '' means local host
myPort = 50008 # assigning a random port


def now(): #This function provides the time stamp when called
    return time.ctime(time.time())

#  Our Recursive function to call itself again and again until all fields are satisfied to search the query
def searchQueryList(request):
    # print("search query called with ", request)
    query_combos = [] # storing all the searchable names [A-Z]
    missing_query_locations = [] # Know the no. of '?' provided in query - we store the indices of '?'

    if "?" in request: # check if '?' available in request
        for index in range(len(request)):
            if "?" == request[index]:
                missing_query_locations.append(index)
        
        # Add all searchable words for the missing characters to query_combos
        for location in range(len(missing_query_locations)):
                # print("query combo:  ", query_combos)
                if location == 0: # we compare to 0 to avoid re-updating the query_combos

                    for alphabet in string.ascii_lowercase: # add all letters for search

                        searchable = list(request) #convert request to list
                        searchable[missing_query_locations[location]] = alphabet
                        searchable = ''.join(searchable) #remove quotes and join the letters
                        # print("Request Searchable: ", searchable)
                        request_searchable = searchable
                        # update and re-update for multiple '?'
                        query_combos.append(request_searchable)


                else:
                    temp_combos = query_combos.copy() # create a copy of query_combos
                    query_combos = [] # empty the query_combos
                    for query in temp_combos:
                        for alphabet in string.ascii_lowercase:
                            searchable = list(query) # convert request word to list of characters
                            searchable[missing_query_locations[location]] = alphabet
                            searchable = ''.join(searchable)
                            query_combos.append(searchable) # append new string to query_combos


    else:
        query_combos.append(request)
    return query_combos


# result = searchQuery("a?a?m")
# print("Result: ", result)


def handleRequest(request, address): # function for handling the request
    print('💬  Client %s Requested word `%s` at %s' % (address, request, now()))
    #open file for checkin if the request available in the file
    WordList = open("../wordlist.txt", "r")
    response_data = [] #empty response
    
    query_combos = searchQueryList(request)
    # print("Query Combos to search: ", query_combos)

    for word in WordList:
        for query in range(len(query_combos)):
            if str(word) == query_combos[query] + "\n": #since we read the data from the file line by line, we need to add the new line since it's saved in it.
                response_data.append(str(word))



    WordList.close() #close the file
    return response_data # return response



#  Handle the Connection and decodes given input from the client

def handleClient(connection, address): # handling the request here
    # time.sleep(5)
    while True:
        request = connection.recv(1024).decode() # decode the data received from the client
        if not request:
            break

        check_message = "Checking if " + request + " available in the wordlist\n"
        connection.send(check_message.encode())

        response = [] # empty response
        response += handleRequest(request, address)

        # response is an array, we can send the response line by line
        no_of_responses = len(response)

        if no_of_responses > 0:
            message = "Found " + str(no_of_responses) + " matches for " + request + " in the word list: \n"
            connection.send(message.encode())

            for i in range(len(response)):
                connection.send(response[i].encode())

                if i == len(response) - 1:
                    connection.send("END_OF_RESPONSE".encode())

        else: # if response is empty, we append the message to the response
            wordNotFound = request + " not found in word list"
            connection.send(wordNotFound.encode())
            connection.send("END_OF_RESPONSE".encode())

        print('📨 Response for %s sent to Client %s at %s' % (request, address, now()))

    connection.close()



def dispatcher(): 
    server_socket = socket(AF_INET, SOCK_STREAM) # SO_REUSE_ADDR helps in rebindin
    server_socket.bind((myHost, myPort))
    server_socket.listen(5)

    print('🖥  Server started at', now())
    # Listens for client connections and dispatches a new thread to handle each connection.
    while True:     # wait for client connection,
        connection, address = server_socket.accept()   
        print('💻 Client ', address,' joined ', end=' ')
        print('at', now())
        thread.start_new_thread(handleClient, (connection, address))

dispatcher()
if __name__ == '__main__':
    dispatcher()    # call the dispatcher function