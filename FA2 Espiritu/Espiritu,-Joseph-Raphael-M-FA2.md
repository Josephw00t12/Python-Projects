FA2 R - Language
================
Espiritu, Joseph Raphael M.
2024-02-18

### **FA2 Questions**

#### ***1.*** Use R to illustrate that the probability of getting:

1)  a head is 0.5 if a fair coin is tossed repeatedly;
2)  a red card is 0.5 if cards are drawn repeatedly with replacement
    from a well-shuffled deck;
3)  an even number is 0.5 if a fair die is rolled repeatedly.

**A**. Answer with Trials set to 100

    ## Frequency of getting a head: 0.47

    ## Frequency of getting a tail: 0.53

**B**. Answer with Trials set to 1000

    ## Frequency of red Cards: 0.522

    ## Frequency of black Cards: 0.478

**C**. Answer with Trials set to 10000

    ## Frequency of getting an even number: 0.5015

    ## Frequency of getting an odd number: 0.4985

#### ***2.*** An experiment consists of tossing two fair coins. Use R to simulate this experiment 100 times and obtain the relative frequency of each possible outcome. Hence, estimate the probability of getting one head and one tail in any order.

***Answer with Trials set to 100***

    ## Probability of getting one head and one tail in any order: 0.42

#### ***3.*** An experiment consists of rolling a die. Use R to simulate this experiment 600 times and obtain the relative frequency of each possible outcome. Hence, estimate the probability of getting each of 1, 2, 3, 4, 5, and 6.

***Answer with Trials set to 600***

    ## Relative frequencies:

    ## Outcome 1 : 0.1816667 
    ## Outcome 2 : 0.165 
    ## Outcome 3 : 0.1766667 
    ## Outcome 4 : 0.1683333 
    ## Outcome 5 : 0.145 
    ## Outcome 6 : 0.1633333
