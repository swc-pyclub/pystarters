import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

spikes = np.load('./calcium_imaging_data_pystarters.npy')


def detect_events(trace, plot_shift=0.0, threshold=0.15, plot=True):
    """
    detect and plot events in a time series

    :param np.array trace: an unfiltered raw calcium imaging time series
    :param np.float plot_shift: affects the spacing between multiple plots
    :param threshold: if the time series crosses this value then an event is marked
    :param bool plot:
    :return:
    """
    filtered_trace = gaussian_filter(trace, 3)
    above_threshold = filtered_trace > threshold
    transitions = np.diff(above_threshold) > 0
    putative_events = np.where(transitions)[0]

    a=2

    if trace[0] > threshold:
        putative_events = putative_events[1:]
    if trace[-1] > threshold:
        putative_events = putative_events[:-1]

    event_starts = putative_events[::2]
    event_ends = putative_events[1::2]

    print(event_starts[1])

    peak_locations = []
    summed_fluorescence = []

    for s, e in zip(event_starts, event_ends):
        peak_locations.append(np.argmax(trace[s:e])+s)
        summed_fluorescence.append(sum(trace[s:e]))

    if plot == True:
        plt.plot(trace + plot_shift)
        plt.plot(filtered_trace + plot_shift)
        plt.vlines(putative_events, plot_shift, plot_shift+0.5, color='k', linewidth=2, alpha=0.5)  # mark the starts and ends with vertical lines
        plt.scatter(peak_locations, trace[peak_locations]+plot_shift, color='r')
        plt.show()
    return event_starts, event_ends, peak_locations, summed_fluorescence


event_starts, event_ends, peak_locations, summed_fluorescence = detect_events(spikes[:, 7], 0, plot=True)
plt.close('all')
plt.figure(figsize=(20, 4))

# this should break use the debugger to troubleshoot why it doesnt work
for i, trace in enumerate(spikes[:, 0:20].T):
    event_starts, event_ends, peak_locations, summed_fluorescence=detect_events(trace, plot_shift=i*1.1)
