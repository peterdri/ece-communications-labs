---
layout: labitem
title: Part 3 - LPF pulse shaping

permalink: /ece450/lab1/impulse-lpf-shaping
course: ece450
prev: /ece450/lab1/square-pulse-lpf-shaping
next: /ece450/lab1/rrc-pulse-shaping
---

## Objectives

You will implement a communications system using a Low Pass Filter (LPF) for pulse shaping.

---

## Part 3 deliverables

For this section, the deliverables are:

- the answer to one deliverable question,
- a dataset for later use in this lab.

---

## LPF pulse shaping

Construct the following GRC flowgraph. It is very similar to the square pulse shaped flowgraph but the interpolation mothod has changed. You can "File>Save As" in GRC in order to not begin from scratch again.

  ![lpf-pulse-blank-flowgraph.png](figures/lpf-pulse-blank-flowgraph.png) <br>
  __*Blank LPF pulse shaping flowgraph*__
  
- For the transmitting stream, the *Low Pass Filter* has a series of parameters that need adjusting. We can use this block to first interpolate the bit stream and then filter it.
  - The "FIR Type" should be "Float->Float (Interpolating)",
  - the interpolation factor is the same function of sampling rate and pulse rate as before,
  - the cutoff frequency has to capture the message frequency, so setting it to twice the pulse rate (`pulse_rate*2`) provides some wiggle room in the filter passband.

- For the receiving stream, the *Decimating FIR Filter* decimates the waveform back to the bitstream. Set the "Decimation" parameter accordingly. Because the block fails to compile without a taps argument, set "Taps" to 1 (meaning there is 1 tap and it's value is 1. This has no impact on the waveform). The Automatic Gain Controller (AGC) that follows the decimator uses default parameters. It adjusts the amplitude of the input to be close to the reference (in the default, 1).

- Test the system by running it. Observe the time sink connected to the end of the receiver chain (below). Notice that the waveform amplitude is very low at the output of the filter. Find the amplitude of the pulse peaks and then change the "Gain" parameter in the *Low Pass Filter* block such that the waveform pulses peak at 1.

    ![lpf-no-gain.png](figures/lpf-no-gain.png) <br>
    __*Output of LPF before gain is applied.*__

    ![lpf-with-gain.png](figures/lpf-with-gain.png) <br>
    __*Output of LPF with the appropriate gain applied.*__

- Using the same method as in the [previous section of the lab]({% link _ece450/lab1/square-pulse-shaping.md %}), find the system delay and apply it. Again, it will differ by computer but mine was around 6.

- Now collect a dataset of SNR and BER at noise amplitudes of 0.0, 0.1, 0.2, ... 0.9, 1.0.
  - The Bit Error Rate can be read off of the *QT GUI Number Sink* output. After changing the noise amplitude, let the BER stabilize before recording it.
  - To read the SNR, activate the "Control Panel" option in the *QT GUI Frequency Sink* block parameters. Then, while the flowgraph is running, set "Trace Options" to "Max Hold" and make sure the "Avg" slider is set to maximum. This should make it easier to read the signal SNR off of the generated spectrum.
  - As you record these values, observe the transmitted noisy pulses and the spectrum. Are you able to read the bitstream off of the received waveform? At which SNR can you no longer do this?

{% include alert.html title="Deliverable question 2" class="info" content="How do the bit error values compare between square pulses and low pass filtered pulses? What is this attributable to?" %}

Review the [section deliverables](#part-3-deliverables) beforing moving on.
