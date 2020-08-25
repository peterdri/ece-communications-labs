
### A real-time RTL-SDR-received FSK signal

- Download and open [this GRC file]({{site.baseurl}}/_ece350/lab4/data/Incomplete-FSK-receiver-RTL-SDR.grc). It is very similar to the one you built in the last lab.

- Add a *QT GUI Eye Diagram* block.
  - Use the included `delay` variable for the block's delay parameter
  - It should look like the following figure

  ![eyediagram_RTL-grc.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_RTL-grc.png)<br>
  __*GRC file of FSK demodulation being fed into a user-controlled eye diagram*__

For this section of the lab you will need to find a strong paging or FSK signal near you. Google it, and if you can't locate one talk to your TA.

- Execute the flowgraph and tune to your chosen 2-level FSK signal.

> Check the bandwidth of the signal. You may need to adjust the filter parameters accordingly. The filter defaults to expecting a 25 kHz tone separation.

In the waterfall plot, the FSK signal should be fairly strong as in the figure below.

  ![eyediagram_FSK-waterfall.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_FSK-waterfall.png)<br>
  __*Waterfall of FSK*__

- Now go to the eye diagram and set the delay to 0. It should look similar to the following figure.
  - By setting the delay to 0, you have perfectly overlapped all 10 streams.

  ![eyediagram_FSK-scope.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_FSK-scope.png)<br>
  __*Demodulated FSK*__

- Now change the delay until the eye diagram becomes clear. It may help to increase the *RF Gain* parameter.

  ![eyediagram_FSK-eyediagram.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_FSK-eyediagram.png)<br>
  __*Eye diagram of FSK signal*__

{% include alert.html title="Deliverable Question 3" class="info" content="What is the bit rate of the control channel for the FSK signal in bits-per-second? Hint: look at the time between the symbols.

Take a screenshot of the eye diagram and attach it to your submission so the TA can confirm your bit-rate." %}
