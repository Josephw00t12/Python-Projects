FA8 Espiritu
================
Joseph Raphael M. Espiritu
2024-04-11

<figure>
<img src="Question%201%20FA8.png" alt="FA8 Question 1" />
<figcaption aria-hidden="true">FA8 Question 1</figcaption>
</figure>

<br> Letter A Answer:

``` r
print(prob224)
```

    ## [1] 0.0668072

``` r
cat("It has a " ,  round(prob224*100,2), "% probability that the signal will exceed 224 microvolts")
```

    ## It has a  6.68 % probability that the signal will exceed 224 microvolts

<br> Letter B Answer:

``` r
print(pnorm(224, mean1, sqrt(var1)))
```

    ## [1] 0.9331928

``` r
print(pnorm(186, mean1, sqrt(var1)))
```

    ## [1] 0.190787

``` r
print(prob224to186)
```

    ## [1] 0.7424058

``` r
cat("It has a " ,  round(prob224to186*100,2), "% probability that the signal will be between 186 to 224 microvolts")
```

    ## It has a  74.24 % probability that the signal will be between 186 to 224 microvolts

<br> Letter C Answer:

``` r
print(percentile25)
```

    ## [1] 189.2082

``` r
cat("The micro voltage below 25% percentile is", percentile25)
```

    ## The micro voltage below 25% percentile is 189.2082

<br> Letter D Answer:

``` r
print(pnorm(240, mean1, sqrt(var1)))
```

    ## [1] 0.9937903

``` r
print(pnorm(210, mean1, sqrt(var1)))
```

    ## [1] 0.7340145

``` r
print(prob240to210)
```

    ## [1] 0.2597759

``` r
cat("It has a " ,  round(prob240to210*100,2), "% probability that the signal will be less than 240 but greater than 210 microvolts")
```

    ## It has a  25.98 % probability that the signal will be less than 240 but greater than 210 microvolts

<br> Letter E Answer:

``` r
print(interquartile)
```

    ## [1] 189.2082 210.7918

``` r
cat("The interquartile Range is:", interquartile[2]-interquartile[1])
```

    ## The interquartile Range is: 21.58367

<br> Letter F Answer:

``` r
print(pnorm(220, mean1, sqrt(var1)))
```

    ## [1] 0.8943502

``` r
print(pnorm(210, mean1, sqrt(var1)))
```

    ## [1] 0.7340145

``` r
print(prob220to210)
```

    ## [1] 0.1603358

``` r
cat("It has a " ,  round(prob220to210*100,2), "% probability that the signal will be less than 220 but greater than 210 microvolts")
```

    ## It has a  16.03 % probability that the signal will be less than 220 but greater than 210 microvolts

<br> Letter G Answer:

``` r
print(1 - pnorm(200, mean1, sqrt(var1)))
```

    ## [1] 0.5

``` r
print(1 - pnorm(220, mean1, sqrt(var1)))
```

    ## [1] 0.1056498

``` r
print(probgreater200then220)
```

    ## [1] 0.3943502

``` r
cat("It has a " ,  round(probgreater200then220*100,2), "% probability that the signal will be greater than 200 microvolts but also be greater than 220 microvolts already")
```

    ## It has a  39.44 % probability that the signal will be greater than 200 microvolts but also be greater than 220 microvolts already

![FA8 Question 2](Question%202%20FA8.png) <br> Letter G Answer:

``` r
# Given parameters
mean_downtime <- 25
variance_downtime <- 144

# (a) Obtain bounds which will include 95% of the downtime of all the customers
lower_bound_95 <- qnorm(0.025, mean_downtime, sqrt(variance_downtime))
upper_bound_95 <- qnorm(0.975, mean_downtime, sqrt(variance_downtime))

# (b) Obtain the bound above which 10% of the downtime is included
bound_above_10 <- qnorm(0.90, mean_downtime, sqrt(variance_downtime))

# Output the results
print(paste("Bounds including 95% of downtime:", round(lower_bound_95, 2), "to", round(upper_bound_95, 2)))
```

    ## [1] "Bounds including 95% of downtime: 1.48 to 48.52"

``` r
print(paste("Bound above which 10% of downtime is included:", round(bound_above_10, 2)))
```

    ## [1] "Bound above which 10% of downtime is included: 40.38"
