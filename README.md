# Running the server (development)

```shell
python3 -m flask run
```

# Regenerating grammar

```shell
antlr4 -visitor -Dlanguage=Python3 Formula.g4
```
