
### A real-time USRP-received FSK signal

- Download and open [this GRC file]({{site.baseurl}}/_ece350/lab4/data/Incomplete-FSK-receiver-USRP.grc). It is very similar to the one you built in the last lab.

- Add a *QT GUI Eye Diagram* block.
  - Use the included `delay` variable for the block's delay parameter
  - It should look like the following figure

  ![eyediagram_CREST-grc.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-grc.png)<br>
  __*GRC file of FSK demodulation being fed into a user-controlled eye diagram*__

- Execute the flowgraph and tune to the 2-level FSK signal at 142.17 MHz. This signal is the control channel for the [CREST public safety radio system](http://www.crest.ca/).

  > The bandwidth of this signal is about 25 kHz compared to the 200 kHz for FM broadcast signals.

  - In the waterfall plot, the CREST signal should be fairly strong as in the figure below.

  ![eye_CREST-waterfall.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-waterfall.png)<br>
  __*Waterfall of CREST FSK*__

- Now go to the eye diagram and set the delay to 0. It should look like the following figure.
  - By setting the delay to 0, you have perfectly overlapped all 10 streams.

  ![eye_CREST-scope.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-scope.png)<br>
  __*Demodulated CREST FSK*__

- Now change the delay until the eye diagram becomes clear. It may help to increase the *RF Gain* parameter.

  ![eye_CREST-eyediagram.png]({{site.baseurl}}/_ece350/lab4/figures/eyediagram_CREST-eyediagram.png)<br>
  __*Eye diagram of CREST FSK signal*__

{% include alert.html title="Deliverable Question 3" class="info" content="What is the bit rate of the control channel for the CREST public safety radio system in bits-per-second? Hint: look at the time between the symbols." %}