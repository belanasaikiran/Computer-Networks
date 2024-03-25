# Project 2: Socket Programming

    Name: Sai Kiran Belana
    Course: Computer Networks and Data Communications 
    Course No: CSE 5299
    NetID: skb23007


## Searchable Word List Server using TCP Sockets

The WordList Server is a simple TCP server written in Python that searches for English words matching a given pattern from a client. It supports wildcard searches using '?' where '?' can be replaced by any letter. The server responds with matching words from a predefined word list file called `wordlist.txt`.

### Main Features

* **TCP Socket Programming**: Utilizes TCP sockets for reliable communication between client and server.
* **Wildcard Search**: Supports queries with '?' as a wildcard for any letter.
* **Multi-Query Support**: Handles multiple query combinations generated from wildcard patterns.
* **Single-Threaded**: Processes one client request at a time in a sequential manner.

### Protocol Description

We use TCP sockets for communication between the client and server. 


## Single Thread Application:

The single-threaded application consists of a client and server that communicate over a TCP socket. The client sends a query to the server, and the server responds with matching words from the word list.

The server is single-threaded, meaning it can handle only one client connection at a time. The server listens for incoming client connections and processes the client's query sequentially.

### Results:

![single-thread-app-demo.png](./images/single-thread-app-demo.png)

### Code Files:

1. [./single-thread/client.py](./single-thread/client.py)
2. [./single-thread/server.py](./single-thread/server.py)

### Client

The client.py file is a simple client that sends a query to the server and waits for the server to respond. 

![single-thread-client.png](./images/single-thread-client.png)

We use the `socket` module to create a socket object and connect to the server. We have defined a function called `requestServer()` that connects to server socket and sends the user query to the server and waits for the server to respond. 

Client mainly involves two functions in order of execution:

1. **checkServerStatus()**: Checks if the server is running and accepting connections.

    This function tries to connect to the server socket. If the connection is successful, it prints `🔗 Connection Established with the server! ` and executes `requestServer()` function.

2. **requestServer()**: Sends a query to the server and waits for the server to respond.

    This function sends the user query to the server and waits for the server to respond. It reads the response from the server and prints the response to the console. The client sends the query to the server using the `client_socket.send()` function and receives the response using the `client_socket.recv()` function. The client also checks for the `END_OF_RESPONSE` string to confirm the final response is received from the server.

### Server Implementation

The server.py file is a simple TCP server that listens for incoming client connections and processes the client's query.

![single-thread-server.png](./images/single-thread-server.png)

### Libraries Used:

1. `socket` - to create a socket object and bind it to a specific port.
2. `time` - to get the current time stamp
3. `string` - to generate all possible query combinations based on the wildcard pattern.

### Code Functionality

The server.py file mainly involves five functions in order of execution: 

1. **dispatch()**: Main loop of the server, accepting client connections and handling them.

    This function handles the socket creation, binding, and listening. It accepts incoming client connections and creates a new thread to handle each client request. The server listens on port 50008 for incoming connections which can be configured by changing the variable `myHost`.

    The server runs indefinitely until the user interrupts the program using `Ctrl+C`. The server logs the activity using the `now()` function, which returns the current timestamp in a human-readable format.

2. **now()**: Returns the current timestamp in a human-readable format. This function is used by **dispatch()** to log the server's activity.

3. **handleClient()**: Manages communication with the connected client, receiving data, and sending responses.

    This function reads the query from the client, acknowledges the client's query,
    uses `handleRequest()` function to process the query, and sends the response back to the client. 
    
    We also send `END_OF_RESPONSE` to the client to indicate the end of the response which is checked by the client to confirm the final response is received.
    
    The server logs the client's query and the matching words found in the word list using `now()` function.

4. **handleRequest()**: Handles incoming queries, searches for matching words, and generates the response.

    This function processes the query received from the client and searches for matching words in the word list using the received output `query_combos` array from `searchQueryList()` function . It generates all possible query combinations based on the wildcard pattern and searches for matching words in the word list. The function returns a list of matching words found in the word list.

5. **searchQueryList()**: Searches for matching words in the word list based on the query pattern.

    This function generates all possible query combinations based on the wildcard pattern and searches for matching words in the word list. It returns a list of matching words found in the word list.


### Test Cases & Results:

1. **Query with no wildcard**:
    * Query: `apple`
    * Expected Response: 
    ```bash
    ✔️ 200 OK
    apple
    ```

    ![apple-query.png](./images/apple-query.png)

2. **Query with a single wildcard**:
    * Query: `a?ple`
    * Expected Response: 
    ```bash
       ```bash
    ✔️ 200 OK
    ['ample', 'apple']
    ```

    ![a-ple-query.png](./images/a-ple-query.png)

3. **Query with multiple wildcards**:
    * Query: `?p?le`
    * Expected Response: 
    ```bash
    ✔️ 200 OK
    ['ample', 'apple', 'opale', 'upile']
    ```

    ![p-le-query.png](./images/p-le-query.png)

4. **Query with no matching words**:
    * Query: `xyz`
    * Expected Response: 
    ```bash
    ❌ 404 Not Found
    ```

    ![xyz-query.png](./images/xyz-query.png)



---


## Multi-Threaded Application:

![multi-thread-app-demo.png](./images/multi-thread-app-demo.png)

This application is an extension of the single-threaded application with the following features:

* **Multi-Threaded Server**: Supports multiple client connections concurrently using threads.
* **Client Threads**: Each client connection is handled by a separate thread on the server.


### Code Files:

1. [./multi-thread/client.py](./multi-thread/client.py)
2. [./multi-thread/server.py](./multi-thread/server.py)



### Additional Libraries Used:

1. `_thread` - to create and manage threads for each client connection.

### Client

The client.py file is a copy of the single-threaded client with no changes. It performs the same functions as the single-threaded client.

### Server

The server.py file is an extension of the single-threaded server with multi-threading support. It creates a new thread for each client connection to handle multiple client connections concurrently.

We use the `_thread` module to create and manage threads for each client connection. 

The server creates a new thread for each client connection using the `thread.start_new_thread()` function.


### Test Cases & Results for Multi-Threaded Application:

1. **Multiple Client Connections**:
    
    * Query: `a?ple` from Client 1
    * Query: `?p?le` from Client 2

    ![multi-thread-results](./images/multi-thread-results.png)

    The server handles multiple client connections concurrently using threads. Each client connection is handled by a separate thread on the server. The server logs the client's query and the matching words found in the word list for each client connection.

2. **Client Disconnect Handling**:

    The server handles client disconnects gracefully by closing the client socket and removing the client thread from the active threads list.

    ![client-disconnect.png](./images/client-disconnect.png)

    The server logs the client's IP address and port number when a client disconnects from the server.


---


### Execution Instructions:

1. **Single-Threaded Application**:

    1. Open two terminal windows.
    2. In the first terminal, run the server using the command:
        ```
        python server.py
        ```
    3. In the second terminal, run the client using the command:
        ```
        python client.py
        ```
    4. Enter the query pattern in the client terminal and press `Enter`.
    5. The client will display the matching words found in the word list.

2. **Multi-Threaded Application**:

    1. Open three terminal windows.
    2. In the first terminal, run the server using the command:
        ```
        python server.py
        ```
    3. In the second terminal, run the client using the command:
        ```
        python client.py
        ```
    4. In the third terminal, run another client using the command:
        ```
        python client.py
        ```    
    4. Enter the query pattern in the client terminal and press `Enter`.
    5. The client will display the matching words found in the word list.

    ### Note:

    You can observe the server displays the client's IP address and port number for each client connection. 


### Trade-offs:

1. Scalability & Performance: 
    * **Single-Threaded**: Can handle only one client connection at a time.
    * **Multi-Threaded**: Supports multiple client connections concurrently.
    Utilizing a single-thread per client model increases overhead due to context switching and thread management, especially with a large number of concurrent clients.

    Solution: Implement a thread pool to limit the number of threads created and reuse threads for handling multiple client connections.

2. Concurrency:
    * **Single-Threaded**: Processes client requests sequentially.
    * **Multi-Threaded**: Processes client requests concurrently using threads.
    Multi-threading introduces complexity in managing shared resources.

    Solution: Implement thread synchronization mechanisms such as locks, or message queues to manage shared resources and prevent

3. Resource Utilization:
    * **Single-Threaded**: Uses fewer resources as it handles one client at a time.
    * **Multi-Threaded**: Uses more resources due to multiple threads running concurrently.
    Multi-threading can lead to resource contention and synchronization issues.

    Solution: Optimize the number of threads created and use thread pools to manage resources efficiently.

4. Complexity in Handling Large Responses:

    Sending large responses by breaking them into chunks and using a special "END_OF_RESPONSE" message to signal completion adds complexity to both client and server logic.

    Solution: Streamline communication protocol by sending the response data size ahead of the actually sending the data. This allows the client to know exactly how much data to expect before the transmission is complete.

5. Error Handling: 

    The current implementation might not robustly handle all potential error scenarios, such as client disconnects during data transmission or file read     errors. 

    Solution: Implement more robust error handling mechanisms to gracefully handle errors and edge cases.

### Fixes and Improvements:

https://stackoverflow.com/questions/5875177/how-to-close-a-socket-left-open-by-a-killed-program
