FA3
================
Espiritu, Joseph Raphael M.
2024-02-25

### **FA3 Questions**

#### ***1.*** A binary communication channel carries data as one of two sets of signals denoted by 0 and 1. Owing to noise, a transmitted 0 is sometimes received as a 1, and a transmitted 1 is sometimes received as a 0. For a given channel, it can be assumed that a transmitted 0 is correctly received with probability 0.95, and a transmitted 1 is correctly received with probability 0.75. Also, 70% of all messages are transmitted as a 0. If a signal is sent, determine the probability that:

1)  A 1 was received;
2)  A 1 was transmitted given than a 1 was received.

#### The **B** answer will be implementing **Bayes Theorem** and is a **Posterior Probability**

``` r
root <- Node$new("Communication Channel")

transmit0 <- root$AddChild("Transmitted 0 (70%)")
transmit1 <- root$AddChild("Transmitted 1 (30%)")

received_0T0 <- transmit0$AddChild("Received 0 (95%)")
received_1T0 <- transmit0$AddChild("Received 1 (5%)")

received_0T1 <- transmit1$AddChild("Received 0 (25%)")
received_1T1 <- transmit1$AddChild("Received 1 (75%)")

prob_transmit_0 <- 0.7
prob_transmit_1 <- 0.3
prob_receive_0_given_0 <- 0.95
prob_receive_1_given_1 <- 0.75

prob_receive_0 <- prob_transmit_0 * prob_receive_0_given_0 +
                  prob_transmit_1 * (1 - prob_receive_1_given_1)
prob_receive_1 <- prob_transmit_0 * (1 - prob_receive_0_given_0) +
                  prob_transmit_1 * prob_receive_1_given_1

prob_transmit_1_given_receive_1 <- (prob_transmit_1 * prob_receive_1_given_1) / prob_receive_1

cat("Probability of receiving 1:", prob_receive_1, "\n")
```

    ## Probability of receiving 1: 0.26

``` r
cat("Probability of transmitting 1 given receiving 1:", prob_transmit_1_given_receive_1, "\n")
```

    ## Probability of transmitting 1 given receiving 1: 0.8653846

``` r
plot(root)
```

![](Espiritu,-Joseph-Raphael-M-FA3_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->
\#### ***2.*** 7. There are three employees working at an IT company:
Jane, Amy, and Ava, doing 10%, 30%, and 60% of the programming,
respectively. 8% of Jane’s work, 5% of Amy’s work, and just 1% of Ava‘s
work is in error. What is the overall percentage of error? If a program
is found with an error, who is the most likely person to have written
it?

``` r
root1 <- Node$new("It Company Employees")

Jane <- root1$AddChild("Jane Works (10%)")
Amy <- root1$AddChild("Amy Works (30%)")
Ava <- root1$AddChild("Ava Works (60%)")

errJane <- Jane$AddChild("Jane Error (8%)")
sucJane <- Jane$AddChild("Jane Success (92%)")
errAmy <- Amy$AddChild("Amy Error (5%)")
sucAmy <- Amy$AddChild("Amy Success (95%)")
errAva <- Ava$AddChild("Ava Error (1%)")
sucAva <- Ava$AddChild("Ava Success (99%)")

Jane$work <- 0.10
Amy$work <- 0.30
Ava$work <- 0.60

Jane$err <- 0.08
Amy$err <- 0.05
Ava$err <- 0.01

Jane$suc <- 1 - Jane$err
Amy$suc <- 1 - Amy$err
Ava$suc <- 1 - Ava$err

cumulativeSuccess <- c(
  Jane$work * Jane$suc,
  Amy$work * Amy$suc,
  Ava$work * Ava$suc
)

cumulativeError <- c(
  Jane$work * Jane$err,
  Amy$work * Amy$err,
  Ava$work * Ava$err
)

cat("Jane, Amy, Ava respectively Successes ", cumulativeSuccess)
```

    ## Jane, Amy, Ava respectively Successes  0.092 0.285 0.594

``` r
cat("Jane, Amy, Ava respectively Errors", cumulativeError)
```

    ## Jane, Amy, Ava respectively Errors 0.008 0.015 0.006

``` r
cat("Amy has the most Error and the Sum of the errors in their work is:", sum(cumulativeError))
```

    ## Amy has the most Error and the Sum of the errors in their work is: 0.029

``` r
cat("Ava is the hardest Worker and their Total Success is:", sum(cumulativeSuccess))
```

    ## Ava is the hardest Worker and their Total Success is: 0.971

``` r
plot(root1)
```

![](Espiritu,-Joseph-Raphael-M-FA3_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->
