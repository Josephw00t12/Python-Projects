FA3
================
Espiritu, Joseph Raphael M.
2024-02-25

### **FA3 Questions**

#### ***1.*** A binary communication channel carries data as one of two sets of signals denoted by 0 and 1. Owing to noise, a transmitted 0 is sometimes received as a 1, and a transmitted 1 is sometimes received as a 0. For a given channel, it can be assumed that a transmitted 0 is correctly received with probability 0.95, and a transmitted 1 is correctly received with probability 0.75. Also, 70% of all messages are transmitted as a 0. If a signal is sent, determine the probability that:

1)  a 1 was received;
2)  a 1 was transmitted given than a 1 was received.

**A**. Answer with Trials set to 100

``` r
# Load required packages
library(data.tree)

# Create the root node
root <- Node$new("Signal Sent")

# Add child nodes for transmission options
transmit_0 <- root$AddChild("Transmit 0")
transmit_1 <- root$AddChild("Transmit 1")

# Add child nodes for received options under transmit 0
receive_0_given_0 <- transmit_0$AddChild("Receive 0 (Given 0)")
receive_1_given_0 <- transmit_0$AddChild("Receive 1 (Given 0)")

# Add child nodes for received options under transmit 1
receive_0_given_1 <- transmit_1$AddChild("Receive 0 (Given 1)")
receive_1_given_1 <- transmit_1$AddChild("Receive 1 (Given 1)")

# Assign probabilities to each node based on the given information
transmit_0$prob <- 0.70
transmit_1$prob <- 0.30

receive_0_given_0$prob <- 0.95
receive_1_given_0$prob <- 1 - receive_0_given_0$prob

receive_1_given_1$prob <- 0.75
receive_0_given_1$prob <- 1 - receive_1_given_1$prob

# Calculate the probability of receiving a 1 overall
prob_receive_1 <- (transmit_0$prob * receive_1_given_0$prob) + (transmit_1$prob * receive_1_given_1$prob)

# Calculate the probability of transmitting a 1 given that a 1 was received
prob_transmit_1_given_receive_1 <- (transmit_1$prob * receive_1_given_1$prob) / prob_receive_1

# Display results
cat("Probability that a 1 was received:", prob_receive_1, "\n")
```

    ## Probability that a 1 was received: 0.26

``` r
cat("Probability that a 1 was transmitted given that a 1 was received:", prob_transmit_1_given_receive_1, "\n")
```

    ## Probability that a 1 was transmitted given that a 1 was received: 0.8653846
