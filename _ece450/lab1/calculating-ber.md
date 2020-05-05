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

- the answer to two deliverable questions,
- the code used to generate the BER curve (with the dataset hard coded into it),
- the resulting BER curve as a .PNG image file.

---

## Generating a BER curve

Using the values collected throughout this lab you can now generate a BER curve. Remember that while you measured the SNR of these systems, you are in generating a $$BER-\frac{E_b}{N_0}$$ curve, _not_ a $$BER-SNR$$ curve.

You can use a programming language of your choice, but python or matlab have some handy tools for this job built in.

The plot should have:

- a log scale on the y-axis
- a linear scale on the x-axis
- appropriate axes titles
- a legend (one entry for each of: "LPF", "RRC", "Theory")

For generating a simulated curve of the theoretical $$BER-\frac{E_b}{N_0}$$ review the theory section of this lab. For the Q-function, Matlab ships with [`qfunc()`](https://www.mathworks.com/help/comm/ref/qfunc.html) while python has [`norm.sf()`](https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.norm.html) included in the scipy package.

A sample of what it might look like is included below (without labelling elements). **This sample had some curve-fitting/interpolation done to it which you do not need to do.**

  ![BER-curve.png](figures/BER-curve.png)
  __*Sample BER curve*__

{% include alert.html title="Deliverable question 4" class="info" content="Provide insight into your results. What does the BER curve tell you about these pulse-shaping options?" %}

{% include alert.html title="Deliverable question 5" class="info" content="How similar are the LPF and RRC curves? If there is any difference, what causes it? _Hint: consider the energy per bit and how you controlled that in these flowgraphs._" %}

Review the [section deliverables](#part-4-deliverables) beforing moving on.
