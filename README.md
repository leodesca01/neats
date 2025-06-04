# neats
evolving topologies

## Using with Slime Volley

This repo contains PrettyNEAT and a helper file from the original
slimevolleygym repository (`prettyNEAT/slimevolleygym/test_state.py`).
Install the optional dependencies and run NEAT training with

```
python prettyNEAT/neat_train.py -p prettyNEAT/p/slime_volley.json
```

This uses the `slimevolleygym` environment. To experiment with different
parameters, copy `prettyNEAT/p/slime_volley.json` and edit the values.

EvoJax can also run Slime Volley via its own tasks, which requires JAX
and provides fast vectorized simulation. After installing `evojax` you
can explore their examples to try alternative algorithms.
