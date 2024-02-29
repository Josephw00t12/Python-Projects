# Geometric Distribution

# Set probability of success
p <- 0.2

# Generate 1000 random variables from the geometric distribution
x <- rgeom(1000, p)

# Calculate mean, variance, and standard deviation
mean_x <- mean(x)
var_x <- var(x)
sd_x <- sd(x)

# Print the results
cat("Number of trials required to achieve first success:\n")
cat("Mean (in 2 decimal places):", round(mean_x, 2), "\n")
cat("Variance (in 2 decimal places):", round(var_x, 2), "\n")
cat("Standard deviation (in 2 decimal places):", round(sd_x, 2), "\n")

# Plot the histogram
hist(x, main = "Histogram of Geometric Distribution", xlab = "Number of Trials", ylab = "Frequency")

# Calculate kurtosis and skewness
kurt <- round(kurtosis(x), 2)
skew <- round(skewness(x), 2)

cat("Kurtosis (in 2 decimal places):", kurt, "\n")
cat("Skewness (in 2 decimal places):", skew, "\n\n")


# Hypergeometric Distribution

# Function to calculate hypergeometric probability mass function
hypergeometric_pmf <- function(x, N, K, n) {
  choose(K, x) * choose(N - K, n - x) / choose(N, n)
}

# Define parameters for the first scenario
N1 <- 40
K1 <- 0.1 * N1
n1 <- 10

# Calculate the probability of more than 10% defectives
prob_more_than_10_percent_1 <- sum(dhyper(1:10, K1, N1 - K1, n1))

# Define parameters for the second scenario
N2 <- 5000
K2 <- 0.1 * N2
n2 <- 10

# Calculate the probability of more than 10% defectives
prob_more_than_10_percent_2 <- sum(dhyper(1:10, K2, N2 - K2, n2))

cat("Probability of more than 10% defectives in scenario 1:", prob_more_than_10_percent_1, "\n")
cat("Probability of more than 10% defectives in scenario 2:", prob_more_than_10_percent_2, "\n")
