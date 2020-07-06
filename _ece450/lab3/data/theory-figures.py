"""
Plotting figures for the theory section of ECE450 Lab 3

Author: Nicholas Bruce (nsbruce@uvic.ca)
"""


import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


fm=1200 #Hz
fs=fm*64 #Hz
fdev=fm/2 #Hz
fc=1800

m_alpha1 = [1,-1,1,-1,1]
m_alpha1 = np.repeat(m_alpha1, fs//fm)
m_alpha2 = [-1,1,1,-1,1]
m_alpha2 = np.repeat(m_alpha2, fs//fm)
t_arr = np.arange(0, len(m_alpha2)/fs, 1/fs)

m_alphas = [m_alpha1, m_alpha2]

figsize=(10,5)

for m_alpha in m_alphas:

    # Integral of message
    m_alpha_int = np.cumsum(m_alpha)
    # Complex baseband
    s_tilda=np.exp(2j*np.pi*fdev/fs*m_alpha_int)
    # Real passband
    s_t = np.exp(2j*np.pi*fc*t_arr)*s_tilda

    # Message
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=figsize)
    ax1.set_title(r'$m(\alpha)$')
    ax1.axhline(0, color='k')
    ax1.axvline(0, color='k')

    ax1.plot(t_arr, m_alpha, color='b')

    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax1.tick_params(axis='y', which='both', left=False, labelleft=False)

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')

    # Integral of message


    ax2.set_title(r'$\int_0^t m(\alpha) d\alpha$')
    ax2.axhline(0, color='k')
    ax2.axvline(0, color='k')

    ax2.plot(t_arr, m_alpha_int, color='r')

    ax2.spines['top'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax2.tick_params(axis='y', which='both', left=False, labelleft=False)

    ax2.set_xlabel('Time')
    ax2.set_ylabel('Amplitude')

    plt.draw()
    # plt.show()

    # Complex baseband

    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(r'$\tilde{s}(t)$')
    ax.axhline(0, color='k')
    ax.axvline(0, color='k')

    ax.plot(t_arr, m_alpha, label=r"$m(\alpha)$", linewidth=1, color='b')
    ax.plot(t_arr, np.real(s_tilda), label="I", linewidth=2.5, color='g')
    ax.plot(t_arr, np.imag(s_tilda), label="Q", linewidth=2.5, color='m')


    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax.tick_params(axis='y', which='both', left=False, labelleft=False)

    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    plt.legend()

    plt.draw()
    # plt.show()

    # Real passband

    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(r'$\mathbb{Re}\left\{ s(t) \right\}$')
    ax.axhline(0, color='k')
    ax.axvline(0, color='k')

    ax.plot(t_arr, m_alpha, label=r"$m(\alpha)$", linewidth=1, color='b')
    ax.plot(t_arr, np.real(s_t), label=r'$\mathbb{R}\left\{ s(t) \right\}$', linewidth=2.5, color='darkorange')
    # ax.plot(t_arr, np.imag(s_t), label="Q", linewidth=2.5)


    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax.tick_params(axis='y', which='both', left=False, labelleft=False)

    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    plt.legend()

    plt.draw()


plt.show()
