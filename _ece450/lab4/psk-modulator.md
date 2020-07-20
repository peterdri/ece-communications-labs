---
layout: labitem
title: Part 2 - PSK Modulator

permalink: /ece450/lab4/psk-modulator
course: ece450
prev: /ece450/lab4/theory
next: /ece450/lab4/coherent-bpsk
---

## Objectives

You will build and study a complex baseband BPSK modulator as well as a real passband BPSK modulator.

---

## Part 2 deliverables

For this section, the deliverables are:

- the answers to two deliverable questions,
- a flowgraph to reuse later in the lab.

---

## Building the baseband flowgraph

Construct the following GRC flowgraph.

  ![complex-bpsk-BB-tx-blank-flowgraph.png](figures/complex-bpsk-BB-tx-blank-flowgraph.png)<br>
  __*Blank complex baseband BPSK modulator flowgraph*__

### Variables

- The `samp_rate` of this flowgraph is 76.8 kHz and the `symbol_rate` is 1200 Hz.

### Transmitter chain

Use the blocks in the above figure to create an M-sample-per-symbol complex BB BPSK signal. The signal should have peaks of 1 and -1, be pseudo-random, and the scope should show an output like the below figure (which matches the [theory section of the lab]({{ site.baseurl }}{% link _ece450/lab4/theory.md %})).

  ![complex-bpsk-PB-tx-blank-flowgraph.png](figures/complex-bpsk-PB-tx-blank-flowgraph.png)<br>
  __*Blank complex passband BPSK modulator flowgraph*__

## Building the passband flowgraph

Saving the baseband flowgraph as a new file, create a complex passband BPSK modulator flowgraph as below.

  ![complex-bpsk-PB-tx-blank-flowgraph.png](figures/complex-bpsk-PB-tx-blank-flowgraph.png)<br>
  __*Blank complex passband BPSK modulator flowgraph*__

### Variables and Import

The sample and symbol rates are unchanged. Use the *Import* block to `import numpy as np`. Now all of the [NumPy](https://numpy.org/) tools can be used.

### QT GUI Range

This block will be used to set the initial phase of the carrier frequency. Set the *Id* to `phi`. The initial value should be `-np.pi/4` and the range should go from `-np.pi` to `np.pi` in small steps (use your best judgement).

### Signal Source

This block multiplies in a carrier frequency. Set the *Frequency* to `symbol_rate` and the *Initial Phase* to `phi`.

## Run the experiment

1. Run the flowgraph and observe the waveform. Since the carrier frequency is equal to the symbol rate the flowgraph, there should be one period of the sine/cosine contained in each symbol.
2. Change the *QT GUI Time Sink* to be *Type* "Float" and to have 3 inputs. Use a *Complex To Float* block at the output of the *Mutiply* block. The three inputs to the time sink are then $$\mathbb{Re}\{s(t)\}$$, $$\mathbb{Im}\{s(t)\}$$, and the M-sample-per-symbol bitstream. Observe the passband waveform as you change $$\phi$$.

  ![complex-bpsk-PB-tx-waveform.png](figures/complex-bpsk-PB-tx-waveform.png)<br>
  __*Complex passband BPSK waveform ($$\phi=-\frac{\pi}{4}$$).*__

{% include alert.html title="Deliverable question 1" class="info" content="In the figure above (and the simulation!) what implication on __demodulation__ does changing the initial phase have?"%}

3. Set the *Frequency* of the *Signal Source* to 0. Observe the waveform while changing $$\phi$$.

{% include alert.html title="Deliverable question 2" class="info" content="When $$f_c=0$$, the waveform does not necessarily look as it did for the [complex baseband version](#building-the-baseband-flowgraph). How does the phase change this even with a signal frequency of 0? Think back to the theory section and the definition of $$\tilde{s}(t)$$."%}

Review the [section deliverables](#part-2-deliverables) before moving on.
