# BisVind Billing Software

## Tech Stack
    - DB                - SQLite
    - Logic             - Python
    - UI Framework      - PyQt6
    - Packaging         - PyInstaller 

## Workflow
    - Data to be stored in a pendrive (a backup in the local machine), to ensure the work can continue from where it is left. 
    - software should be packaged as a .exe file at the end
    - user should be able to choose the location of the pendrive to store and retrieve the data.

## requirements

    - new customer, edit customer, customer ledger 
    - new supplier, edit supplier, supplier ledger
    - new product, edit product, product ledger
    - Journal
        - cash book (Credit, debit)
        - bank book (Credit, debit)
    - ledger (total of the day's credit and debit - option to check the bank book and cash book separately)
    - report 

    - new transaction (bill), edit transaction, transaction ledger