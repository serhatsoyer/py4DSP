# Written by serhatsoyer

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from IPython.display import Latex, display # Only necessary for fn. equation


def bode(numerator_coeffs, denum_coeffs=[1]):
    """
    Draws Bode plot of an LTI filter
    """
    freqs, responses = signal.freqz(numerator_coeffs, denum_coeffs)

    plt.style.use('Solarize_Light2')
    default_size = plt.rcParams.get('figure.figsize')
    fig, axes = plt.subplots(2, 1, sharex=True,
                             figsize=(default_size[0], 1.2*default_size[1]),
                             gridspec_kw={'height_ratios': [2, 1]})
    fig.subplots_adjust(hspace=0)

    assumed_zero = 1e-8
    assumed_zero_db = 20 * np.log10(np.abs(assumed_zero))
    magnitude_response_db = np.zeros_like(responses)
    for idx, response in enumerate(responses):
        response = np.abs(response)
        if response < assumed_zero:
            magnitude_response_db[idx] = assumed_zero_db
        elif np.abs(response - 1) > assumed_zero:
            magnitude_response_db[idx] = 20 * np.log10(response)
    
    phase_response_rad = np.unwrap(np.angle(responses))

    axes[0].set_title('Digital LTI Filter Frequency Response')

    axes[0].plot(freqs, np.real(magnitude_response_db), lw=2)
    axes[0].set_ylabel('Magnitude [dB]')
    axes[0].grid(True)
    if assumed_zero_db in magnitude_response_db:
        axes[0].legend([f'Assumed Zero: {assumed_zero_db} dB'])

    axes[0].spines['bottom'].set_color(fig.get_facecolor())
    axes[0].spines['bottom'].set_linewidth(6)
    axes[0].spines['bottom'].set_capstyle('round')

    axes[1].plot(freqs, np.real(phase_response_rad), lw=2)
    axes[1].set_ylabel('Phase (rad)')
    axes[1].grid(True)

    axes[1].set_xlabel('Frequency')
    plt.xlim(0, np.pi)
    plt.xticks(np.linspace(0, np.pi, num=5),
               labels=['$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])

    plt.show()


def plot_filter_coefficients(numerator_coeffs, denum_coeffs=[1]):
    """
    Shows the numerator and denumerator coefficients of an LTI filter on a figure
    """
    plt.style.use('Solarize_Light2')
    default_size = plt.rcParams.get('figure.figsize')
    fig, axes = plt.subplots(2, 1, figsize=(default_size[0], default_size[1]))
    fig.subplots_adjust(hspace=0)
    axes[0].set_title('Filter Coefficients')
    axes[0].stem(numerator_coeffs)
    axes[0].set_xticks([])
    axes[0].spines['bottom'].set_color(fig.get_facecolor())
    axes[0].spines['bottom'].set_linewidth(6)
    axes[0].spines['bottom'].set_capstyle('round')
    axes[0].legend([f'Numerator Coeffs. $b[n]$\nNum. of Coeffs: {len(numerator_coeffs)}'])
    axes[1].stem(denum_coeffs)
    axes[1].set_xticks([])
    axes[1].legend([f'Denum. Coeffs. $a[n]$\nNum. of Coeffs: {len(denum_coeffs)}'])
    plt.show()


def correct_denum_coeffs(numerator_coeffs, denum_coeffs):
    """
    This function is necessary to calculate the following line without errors:
    signal.dlti(numerator_coeffs, denum_coeffs)
    """
    if len(numerator_coeffs) > len(denum_coeffs):
        denum_coeffs = np.pad(denum_coeffs, (0, len(numerator_coeffs)-len(denum_coeffs)))
    
    return denum_coeffs


def plot_impulse_response_to_axis(axis, numerator_coeffs, denum_coeffs):
    """
    Plots the impulse response of an LTI filter on an axis
    """
    denum_coeffs = correct_denum_coeffs(numerator_coeffs, denum_coeffs)
    indices, filter_out = signal.dimpulse(signal.dlti(numerator_coeffs, denum_coeffs))
    axis.stem(indices, np.squeeze(filter_out))
    axis.grid(True)
    axis.set_xlabel('Sample Index')
    axis.set_ylabel('Signal Unit')
    axis.legend([r'Input $x[n]=\delta[n]$'])


def plot_step_response_to_axis(axis, numerator_coeffs, denum_coeffs):
    """
    Plots the step response of an LTI filter on an axis
    """
    denum_coeffs = correct_denum_coeffs(numerator_coeffs, denum_coeffs)
    indices, filter_out = signal.dstep(signal.dlti(numerator_coeffs, denum_coeffs))
    axis.stem(indices, np.squeeze(filter_out))
    axis.grid(True)
    axis.set_xlabel('Sample Index')
    axis.set_ylabel('Signal Unit')
    axis.legend([r'Input $x[n]=u[n]$'])


def plot_impulse_response(numerator_coeffs, denum_coeffs=[1]):
    """
    Plots the impulse response of an LTI filter on a new figure
    """
    plt.style.use('Solarize_Light2')
    default_size = plt.rcParams.get('figure.figsize')
    fig, axis = plt.subplots(1, 1, figsize=(default_size[0], default_size[1]))
    axis.set_title('Impulse Response $y[n]$')
    plot_impulse_response_to_axis(axis, numerator_coeffs, denum_coeffs)
    plt.show()


def plot_step_response(numerator_coeffs, denum_coeffs=[1]):
    """
    Plots the step response of an LTI filter on a new figure
    """
    plt.style.use('Solarize_Light2')
    default_size = plt.rcParams.get('figure.figsize')
    fig, axis = plt.subplots(1, 1, figsize=(default_size[0], default_size[1]))
    axis.set_title('Step Response $y[n]$')
    plot_step_response_to_axis(axis, numerator_coeffs, denum_coeffs)
    plt.show()


def plot_impulse_and_step_responses(numerator_coeffs, denum_coeffs=[1]):
    """
    Plots the impulse and step responses of an LTI filter on a new figure as subplots
    """
    plt.style.use('Solarize_Light2')
    default_size = plt.rcParams.get('figure.figsize')
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(default_size[0], 1.5*default_size[1]))
    fig.subplots_adjust(hspace=0)
    axes[0].set_title('Impulse and Step Responses')
    axes[0].spines['bottom'].set_color(fig.get_facecolor())
    axes[0].spines['bottom'].set_linewidth(6)
    axes[0].spines['bottom'].set_capstyle('round')
    plot_impulse_response_to_axis(axes[0], numerator_coeffs, denum_coeffs)
    plot_step_response_to_axis(axes[1], numerator_coeffs, denum_coeffs)
    plt.show()


def format(letter, idx, coeff, first=False):
    abs_coeff = abs(coeff)
    if abs_coeff > 1e-1: num = f'{coeff:.2f}'
    elif abs_coeff > 1e-2: num = f'{coeff:.3f}'
    elif abs_coeff > 1e-3: num = f'{coeff:.4f}'
    elif abs_coeff > 1e-4: num = f'{coeff:.5f}'
    else: num = f'{coeff:.6f}'
    if num == '1.00': num = '+'
    elif num == '-1.00': num = '-'
    elif num[0] != '-': num = '+' + num
    if first and (num[0] == '+'): num = num[1:]
    return num + f'{letter}_' + (f'{{n}}' if (idx == 0) else f'{{n-{idx}}}')


def equation(numerator_coeffs, denum_coeffs=[1]):
    """
    Displays LTI filter equation
    """
    denum_coeffs = correct_denum_coeffs(numerator_coeffs, denum_coeffs)
    den_first_found, den_second_found, den_third_found = False, False, False
    for idx, coeff in enumerate(denum_coeffs):
        if coeff != 0: 
            if not den_first_found: den_first_found = True; den_first_idx = idx; den_first_coeff = coeff
            elif not den_second_found: den_second_found = True; den_second_idx = idx; den_second_coeff = coeff
            else: den_third_found = True; den_third_idx = idx; den_third_coeff = coeff

    num_first_found, num_second_found = False, False
    for idx, coeff in enumerate(numerator_coeffs):
        if coeff != 0: 
            if not num_first_found: num_first_found = True; num_first_idx = idx; num_first_coeff = coeff
            else: num_second_found = True; num_second_idx = idx; num_second_coeff = coeff
    
    msg = '$'
    if den_first_found: msg += (format('y', den_first_idx, den_first_coeff, True) + '=')
    right = True
    if den_second_found: msg += format('y', den_second_idx, -den_second_coeff, right); right = False
    if den_third_found:
        if den_third_idx - den_second_idx > 1: msg += '+...'
        msg += format('y', den_third_idx, -den_third_coeff)
    
    if num_first_found: msg += format('x', num_first_idx, num_first_coeff, right); right = False
    if num_second_found:
        if num_second_idx - num_first_idx > 1: msg += '+...'
        msg += format('x', num_second_idx, num_second_coeff)
    
    if right: msg += '0'
    msg += '$'
    display(Latex(msg))