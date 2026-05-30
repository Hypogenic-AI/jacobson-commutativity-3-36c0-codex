# Computational Tools

## SymPy finite-field reduction helper

- Location: `code/finite_field_reductions.py`
- Purpose: small-case checks for the one-variable finite-field gcd reductions used in Brandenburg's equational proof method.
- Example:

```bash
source .venv/bin/activate
python code/finite_field_reductions.py --n 7 --p 2 --max-degree 3
python code/finite_field_reductions.py --p 7 --k 3
```

## External tools worth using

- SageMath: best fit for the polynomial and finite-field routines in Brandenburg's appendix. Not installed here because it is a heavy system dependency.
- Prover9/Mace4: useful for equational proof search and countermodel checks; used by Kinyon and MacHale for Herstein-type commutativity proofs.
- SymPy: installed in this workspace for lightweight polynomial gcd and modular arithmetic checks.
