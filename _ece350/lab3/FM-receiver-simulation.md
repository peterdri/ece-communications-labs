---
layout: labitem
title: Part 2 - FM receiver simulator
permalink: /ece350/lab3/FM-receiver-simulation
firstHeading: Part 2 - FM receiver simulator
course: ece350
prev: /ece350/lab3/FM-transmitter-sim
next: /ece350/lab3/FM-receiver-USRP
---

<!-- [**Back to Part 1**](FM-transmitter-simulation.md) | [**Begin Part 3**](FM-receiver-USRP.md) -->

## Objectives

This part of the lab is a guide to receiving FM signal waveforms. You will:

- learn the theory and equations of FM signals, power spectra, bandwidths, and FM demodulation

- construct an FM receiver flowgraph to recover messages from an FM waveform

---

## Part 2 Deliverables
<!-- #TODO review -->

- One GRC files of an FM receiver. You will be stepped through building it.
<!-- - There is 1 question in this part. It is clearly indicated.
  - The question requires approximately 1 line of writing, and addresses a concept, not details. Answer the question and submit a single page containing the answers to your TA at the end of the lab. -->

---

## Theory

- Review the theory of [FM Signals](../../_docs/pdriessen_textbook.pdf) (section 5).
- Recall that a digital FM demodulator starts with the I and Q outputs of a general IQ receiver. For an FM signal,

    $$ s(t) = A_c cos \left( 2\pi f_c t + 2\pi k_f \int_{0}^{1} m(\alpha )d\alpha \right) $$

    $$ I(t) = A_c cos \left( 2\pi k_f \int_{0}^{1} m(\alpha )d\alpha \right) $$

    $$ Q(t) = A_c sin \left( 2\pi k_f \int_{0}^{1} m(\alpha )d\alpha \right) $$

- To extract $$ m(t) $$ from $$ I(t) $$ and $$ Q(t) $$, consider them as a complex signal.

  $$
  \begin{align*}
      s(t) &= Re \{ a(t) e^{j\phi (t)} e^{j2\pi f_c t} \} \\

      &= Re \{ [ I(t) + j Q(t) ] e^{j2\pi f_c t}\} \\

      &= Re \{ \tilde{s}(t) e^{j2\pi f_c t } \}
  \end{align*}
  $$

  where,
  
  $$
  \begin{align*}
      \tilde{s}(t) &= I(t) + jQ(t) \\
      &= a(t) e^{j\phi (t) }
  \end{align*}
  $$

- It can be shown that $$ m(t) $$ is obtained from the following formula:

  $$ m(t) = arg[ \tilde{s}(t-1) \tilde{s}^{*} (t) ] $$

  where,

  $$ (t-1) \rightarrow z^{-1} $$

  represents one sample delay.

  >**Proof**:
  >$$
  >\\
  >\begin{align*}
  >    arg[ \tilde{s}(t-1)\tilde{s}^{*} (t) ] &= arg[ a(t-1) e^{j\phi (t-1)} a(t)e^{-j\phi (t)} ] \\
  >    &= \phi (t-1)- \phi (t) \\
  >    &\approx \frac{d\phi}{dt} \\
  >    &\approx 2\pi k_f m(t) 
  >\end{align*}
  >$$

## Receiving a demodulating simulated FM signals

- To begin, download this [partially completed flowgraph](./data/Incomplete-FM-Receiver.grc).
  - The completed portion implements two sources:
    - a *USRP Source* and filter as well which is "disabled".
    - a *File Source*, down conversion, and filter which are "enabled".
  - Each of these sources can be used and controlled with the same *QT GUI Range* parameters.
  - If you want to use the USRP as a source, disable the stream coming from the *File Source*. If you want to use the *File Source* stream, do the opposite.
  - **For now, leave the *USRP Source* stream disabled and the *File Source* stream enabled.**

The output of each stream is $$ \tilde{s}(t) $$.

Before you add or change anything, the flowgraph should look like the following figure.

  ![fmrx_incomplete-grc.png](./figures/fmrx_incomplete-grc.png)<br>
  __*Incomplete flowgraph for receiving FM signals*__

- Open the *File Source* block and point it at `FM_TX_5kHz_sine.dat`.

- Execute the flowgraph and check that the output at $$ \tilde{s}(t) $$ is as expected. The spectrum should look like the following figure after the filtering.

  ![fmrx_filtered-fft.png](./figures/fmrx_filtered-fft.png)<br>
  __*Spectrum after filtering*__

- Implement $$ m(t) = arg[ \tilde{s}(t-1) \tilde{s}^{*} (t) ] $$ from the [theory section](#theory) to extract the message from the baseband signal.
  - You will need a [Delay](https://wiki.gnuradio.org/index.php/Delay) block with the *Delay* property set to 1. This delays every sample that enters the block by 1 sample.
  - You will also need one of each a [Multiply Conjugate](https://wiki.gnuradio.org/index.php/Multiply_Conjugate) block and a [Complex to Arg](https://wiki.gnuradio.org/index.php/Complex_to_Arg) block.
  - **Try to do this without looking at the figure of the final flowgraph below. Interpret the math and implement it by using the mentioned blocks.**

- Add a **QT GUI Time Sink** and a **QT GUI Frequency Sink** to the output to view the demodulated message.
  - Set the *GUI Hint* parameter of the time sink to *tabs@1*.
  - Set the *GUI Hint* parameter of the frequency sink to *tabs@2*.

- The flowgraph should now look like the following figure.

  ![fmrx_receiver-grc.png](./figures/fmrx_receiver-grc.png)<br>
  __*FM receiver flowgraph*__

- Execute the flowgraph. You should see the demodulated 2 kHz sine wave in the output spectrum and time scope.

  ![fmrx_m-of-t-sine-scope.png](./figures/fmrx_m-of-t-sine-scope.png)<br>
  __*Demodulated sine message, $$ m(t) $$ in time domain*__

  ![fmrx_m-of-t-sine-fft.png](./figures/fmrx_m-of-t-sine-fft.png)<br>
  __*Demodulated sine message, $$ m(t) $$ in frqeuency domain*__

- Switch the input file to be `FM_TX_5kHz_square.dat`. You should be able to read the `1010...` FSK sequence

  ![fmrx_m-of-t-square-scope.png](./figures/fmrx_m-of-t-square-scope.png)<br>
  __*Demodulated FSK message, $$ m(t) $$ in time domain*__

  ![fmrx_m-of-t-square-fft.png](./figures/fmrx_m-of-t-square-fft.png)<br>
  __*Demodulated FSK message, $$ m(t) $$ in frqeuency domain*__

- This flowgraph will be a deliverable. Save it as `FM_receiver.grc`, and in the *Options* block, set the following:

  - **Title:** FM receiver
  - **Author:** V00xxxxxx, V00yyyyyy (where all of your student numbers are included)

---

At this point, you should have:

- one GRC file
  - `FM_receiver.grc`

## Deliverables

From this lab part, keep the following for later submission to your TA:

- `FM_receiver.grc`
<!-- - The answer to [Question 1](#deliverable-question-1) -->

**Do not attach the `top_block.py` or `.dat` files.**

<!-- ---

[**Back to Part 1**](FM-transmitter-simulation.md) | [**Begin Part 3**](FM-receiver-USRP.md) -->
