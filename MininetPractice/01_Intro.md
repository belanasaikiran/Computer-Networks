# Intro

## Installation

## Virtual Machine or Ubuntu(Dual Boot)

> If you are using Virtual Box or Dual Booting, most likely you shouldn't facing any issue in installing mininet software. Just run the below commands on your ubuntu machine.

1. Install mininet software on **Ubuntu-22.04**

    ```bash
    sudo apt install mininet
    ```

2. Install mininet ovs test controller.

    ```bash
    sudo apt install openvswitch-testcontroller
    ```

3. Install Wireshark

    ```bash
    sudo apt install wireshark
    ```
---

### Mininet in Windows Subsystem for Linux

> I have setup the **mininet** and **wireshark** on WSL. **The default `microsoft-standard-wsl` kernel does not support `openvswitch`**. So, I have followed this below link to add the `openvswitch` and rebuild the existing kernel and updated it to support.

Link: [https://zenn.dev/takai404/articles/9c96d5d1bcc9d0](https://zenn.dev/takai404/articles/9c96d5d1bcc9d0)

**Error**: BTF: .tmp_vmlinux.btf: pahole (pahole) is not available

**Fix** -> Try to install dwarves:
([https://stackoverflow.com/questions/61657707/btf-tmp-vmlinux-btf-pahole-pahole-is-not-available](https://stackoverflow.com/questions/61657707/btf-tmp-vmlinux-btf-pahole-pahole-is-not-available))

```bash
$sudo apt install dwarves
```

> NOTE: You have to rebuild your existing WSL kernel to make `openvswitch` & `mininet` work.

### Controller

1. If incase the `mininet` has no controller available, then you can install the `ovs-testcontroller` or any other controller which runs on port `6653`.

2. Install the controller using `sudo apt install openvswitch-testcontroller`

3. Check if the controller is running

    ```bash
    sudo systemctl status openvswitch-testcontroller
    ```

4. Make sure you clean up the mininet before launching.

    ```bash
    sudo mn -c #cleans up mininet and any process running under it.
    ```

5. [Not required if you are not facing any issue with the test controller] You can also install any other controller like [POX](git clone https://github.com/noxrepo/pox), `RYU` for remote controllers.

**Error:**  Error: shutdown controller which is running on port 6653

-> Fix: Ref - https://github.com/intrig-unicamp/mininet-wifi/issues/96

 You need to kill the existing port and clean mininet.

 ```bash
 #killing port of controller
 sudo fuser -k 6653/tcp 
 
 #cleaning mininet
 sudo mn -c 
 ```

## Running Mininet / Starting with Mininet

> **Reference:** [https://mininet.org/walkthrough/](https://mininet.org/walkthrough/)

1. At default, mininet creates to hosts, one controller and one switch by running.

    ```bash
    sudo mn
    ```

    Output:

    ```bash
    $ sudo mn
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
    *** Starting CLI:
    mininet>

    ```

2. If you would like to launch your own topology(let's say 4 hosts), you can run the following command.

    ```bash
    sudo mn --topo=single,4 # creating 4 hosts, a switch and a controller
    ```bash
    Output:
    ```bash
    $ sudo mn --topo=single,4
    *** Creating network
    *** Adding controller
    *** Adding hosts:
    h1 h2 h3 h4
    *** Adding switches:
    s1
    *** Adding links:
    (h1, s1) (h2, s1) (h3, s1) (h4, s1)
    *** Configuring hosts
    h1 h2 h3 h4
    *** Starting controller
    c0
    *** Starting 1 switches
    s1 ...
    *** Starting CLI:
    mininet>
    ```

3. Check the `network` by running `net` command.
    > This command shows all the devices/nodes that are exising in your topology. This includes switches and controllers as well.

    Output:

    ```bash
    mininet> net
    h1 h1-eth0:s1-eth1
    h2 h2-eth0:s1-eth2
    h3 h3-eth0:s1-eth3
    h4 h4-eth0:s1-eth4
    s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:h3-eth0 s1-eth4:h4-eth0
    c0
    ```

4. To check the bandwidth from first node to the last one. Run `iperf`.
    > This will show the link bandwidth b/w two hosts/nodes.
    Output:

    ```bash
    mininet> iperf
    *** Iperf: testing TCP bandwidth between h1 and h4
    *** Results: ['60.2 Gbits/sec', '60.1 Gbits/sec']
    ```

    If you want to check bandwidth b/w specific nodes, run `iperf h2 h3`.

5. To Ping all the hosts, just run `pingall` command.

    ```bash
    mininet> pingall
    *** Ping: testing ping reachability
    h1 -> h2 h3 h4
    h2 -> h1 h3 h4
    h3 -> h1 h2 h4
    h4 -> h1 h2 h3
    *** Results: 0% dropped (12/12 received)
    ```

6. Test connectivity between hosts by running. Ping from one host to another

    ```bash
    mininet> h1 ping -c 2 h3
    PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
    64 bytes from 10.0.0.3: icmp_seq=1 ttl=64 time=0.119 ms
    64 bytes from 10.0.0.3: icmp_seq=2 ttl=64 time=0.099 ms

    --- 10.0.0.3 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 999ms
    rtt min/avg/max/mdev = 0.099/0.109/0.119/0.010 ms
    ```

    > `-c` for no. of times. here, we have pinged h3 from h1 for 2 times.

7. To Display nodes: Run `nodes`

    ```bash
    mininet> nodes
    available nodes are:
    c0 h1 h2 h3 h4 s1
    ```

8. Dump information about all nodes: Run `dump`
    > This displays IP addresses, ports & PIDs of the all the nodes.

    ```bash
    mininet> dump
    <Host h1: h1-eth0:10.0.0.1 pid=53742>
    <Host h2: h2-eth0:10.0.0.2 pid=53744>
    <Host h3: h3-eth0:10.0.0.3 pid=53746>
    <Host h4: h4-eth0:10.0.0.4 pid=53748>
    <OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None,s1-eth3:None,s1-eth4:None pid=53753>
    <OVSController c0: 127.0.0.1:6653 pid=53735>
    ```

9. To Know more info of a specific device, run `ifconfig`

    Eg: `h1 ifconfig -a` for h1 information

    ```bash
    mininet> h1 ifconfig -a
    h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
            inet6 fe80::a093:1eff:fec0:4f97  prefixlen 64  scopeid 0x20<link>
            ether a2:93:1e:c0:4f:97  txqueuelen 1000  (Ethernet)
            RX packets 191553  bytes 12643442 (12.6 MB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 673581  bytes 37662153894 (37.6 GB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ```

    > You can also check the **switch** status by running `s1 ifconfig -a`

10. Note that only the network is virtualized; each host process sees the same set of processes and directories. For example, print the process list from a host process:

    ```bash
    mininet> h1 ps -a
    ```

12. You can use `help` section provided by minnet.

    **Before launching**:

    ```bash
    sudo mn -h
    ```

    **While in Mininet**:

    ```bash
    help
    ```

    Output:

    ```bash
    mininet> help

    Documented commands (type help <topic>):
    ========================================
    EOF    gterm  iperfudp  nodes        pingpair      py      switch  xterm
    dpctl  help   link      noecho       pingpairfull  quit    time
    dump   intfs  links     pingall      ports         sh      wait
    exit   iperf  net       pingallfull  px            source  x

    You may also send a command to a node using:
    <node> command {args}
    For example:
    mininet> h1 ifconfig

    The interpreter automatically substitutes IP addresses
    for node names when a node is the first arg, so commands
    like
    mininet> h2 ping h3
    should work.

    Some character-oriented interactive commands require
    noecho:
    mininet> noecho h2 vi foo.py
    However, starting up an xterm/gterm is generally better:
    mininet> xterm h2
    ```
