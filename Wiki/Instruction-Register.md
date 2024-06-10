# The instruction register


### how fetching is obtained?
```
1) PC    -> MAR; PC++  | PCout, MARin, PCinc
2) M[MA] -> MD         | MDRwe, Msel, ??? depends on mem module
3) MD    -> IR         | MDRoe, IRin
```
