# Run a Simple Web Server and Client

> `Ping` is not the only command to run on hosts!.
> We can use other commands avaialble in linux system. This includes job control such as `&`, `jobs`, `kill` using the `bash` command.

Let's start a simple HTTP server on `h1` and make a request from `h2` to `h1`.

    ```bash
    mininet> h1 python -m http.server 80 &
    mininet> h2 wget -O - h1
    
    
    ...
    # kill the webserver
    mininet> h1 kill %python
    ```

>NOTE: If mininet crashes for some reason, you need to clean it up by running `sudo mn -c`
