"""
Plotting figures for the theory section of ECE450 Lab 4

Author: Nicholas Bruce (nsbruce@uvic.ca)
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


fm=1200 #Hz
fs=fm*64 #Hz
fc=fm

m_alpha = [-1,1,1,-1,1]
m_alpha = np.repeat(m_alpha, fs//fm)
t_arr = np.arange(0, len(m_alpha)/fs, 1/fs)

s_tilda = m_alpha+1j*m_alpha
s_t_complex = s_tilda*np.exp(1j*(2*np.pi*fc*t_arr-np.pi/4))


## BPSK waveform
figsize=(10,8)
fig, ax = plt.subplots(3,1, figsize=figsize)

for ai in ax:
    ai.axhline(0, color='k')
    ai.axvline(0, color='k')
    ai.spines['top'].set_visible(False)
    ai.spines['bottom'].set_visible(False)
    ai.spines['right'].set_visible(False)
    ai.spines['left'].set_visible(False)
    ai.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ai.tick_params(axis='y', which='both', left=False, labelleft=False)

    ai.set_xlabel('Time')
    ai.set_ylabel('Amplitude')

# Message
ax[0].set_title(r'$m(\alpha)$')
ax[0].plot(t_arr, m_alpha, linewidth=2.5, color='b')

# Baseband
ax[1].set_title(r'$\tilde{s}(t)$')
ax[1].plot(t_arr, np.imag(s_tilda), label='Q', linewidth=2.5, color='m')
ax[1].plot(t_arr, np.real(s_tilda), label='I', linewidth=2.5, color='g')
ax[1].legend()

# Passband
ax[2].set_title(r'$s(t)$')
ax[2].plot(t_arr, np.imag(s_t_complex), label='Q', linewidth=2.5, color='m')
ax[2].plot(t_arr, np.real(s_t_complex), label='I', linewidth=2.5, color='g')
ax[2].legend()

plt.tight_layout()
plt.show()


## BPSK Taps

figsize=(5,3)
fig, ax = plt.subplots(1,2, figsize=figsize)

for ai in ax:
    ai.axhline(0, color='k')
    ai.axvline(0, color='k')
    ai.spines['top'].set_visible(False)
    ai.spines['bottom'].set_visible(False)
    ai.spines['right'].set_visible(False)
    ai.spines['left'].set_visible(False)
    ai.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ai.tick_params(axis='y', which='both', left=False, labelleft=False)

    ai.set_xlabel('Time')
    ai.set_ylabel('Amplitude')

m_alpha = [-1]
m_alpha = np.repeat(m_alpha, fs//fm)
t_arr = np.arange(0, len(m_alpha)/fs, 1/fs)

s_tilda = m_alpha+1j*m_alpha
s_t_complex = s_tilda*np.exp(1j*(2*np.pi*fc*t_arr-np.pi/4))

ax[0].plot(t_arr, np.imag(s_t_complex), label='Q', linewidth=2.5, color='m')
ax[0].plot(t_arr, np.real(s_t_complex), label='I', linewidth=2.5, color='g')

m_alpha = [1]
m_alpha = np.repeat(m_alpha, fs//fm)
t_arr = np.arange(0, len(m_alpha)/fs, 1/fs)
s_tilda = m_alpha+1j*m_alpha
s_t_complex = s_tilda*np.exp(1j*(2*np.pi*fc*t_arr-np.pi/4))

ax[1].plot(t_arr, np.imag(s_t_complex), label='Q', linewidth=2.5, color='m')
ax[1].plot(t_arr, np.real(s_t_complex), label='I', linewidth=2.5, color='g')

plt.tight_layout()
plt.show()


## DPSK Taps

figsize=(10,3)
fig, ax = plt.subplots(1,2, figsize=figsize)

for ai in ax:
    ai.axhline(0, color='k')
    ai.axvline(0, color='k')
    ai.spines['top'].set_visible(False)
    ai.spines['bottom'].set_visible(False)
    ai.spines['right'].set_visible(False)
    ai.spines['left'].set_visible(False)
    ai.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ai.tick_params(axis='y', which='both', left=False, labelleft=False)

    ai.set_xlabel('Time')
    ai.set_ylabel('Amplitude')

m_alpha = [1, 1]
m_alpha = np.repeat(m_alpha, fs//fm)
t_arr = np.arange(0, len(m_alpha)/fs, 1/fs)

s_tilda = m_alpha+1j*m_alpha
s_t_complex = s_tilda*np.exp(1j*(2*np.pi*fc*t_arr-np.pi/4))

ax[0].plot(t_arr, np.imag(s_t_complex), label='Q', linewidth=2.5, color='m')
ax[0].plot(t_arr, np.real(s_t_complex), label='I', linewidth=2.5, color='g')

m_alpha = [1, -1]
m_alpha = np.repeat(m_alpha, fs//fm)
t_arr = np.arange(0, len(m_alpha)/fs, 1/fs)
s_tilda = m_alpha+1j*m_alpha
s_t_complex = s_tilda*np.exp(1j*(2*np.pi*fc*t_arr-np.pi/4))

ax[1].plot(t_arr, np.imag(s_t_complex), label='Q', linewidth=2.5, color='m')
ax[1].plot(t_arr, np.real(s_t_complex), label='I', linewidth=2.5, color='g')

plt.tight_layout()
plt.show()


## THEORY BER CURVES

theory_eb_n0_db = np.arange(0,11,1)
theory_eb_n0_lin = 10**(theory_eb_n0_db/10)


# Coherent BPSK theory
theory_c_psk = norm.sf(np.sqrt(2*theory_eb_n0_lin))
print("Coherent BPSK: {}".format(np.log10(theory_c_psk)[::2]))

# Differentially coherent DPSK theory
theory_c_dpsk = 0.5 * np.exp(-theory_eb_n0_lin)
print("Coherent DPSK: {}".format(np.log10(theory_c_dpsk)[::2]))

# Noncoherent DPSK theory
theory_nc_dpsk = 0.5 * np.exp(-0.5*theory_eb_n0_lin)
print("Noncoherent DPSK: {}".format(np.log10(theory_nc_dpsk)[::2]))

fig, ax = plt.subplots()
ax.plot(theory_eb_n0_db, theory_c_psk, label="Coherent BPSK")
ax.plot(theory_eb_n0_db, theory_nc_dpsk, label='Noncoherent DPSK')
ax.plot(theory_eb_n0_db, theory_c_dpsk, label='Coherent DPSK')

ax.set_yscale('log')
ax.set_xlabel('Eb/N0 (dB)')
ax.set_ylabel(('BER'))
plt.legend()
plt.tight_layout()

plt.show()
