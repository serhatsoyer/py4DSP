## py4DSP
*DSP (Digital Signal Processing) code in Python*

### Intro
- This repo is for my personal study of some DSP (digital signal processing) conceps and to study [*scipy.signal*](https://docs.scipy.org/doc/scipy/reference/signal.html) library
- Jupyter Notebooks have some markdown cells which contain explanations in LaTeX which are sometimes rendered incorrectly by GitHub. So, it is sometimes better to study locally
- Example notebooks start with: [/examples/freq_domain/fft_intro.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/freq_domain/fft_intro.ipynb)
- Following examples are linked to the beginning cell of the former notebook
- All code and all examples are prone to all kinds of errors
- Any corrections, suggestions, improvements, etc. are welcome

### Contents
- [/examples/freq_domain/fft_intro.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/freq_domain/fft_intro.ipynb)
    - Write complex equations in markdown cells
    - FFT math
    - Simulate a sinusoid together with its time vector
    - Take the FFT
    - Plot the signal, plot the FFT, or together
    - Effect of removing the offset from a signal on the FFT
    - Relation between the signal amplitudes and the size of the FFT peaks
- [/examples/freq_domain/fft_index_freq_match.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/freq_domain/fft_index_freq_match.ipynb)
    - Effect of the size of the FFT
- [/examples/freq_domain/spectrogram.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/freq_domain/spectrogram.ipynb)
    - Generate chirp with [*signal.chirp*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.chirp.html#scipy.signal.chirp)
    - Different kinds of chirp signals: *linear*, *quadratic*, *logarithmic*, *hyperbolic*
    - Plot spectrogram together with the signal power
- [/examples/lti_filters/filter_bank.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/filter_bank.ipynb)
    - Create a filter object with [*signal.dlti*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.dlti.html#scipy.signal.dlti)
    - Design IIR filters with [*signal.iirdesign*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.iirdesign.html#scipy.signal.iirdesign)
    - Create a filter bank consisting of IIR filters
    - Draw the bode plot
    - Use the filter bank with [*signal.dlsim*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.dlsim.html#scipy.signal.dlsim) which simulates the output of a discrete-time linear system
- [/examples/lti_filters/phase_response.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/phase_response.ipynb)
    - Design FIR filter with [*signal.firwin*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html#scipy.signal.firwin)
    - Display filter equation in LaTeX
    - Plot filter coefficients
    - Plot impulse and step responses
    - Simulate superposition of sinusoids
    - Given numerator, denumerator, and the input signal, calculate the output of an LTI filter with [*signal.lfilter*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html#scipy.signal.lfilter)
    - Compare similar FIR and IIR filters in terms of phase responses
- [/examples/lti_filters/speed.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/speed.ipynb)
    - Use timers to measure execution time
    - Compare similar FIR and IIR filters in terms of speed
- [/examples/lti_filters/fir](https://github.com/serhatsoyer/py4DSP/tree/main/examples/lti_filters/fir)
    - [Design low-pass FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/lpf.ipynb)
    - [Design high-pass FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/hpf.ipynb)
    - [Design band-pass FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/band-pass.ipynb)
    - [Design band-stop FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/band-stop.ipynb)
    - [Design all-pass FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/all-pass.ipynb)
    - [Design all-stop FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/all-stop.ipynb)
- [/examples/lti_filters/fir/params](https://github.com/serhatsoyer/py4DSP/tree/main/examples/lti_filters/fir/params)
    - [Number of parameters of an FIR filter is too small](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/params/too_small_num_of_coeffs.ipynb)
    - [Number of parameters of an FIR filter is too big](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/params/too_big_num_of_coeffs.ipynb)
    - [Number of parameters of an FIR filter is even](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/params/even_or_odd_num_of_coeffs.ipynb)
    - [Pass as it is FIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/fir/params/no_filter.ipynb)
- [/examples/lti_filters/iir](https://github.com/serhatsoyer/py4DSP/tree/main/examples/lti_filters/iir)
    - [Design low-pass IIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/lpf.ipynb)
    - [Design high-pass IIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/hpf.ipynb)
    - [Design band-pass IIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/band-pass.ipynb)
    - [Design band-stop IIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/band-stop.ipynb)
- [/examples/lti_filters/iir/params](https://github.com/serhatsoyer/py4DSP/tree/main/examples/lti_filters/iir/params)
    - [Bad *pass_loss_dB*](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/params/bad_pass_loss_dB.ipynb)
    - [Good *pass_loss_dB*](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/params/good_pass_loss_dB.ipynb)
    - [Good *stop_loss_dB*](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/params/good_stop_loss_dB.ipynb)
    - [All good IIR filter](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/iir/params/all_good_iir.ipynb)
- [/examples/lti_filters/convolution.ipynb](https://github.com/serhatsoyer/py4DSP/blob/main/examples/lti_filters/convolution.ipynb)
    - Caclulate the impulse response using [*signal.dimpulse*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.dimpulse.html#scipy.signal.dimpulse)
    - Calculate the LTI filter output using the impulse response and the convolution operation with [*signal.convolve*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html#scipy.signal.convolve)
    - Compare [*signal.lfilter*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html#scipy.signal.lfilter) with [*signal.convolve*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html#scipy.signal.convolve)
- [/functions/fft.py](https://github.com/serhatsoyer/py4DSP/blob/main/functions/fft.py)
    - Functions related to *FFT* with [*numpy*](https://numpy.org) and [*matplotlib*](https://matplotlib.org)
- [/functions/lti.py](https://github.com/serhatsoyer/py4DSP/blob/main/functions/lti.py)
    - Functions related to *LTI* systems with [*numpy*](https://numpy.org), [*matplotlib*](https://matplotlib.org), and [*scipy.signal*](https://docs.scipy.org/doc/scipy/reference/signal.html)
    - Display LaTeX equations with [from IPython.display import Latex, display](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html)

### To Do List
- Study and demonstrate wavelet basics. Find a popular and stable library if any exists. Implement yourself otherwise
- Study and demonstrate wavelet scattering basics
- Linear algebra review. Study a popular and stable library

### My Other Study Repos
- [py4ML: ML code in Python](https://github.com/serhatsoyer/py4ML)
- [py4Nav: Navigation code in Python](https://github.com/serhatsoyer/py4Nav)
- [py4Me: Daily code in Python](https://github.com/serhatsoyer/py4Me)

Written by [*serhatsoyer*](https://github.com/serhatsoyer)