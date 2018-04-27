# 5: Distributed Computing
This week you need to implement distributed computing via [remote procedure call (RPC)](https://en.wikipedia.org/wiki/Remote_procedure_call), which has similiar interface you get with real robot via PyNaoQi.

The server and client have to be implemented together:
* [ServerAgent](./agent_server.py) provides remote RPC service;
* [ClientAgent](./agent_client.py) requests remote call from server and provides non-blocking capibility.


