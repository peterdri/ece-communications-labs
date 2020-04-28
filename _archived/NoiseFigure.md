### Noise figure

- Review [link budget notes](data/350link4.pdf) with particular attention to **equation (14)**.

- When you tune the receiver to a frequency where there is no station broadcasting, there is still a residual noise floor visible on the spectrum display. The noise level can be estimated by looking at the display and observing the level in dBm (dB relative to one milliwatt). This is thermal noise that is calculated from the formula
 *P~noise~ = kT(S/N)WF*
 where
  - k is Boltzmann's constant
  - T is the noise temperature, typically 290 degrees Kelvin
  - W is the bandwidth in Hz and
  - F is a dimensionless noise figure representing imperfect amplifiers.

- By substituting values for *k* and *T* and taking logs of both sides of this formula, we can write in dB:
 P~noise~ = -228.6 + T + (S/N) + W + F.

- Estimate the noise figure of the receiver based on the noise level in dBm on the computer spectrum display and the receiver bandwidth of 250 KHz.
  - All the variables in the noise figure equation except F are known or can be measured, so the equation can be solved for F.
  - The specified value for the URSP with WBX board is 5.5 dB.