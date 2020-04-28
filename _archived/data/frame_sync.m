% MATLAB script to generate the sync word locations.

% Read in the waveforms
[signal, fs] = wavread('FLEX_bits.wav');
sync         = wavread('FLEX_sync.wav');

% Correlate the waveforms
correlation = xcorr(signal, sync);

% Trim the correlation (sync gets zero padded)
correlation = correlation(length(signal)-length(sync)+1:end-length(sync)+1);

% Find the peaks
[~, loc] = findpeaks(correlation, 'MINPEAKHEIGHT', 300);

% Convert back to times. Sync word is 960 samples long, subtracting this
% length gives the start time of the sync word A6C6 AAAA
(loc-length(sync)) / fs