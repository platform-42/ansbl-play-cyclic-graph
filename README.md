* Find directed cycles that start and end at the same node
* Add time window filtering to focus on rapid circular transactions (e.g. within 3 days)
* Detect cyclic regions by finding groups of accounts that can reach each other — strongly connected components
* Frequency-based cycle scoring - rank cycles by how frequently they occur
* Find large-value circular flows if you only care about loops moving a lot of money

# Simulation money laundering
Build graph based on accounts (nodes) and transactions (edges)

---

## Populate graph
* cyclic.yml -> playbook to populate graph
* cyclic.sh -> shell script to launch cyclic.yml playbook

## Query graph (Detect)
* detect.yml -> playbook to detect suspicious transactions
* detect.sh -> shell script to lunch detect.yml playbook

---

## Detection funnel 
Detect play is implemented as a analytic funnel.
So: 
- output Phase I -> input Phase II
- output Phase II -> input Phase III
- output Phase III -> input Phase IV

* Phase I -> determine all cyclic accounts with hop-count between 2 and 6
* Phase II -> reduce to accounts with quick turnaroud (<= 3 days)
* Phase III -> check frequency and amount
* Phase IV -> report results (e.g. Label nodes as SUSPECT)