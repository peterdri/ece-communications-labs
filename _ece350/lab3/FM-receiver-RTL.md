
## FM broadcast receiver

In this section, we consider a practical FM receiver that can receive real off-air FM signals using the RTL-SDR. You will adjust the FM receiver built in the last part of the lab to work with these real signals.

- Open the FM receiver flowgraph you completed in the last part of this lab and make the following changes:
  - Disable the *File Source* stream up to and including the streams *Low Pass Filter* block.
  - Enable to *RTL-SDR Source* stream. You will need to reroute the inputs to the *Delay* and *Multiply Const* blocks from the newly enabled *Low Pass Filter*.

{% include alert.html title="Deliverable Question 2" class="info" content="Which blocks from the *File Source* stream are replaced with the *RTL-SDR Source* block? Which blocks are replaced with the *Low Pass Filter* block?" %}

{% include alert.html title="Deliverable Question 3" class="info" content="What is the transition width of the low pass filter used on the RTL-SDR's output? Why was this value chosen? (Hint: Consider FM broadcast channel spacings. FM channels exist at the same frequencies everywhere in the world: 88.1 MHz, 88.3 MHz, 88.5 MHz, ..., 108.1 MHz. What happens if there are a series of closely packed channels at say 101.1, 101.3 and 101.5 MHz and you want to listen to the station at 101.3 MHz?)" %}

Execute the flowgraph. By default the radio is tuned to 98.1 MHz and the RF gain is set to 7.

- You may find it helpful to add a *QT GUI Frequency Sink* and/or a *QT GUI Waterfall Sink* to the output of the *RTL-SDR Source* block (and set the sampling rate of the sink appropriately). This will allow you to observe where there are FM broadcast stations!

Look up a FM station in your area and tune to it using the slider. When you are centered on it, increase the RF gain until the channel is clearly visible in the spectrum.

- This FM receiver is not particularly useful without an audio output.
  - Add a *Rational Resampler* block after the *Complex to Arg* block and resample the signal to 48 kHz. Set the *Type* to be *Float->Float (Real Taps)*.
  - Add a *Multiply Const* block with the *Constant* parameter set to a variable, `af_gain`.
    - Notice that the variable is set using a *QT GUI Range* block.
  - Add an *Audio Sink* block with the *Sample Rate* set to 48 kHz.

- The flowgraph should now look like the following figure.

  ![fmrx_RTL-receiver-with-audio-grc.png]({{site.baseurl}}/_ece350/lab3/figures/fmrx_RTL-receiver-with-audio-grc.png)<br>
  __*RTL-SDR FM receiver with an audio output*__

- Execute the flowgraph and increase the RF Gain until the audio is legible. Sing along.

## Dynamic Range with FM

- Review the theory of [dynamic range]({{site.baseurl}}/_ece350/lab3/data/DynamicRange.pdf). These notes will also be useful for subsequent sections on dynamic range with IQ signals and on noise figure.

- Tune the RTL-SDR to a weak FM channel. You can add a *QT GUI Waterfall* at the output of the *RTL-SDR Source* to help search for a weak channel.

- Increase the RF gain from 7 dB until you hear a second radio station at the same time, or instead of the original station.

  - Notice that the signal level increases and then suddenly both noise and signal jump up and the audio changes to a different program. What is happening is that a strong signal somewhere within the 2.4 MHz bandwidth of the RTL-SDR's receiver is clipping the 8 bit A/D converter in the RTL-SDR. The 8 bit A/D converter has a dynamic range of about 48 dB (8 bits times 6 dB per bit), so a signal 48 dB above the noise floors value will clip the converter.

  - Cross‐modulation (where a strong signal transfers it's modulation to a frequency (CW tone) at the receiver input) can be shown to occur by modelling the non‐linear receiver as having the output:

    $$ y(t) = a_1 s(t) + a_2 s^2 (t) + a_3 s^3 (t) $$

    (ignoring higher order terms), where $$ s(t) $$ is the sum of the strong and the weak signal.

  - Reduce the RF gain and notice that the original signal is restored. Next, we will look for this strong signal.

- Tune the FM receiver to the strongest FM station you can find. Notice that the signal level is much higher. Now increase the RF gain to at least 20 dB and observe the signal level can be increased to above the previous limit without the audio changing. This signal may have been causing the clipping.

- Experiment more with the FM receiver. Notice that many signals can be received, FM signals are spaced every 0.2 MHz with an odd last digit, from 88.1 MHz up to 107.9 MHz.
