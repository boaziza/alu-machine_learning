# Advanced Linear Algebra

Pure-Python implementations of core linear algebra operations.

| File | Function | Description |
|------|----------|-------------|
| `0-determinant.py` | `determinant(matrix)` | Determinant via cofactor expansion (`[[]]` -> 1) |
| `1-minor.py` | `minor(matrix)` | Minor matrix |
| `2-cofactor.py` | `cofactor(matrix)` | Cofactor matrix |
| `3-adjugate.py` | `adjugate(matrix)` | Adjugate (transpose of cofactor) |
| `4-inverse.py` | `inverse(matrix)` | Inverse via adjugate / determinant, `None` if singular |
| `5-definiteness.py` | `definiteness(matrix)` | Definiteness via eigenvalues (numpy) |
