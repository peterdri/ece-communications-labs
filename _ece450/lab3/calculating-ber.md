---
layout: labitem
title: Part 5 - Calculating BER

permalink: /ece450/lab3/calculating-ber
course: ece450
prev: /ece450/lab3/coherent-fsk
next: /ece450/lab3/conclusion
---

## Objectives

You will use the values recorded to plot a $$BER-\frac{E_b}{N_0}$$ curve for each of the noncoherent and coherent simulations and then compare them with theory.

---

## Part 5 deliverables

For this section, the deliverables are:

- the answer to three deliverable questions,
- the code used to generate the BER curve (with the dataset hard coded into it),
- the resulting BER curve as a .PNG image file.

---

## Generating a BER curve

Using the values collected throughout this lab you can now generate some $$BER-\frac{E_b}{N_0}$$ curve.

You can use a programming language of your choice, but python or matlab have some handy tools for this job built in.

Plot four curves on the same axes:

1. BER curve for the theoretical noncoherent BFSK,
2. BER curve for the simulated noncoherent BFSK,
3. BER curve for the theoretical coherent BFSK,
4. BER curve for the simulated coherent BFSK.

### Theory curves

For generating the curves of the theoretical $$BER-\frac{E_b}{N_0}$$ review [the theory section]({{ site.baseurl }}{% link _ece450/lab3/theory.md %}) of this lab. For the Q-function, Matlab ships with [`qfunc()`](https://www.mathworks.com/help/comm/ref/qfunc.html) while python has [`norm.sf()`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.norm.html) included in the scipy package.

### Simulation curves

You collected datasets of BER values for Eb/N0 values of 0, 2, 4, 6, 8, 10 dB. Plot them against each other (remembering that $$BER=10^{-X}$$).

### Plotting details

Now that you have the four curves, ensure that the plot has:

- a log scale on the y-axis
- a linear scale on the x-axis
- appropriate axes titles
- a legend (one entry for each of: "Noncoherent theory", "Noncoherent simulation", "Coherent theory", "Coherent simulation")

A sample of what the plot might look like is included below (with all the labelling elements removed).

  ![BER-curve.png](figures/BER-curve.png)<br>
  __*Sample BER curve.*__

{% include alert.html title="Deliverable question 5" class="info" content="Provide insight into your results. What does the BER curve tell you about the difference between coherent and noncoherent BFSK signals?" %}

Review the [section deliverables](#part-5-deliverables) beforing moving on.
