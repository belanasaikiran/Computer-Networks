# Link Variations

> Mininet 2.0 allows you to set link parameters, and these can even be set automatially from the command line.

To Set Link Variations, run:

    ```bash
    sudo mn --link tc,bw=10,delay=10ms
    ```

**NOTE**:

1. `--link` indicates that you're setting link properties.
2. `tc` tells Mininet to use the Traffic Control (TC) system for managing network traffic.
3. `bw=10` sets the bandwidth of the links to 10 Mbps (megabits per second).
4. `delay=10ms` adds a delay of 10 milliseconds to all packets traversing the links.

> Bandwidth: Limited to 10 Mbps, simulating a slower or constrained network connection.
> Delay: Packets experience a 10-millisecond delay, mimicking a network with propagation delays or congestion.

Output: I got some errors, I'm working on resolving them.

    ```bash
    n$ sudo mn --link tc,bw=10,delay=10ms
    *** Creating network
    *** Adding controller
    *** Adding hosts:
    h1 h2
    *** Adding switches:
    s1
    *** Adding links:
    (10.00Mbit 10ms delay) *** Error: Error: Specified qdisc kind is unknown.
    *** Error: RTNETLINK answers: No such file or directory
    *** Error: Error: Failed to find specified qdisc.
    (10.00Mbit 10ms delay) *** Error: Error: Specified qdisc kind is unknown.
    *** Error: RTNETLINK answers: No such file or directory
    *** Error: Error: Failed to find specified qdisc.
    (h1, s1) (10.00Mbit 10ms delay) *** Error: Error: Specified qdisc kind is unknown.
    *** Error: RTNETLINK answers: No such file or directory
    *** Error: Error: Failed to find specified qdisc.
    (10.00Mbit 10ms delay) *** Error: Error: Specified qdisc kind is unknown.
    *** Error: RTNETLINK answers: No such file or directory
    *** Error: Error: Failed to find specified qdisc.
    (h2, s1)
    *** Configuring hosts
    h1 h2
    *** Starting controller
    c0
    *** Starting 1 switches
    s1 ...(10.00Mbit 10ms delay) *** Error: Error: Specified qdisc kind is unknown.
    *** Error: RTNETLINK answers: No such file or directory
    *** Error: Error: Failed to find specified qdisc.
    (10.00Mbit 10ms delay) *** Error: Error: Specified qdisc kind is unknown.
    *** Error: RTNETLINK answers: No such file or directory
    *** Error: Error: Failed to find specified qdisc.

    *** Starting CLI:

    ```
Check link bandwidth:

    ```bash
    mininet> iperf
    ```

    output:

    ```bash
    mininet> iperf
    *** Iperf: testing TCP bandwidth between h1 and h2
    *** Results: ['57.5 Gbits/sec', '57.5 Gbits/sec']
    ```

Ping:

    ```bash
    mininet> h1 ping -c10 h2
    ```

    output:

    ```bash
    mininet> h1 ping -c10 h2
    PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
    64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=2.62 ms
    64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=1.44 ms
    64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.363 ms
    64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.092 ms
    64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.094 ms
    64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=0.073 ms
    64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=0.054 ms
    64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=0.071 ms
    64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=0.069 ms
    64 bytes from 10.0.0.2: icmp_seq=10 ttl=64 time=0.077 ms

    --- 10.0.0.2 ping statistics ---
    10 packets transmitted, 10 received, 0% packet loss, time 8997ms
    rtt min/avg/max/mdev = 0.054/0.495/2.616/0.815 ms
    ```
