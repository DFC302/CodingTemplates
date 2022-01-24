```
ffuf -u http(s)://URL/FUZZ -b "use a cookie" -r -recursion-depth 2 -recursion-strategy greedy -recursion -rate 25 -fc 404 -w <path to wordlist> -o <filename>
```
