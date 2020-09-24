
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

- Review [IQ theory](../../_docs/pdriessen_textbook.pdf) in the textbook (Section 1.1).

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

- This frequency $$ f_b $$ represents the offset between the received RF signal $$ f_c $$ and the SDR's local oscillator $$ f_{LO} $$, so that

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

  When the two are multiplied, and $$ f_b  = f_c  - f_{LO} $$ is substituted:

    $$ I(t) = a(t)cos\left( 2\pi f_b t + \phi (t) \right) $$

    $$ Q(t) = a(t)sin \left( 2\pi f_b t + \phi (t) \right) $$

  This is how you are able to read $$ f_b $$ directly off of the phase ramp.

- Assuming that $$f_c$$ is exactly 144 Mhz, use the phase ramp to find your RTL-SDRs local oscillator frequency. Confirm your solution for $$f_{LO}$$ with your TA.

### Dynamic range with IQ signals

> This section is possible to do in practice if you have a signal generator nearby. If so, set it to generate a 200 MHz tone with the minimum possible amplitude (when done in the lab the starting amplitude is -10 dBm) and plug the output into your RTL-SDR using a coaxial cable. Then slowly and carefully (so as not to fry your SDR), increase the amplitude until you see what is outlined below.
>
> If you do not have a signal generator at home follow along with the following explanation instead.

As your radio receives a pure tone, the constellation looks like the following figure.

  ![part2_constellation-round.png]({{site.baseurl}}/_ece350/lab2/figures/part2_constellation-round.png)<br>
  __*Round constellation plot showing no clipping in the ADCs*__

As the amplitude of the signal is increased, the radius of the circle grows until the ADCs (one for I and one for Q) begin clipping and the constellation starts to get "squashed" as in the following figure.

  ![part2_constellation-squashed.png]({{site.baseurl}}/_ece350/lab2/figures/part2_constellation-squashed.png)<br>
  __*Squashed constellation plot showing some clipping in the ADCs*__

This continues until the constellation is a square at which point increasing the signal amplitude makes no difference to the constellation.

  ![part2_constellation-square.png]({{site.baseurl}}/_ece350/lab2/figures/part2_constellation-square.png)<br>
  __*Square constellation plot showing extreme clipping in the ADCs*__
  
{% include alert.html title="Deliverable Question 1" class="info" content="Why do you see the constellation plot of the I/Q plane get squashed from a circle into a square as you increase the power of the received signal?" %}

## IQ Transmitter

### Carrier wave transmission

The RTL-SDR is a receive-only SDR and so cannot transmit signals. Follow along with the description and simulation below to explore some key ideas to do with SDR transmission.

Download [this GRC file]({{site.baseurl}}/_ece350/lab2/data/RTLSDR_tx_sim.grc).

- Review the theory of [spectrum analyzers](../../_docs/pdriessen_textbook.pdf) (section 1.4)
  > For more detailed information, you may also wish to review [Spectrum Analyzer Basics](../../_docs/5965-7920E.pdf) and [The Basics of Spectrum Analyzers](../../_docs/spec_analyzer.pdf). **The concepts presented here will be applicable to any spectrum analyzer you may use in your career.**

Consider a setup where you have an SDR transmitting a complex signal. The complex signal is made up of two tones, a cosine and a sine as in the figure below.

  ![part2_tx_block_diagram.png]({{site.baseurl}}/_ece350/lab2/figures/part2_tx_block_diagram.png)<br>
  __*GRC block diagram to transmit a complex signal through a USRP.*__

Notice that:

- the SDR's center frequency is set to 50 MHz,
- the sine and cosine signal sources are set to 10 kHz.

What frequency do you expect the transmitted signal to be at? The SDR will take a baseband input and shift it up to the desired passband center frequency. In this case the transmitted signal exists at 50.01 MHz (50 MHz + 10 kHz).

Plugging a USRP into a spectrum analyzer and running this program yields the following output.

  ![part2_spectrum-analyzer1.jpg]({{site.baseurl}}/_ece350/lab2/figures/part2_spectrum-analyzer1.jpg)<br>
  __*Spectrum analyzer output with $$f_c = 50.01 MHz$$.*__

You can see the same thing by running the above GRC simulation and setting $$Q(t)=sin(2*\pi*f_c*t)$$. Look through the simulation to see how this works (what is it changing in the signal source blocks?).

In this case $$f_c = 50.01 MHz$$. The signal is complex and can be written as:

$$
\begin{align}
s(t) &= e^{j2\pi f_c t} \\
&= sin(2\pi f_c t) + jcos(2\pi f_c t)\\
\end{align}
$$

Now, changing the amplitude of the signal source which makes up $$Q$$ to be negative yields the following spectrum.

  ![part2_spectrum-analyzer2.jpg]({{site.baseurl}}/_ece350/lab2/figures/part2_spectrum-analyzer2.jpg)<br>
  __*Spectrum analyzer output with $$f_c = 49.99 MHz$$.*__

Running the simulation and setting $$Q(t)=-sin(2*\pi*f_c*t)$$ will show the same thing - a single frequency component shifted down from the center of the spectrum.

In this case the signal can be written as:

$$
\begin{align}
s(t) &= e^{j2\pi f_c t} \\
&= sin(2\pi f_c t) - jcos(2\pi f_c t)\\
\end{align}
$$

Finally, changing the amplitude of the signal source which is fed into  $$Q$$ to be 0 yields the following spectrum.

  ![part2_spectrum-analyzer3.jpg]({{site.baseurl}}/_ece350/lab2/figures/part2_spectrum-analyzer3.jpg)<br>
  __*Spectrum analyzer output with $$f_c = 50 MHz$$.*__

In the simulation, set $$Q(t)=0$$ to see this real signal.

In this case the signal can be written as:

$$
\begin{align}
s(t) &= e^{j2\pi f_c t} \\
&= sin(2\pi f_c t)\\
\end{align}
$$

{% include alert.html title="Deliverable Question 2" class="info" content="The GRC flowgraph simulation shows a *complex* stream getting fed into the *QT GUI Frequency Sink* block. How come when $$Q(t)=0$$ a *real* spectrum is shown on the Frequency sink (as well as the actual spectrum analyzer)?" %}

### USRP power levels

The *USRP Sink* and *RTL-SDR Source* blocks include parameters for the radio hardware. In the last section the the radio center frequency was set. Another key parameter is to change the power output by a transmitter. The spectrum analyzer screen shows the following output for a positive gain value (note the dB level of the peak).

  ![part2_spectrum-analyzer3.jpg]({{site.baseurl}}/_ece350/lab2/figures/part2_spectrum-analyzer3.jpg)<br>
  __*Spectrum analyzer output with a positive transmitter gain value.*__

Without changing the *Signal Source* blocks, but changing the gain of the transmitter to 0 yields the following spectrum analyzer output. Again note the dB level of the peak.

  ![part2_spectrum-analyzer4.jpg]({{site.baseurl}}/_ece350/lab2/figures/part2_spectrum-analyzer4.jpg)<br>
  __*Spectrum analyzer output with a transmitter gain value of 0.*__

{% include alert.html title="Deliverable Question 3" class="info" content="The USRP is plugged in, powered on and tied with coaxial cable into the spectrum analyzer. Why, when the USRP is active in transmit-mode, is its minimum output power greater than 0?" %}
