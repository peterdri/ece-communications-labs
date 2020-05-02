---
layout: labitem
title: Part 4 - RRC pulse shaping

permalink: /ece450/lab1/rrc-pulse-shaping
course: ece450
prev: /ece450/lab1/lpf-pulse-shaping
next: /ece450/lab1/BER-calculation
---

## Objectives

You will implement a communications system using a Root Raised Cosine (RRC) filter for pulse shaping. 

---

## Part 4 deliverables

TBD

---

## RRC pulse shaping

Construct the following GRC flowgraph. It is very similar to the previous pulse shaping flowgraphs. You can "File>Save As" in GRC in order to not begin from scratch again.

  ![rrc-pulse-blank-flowgraph.png](figures/rrc-pulse-blank-flowgraph.png) <br>
  __*Blank RRC pulse shaping flowgraph*__

- The receiver chain is unchanged from the LPF version.

- The tranmitter chain is now pulse shaping with a *Root Raised Cosine Filter* block.
  - The filter roll-off factor ($$\alpha$$) indirectly specifies the bandwidth of the filter. Set $$\alpha=0.35$$.
  - An ideal RRC filter has an infinite number of taps but in practice must be windowed. Set the number of taps to the sampling rate.
  - The symbol rate is the pulse rate (considering we're operating a random source with one bit per symbol).
  - The interpolation factor is the same as for the previous pulse-shaping methods (and for all pulse shaping methods it is the number of samples per pulse when coming from a bit stream to a waveform).
  - The gain can be found in the same way as with the LPF pulse shaping. Measure the amplitude and set the gain such that the shaped pulses are 1 or 0.

- The delay can be found as before. For me it was 500 samples with the above listed filter parameters.

- Note the added *QT GUI Frequency Sink* block. You will use it with "Trace hold" set to "Max" to measure the SNR of the received noisy signal.

- Record the BER values for noise amplitudes of 0, 0.25, 0.5, 0.75 and 1. Observe the transmitted noisy pulses to see whether you're able to visually read off the bitstream.
