---
layout: labitem
title: Part 1 - Theory

permalink: /ece450/lab1/theory
course: ece450
prev: /ece450/lab1
next: /ece450/lab1/noisy-bpsk-histogram
---

The theory for this lab is covered in the textbook "Digital Communications: Fundamentals and Applications", 2nd edition, by Bernard Sklar [1]. The text section numbers referenced below are from it.

## 1.1 GLFSR data source

_From text section 12.2.2._ In order to practice pulse-shaping, it is convenient to have a random data source, with an equal number of logic 1s and 0s, or an equal number of positive and negative pulses. This can be achieved with a so-called linear feedback shift register (LFSR).

  ![lfsr.png](figures/lfsr.png) <br>
  __*Linear feedback shift register*__

At each time step (symbol time) $$T$$, the input on the left is determined by the XOR gate output and all the bits slide along one step and the output is the bit on the right. If the feedback shift register is of length $$M$$ and the feedback taps (XOR gates) are selected correctly, the output sequence will have length $$2^M -1$$ before it repeats.

For more information on this refer to Dr. Driessen's handwritten notes (pp. 29 and 33).

## 1.2 BER curves

_From text sections 3.1.4 and 3.1.5._ Is is standard to measure the performance of channels and modulation techniques using a $$BER-\frac{E_b}{N_0}$$ curve. This is closely related to the $$BER-SNR$$ curve as

$$
\frac{E_b}{N_0} = SNR\frac{W}{R}, \text{(text eqn. 3.30)},
$$

where $$SNR=\frac{S}{N}$$ (the signal to noise ratio), $$W$$ is the channel bandwidth and $$R$$ is the bit rate (all terms in the equation are linear). Hence $$\frac{E_b}{N_0}$$ is the signal to noise ratio normalized to the channel and the symbol rate. This can be intuitively understood when reorganized as $$SNR = \frac{E_b}{N_0}\frac{R}{W}$$ since the numerator is the total power of the received signal (energy-per-bit multiplied with the bit rate) while the denominator is the total noise power in the channel (noise power in 1 Hz multiplied with the number of Hz in the channel).

It is shown in the text section 3.2.2 that for a binary signal in a gaussian noise channel, this can be further simplified to $$SNR_{MAX} = \frac{2E_b}{N_0}$$ (text eqn. 3.52).

We are interested in this because we want to know the probability of receiving the correct bit. Consider the following figure,

  ![pdf-overlap.png](figures/pdf-overlap.png)<br>
  __* Overlapping conditional probability density functions (text fig. 3.2) [1]*__

At the entire symbol duration from $$a_1$$ to $$a_2$$ there is some probability in the tail of these gaussian distrubutions that the wrong signal is received. This area under the tail of a gaussian PDF (probability density function) is characterized by the Q-function (a.k.a. gaussian survival function, a.k.a. complementary error function, a.k.a. co-error function). See text section 3.2.1 for more on this, and text equation 3.4.4 for more on the Q-function.

For BPSK the function relating BER with SNR is,

$$
BER = Q\left( \sqrt{2\frac{E_b}{N_0}} \right) \text{all linear terms}
$$

where $$Q$$ is the Q-function.

## 1.3 Theory summary

BER can be calculated by measuring the SNR of a BPSK signal.

## References

[1] Sklar, B., & Ray, P. K. (2013). Digital Communications: Fundamentals and Applications (2nd ed.). Pearson. https://doi.org/10.1201/9781420049763.ch70