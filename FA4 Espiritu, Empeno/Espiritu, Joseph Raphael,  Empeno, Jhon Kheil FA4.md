FA4
================
Espiritu, Empeno
2024-03-03

### **FA6 Questions**

#### ***1.*** A geospatial analysis system has four sensors supplying images. The percent- age of images supplied by each sensor and the percentage of images relevant to a query are shown in the following table.

| Sensor | Percentage_of_Images_Supplied | Percentage_of_Relevant_Images |
|-------:|------------------------------:|------------------------------:|
|      1 |                            15 |                            50 |
|      2 |                            20 |                            60 |
|      3 |                            25 |                            80 |
|      4 |                            40 |                            85 |

What is the overall Percentage of the Relevant Images?

``` r
percentSupplied <- c(15, 20, 25, 40)
percentRelevant <- c(50, 60, 80, 85)

overallPercentage <- sum(percentSupplied * percentRelevant) / sum(percentSupplied)

cat("Overall percentage of the Relevant images:", overallPercentage, "%\n")
```

    ## Overall percentage of the Relevant images: 73.5 %

#### ***2.*** A fair coin is tossed twice.

Let E be the event that both tosses have the same outcome, that is, E1 =
(HH, TT). Let E2 be the event that the first toss is a head, that is, E2
= (HH, HT). Let E3 be the event that the second toss is a head, that is,
E3 = (TH, HH). Show that E1, E2, and E3 are pairwise independent but not
mutually independent.

|       | Heads | Tails |
|:------|:------|:------|
| Heads | HH    | HT    |
| Tails | TH    | TT    |

    ## E1 is the Event both results are the Same

    ## E2 is the Event first results are the Heads

    ## E1 is the Event second results are the Heads

    ## From the table we can see each event has 1/2 of the chance

    ## 0.5 0.5 0.5

    ## The two events E1 UNION E2 happening are the the products of its probabilities

    ## 0.25 Which is just the probability of HH on the table which is 1/4 and the UNION of the two events is HH

    ## We can derive that E1 UNION E3 and E2 UNION E3 will also have 1/4 probabilities
    ## and respectively have HH as the UNION too

    ## 0.25 0.25

    ## These prove their Pairwise Independent but now to show they are not Mutually Independent.
    ## We can just apply the same priciple of multiplying the Probabilities and theirs UNION's and we will see the probem

    ## E1 UNION E2 UNION E3 have HH as the probability which is 1/4 but is not equal to the probability of multiplying all of them

    ## 0.125 Hence they are not Mutually Independent because E2 and E3 itself doesnt cary information or
    ## data to help form the probability of E1 it is still 1/2 but having the UNION of E2 and E2 will
    ## change the probability of E1 to happen becoming 1 means its guaranteed
