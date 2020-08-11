
## Setup

To do this lab remotely you will need an [RTL-SDR](https://www.rtl-sdr.com/). It is recommended that you install [CubicSDR](https://cubicsdr.com/) to test out your radio. It is a user-friendly piece of software which will allow you to find signals and troubleshoot your GNU Radio flowgraphs.

The RTL-SDR digitally downconverts the received (Rx) input signal into I/Q format and sends it via USB to the computer. The RTL-SDR is not capable of transmitting signals.

- Plug your RTL-SDR into your computer (remove any connected antenna) and using CubicSDR tune to 144 MHz. You should see an internally generated tone like in the figure below.

![RTL-SDR-CubicSDR-144MHz.png]({{site.baseurl}}/_ece350/lab2/figures/part2_cubicsdr_144mhz.png)<br>
__*Internally generated 144 MHz tone*__

## I/Q Receiver

For detailed information on the usage of the RTL-SDR, you can find data sheets, user manuals as well as quickstart guides and tutorials at the dedicated [RTL-SDR website](https://www.rtl-sdr.com/).

Although the USRPs are not available to you for this lab, it is still useful to review how they work. USRPs are far more powerful than the RTL-SDR and very well documented.

Refer to the following block diagram to understand the receive path of a USRP as they are set up at UVic. The USRPs in the lab have the WBX daughtercard installed which feature a programmable attenuator, programmable local oscillator and analog I/Q mixer. The WBX daughterboard is an analog front end for the GNU Radio software. It consists of a local oscillator implemented as a wideband frequency synthesizer, thus allowing the USRP to receive signals in the range from 50 MHz to 2.2 GHz. The WBX Daughterboard performs complex downconversion of a 100 MHz slice of spectrum in the 50-2200 MHz range down to -50 to +50 MHz range for processing by the USRP motherboard.

![USRP.png]({{site.baseurl}}/_ece350/lab2/figures/USRP.png)<br>
__*USRP block diagram.*__

The main function of the USRP motherboard is to act as a [Digital Downconverter (DDC)](http://en.wikipedia.org/wiki/Digital_down_converter). The motherboard implements a digital I/Q mixer, sample rate converter and lowpass filter. The samples are then sent to the host PC over a gigabit ethernet link.

RTL-SDR is a name used by a variety of dongles which are all based on the same premise - making cheap SDRs easily available and supported by open-sourced software. Depending on which dongle you have it may be able to receive frequencies from 500 kHz up to 2 GHz.

### I/Q Receiver output

- Review [IQ theory](../../_docs/pdriessen_IQ.pdf).

- Download and open the GRC file [general-IQ-from-RTL.grc]({{site.baseurl}}/_ece350/lab2/data/general-IQ-from-RTL.grc).

  - The *RTL-SDR Source* block outputs the complex signal $$ I(t) + jQ(t) $$.
  - This output is connected to 4 blocks that extract the magnitude, phase, real and imaginary parts of the complex signal, as well as a constellation scope and waterfall plot.
  - The *RTL-SDR Source* is tuned to a frequency of 144 MHz.

- Execute the flowgraph. Observe the waterfall plot and see that there is a signal right in the center of the received spectrum at 144 MHz. Now observe the Output Display window with 4 tabs labelled **IQ Plane, Magnitude, Phase** and **IQ Scope Plot**.

  - The "IQ Plane" tab should show a circle. Turn up the *RF Gain* parameter to 60 and see if the increased gain makes the circle bigger. This makes sense as the amplitude of the received signal has become larger.
  - The "Magnitude" tab will show a (noisy) DC level
  - The "Phase" tab will show a phase ramp wrapping between $$ -\pi $$ and $$ \pi $$ (saw-tooth wave) with a period that is the reciprocal of the frequency offset ( $$ f_b $$)
  - The "IQ Scope Plot" tab will show the real and imaginary sine waves.

  > Change the *X Max* parameter and use the *Autoscale* button on some of the plots to get a cleaner display.

- Determine the frequency $$ f_b $$ of the sine waves using the Phase display as well as the Real and Imaginary displays by placing your mouse cursor over the scope plot to show the time offset at different points on the waveform as in the figure below.

  ![part2_phase-ramp-rtl.png]({{site.baseurl}}/_ece350/lab2/figures/part2_phase-ramp-rtl.png)<br>
  __*Phase ramp showing frequency offset*__

- This frequency $$ f_b $$ represents the offset between the received RF signal $$ f_c $$ and the USRP local oscillator $$ f_{LO} $$, so that

  $$ f_b  = f_c  - f_{LO} $$

  The input RF signal is described by:

    $$
    \begin{align*}
      s(t) &= a(t) e^{j\phi (t)} e^{j2\pi f_c t} \\
      &= a(t)cos\left( 2\pi f_c t + \phi (t)\right) + ja(t)sin\left( 2\pi f_c t+ \phi (t) \right)
    \end{align*}
    $$

  The local oscillator is described by:

    $$ e^{-j\pi f_{LO} t}  = cos\left( 2\pi f_{LO} t \right) - jsin\left( 2\pi f_{LO} t \right) $$

  When the two are multiplied, and $$ f_b  = f_c  - f_LO $$ is substituted:

    $$ I(t) = a(t)cos\left( 2\pi f_b t + \phi (t) \right) $$

    $$ Q(t) = a(t)sin \left( 2\pi f_b t + \phi (t) \right) $$

  This is how you are able to read $$ f_b $$ directly off of the phase ramp.

  - Confirm that $$ f_b $$ is as expected (ask your TA for $$ f_c $$)
  - To find $$ f_c $$, ask your TA or go check the signal generator at the back of the lab.

- The USRP source block has the *Clock Source* set to use an *External* 10 MHz clock reference frequency, and the same external reference is used for the signal generator. Thus the frequency difference between the USRP source block (local oscillator) and signal generator RF frequency will be observed to be exactly as expected from their respective frequency settings.

  - If we change the USRP source block to use an *Internal* clock reference, then expect to observe some frequency error between the signal generator and the USRP frequency settings as they are running from independent oscillators.
  - Try changing the USRP clock source to *Internal* and repeat the frequency measurement of the I and Q outputs. You will see the frequency drifting over time.

### Dynamic range with IQ signals

- Ask the TA to vary the 200 MHz signal generator level from ‐10 dBm (dB relative to one milliwatt) to 10 dBm in 1 dB steps. Some of the steps are shown in the figures below.

- Observe and describe how the signals look at each signal level, and explain why.
  >The waveform appearance results from clipping in the 2 ADCs (one ADC for I, one ADC for Q).

  ![part2_constellation-round.png]({{site.baseurl}}/_ece350/lab2/figures/part2_constellation-round.png)<br>
  __*Round constellation plot showing no clipping in the ADCs*__

  ![part2_constellation-squashed.png]({{site.baseurl}}/_ece350/lab2/figures/part2_constellation-squashed.png)<br>
  __*Squashed constellation plot showing some clipping in the ADCs*__

  ![part2_constellation-square.png]({{site.baseurl}}/_ece350/lab2/figures/part2_constellation-square.png)<br>
  __*Square constellation plot showing extreme clipping in the ADCs*__

{% include alert.html title="Deliverable Question 1" class="info" content="Why do you see the constellation plot of the I/Q plane get squashed from a circle into a square as you increase the power of the received signal?" %}

Look at the plot of the phase now. **Why does the phase ramp become a staircase? How does this relate to the constellation diagram?**

## IQ Transmitter

### Carrier wave transmission

In this section, we test the transmit functions of the USRP that we can use later when building a communications system. We will observe the transmitted spectrum, minimum and maximum power level in dBm. You will use both the osciloscope and the spectrum analyzer at your bench to view and measure the output from the USRP transmitter.

- Review the theory of [spectrum analyzers](../../_docs/pdriessen_textbook.pdf) (section 1.4)
  > For more detailed information, you may also wish to review [Spectrum Analyzer Basics](../../_docs/5965-7920E.pdf) and [The Basics of Spectrum Analyzers](../../_docs/spec_analyzer.pdf). **The concepts presented here will be applicable to any spectrum analyzer you may use in your career.**

- Download and open [this GRC file]({{site.baseurl}}/_ece350/lab2/data/tx_carrier.grc).

- Observe that the USRP sink center frequency is set to 50 MHz. This block represents the USRP transmitter hardware.

- Observe that the sine and cosine signal sources are configured for 10 kHz.

- Connect the USRP Tx output to the spectrum analyzer and execute the flowgraph. A scope display will come up along with three buttons that allow you to select different values for Q(t).

- Set the spectrum analyzer's center frequency to 50 MHz and the span to 50 kHz by using the FREQUENCY and SPAN buttons. Adjust the LEVEL as necessary.

- What do you observe on the spectrum analyzer display with Q(t) = 0? Try the other two options for Q(t). What do you observe on the spectrum analyzer?

{% include alert.html title="Deliverable Question 2" class="info" content="The GRC flowgraph shows a complex stream getting fed into the USRP. How come when **Q(t)=0** a real spectrum is shown on the spectrum analyzer?" %}

### USRP power levels

- What is the minimum and maximum signal power output from the USRP? The USRP output power level can be set via the *QT GUI Range Widget* seen when running the flowgraph.

{% include alert.html title="Deliverable Question 3" class="info" content="Why, when the USRP is active in transmit-mode, is its minimum output power greater than 0?" %}
