---
layout: labitem
title: Part 2 - Pulse shaping in GRC

permalink: /ece450/lab1/pulse-shaping
course: ece450
prev: /ece450/lab1/pulse-shaping-theory
next: /ece450/lab1/pulse-shaping
---

## Objectives

You will implement the three pulse shaping methods described in the previous theory section of this lab. 

<!-- TODO check under "Lab instructions" heading -->

---

## Part 2 deliverables

TBD

---

## Square pulse shaping

Construct the following GRC flowgraph.

  ![](figures/square-pulses-blank-flowgraph.png) <br>
  __*Blank square pulse shaping flowgraph*__

- The `samp_rate` has been changed to 100 kHz and a `pulse_rate` variable added (at 1 kHz).

- As an input, the *Random Source* block generates a random bit stream of 1000 samples which can be set to repeat (ensure that it repeats). We now desire to shape each of those bits into a square pulse. This is done using the *Repeat* block. Knowing the sampling and pulse rates, pick the appropriate interpolation rate. Notice as well that when the minimum and maximum parameters are 0 and 2 respectively, it means `[0, 2)` so the values output are only ever a 0 or a 1.

{% include alert.html title="Note" content="It can be set as a function of `samp_rate` and `pulse_rate`. You could type `samp_rate**2 * pulse_rate` in, and it would work (but that would be very wrong)." %}

- The WGN (White Gaussian Noise) is controlled by a *QT GUI Range* block. The "Amplitude" here indicates the noise standard deviation which be used for calculating the SNR.

- The *Virtual Sink* and *Virtual Source* blocks can be considered an "invisible" line on the flowgraph. They can be used for more complex tasks, but here they just keep the flowgraph from being criss-crossed with lines. They are also used to simulate a "transmitter" and "receiver". In this case the *Virtual Sink* transmits the noisy baseband waveform while the *Virtual Source* receives it.

- The *Rational Resampler* is used to turn the received pulses back into a bitstream. You will need to set the interpolation and decimation rates appropriately (think back to the interpolation factor you chose above for the *Repeat* block).

- The threshold block is used for data detection:
  - When the input signal transitions from below to above the "High" threshold, the output becomes a 1,
  - When the input signal transitions from above to below the "Low" threshold, the output becomes a 0.
  - For our input an intelligent starting place would be to have 0.25 and 0.75 as the threshold bounds, but you should set up two *QT GUI Range* blocks to control these values.

- To evaluate the system performance, we can compute the BER of the system by using the *Error Rate* block. This block compares the two input bit streams. The "Window Size" parameter determines the number of samples used for the BER computation. Use a Window Size of 1000 and set the Bits per Symbol to 1.

- Because the "received" bitstream is processed by more blocks before feeding into the *Error Rate* block, a delay must be added to the other input stream. The delay can be found by setting the noise amplitude to 0 and either:
  - storing both streams (using *File Sink* blocks) and correlating them in Matlab or Python,
  - adding a *QT GUI Range* block to control the delay. In this case, set the "Type" in the *QT GUI Range* block to "Int" since the delay is in units of samples.