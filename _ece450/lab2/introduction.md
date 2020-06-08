---
layout: labitem
title: Lab 2 - Pulse Shaping and Matched Filters

permalink: /ece450/lab2
course: ece450
next: /ece450/lab2/theory
---

In this lab, you will use GNURadio to construct a baseband digital communication system including data source, pulse shaping, AWGN channel, receiver and bit error rate counter. Previously (in [Lab 1]({{site.baseurl}}{% link _ece450/lab1/introduction.md %})) you built a 1-sample-per symbol system with no pulse shaping. In this lab you will build an N-sample-per-symbol system with pulse shaping.

**If you are unfamiliar with GNU Radio, it is strongly recommended that you complete the [introductory GRC tutorials]({{site.baseurl}}{% link _GRC-tutorials/introduction.md%}) hosted on this site before trying these labs.**

You will learn about:

- pulse shaping
- timing recovery in baseband receivers
- BER (bit error rate) measurements
- The $$\frac{E_b}{N_0}$$ metric

## Prelab

1. Read the [theory page]({{site.baseurl}}{% link _ece450/lab2/theory.md%}) of this lab.
2. Read the notes at the start of Dr. Driessen's chapter 3 worksheets (Worksheet #5).
3. Consider a matched filter. Derive an expression for $$\frac{E_b}{N_0}$$ in linear terms as a function of $$a_i, \sigma_0, W, R$$ (also all in linear terms). Sklar equations 3.30 and 3.45 are a good starting point.
4. Take the derived expression above and rearrange it to solve for $$\sigma_0$$. This time the expression should be a function of $$a_i, W, R$$ (in linear terms) and $$\frac{E_b}{N_0}$$ (in dB).
5. Consider the the above derived expression for $$\sigma_0$$ in the context of a sampled system. $$a_i$$ is the signal amplitude (and so $$a_i^2$$ is the signal power), $$R$$ is the symbol frequency ($$f_{SYM}$$) and $$W$$ is the channel bandwidth. Rewrite the expression for $$\sigma$$ as a function of $$a_i^2$$, $$\frac{E_b}{N_0} \text{ (dB)}$$, $$f_{SYM}$$, and $$f_s$$.

{% include alert.html title="Prelab" content="Show this expression for $$\sigma_0$$ to your TA before beginning the lab." %}

## Deliverables

In this lab there are the following deliverables:

- a single page of answers to the deliverable questions laid out in the lab. In this lab there are 6 of them. They are all highlighted and labelled with their respective question numbers. Each question will require some thought and should be answered concisely with 1 to 2 sentences of text and perhaps an accompanying figure.
- a short code you write to generate some BER versus Eb/N0 curves
- your final BER versus Eb/N0 figure
