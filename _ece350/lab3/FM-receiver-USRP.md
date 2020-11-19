
## FM broadcast receiver

In this section, we consider a practical FM receiver that can receive real off-air FM signals using the USRP. You will adjust the FM receiver built in the last part of the lab to work with these real signals.

- Open the FM receiver flowgraph you completed in the last part of this lab.

- Disable the *File Source* stream up to and including the *Float To Complex* block.

- Enable to *USRP Source* stream. You will need to reroute the inputs to the *Delay* and *Multiply Const* blocks from the newly enabled *Low Pass Filter*.

{% include alert.html title="Deliverable Question 2" class="info" content="Which blocks from the *File Source* stream are replaced with the *USRP Source* block? Which blocks are replaced with the *Low Pass Filter* block?" %}

{% include alert.html title="Deliverable Question 3" class="info" content="What is the transition width of the low pass filter used on the USRP's output? Why was this value chosen? (Hint: Consider FM Broadcast channel spacings.)" %}

- Execute the flowgraph and Observe the waterfall and spectrum.
  - The radio is tuned to 98.1 MHz (an FM station in Seattle), the RF gain is set to 7.

- Notice the noise level of the filtered signal is around ‐120 dBm and the signal peak level is 10‐20 dB higher than that.

- This FM receiver is not particularly useful without an audio output.
  - Add a *Rational Resampler* block after the *Complex to Arg* block and resample the signal to 48 kHz. Set the *Type* to be *Float->Float (Real Taps)*.
  - Add a *Multiply Const* block with the *Constant* parameter set to a variable, `af_gain`.
    - Notice that the variable is set using a *QT GUI Range* block.
  - Add an *Audio Sink* block with the *Sample Rate* set to 48 kHz.

- The flowgraph should now look like the following figure.

  ![fmrx_USRP-receiver-with-audio-grc.png]({{site.baseurl}}/_ece350/lab3/figures/fmrx_USRP-receiver-with-audio-grc.png)<br>
  __*USRP FM receiver with an audio output*__

- Execute the flowgraph. Tune to 101.9 MHz (CFUV) which is the radio station run on UVic's campus transmitted from the Student Union Building. Sing along.

## Dynamic Range with FM

- Review the theory of [dynamic range]({{site.baseurl}}/_ece350/lab3/data/DynamicRange.pdf). These notes will also be useful for subsequent sections on dynamic range with IQ signals and on noise figure.

- Tune the USRP to the FM broadcast station at 101.5 MHz.

- Increase the RF gain from 7 dB until you hear a second radio station at the same time, or instead of the original station.

  - Notice that the signal level increases and then suddenly both noise and signal jump up and the audio changes to a different program.

  > What is happening is that a strong signal somewhere within the 40 MHz bandwidth of the USRP's receiver is clipping the 14 bit A/D converter in the USRP. The 14 bit A/D converter has a dynamic range of about 84 dB (14 bits times 6 dB per bit), so a signal above about ‐100 dBm + 84 dB = ‐16 dBm will clip the converter. With the RF gain set to around 20 dB, the receiver becomes non‐linear and the audio from the strong signal is cross‐modulating on top of the signal at 98.1 MHz.

  - Cross‐modulation can be shown to occur by modelling the non‐linear receiver as having the output:

    $$ y(t) = a_1 s(t) + a_2 s^2 (t) + a_3 s^3 (t) $$

    (ignoring higher order terms), where $$ s(t) $$ is the sum of the strong and the weak signal.

  - Reduce the RF gain and notice that the original signal is restored. Next, we will look for this strong signal.

- Tune the FM receiver to 101.9 MHz (the local UVic radio station CFUV). Notice that the signal level is much higher (close to ‐30 dBm). Now increase the RF gain to at least 20 dB and observe the signal level can be increased to above ‐16 dBm, however, the audio is not changed. This signal at 101.9 MHz was causing the clipping.

- Experiment more with the FM receiver. Notice that many signals can be received, FM signals are spaced every 0.2 MHz with an odd last digit, from 88.1 MHz up to 107.9 MHz.
