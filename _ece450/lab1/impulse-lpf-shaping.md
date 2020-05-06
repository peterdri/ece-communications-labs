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

  ![impulses-lpf-blank-flowgraph.png](figures/impulses-lpf-blank-flowgraph.png)
  __*Blank impulse LPF shaping flowgraph*__

- The `samp_rate` has been changed to 100 kHz and a `pulse_rate` variable added (at 1 kHz).

- As an input, the *GLFSR Source* block generates a random bit stream of 1000 samples which can be set to repeat (ensure that it repeats). This is done using a shift register as described in the [theory section]({%link _ece450/lab1/theory.md%}). Set the Degree of the shift register to 10.

- We now need to interpolate this bit stream so that a single impulse happens at the `pulse_rate`. This can be done directly in the *Low Pass Filter* block by setting the "Interpolation" parameter appropriately. Knowing the sampling and pulse rates, pick the appropriate interpolation rate.

{% include alert.html title="Note" content="It can be set as a function of `samp_rate` and `pulse_rate`. You could type `samp_rate**2 * pulse_rate` in, and it would work (but that would be very wrong)." %}

- A few other LPF parameters need to be adjusted:
  - The "FIR Type" should be "Float->Float (Interpolating)",
  - the cutoff frequency has to capture the message frequency, so setting it to twice the pulse rate (`pulse_rate*2`) provides some wiggle room in the filter passband.

- The WGN (White Gaussian Noise) is controlled by a *QT GUI Range* block. The "Amplitude" here indicates the noise standard deviation which be used for estimating the noise power. The noise power of pure White Gaussian noise is the variance of the distribution (text section 3.1.3.4).

- The *Virtual Sink* and *Virtual Source* blocks can be considered as connected by an "invisible" line on the flowgraph. They can be used for more complex tasks, but here they just keep the flowgraph from being criss-crossed with lines. They are also used to simulate a "transmitter" and "receiver". In this case the *Virtual Sink* transmits the noisy baseband waveform while the *Virtual Source* receives it.

- For the receiving stream, the *Decimating FIR Filter* decimates the waveform back to the bitstream. Set the "Decimation" parameter accordingly (think back to the interpolation done in the transmitter).
  - Because the block fails to compile without a taps argument, set "Taps" to 1 (meaning there is 1 tap and it's value is 1).
  - The Automatic Gain Controller (AGC) that follows the decimator uses default parameters. It adjusts the amplitude of the input to be close to the reference (in the default, 1).

- The threshold block is used for data detection:
  - When the input signal transitions from below to above the "High" threshold, the output becomes a 1,
  - When the input signal transitions from above to below the "Low" threshold, the output becomes a 0.
  - For our input an intelligent starting place would be to have 0.25 and 0.75 as the threshold bounds, but you should set up two *QT GUI Range* blocks to control these values.

- To evaluate the system performance, we can compute the BER of the system by using the *Error Rate* block. This block compares the two input bit streams. The "Window Size" parameter determines the number of samples used for the BER computation. Use a Window Size of 10000000 and set the Bits per Symbol to 1.

{% include alert.html title="Note" content="Ensure the Window Size is at least 10 million samples, if your computer is able, increase this number as much as you can. This directly impacts the resolution of your BER measurements. The larger the window, the more accurate the measurement!" %}

- The output of the *Error Rate* block is a percentage (from 0 to 1) so set the limits of the *QT GUI Number Sink* to reflect this.

- Test the system by running it. Observe the time sink connected to the end of the receiver chain (below). Notice that the waveform amplitude is very low at the output of the filter. Find the amplitude of the pulse peaks and then change the "Gain" parameter in the *Low Pass Filter* block such that the waveform pulses peak at 1.

    ![lpf-no-gain.png](figures/lpf-no-gain.png)
    __*Output of LPF before gain is applied.*__

    ![lpf-with-gain.png](figures/lpf-with-gain.png)
    __*Output of LPF with the appropriate gain applied.*__

### Correcting timing offsets

Because the "received" bitstream is processed by more blocks before feeding into the *Error Rate* block, a delay must be added to the other input stream. The delay can be found by setting the noise amplitude to 0 and either:

- storing both streams (using *File Sink* blocks) and correlating them in Matlab or Python,
- adding a *QT GUI Range* block to control the delay block value then finding the delay value by slowing adjusting the slider. This is what the following instructions explain (you're free to correlate though!).
  - Set the "Type" in the *QT GUI Range* block to "Int" since the delay is in units of samples.
  - Remembering that the random source repeats every $$2^M-1$$ samples, set the "Start" and "Stop" parameters appropriately.
  - Add a *QT GUI Time Sink* with two float inputs: one directly from the shift register source and one from the output of the threshold block (you will need a *Char To Float* block in there too).
  - It is helpful to configure the sink plot so that there are markers. This is helpful considering both inputs are bitstreams, which we want to align.

      ![delay-qt-sink-config.png](figures/delay-qt-sink-config.png)
      __*Sink params to make finding the delay grahically a little easier*__

    - When you run the flowgraph you'll likely see an error rate of near 50 percent. If you zoom in on the time series plot you'll see that the bitstreams are not aligned. Click "Stop" on the flowgraph so that everything freezes and zoom in (you will want to enable "Control Panel" in the block settings), looking for offset patterns in the two streams. Once an offset has been found (as in the figure below), the delay can be adjusted by the correct number of samples. The delay is mostly dependent on the length of the filter taps on use. For this system, the delay is greater than 0 samples and less than 10 samples.

      ![un-delayed-bitstreams.png](figures/un-delayed-bitstreams.png)
      __*A pattern found in the un-delayed bitstream. The blue bitstream between the blue arrows matches the red bitstream between the red arrows. BER=50%.*__

    - You will know you have the correct delay when your error rate drops to 0.

      ![delayed-bitstreams.png](figures/delayed-bitstreams.png)
      __*Delay corrected bitstreams. BER=0%.*__

- Once you have the delay parameter set, you can disable the blocks you used to capture that value.

<!-- - Now collect a dataset of SNR and BER at noise amplitudes of 0.0, 0.1, 0.2, ... 0.9, 1.0.
  - The Bit Error Rate can be read off of the *QT GUI Number Sink* output. After changing the noise amplitude, let the BER stabilize before recording it. Record it to as many decimal places as you feel confident about.
  - To read the SNR, activate the "Control Panel" option in the *QT GUI Frequency Sink* block parameters. Then, while the flowgraph is running, set "Trace Options" to "Max Hold" and make sure the "Avg" slider is set to maximum. This should make it easier to read the signal SNR off of the generated spectrum.
  - As you record these values, observe the transmitted noisy pulses and the spectrum. Is the spectral shape what you expected? -->

- Record the BER rate at SNRs of 60 dB, 30 dB and 10 dB.

- Offset the delay by a single sample. Check the BER with no added noise.

{% include alert.html title="Deliverable question 1" class="info" content="What do your observations suggest about the relative impact on a communications system between a timing offset and noise?"%}

Review the [section deliverables](#part-2-deliverables) beforing moving on.
