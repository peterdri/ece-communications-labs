
### A real-time RTL-SDR-received FSK signal

Download and open [this GRC file]({{site.baseurl}}/_ece350/lab4/data/Incomplete-FSK-receiver-RTL-SDR.grc). It is very similar to the one you built in the last lab.

Open the *QT GUI Eye Diagram* block.

- Use the included `delay` variable for the block's delay parameter
- Set the Sample Rate parameter of teh *QT GUI Eye Diagram* to the variable `samp_rate`.
- It should look like the following figure

  ![eyediagram_RTL-grc.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_RTL-grc.png)<br>
  __*GRC file of FSK demodulation being fed into a user-controlled eye diagram*__

For this section of the lab you will need to find a strong paging or FSK signal near you. A good reference for finding a signal is [RadioReference](https://www.radioreference.com/). If you are near Victoria, there are several near 142 MHz and a very strong (but intermittent) one at ~929.22 MHz. It is often easiest to find a signal using CubicSDR which has a built in FM demodulator so you can check how many levels the FSK is (top right of the figure below). If you are still unable to find a suitable signal contact your lab TA.

  ![eyediagram_FLEX-cubicsdr.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_FLEX-cubicsdr.png)<br>
  __*CubicSDR showing the very strong two level CREST FSK signal at 929.22 MHz (near Victoria, BC)*__

Execute the flowgraph and tune to your chosen 2-level FSK signal.

{%include alert.html title="Note" content="You may need to set the device argument to `rtl=0`. Try with and without and see what works on your system! Also, make sure that CubicSDR is closed while you're trying to run this flowgraph - otherwise GNU Radio can't access the radio."%}

> Check the bandwidth of the signal. You may need to adjust the filter parameters accordingly. The filter defaults to expecting a 25 kHz tone separation.

In the waterfall plot, the FSK signal will hopefully be fairly strong as in the figure below.

  ![eyediagram_CREST-waterfall.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-waterfall.png)<br>
  __*Waterfall of FSK*__

Now go to the eye diagram and set the delay to 0. It should look similar to the following figure. By setting the delay to 0, you have perfectly overlapped all 10 streams.

  ![eyediagram_CREST-scope.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-scope.png)<br>
  __*Demodulated FSK*__

Now change the delay until the eye diagram becomes clear. It may help to increase the *RF Gain* parameter.

  ![eyediagram_CREST-eyediagram.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-eyediagram.png)<br>
  __*Eye diagram of FSK signal*__

If you are unable to get a clear enough eye diagram to measure the bit rate, you may use [this file]({{site.baseurl}}/_ece350/lab4/data/FLEX_bits.wav) of demodulated FLEX 2-level paging. To use it you can check what the sample rate is (most OS's will show you in the file explorer/browser). Because it is already demodulated you just need a *WAV Source* block with the appropriate number of channels, a *Throttle* block and a *QT Eye Diagram* block.

{% include alert.html title="Deliverable Question 3" class="info" content="What is the bit rate of the control channel for the FSK signal in bits-per-second? Hint: look at the time between the symbols.

Take a screenshot of the eye diagram and attach it to your submission so the TA can confirm your bit-rate." %}
