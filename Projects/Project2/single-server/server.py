from socket import *                     # get socket constructor and constants
import time
import string

myHost = ''    # server machine, '' means local host
myPort = 50008 # assigning a random port

server_socket = socket(AF_INET, SOCK_STREAM) # SO_REUSE_ADDR helps in rebindin
server_socket.bind((myHost, myPort))
server_socket.listen(5)


def now(): #This function provides the time stamp when called
    return time.ctime(time.time())

#  Our Recursive function to call itself again and again until all fields are satisfied to search the query
def searchQuery(request):
    print("search query called with ", request)
    query_combos = [] # storing all the searchable names [A-Z]
    missing_query_locations = [] # Know the no. of '?' provided in query - we store the indices of '?'

    if "?" in request: # check if '?' available in request
        for index in range(len(request)):
            if "?" == request[index]:
                missing_query_locations.append(index)
        
        # Add all searchable words for the missing characters to query_combos
        for location in range(len(missing_query_locations)):
                print("query combo:  ", query_combos)
                if location == 0:

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


def handleRequest(request): # function for handling the request
    print('Echo => %s at %s' % (request, now()))
    print("request received: ", request)
    #open file for checkin if the request available in the file
    WordList = open("../wordlist.txt", "r")
    response_data = '' #empty response
    found = False # default is False
    
    query_combos = searchQuery(request)
    print("Query Combos to search: ", query_combos)

    for word in WordList:
        for query in query_combos:
            if str(word) == query + "\n": #since we read the data from the file line by line, we need to add the new line since it's saved in it.
                response_data = str(word)
                found = True # set bool to true when the matching word found.
                print("match found for ", word)
                break            # break if match is found
        if found:
            break



    if found == False:
        response_data = request + " not found in word list"
    
    WordList.close() #close the file
    return response_data # return response

def handleClient(connection): # handling the request here
    time.sleep(5)
    while True:
        data = connection.recv(1024).decode() # decode the data received from the client
        if not data:
            break

        response = handleRequest(data)
        connection.send(response.encode())

    connection.close()



def dispatcher():     
    while True:     # wait for client connection,
        connection, address = server_socket.accept()   
        print('Server connected by Client ', address, end=' ')
        print('at', now())
        handleClient(connection)

dispatcher()
if __name__ == '__main__':
    dispatcher()    # call the dispatcher function