# Homework 
- Name: Bryan D. Morales Sosa
## Question 6) Coverage
- **Coverage Results**:

Name | Stmts | Miss | Cover | Missing 
--- | --- | --- | --- | ---
src/__init__.py | 0 | 0 | 100% |   
src/order_io.py | 20 | 2 | 90% |  12, 15 
src/pricing.py | 22 | 0 |  100% |   
TOTAL | 42 | 2 | 95%
- **Uncovered lines/functions**: Two lines are unconvered in order_io.py in the loadOrder() function, which are:
  - if not ln.strip() --> continue
  - if len(parts) != 2 --> raise ValueError("Malformed line: " + ln.strip())
- **Acceptable uncoverage**: The continue conditional is considered acceptable uncoverage because it simply checks for whitespace.
The valueError conditional should be tested to understand when code exception occur.
