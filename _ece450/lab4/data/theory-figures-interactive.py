"""
Plotting interactive figures for the theory section of ECE450 Lab 3

Author: Nicholas Bruce (nsbruce@uvic.ca)
"""


import numpy as np
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

fm=1200 #Hz
fs=fm*64 #Hz
fc=fm

fm=1200 #Hz
fs=fm*64 #Hz
fc=fm

m_alpha = [-1,1,1,-1,1]
m_alpha = np.repeat(m_alpha, fs//fm)
t_arr = np.arange(0, len(m_alpha)/fs, 1/fs)

m_alphas = [m_alpha]


fig = make_subplots(
    rows=1, cols=1,
    specs=[[{'type': 'scatter3d'}]],
    subplot_titles=("BPSK helix of square pulse shaped bits")
)

for i in np.arange(len(m_alphas)):
    m_alpha=m_alphas[i]

    s_tilda = m_alpha+1j*m_alpha
    s_t_complex = s_tilda*np.exp(1j*(2*np.pi*fc*t_arr-np.pi/4))

    fig.add_trace(
        go.Scatter3d(
            x=t_arr,
            y=np.real(s_t_complex),
            z=np.imag(s_t_complex),
            mode='lines',
            line=dict(width=6, color='midnightblue')
        ),
        row=1, col=i+1
    )
    fig.add_trace(
        go.Scatter3d(
            x=t_arr,
            y=[1.25]*len(t_arr),
            z=np.imag(s_t_complex),
            mode='lines',
            line=dict(width=2.5, color='magenta')
        ),
        row=1, col=i+1
    )
    fig.add_trace(
        go.Scatter3d(
            x=t_arr,
            y=[1.25]*len(t_arr),
            z=m_alpha,
            mode='lines',
            line=dict(width=2.5, color='blue')
        ),
        row=1, col=i+1
    )
    fig.add_trace(
        go.Scatter3d(
            x=t_arr,
            y=np.real(s_t_complex),
            z=[-1.25]*len(t_arr),
            mode='lines',
            line=dict(width=2.5, color='green')
        ),
        row=1, col=i+1
    )
    fig.add_trace(
        go.Scatter3d(
            x=t_arr,
            y=m_alpha,
            z=[-1.25]*len(t_arr),
            mode='lines',
            line=dict(width=2.5, color='blue')
        ),
        row=1, col=i+1
    )

# Configure the layout.

scene=dict(
    xaxis_title="Time",
    yaxis_title='Real',
    zaxis_title='Imag.',
    camera=dict(
        eye=dict(x=2, y=-2, z=2), #the default values are 1.25, 1.25, 1.25
        projection=dict(type='orthographic')
    ),
    aspectmode='manual',
    aspectratio=dict(x=2, y=1, z=1),
    xaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
        showbackground=False,
    ),
    yaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=True,
        zerolinewidth=5,
        zerolinecolor='black',
        showbackground=False,
    ),
    zaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=True,
        zerolinewidth=5,
        zerolinecolor='black',
        showbackground=False,
    )
)

fig.update_layout(
    go.Layout(
        scene1=scene,
        scene2=scene,
        showlegend=False
    ),
    )


# Render the plot.
plotly.io.write_html(fig=fig, file="test.html", include_plotlyjs='cdn')
fig.show()




