# Regression Test

1. To do a regression test without dropping in to the CLI, Run

    ```bash
    sudo mn --test pingpair
    ```

    output:

    ```bash
    sanju@SANJU:~/ComputerNetworks/Python$ sudo mn --test pingpair
    *** Creating network
    *** Adding controller
    *** Adding hosts:
    h1 h2
    *** Adding switches:
    s1
    *** Adding links:
    (h1, s1) (h2, s1)
    *** Configuring hosts
    h1 h2
    *** Starting controller
    c0
    *** Starting 1 switches
    s1 ...
    *** Waiting for switches to connect
    s1
    h1 -> h2
    h2 -> h1
    *** Results: 0% dropped (2/2 received)
    *** Stopping 1 controllers
    c0
    *** Stopping 2 links
    ..
    *** Stopping 1 switches
    s1
    *** Stopping 2 hosts
    h1 h2
    *** Done
    completed in 5.730 seconds
    ```

    > This command created a minimal topology, started up the OpenFlow reference controller, ran an all-pairs-ping test, and tore down both the topology and the controller.

2. You can also test with `iperf`

   ```bash
   sudo mn --test iperf
   ```

   output:

   ```bash
   sanju@SANJU:~/ComputerNetworks/Python$ sudo mn --test iperf
    *** Creating network
    *** Adding controller
    *** Adding hosts:
    h1 h2
    *** Adding switches:
    s1
    *** Adding links:
    (h1, s1) (h2, s1)
    *** Configuring hosts
    h1 h2
    *** Starting controller
    c0
    *** Starting 1 switches
    s1 ...
    *** Waiting for switches to connect
    s1
    *** Iperf: testing TCP bandwidth between h1 and h2
    *** Results: ['47.1 Gbits/sec', '47.1 Gbits/sec']
    *** Stopping 1 controllers
    c0
    *** Stopping 2 links
    ..
    *** Stopping 1 switches
    s1
    *** Stopping 2 hosts
    h1 h2
    *** Done
    completed in 11.558 seconds
   ```
