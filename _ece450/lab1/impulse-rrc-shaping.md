---
layout: labitem
title: Part 3 - RRC pulse shaping

permalink: /ece450/lab1/impulse-rrc-shaping
course: ece450
prev: /ece450/lab1/impulse-lpf-shaping
next: /ece450/lab1/calculating-ber
---

## Objectives

You will implement a communications system using a Root Raised Cosine (RRC) filter for pulse shaping.

---

## Part 3 deliverables

For this section, the deliverables are:

- the answers to three deliverable questions,
- a dataset for later use in this lab.

---

## RRC pulse shaping

Construct the following GRC flowgraph. It is very similar to the previous pulse shaping flowgraphs. You can "File>Save As" in GRC in order to not begin from scratch again.

  ![impulses-rrc-blank-flowgraph.png](figures/impulses-rrc-blank-flowgraph.png)<br>
  __*Blank RRC pulse shaping flowgraph*__

- The tranmitter chain is now pulse shaping with a *Root Raised Cosine Filter* block.
  - The filter is of type "Float->Float (Interpolating)".
  - The filter roll-off factor ($$\alpha$$) indirectly specifies the bandwidth of the filter. Set $$\alpha=0.35$$.
  - An ideal RRC filter has an infinite number of taps but in practice must be windowed. Set the number of taps to the sampling rate.
  - The symbol rate is the pulse rate (considering we're operating a random source with one bit per symbol).
  - The interpolation factor is the same as for the previous pulse-shaping methods (and for all pulse shaping methods it is the number of samples per pulse when coming from a bit stream to a waveform).
  - The gain can be found in the same way as with the LPF pulse shaping. Measure the amplitude and set the gain such that the shaped pulses are 1 or 0.

- The receiver chain is now using a matching *Root Raised Cosine Filter* to obtain a final pulse shape that is a raised cosine (review [the theory section]({% link _ece450/lab1/theory.md %}) for more on this).
  - The filter is of type "Float->Float (Decimating)"
  - Set the number of taps to the sampling rate.
  - Set the symbol rate and decimation rates appropriately.
  - Do not change the gain, by observing the output of the filter you will see that the input symbols (scaled to 1 above) are all either 1 or 0. The threshold block helps when noise is added, so leave it in.

{% include alert.html title="Note" content="Since this is a **matched filter** it is the dual to the transmitter RRC filter. It's parameters should reflect this." %}

- The delay can be found as before. It is 1000 samples with the above listed filter parameters (which means a 500 sample delay for each of the matched filters).

- Now collect a dataset of signal power and BER values at noise standard deviations of 0.0, 0.1, 0.2, ..., 0.9, 1.0.
  - Since we can set the standard deviation of the noise source, we can estimate the noise power (text section 3.1.3.4)
  - The Bit Error Rate can be read off of the appropriate *QT GUI Number Sink* output. After changing the noise variance, let the BER stabilize before recording it. Remember that the sampling rate of the system is 100 kHz and the averaging window for the BER measurement is 10M samples. It follows that the first valid BER value will be delivered after 100s. I waited 5 minutes for each number to stabilize to 4 decimal places
  - To get the signal power, read off of the appropriate *QT GUI Number Sink* output. This number should not change with the noise power since it is measured before the WGN is added to the signal.
  - As you record these values, observe the transmitted noisy pulses. How does the spectral shape compare with the LPF version?

- Change the noise amplitude back to 0 and offset the delay value by 1.

{% include alert.html title="Deliverable question 2" class="info" content="Consider the time domain shape (impulse response) of the root raised cosine filter. In an ideal system, RRC filters have zero-ISI (inter-symbol interference). Why is this? It may help your understanding to draw multiple pulses `[1, 1, 1]` next to each other." %}

{% include alert.html title="Deliverable question 3" class="info" content="Consider the relative impact of noise versus a timing offset on the system. Does the RRC filter fare any better than the square pulses did with an offset of 1 sample?" %}

{% include alert.html title="Deliverable question 4" class="info" content="Consider the results you gathered for the LPF pulse shaping method (at noise powers of 0.01, 0.025 and 0.1). How do they compare with this matched filter version?" %}

Review the [section deliverables](#part-3-deliverables) beforing moving on.
