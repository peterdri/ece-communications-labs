### Prerecorded FSK signals

[This data file](./data/fsk.dat), was recorded at a sample rate of 48 kHz containing complex samples of two FSK signals. One signal is at an offset of -10 kHz while the other is at +15 kHz. One signal has two tones while the other uses eight tones.

- Use a complex *File Source* block to read the file and your FM discriminator from the previous section to demodulate the signals one at a time.

- The demodulated two-tone signal should look similar to the one below.

    ![fsk2level.png](./figures/fsk2level.png)<br>
    __*2 level FSK*__

- The demodulated eight-tone signal should look similar to the one below.

    ![fsk8level.png](./figures/fsk8level.png)<br>
    __*8 level FSK*__

---

#### Deliverable Question 2

For each signal, determine:

1. What is the signal offset? (What is the spacing between the center frequency and the tones)
2. What is the symbol rate?

---
