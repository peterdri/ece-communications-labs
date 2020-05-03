---
layout: labitem
title: Part 5 - Calculating BER

permalink: /ece450/lab1/calculating-ber
course: ece450
prev: /ece450/lab1/rrc-pulse-shaping
next: /ece450/lab1/conclusion
---

## Objectives

You will use the values recorded for each pulse shape to plot a BER-SNR curve.

---

## Part 5 deliverables

For this section, the deliverables are:

- the answer to one deliverable question,
- the code used to generate the BER curve (with the dataset hard coded into it),
- the resulting BER curve as a .PNG image file.

---

## Generating a BER curve

Using the values collected throughout this lab you can now generate a BER curve.

You can use a programming language of your choice, but python or matlab have some handy tools for this job built in.

The plot should have:

- a log scale on the y-axis
- a linear scale on the x-axis
- appropriate axes titles
- a legend (one entry for each of "Square", "LPF", "RRC")

A sample of what it might look like is included below (without labelling elements). **This sample had some curve-fitting/interpolation done to it which you do not need to do.**

{% include alert.html title="Deliverable question 5" class="info" content="Provide insight into your results. What does the BER curve tell you about these pulse-shaping options?" %}

Review the [section deliverables](#part-5-deliverables) beforing moving on.