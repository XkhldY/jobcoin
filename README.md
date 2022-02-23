# JobCoin Mixer

### Requirements:
* click
* python
* requests

### Workflow:
1. Ask the user to enter the addresses needed to be mixed.
2. Once the user enters the addresses, the system generate deposit account for adding funds.
3. The system then listen to the transactions on this deposit account.
4. If the user adds funds to the deposit account.
    * the system transfer the funds to house account with other coins.
    * the system then dole out the funds to the given addresses.

### Assumptions:
1. The user have already addresses on the server previously, 
       can transfer from them to the deposit account.
2. The user addresses entered are new, if not the system won't stop 
       just will add the funds anyway.
3. The system consumed by one user and assign one deposit account at a time. 
4. Creating new deposit accounts to the system is acceptable 


### Enhancements:
1. The system could be asynchronous, so the process doesn't wait for the 
       transaction to be made.
2. The mixing algorithm can be more complex to reduce tracking
3. Create the mixer as a set of rest apis
4. Create local database with users, and their details.
5. Be able to push directly to house account with creating temp accounts
6. Features for the user to be able to check the balance of the addresses
7. Add more testcases to the system

