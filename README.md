# Equational Jacobson Proofs for \(k=3\)

This workspace investigates characteristic-\(p\) rings satisfying \(x^{p^3}=x\). The main report gives a proof schema completing the missing \(p\equiv 1\pmod 3\) case by reducing the Frobenius 3-cycle to a finite cyclic norm certificate.

## Key Results

- Brandenburg's period criterion covers \(p=2\), \(p=3\), and primes \(p\equiv 2\pmod 3\).
- For primes \(p\equiv 1\pmod 3\), the notes prove the monomial Wedderburn statements \(W_{p,3,T^p}\) and \(W_{p,3,T^{p^2}}\) using a norm-section argument.
- For each fixed \(p\), the remaining norm-section step is a finite polynomial identity, so it can be emitted as an equational certificate.

## Reproduce Checks

```bash
source .venv/bin/activate
python src/k3_wedderburn_checks.py
python src/k3_wedderburn_checks.py --json > results/k3_checks.json
```

## File Structure

- `REPORT.md`: main mathematical report.
- `planning.md`: research plan and novelty assessment.
- `definitions.md`: notation used in the proof.
- `results/proof_notes.md`: theorem and lemma proof notes.
- `src/k3_wedderburn_checks.py`: deterministic finite-field/skew-algebra checks.
- `results/k3_checks.json`: saved computational output.
- `literature_review.md`, `resources.md`, `papers/`: pre-gathered source material.
