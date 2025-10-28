* Find directed cycles that start and end at the same node
* Add time window filtering to focus on rapid circular transactions (e.g. within 3 days)
* Detect cyclic regions by finding groups of accounts that can reach each other — strongly connected components
* Frequency-based cycle scoring - rank cycles by how frequently they occur
* Find large-value circular flows if you only care about loops moving a lot of money
