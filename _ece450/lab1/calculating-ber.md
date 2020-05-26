---
layout: labitem
title: Part 4 - Calculating BER

permalink: /ece450/lab1/calculating-ber
course: ece450
prev: /ece450/lab1/noisy-bpsk-ber
next: /ece450/lab1/conclusion
---

## Objectives

You will use the BER values recorded for the baseband BPSK communication systems (both uni- and bipolar) to plot the $$BER-\sigma$$ curves and compare them with theory.

---

## Part 5 deliverables

For this section, the deliverables are:

- the answer to two deliverable questions,
- the code used to generate the BER curve (with the datasets hard coded into it),
- the resulting BER curve as a .PNG image file.

---

## Generating a BER curve

Using the values collected throughout this lab you can now generate a $$BER-\sigma$$ curve.

You can use a programming language of your choice, but python or matlab have some handy tools for this job built in.

Plot three curves on the same axes:

1. BER curve for the theoretical $$BER=Q\left( \frac{a_1 - a_2}{2\sigma_0} \right)$$,
2. BER curve using the collected BER and set $$\sigma$$ values from earlier in this lab.

### 1. Theory

For generating a simulated curve of the theoretical $$BER-\frac{a_1 - a_2}{2\sigma_0}$$ review [the theory section]({{ site.baseurl }}{% link _ece450/lab1/theory.md %}) of this lab.

For the Q-function, Matlab ships with [`qfunc()`](https://www.mathworks.com/help/comm/ref/qfunc.html) while python has [`norm.sf()`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.norm.html) included in the scipy package.

Remember to plot two curves, one for bipolar ($$a_1, a_2 = 1, -1$$) and one for unipolar ($$a_1, a_2 = 1, 0$$). You can use the same $$\sigma$$ values as those set during the experiment to ensure the curves will line up in the x-axis.

### 2. Collected BER and set $$\sigma$$ values

<!-- You collected a dataset of BER values for $$\sigma$$ values of `[0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.75, 1, 1.5, 3, 100]`. While plotting these remember that the BER values collected from the number sink are log10(BER). So to obtain the BER you will need to raise your collected values, -X by realizing that $$BER = 10^{-X}$$. -->
You collected a dataset of BER values for $$\sigma$$ values of `[ 0.3, 0.5, 1, 1.5, 2, 3, 4, 5, 8, 12]`. While plotting these remember that the BER values collected from the number sink are log10(BER). So to obtain the BER you will need to raise your collected values, -X by realizing that $$BER = 10^{-X}$$.

Remember to plot two curves, one for bipolar ($$a_1, a_2 = 1, -1$$) and one for unipolar ($$a_1, a_2 = 1, 0$$). You can use the same $$\sigma$$ values as those set during the experiment to ensure the curves will line up in the x-axis.

### Plotting details

Now that you have the three curves, ensure that the plot has:

<!-- - a log scale on the y-axis -->
<!-- - a linear scale on the x-axis -->
- appropriate axes titles
- a legend (one entry for each of: "unipolar sim.", "unipolar theory", "bipolar sim.", "bipolar theory")

A sample of what the plot might look like is included below (with all the labelling elements removed).

  ![BER-curve.png](figures/BER-curve.png)<br>
  __*Sample BER curve*__

{% include alert.html title="Deliverable question 4" class="info" content="Provide insight into your results. What does the BER curve tell you about each (unipolar/bipolar) communication system? What does it tell you about the performance of the two systems when compared?" %}

{% include alert.html title="Deliverable question 5" class="info" content="Relate the BER curve to the histogram you generated earlier in this lab." %}

Review the [section deliverables](#part-4-deliverables) beforing moving on.
