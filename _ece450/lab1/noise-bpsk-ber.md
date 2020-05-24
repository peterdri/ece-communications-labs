---
layout: labitem
title: Part 3 - Noisy BPSK BER measurement

permalink: /ece450/lab1/noisy-bpsk-ber
course: ece450
prev: /ece450/lab1/noisy-bpsk-histogram
next: /ece450/lab1/calculating-ber
---

## Objectives

You will implement a communications system using baseband BPSK and record data to later generate a BER curve with.

---

## Part 3 deliverables

For this section, the deliverables are:

- the answer to one deliverable question,
- a dataset for later use in this lab.

---

## Building the flowgraph

Edit the GRC flowgraph from the last part of the lab. Remove the histogram and constellation sink blocks as well as the *QT GUI Range* block.

Add a *Variable* block and an *Import* block.

### Variables

Create a variable called `eb_n0_db`. Set it's value to 0.

### Import

The argument is `import math`. This will load the [python math library](https://docs.python.org/3/library/math.html). To call the library functions you would precede them with `math`. For example, to take the square root of the number 5 you would write `math.sqrt(5)` wherever you wanted the result.

### Noise Source

Remember that the *Amplitude* parameter sets the noise standard deviation, $$\sigma$$ and that the noise power of pure White Gaussian noise is the variance of the distribution ($$\sigma^2$$) (text section 3.1.3.4). Also recall from the [theory section]({{ site.baseurl }}{% link _ece450/lab1/theory.md %}) that $$\frac{E_b}{N_0}$$ = \frac{SNR}{2}$$.

Consider as well that $$\frac{S}{N}=\frac{a_i^2}{\sigma_0^2}$$ (text eqn. 3.45) where $$a_i^2$$ is the signal power and $$\sigma_0^2$$ is the noise power. Combining these two and solving for $$\sigma$$ yields

$$
\sigma = \sqrt{\frac{a_i^2}{2*\frac{E_b}{N_0}}}
$$

where it's important to remember that $$\frac{E_b}{N_0}$$ is in linear units.

Set the *Amplitude* parameter to an expression equivalent to the this function using the `eb_n0_db` variable you set earlier. You will need to:

- convert `eb_n0_db` to linear terms,
- use the `math` library. In particular you will need `math.sqrt()` and `math.pow()` (unless you prefer the python `**` notation),
- know the power of the signal (it's a binary stream of 1s and -1s)

You can check that you have the correct formula by plugging in some known numbers. For example when the `eb_n0_db` variable is set to 0, $$\sigma$$ should be $$\frac{1}{\sqrt{2}}$$.

## Run the experiment

1. Run the flowgraph.
2. For `eb_n0_db` values of 0, 1, ..., 10 record the BER.

{% include alert.html title="Note" content="Note you will have to kill the flowgraph each time you desire a new `eb_n0_db` value. Changing it during runtime with a *QT GUI Range* or similar will result in large delays for the BER to stabilize." %}

{% include alert.html title="Deliverable question 3" class="info" content="If you made a BER vs Eb/N0 curve and plotted it on top of a BER vs SNR curve (a plot with two x-axes), would they be the same or would they be offset? If offset, in which direction and by how much? __*This exercise can be done intuitively without plotting the curves or doing any calculations.*__"%}

Review the [section deliverables](#part-3-deliverables) before moving on.
