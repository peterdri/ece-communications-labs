---
layout: labitem
title: Part 4 - Calculating BER

permalink: /ece450/lab1/calculating-ber
course: ece450
prev: /ece450/lab1/impulse-rrc-shaping
next: /ece450/lab1/conclusion
---

## Objectives

You will use the values recorded for each pulse shape to plot a $$BER-\frac{E_b}{N_0}$$ curve and then compare it with theory.

---

## Part 5 deliverables

For this section, the deliverables are:

- the answer to three deliverable questions,
- the code used to generate the BER curve (with the dataset hard coded into it),
- the resulting BER curve as a .PNG image file.

---

## Generating a BER curve

Using the values collected throughout this lab you can now generate a $$BER-\frac{E_b}{N_0}$$ curve.

You can use a programming language of your choice, but python or matlab have some handy tools for this job built in.

Plot three curves on the same axes:

1. BER curve for the theoretical $$BER=\sqrt{2\frac{E_b}{N_0}}$$,
2. BER curve using the collected BER and Eb/N0 values for the matched filter flowgraph,
3. BER curve using the collected BER values but calculating Eb/No using the collected signal and noise powers at the output of the matched filter.

### 1. Theory

For generating a simulated curve of the theoretical $$BER-\frac{E_b}{N_0}$$ review [the theory section]({{ site.baseurl }}{% link _ece450/lab1/theory.md %}) of this lab. For the Q-function, Matlab ships with [`qfunc()`](https://www.mathworks.com/help/comm/ref/qfunc.html) while python has [`norm.sf()`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.norm.html) included in the scipy package.

### 2. Collected BER and user-set Eb/N0 values

You collected a dataset of BER values for Eb/N0 values of 0, 2, 4, 6, 8 dB. While plotting these remember that the BER values collected from the number sink are log10(BER). So to obtain the BER you will need to raise your collected values, -X by realizing that $$BER = 10^{-X}$$.

### 3. Collected BER and calculated Eb/N0 values

Remember back to the derivation for $$\sigma$$ done [previously in this lab]({{ site.baseurl }}{% link _ece450/lab1/impulse-lpf-shaping.md %}),

$$
\frac{E_b}{N_0} = \frac{1}{2} \frac{a_i^2}{\sigma_0^2} \frac{W}{R}.
$$

Use the signal power and noise powers measured at the output of the matched filter to calculate Eb/N0 values to match the collected BER values.

### Plotting details

Now that you have the three curves, ensure that the plot has:

- a log scale on the y-axis
- a linear scale on the x-axis
- appropriate axes titles
- a legend (one entry for each of: "Matched filter set Eb/N0", "Matched filter calculated Eb/N0", "Theory")

A sample of what the three curves it might look like is included below (with all the labelling elements removed).

  ![BER-curve.png](figures/BER-curve.png)<br>
  __*Sample BER curve*__

{% include alert.html title="Deliverable question 5" class="info" content="Provide insight into your results. What does the BER curve tell you about your communication system?" %}

{% include alert.html title="Deliverable question 6" class="info" content="How similar are the simulation and the theory results? What causes any differences that exist?" %}

{% include alert.html title="Deliverable question 7" class="info" content="How similar is the calculated Eb/N0 curve to the set Eb/N0 curve? Explain why this is so." %}

Review the [section deliverables](#part-4-deliverables) beforing moving on.
