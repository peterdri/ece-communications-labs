---
layout: labitem
title: Part 2 - LPF pulse shaping

permalink: /ece450/lab1/impulse-lpf-shaping
course: ece450
prev: /ece450/lab1/theory
next: /ece450/lab1/impulse-rrc-shaping
---

## Objectives

You will implement a communications system using impulses pulses as an input and a LPF (low pass filter) for pulse shaping.

---

## Part 2 deliverables

For this section, the deliverables are:

- the answer to one deliverable question,
- a dataset for later use in this lab.

---

## Building the flowgraph

Construct the following GRC flowgraph.

  ![impulses-lpf-blank-flowgraph.png](figures/impulses-lpf-blank-flowgraph.png)<br>
  __*Blank impulse LPF shaping flowgraph*__

### Variables

The `samp_rate` of this flowgraph is 100 kHz and the `symbol_rate` is 1 kHz. Leave the `sig_pwr` variable blank for now.

### Import

The argument is `import math`. This will load the [python math library](https://docs.python.org/3/library/math.html). To call the library functions you would precede them with `math`. For example, to take the square root of the number 5 you would write `math.sqrt(5)` wherever you wanted the result.

### QT GUI Range

This will be used to control the $$\frac{E_b}{N_0}$$ of the system later. Ensure it is labelled appropriately and the __*id*__ is `eb_n0_db`. The values should range from 0 to 12.

### GLFSR Source

This block outputs a pseudo-random bit stream using a shift register as described in the [theory section]({{ site.baseurl }}{% link _ece450/lab1/theory.md %}). Set the Degree of the shift register to 10 (this is the LFSR's $$M$$ value). Set it to repeat.

### Char To Float & Add Const

The output of the GLFSR block is a series of 1's and 0's. In order to build a bipolar BPSK system the 0s must become -1s. This can be done using the following equation

$$
y[n] = 2x[n]-1
$$

where $$y[n]$$ is the output stream made up of -1s and 1s and $$x[n]$$ is the input stream of 0s and 1s.

Setting the *Scale* parameter of the *Char To Float* block to 0.5 and the *Constant* parameter of the *Add Const* block to -1. You can observe the output of the *Add Const* block using a *QT GUI Constellation Sink* to see that this is now a BPSK signal.

### Low Pass Filter

The bitstream must be interpolated such that a single impulse happens at the `symbol_rate`. Then these impulses are to be pulse shaped. This can all be done directly in the *Low Pass Filter* block by setting the "Interpolation" parameter appropriately. Knowing the sampling and symbol rates, pick the appropriate interpolation rate.

{% include alert.html title="Note" content="When possible it is best to not 'hard code' when you can reference variables. The interpolation rate can be set as a function of `samp_rate` and `symbol_rate`. You could type `samp_rate**2 * symbol_rate` in, and it would work (but that would be very wrong). This makes your program robust if you later change the sampling or symbol rate. " %}

{% include alert.html title="Note" content="GRC often throws type errors like `Expression is invalid for type int`. To fix this you can either cast type by wrapping the argument in an `int()`, use the built in python operators like `//`, or use one of the math functions you previously imported like `math.ceil()`." %}

- A few other LPF parameters need to be adjusted:
  - The "FIR Type" should be "Float->Float (Interpolating)",
  - the cutoff frequency has to capture the message frequency, so setting it to twice the symbol rate (`symbol_rate*2`) will critically sample the message,
  - the transition width to `symbol_rate*0.2`.

### Noise Source

The *Amplitude* variable sets the noise standard deviation, $$\sigma$$. The noise power of pure White Gaussian noise is the variance of the distribution ($$\sigma^2$$) (text section 3.1.3.4). This means you can directly control the noise power by setting this value.

For now, set the noise *Amplitude* to 0.

### Virtual Sink & Virtual source

These blocks can be considered as connected by an "invisible" line on the flowgraph. They can be used for more complex tasks, but here they just keep the flowgraph from being criss-crossed with lines. They are also used to simulate a "transmitter" and "receiver". In this case the *Virtual Sink* transmits the noisy baseband waveform while the *Virtual Source* receives it.

### Decimating FIR Filter

Set the decimation parameter appropriately (think back to the interpolation done in the LPF), remembering to reference the symbol and sample rate variables. The block fails to compile without a taps argument so set *Taps* to 1 (meaning there is 1 tap with a value of 1).

### Binary Slicer

This block outputs a 0 for every negative input and a 1 for every positive output.

- Before adding noise the the signal, we want to measure the signal power so we use a *Multiply* block with both inputs being the signal. This gives us instantaneous power ($$s^2(t)$$) for later computing $$\frac{E_b}{N_0}$$. Set the length of the moving average filter to 1000000 (1M) and the scale to the inverse (the scale must be 1/Length in order to computer the actual moving average instead of a moving sum. GR erroneously makes this a "0" so you need to enter it as a decimal (0.0001 instea)).

### Pack K Bits

Set *K* to 8. This is the packet byte size that the later *BER* block requires.

### BER

This computes the error between the two inputs. It outputs to log of the BER, so if it outputs a value of -2, the BER is $$10^-2=0.01$$.

Set *Test Mode* to False, which will mean the block immediately starts outputting results (as opposed to waiting for the error rate to stabilize first). While *Test Mode* is False, the other parameters don't do anything, so you can leave them as they are.

### QT GUI Number sink

This will draw the output of the BER block on a number line. Set the maximum to 0 (since $$10^0=1$$ meaning that every bit is wrong) and the minumum to -7.

### Skip Head

To compute the BER of the system, the input and output bitstreams must be aligned. The filter causes a delay which can be measured by correlating the bitstreams, or observing them using a *QT GUI Time Sink* as shown in the two figures below.

To do this you can observe the overlapped bitstreams and try to find the offset between them. When the bitstreams are not aligned, the BER rate will be about 50% (this just means both streams are random and equally consist of 1s and 0s).

  ![un-delayed-bitstreams.png](figures/un-delayed-bitstreams.png)<br>
  __*A pattern found in the un-delayed bitstream. The blue bitstream between the blue arrows matches the red bitstream between the red arrows. BER=50%.*__

You will know you have the correct delay when your error rate drops to 0.

  ![delayed-bitstreams.png](figures/delayed-bitstreams.png)<br>
  __*Delay corrected bitstreams. BER=0%.*__

This is a finicky task to find the correct delay and not the intent of the delay. Assuming you have correctly set your LPF parameters, the *Skip Head* block should have the *Num Items* argument set to 6. This means the first six block inputs are discarded before the input is sent directly to the output.

### Setting LPF Gain

Test the system by running it. Observe the time sink connected to the end of the transmitter chain (below). Notice that the waveform amplitude is very low at the output of the filter. Find the amplitude of the pulse peaks and then change the "Gain" parameter in the *Low Pass Filter* block such that the waveform pulses peak at 1.

  ![lpf-no-gain.png](figures/lpf-no-gain.png)<br>
  __*Output of LPF before gain is applied.*__

  ![lpf-with-gain.png](figures/lpf-with-gain.png)<br>
  __*Output of LPF with the appropriate gain applied.*__

### Finding the signal power

In order to control the simulation, we need to set the `Eb_N0_dB` range and have that control the noise power ($$\sigma$$) in the *Noise Source* block.

Consider the following equations (some repeated from the theory section),

$$
\begin{eqnarray}
  \frac{E_b}{N_0} = SNR\frac{W}{R}, &\text{(text eqn. 3.30)},\\

  SNR = \frac{a_i^2}{\sigma_0^2}, &\text{(text eqn. 3.45)},\\

  SNR_{MAX} = \frac{2E_b}{N_0}, &\text{(text eqn. 3.52)},
\end{eqnarray}
$$

where $$a_i^2$$ is the signal power. Notice also that $$SNR$$ and $$\frac{E_b}{N_0}$$ are linear in these equations (unlike their normal use in decibels). Combining the three equations yields

$$
\frac{E_b}{N_0} = \frac{1}{2} \frac{a_i^2}{\sigma_0^2} \frac{W}{R}.
$$

Again remembering that all of these terms are linear, and that the objective is to set $$\sigma$$ using $$\frac{E_b}{N_0}$$ in decibels.

Rearranging the above gives

$$
\sigma = \sqrt{\frac{1}{2} \frac{a_i^2}{10^{\frac{E_b}{N_0}/10}} \frac{W}{R}}.
$$

Of all these parameters the only one still missing is the signal power. Build the following three blocks to measure the signal power and attach the output of the LPF to both inputs of the multiply block.

  ![power-measurement.png](figures/power-measurement.png)<br>
  __*Flow diagram to measure average power of a data stream.*__

The *Length* of the *Moving Average* block is 100000 and the *Scale* is the inverse (ensure that the inverse is a float and not an integer.)

{% include alert.html title="Note" content="Ensure that the *Scale* parameter is a float and not an integer. GR versions < 3.8 are build on Python 2 and so 1/100000 will result in the int 0. GR versions 3.8+ are built on Python 3 and so the same argument will yield the float 0.00001. In GR versions < 3.8 this can be solved by casting the entire argument as a float by wrapping it with a `float()`." %}

Run the flowgraph and record this power value. Take a second and consider whether the value you have measured is reasonable. The peaks of the LPF output are at about 1 after the gain adjustment above. Save this value in the `sig_pwr` variable block.

Now all of the variables in the above derivation for $$\sigma$$ have been found. It is now possible to control the $$\frac{E_b}{N_0}$$ of the system by holding the signal power constant and varying the noise power. Enter the expression for $$\sigma$$ in the *Amplitude* parameter of the *Noise Source* block. It is repeated below for your convenience.

```python
sigma = math.sqrt((sig_pwr/(10**(eb_n0_db/10)))*(samp_rate/symbol_rate)*0.5)
```

## Run the experiment

1. Run the flowgraph. Record the BER at $$\frac{E_b}{N_0}$$ values of 0, 4, 8 dB. It will take some time for the BER values to stabilize. Grab a coffee.

2. Offset the delay by a single sample. Check the BER with no added noise.

{% include alert.html title="Deliverable question 1" class="info" content="What do your observations suggest about the relative impact on a communications system between a timing offset and noise?"%}

Review the [section deliverables](#part-2-deliverables) before moving on.
