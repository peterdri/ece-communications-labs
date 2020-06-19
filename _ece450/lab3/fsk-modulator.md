---
layout: labitem
title: Part 2 - FSK Modulator

permalink: /ece450/lab3/fsk-modulator
course: ece450
prev: /ece450/lab3/theory
next: /ece450/lab3/non-coherent-fsk
---

## Objectives

You will build and study a complex baseband FSK modulator.

---

## Part 2 deliverables

For this section, the deliverables are:

- the answer to one deliverable question,
- a dataset for later use in this lab.

---

## Building the flowgraph

Construct the following GRC flowgraph.

  ![bfsk-tx-blank-flowgraph.png](figures/bfsk-tx-blank-flowgraph.png)<br>
  __*Blank BFSK modulator flowgraph*__

### Variables

- The `samp_rate` of this flowgraph is 76.8 kHz and the `symbol_rate` is 1200 Hz.
- Set the `deviation` variable appropriately (review the [theory section]({{ site.baseurl }}{% link _ece450/lab3/theory.md %}) if needed).
- Leave the other variables set to 0 for now.

### Import

Import the math library with `import math`.

### GLFSR Source

This block outputs a pseudo-random bit stream using a shift register as described in the [theory section of Lab 1]({{ site.baseurl }}{% link _ece450/lab1/theory.md %}). Set the Degree of the shift register to 20 (this is the LFSR's $$M$$ value). Set it to repeat.

### Char To Float & Add Const

The output of the GLFSR block is a series of 1's and 0's. In order to build a bipolar signal the 0s must become -1s. This can be done using the following equation

$$
y[n] = 2x[n]-1
$$

where $$y[n]$$ is the output stream made up of -1s and 1s and $$x[n]$$ is the input stream of 0s and 1s.

Setting the *Scale* parameter of the *Char To Float* block to 0.5 and the *Constant* parameter of the *Add Const* block to -1. You can observe the output of the *Add Const* block using a *QT GUI Constellation Sink* to see that this is now a bipolar signal.

### Repeat

Now use the repeat block to turn the 1-sample-per-symbol signal into an M-sample-per-symbol square pulse-shaped signal. Use the `samp_rate` and `symbol_rate` variables.

### Embedded Python Block

This block allows you to create a custom block by writing some Python and embedding it in the flowgraph. Recalling the expression for a sampled complex baseband BFSK signal, the output of the *Repeat* block is $$m(\alpha)$$. This *Embedded Python Block* will be made into a cumculative sum block so that the output of the block is the integral, $$\int_0^t m(\alpha)d\alpha$$.

Open the block and click "Open in Editor". You will now be able to edit the Python that processes the input. The code already filling the block takes the input and multiplies it by a constant, delivering the product as the blocks output. First look at the constructor (`__def init()`). It takes an argument and a default value for it, `example_param=1.0`. Anything added here becomes a parameter of the block which can be easily adjusted from the normal block parameters GUI. Since the cumulative sum requires no input paramters, remove the argument.

A few lines lower is the name of the block, `name='Embedded Python Block'`. You can change it to something more meaningful, like `CumSum` so that the flowgraph is easy to interpret. The next two lines indicate the input and output signal types. The default is `np.complex64`. Looking back at the flowgraph you can see that the necessary datatype is a float (`np.float`) so change them appropriately.

The callback slightly lower is for the example paramter and it can be removed since the `example_param` argument no longer exists. We will now add a variable to store the cumulative sum. Add the following line where the callback used to be.

```python
self.cumsum = [0.0]
```

Now the `work()` function must be changed. Reading through it now shows the multiplication with the example parameter. Remove this and replace it with the following:

```python
for i in np.arange(len(output_items[0])):
  self.cumsum += input_items[0][i]
  out_items[0][i] = self.cumsum

return len(output_items[0])
```

The input to the block is delivered in chunks of samples (the size of the chunk depends on a number of factors including OS and available hardware, but is generally around 8192 samples). This code block will take the input, add every input to the existing cumulative sum and put it in the output buffer. The complete code snippet should look like the following.

```python
"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    """Embedded Python Block - Cumulative Sum"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='CumSum',       # will show up in GRC
            in_sig=[np.float32], # input datatype
            out_sig=[np.float32] # output datatype
        )
        self.cumsum = [0.0]


    def work(self, input_items, output_items):
        in_arr = input_items[0]
        out_arr = output_items[0]

        for i in np.arange(len(output_items[0])):
            self.cumsum += input_items[0][i]
            output_items[0][i] = self.cumsum

        return len(output_items[0])

```

Save your changes and exit back to the flowgraph.

### Phase Mod

It is helpful to see the [Phase Mod documentation](https://wiki.gnuradio.org/index.php/Phase_Mod). This block has one parameter, *Sensitivity* and the output is 

### Noise Source

For now set the *Amplitude* to 0.

### Virtual Sink & Virtual source

These blocks can be considered as connected by an "invisible" line on the flowgraph. They can be used for more complex tasks, but here they just keep the flowgraph from being criss-crossed with lines. They are also used to simulate a "transmitter" and "receiver". In this case the *Virtual Sink* transmits the noisy baseband waveform while the *Virtual Source* receives it.

Ensure that the *Stream ID* matches between the two.

### Decimating FIR Filter

Set the decimation parameter appropriately (think back to the interpolation done in the LPF), remembering to reference the symbol and sample rate variables. The block fails to compile without a taps argument so set *Taps* to 1 (meaning there is 1 tap with a value of 1).

{% include alert.html title="Note" content="Some systems seem to throw a weird error unless the 1 is enclosed in square brackets. If you get this error try setting the taps to `[1]`."%}

### Binary Slicer

This block outputs a 0 for every negative input and a 1 for every positive output.

### Pack K Bits

Set *K* to 8. This is the packet byte size that the later *BER* block requires.

### BER

This computes the error between the two inputs. It outputs to log of the BER, so if it outputs a value of -2, the BER is $$10^{-2}=0.01$$.

Set *Test Mode* to False, which will mean the block immediately starts outputting results (as opposed to waiting for the error rate to stabilize first). While *Test Mode* is False, the other parameters don't do anything, so you can leave them as they are.

### QT GUI Number Sink

This will draw the output of the BER block on a number line. Set the maximum to 0 (since $$10^0=1$$ meaning that every bit is wrong) and the minumum to -7.

### Skip Head

To compute the BER of the system, the input and output bitstreams must be aligned. The filter causes a delay which can be measured by correlating the bitstreams, or observing them using a *QT GUI Time Sink* as shown in the two figures below.

To do this you can observe the overlapped bitstreams and try to find the offset between them. When the bitstreams are not aligned, the BER rate will be about 50% (this just means both streams are random and equally consist of 1s and 0s).

  ![un-delayed-bitstreams.png](figures/un-delayed-bitstreams.png)<br>
  __*A pattern found in the un-delayed bitstream. The blue bitstream between the blue arrows matches the red bitstream between the red arrows. BER=50%.*__

You will know you have the correct delay when your error rate drops to 0.

  ![delayed-bitstreams.png](figures/delayed-bitstreams.png)<br>
  __*Delay corrected bitstreams. BER=0%.*__

It is a finicky task to find the correct delay and not the intent of the lab. So, assuming you have correctly set your LPF parameters the *Skip Head* block should have the *Num Items* argument set to 6. This means the first six block inputs are discarded before the input is sent directly to the output.

### Setting LPF Gain

Test the system by running it. Observe the time sink connected to the end of the transmitter chain (below). Notice that the waveform amplitude is very low at the output of the filter. Find the amplitude of the pulse peaks and then change the "Gain" parameter in the *Low Pass Filter* block such that the waveform pulses peak at 1.

  ![lpf-no-gain.png](figures/lpf-no-gain.png)<br>
  __*Output of LPF before gain is applied.*__

  ![lpf-with-gain.png](figures/lpf-with-gain.png)<br>
  __*Output of LPF with the appropriate gain applied.*__

## Run the experiment

1. Run the flowgraph.
2. Record the BER at $$\sigma$$ values of `[0.7, 0.55, 0.44, 0.35, 0.28]`. You will need to kill the flowgraph each time you need to set a new value.
   - Plotting the time sink values also eats computational power. While waiting for the BER values to stabilize you may disable the *QT GUI Time Sink* blocks and any other unneeded QT GUI blocks.
3. Offset the delay (in the *Skip Head* block) by a single sample. Check the BER with no added noise.
4. Measure output powers as described below.
   - As shown in the [theory section]({{ site.baseurl }}{% link _ece450/lab2/theory.md %}), $$SNR_{MAX} = \frac{2E_b}{N_0}$$.
   - The $$SNR_{MAX}$$ is the ratio of the output signal and noise powers. To calculate the $$\frac{E_b}{N_0}$$ value for each above recorded BER value we need to find the output signal power and output noise power.
   - Build the following three blocks to measure the signal power and attach the output of the *Decimating Filter* to both inputs of the multiply block.

     ![power-measurement.png](figures/power-measurement.png)<br>
    __*Flow diagram to measure average power of a data stream.*__

   - The *Length* of the *Moving Average* block is 100000 and the *Scale* is the inverse (ensure that the inverse is a float and not an integer.)

   {% include alert.html title="Note" content="Ensure that the *Scale* parameter is a float and not an integer. GR versions < 3.8 are build on Python 2 and so 1/100000 will result in the int 0. GR versions 3.8+ are built on Python 3 and so the same argument will yield the float 0.00001. In GR versions < 3.8 this can be solved by casting the entire argument as a float by wrapping it with a `float()`." %}

   - Disable the *Binary Slicer*, *Skip Head*, both *Pack K Bits* blocks, the *BER* and it's number sink block.
   - Set the *Amplitude* of the *Noise Source* block to 0 so that the signal $$a_i$$ goes throught the LPF and decimation with no noise added before the power is measured.
   - Measure this value and record it.
   - Now measure the noise power by setting the gain of the LPF to 0. Measure and record the noise power at the output of the decimator for `sigma` values of `[0.7, 0.55, 0.44, 0.35, 0.28]`. It takes some time for these numbers to stabilize.

At this point you should have recorded 5 BER values, 5 output noise power values and 1 output signal power value.

{% include alert.html title="Deliverable question 1" class="info" content="What do your observations suggest about the relative impact on a communications system between a timing offset and noise?"%}

Review the [section deliverables](#part-2-deliverables) before moving on.
