---
layout: labitem
title: Part 4 - Calculating BER

permalink: /ece450/lab1/calculating-ber
course: ece450
prev: /ece450/lab1/noisy-bpsk-ber
next: /ece450/lab1/conclusion
---

## Objectives

You will use the values recorded for the baseband BPSK communication system to plot a $$BER-\frac{E_b}{N_0}$$ curve and compare it with theory.

---

## Part 5 deliverables

For this section, the deliverables are:

- the answer to two deliverable questions,
- the code used to generate the BER curve (with the dataset hard coded into it),
- the resulting BER curve as a .PNG image file.

---

## Generating a BER curve

Using the values collected throughout this lab you can now generate a $$BER-\frac{E_b}{N_0}$$ curve.

You can use a programming language of your choice, but python or matlab have some handy tools for this job built in.

Plot three curves on the same axes:

1. BER curve for the theoretical $$BER=\sqrt{2\frac{E_b}{N_0}}$$,
2. BER curve using the collected BER and Eb/N0 values from earlier in this lab.

### 1. Theory

For generating a simulated curve of the theoretical $$BER-\frac{E_b}{N_0}$$ review [the theory section]({{ site.baseurl }}{% link _ece450/lab1/theory.md %}) of this lab.

For the Q-function, Matlab ships with [`qfunc()`](https://www.mathworks.com/help/comm/ref/qfunc.html) while python has [`norm.sf()`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.norm.html) included in the scipy package.

### 2. Collected BER and set Eb/N0 values

You collected a dataset of BER values for Eb/N0 values of 0, 1, ..., 10 dB. While plotting these remember that the BER values collected from the number sink are log10(BER). So to obtain the BER you will need to raise your collected values, -X by realizing that $$BER = 10^{-X}$$.

### Plotting details

Now that you have the three curves, ensure that the plot has:

- a log scale on the y-axis
- a linear scale on the x-axis
- appropriate axes titles
- a legend (one entry for each of: "Theory", "Simulation")

A sample of what the plot might look like is included below (with all the labelling elements removed).

  ![BER-curve.png](figures/BER-curve.png)<br>
  __*Sample BER curve*__

{% include alert.html title="Deliverable question 4" class="info" content="Provide insight into your results. What does the BER curve tell you about your communication system?" %}

{% include alert.html title="Deliverable question 5" class="info" content="Relate the BER curve to the histogram you generated earlier in this lab." %}

Review the [section deliverables](#part-4-deliverables) beforing moving on.
