# Running Python Scripts

Running a custom mininet file using a python script for adding new topologies, switch types, test to command line.

```bash
sudo mn --custom ./CustomTopology.py --topo mytopo --test pingall
```

> Make sure the topology name matches with the one you have mentioned in the python script.

```python
topos = { 'mytopo': (lambda: MyTopo())}
```



### Issues

1. Error: `Python ImportError: cannot import name utils`

A: install requests.
    ```python
    pip install requests
    ```

2. If miniedit is not launching from examples folder and you are facing the below error, then use.

Error: `ImportError: cannot import name 'StrictVersion' from 'mininet.util' (/usr/lib/python3/dist-packages/mininet/util.py)`

A: Make sure you have installed `python3-tk` package on ubuntu.

If you are facing the util issue, comment `strictversion` package or remove it. Ref: [https://stackoverflow.com/questions/76810006/cannot-resolve-the-problem-of-not-opening-miniedit-in-mininet](https://stackoverflow.com/questions/76810006/cannot-resolve-the-problem-of-not-opening-miniedit-in-mininet)

Also, make sure you have `x11-apps` & `x11-utils` packages installed if you are using ubuntu in `wsl`.




For learning the API, I have refered these:

1. Introduction to Mininet - [https://hackmd.io/@pmanzoni/BklqpKddS](https://hackmd.io/@pmanzoni/BklqpKddS)
   