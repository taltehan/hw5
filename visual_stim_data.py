import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


class VisualStimData:
    """
    Data and methods for the visual stimulus ePhys experiment.
    The data table itself is held in self.data, an `xarray` object.
    Inputs:
        data: xr.Dataset
    Methods:
         plot_electrode(rep_number, rat_id, elec_number) - plots the voltage of the selected electrodes for a specific
                                                           rat and repetition number.
         experimenter_bias - plots the mean, std and median voltage across different experimenters.
    """
    def __init__(self, data):
        self.data = data
        self.vars = self.data.data_vars
        self.experimenters = list(set([self.data[da].attrs['experimenter_name'] for da in self.vars]))
        self.num_rats = len(self.vars)
        self.num_repetitions = len(self.data.repetition)
        # Stimulus Index: division of the data by pre- post- and during-stimulus times:
        self.pre_stimulus = self.data.where(self.data.time < 1, drop=True)
        self.post_stimulus = self.data.where(self.data.time > 1.1, drop=True)
        self.after_stimulus = self.data.where(self.data.time >= 1, drop=True)
        self.during_stimulus = self.after_stimulus.where(self.after_stimulus.time <= 1.1, drop=True)

    def plot_electrode(self, rep_number: int, rat_id: int, elec_number: tuple=(0,)):
        """
        Plots the voltage of the electrodes in "elec_number" for the rat "rat_id" in the repetition
        "rep_number". Shows a single figure with subplots.
        """
        rat_data = self.data[rat_id].sel(repetition=[rep_number])
        fig = plt.figure(1)
        ax = fig.add_subplot(111)
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Voltage')
        ax.set_title(f'Repetition: {rep_number}, Rat ID: {rat_id}')
        for elec in elec_number:
            ax.scatter(rat_data.time.values, rat_data.isel(electrode=elec).values, label=f'elec {elec}', s=0.05)
        ax.legend()
        plt.show()

    def experimenter_bias(self):
        """ Shows the statistics of the average recording across all experimenters """
        fig = plt.figure(2)
        ax = fig.add_subplot(111)
        x = np.arange(3)
        labels = ('mean', 'std', 'median')
        width = 0
        # get the data of each experimenter and plot the mean, std and median
        for experimenter in self.experimenters:
            exp_data = self.data.filter_by_attrs(experimenter_name=experimenter)
            vals = [exp_data[da].values for da in exp_data.data_vars]
            y = [np.mean(vals), np.std(vals), np.median(vals)]
            ax.bar(x + width, y, 0.2, label=f'{experimenter}')
            width += 0.2
        plt.xticks(x, labels)
        ax.set_xticks(np.arange(3) + 0.5 / 2)
        ax.legend()
        plt.show()


def mock_stim_data() -> VisualStimData:
    """ Creates a new VisualStimData instance with mock data """
    num_of_rats = np.random.randint(10, 21)
    dims = ('electrode', 'time', 'repetition')
    coords = {'electrode': np.arange(10), 'time': np.linspace(0, 2, num=10000), 'repetition': np.arange(4)}
    rat_ids = list(range(num_of_rats))
    experimenter_name = ['Leonardo', 'Donatello', 'Michelangelo', 'Raphael']
    genders = ['F', 'M']
    rats_arrays = {}
    # for each rat in the experiment, create mock attributes and a DataArray with mock data
    for rat in rat_ids:
        attrs = {'rat_ID': rat,
                 'room_temp': np.random.randint(20, 30),
                 'room_humidity': np.random.randint(30, 70),
                 'experimenter_name': np.random.choice(experimenter_name),
                 'rat_gender': np.random.choice(genders)
                 }
        rats_arrays[rat] = xr.DataArray(np.random.random((len(coords['electrode']),
                                                          len(coords['time']),
                                                          len(coords['repetition']))),
                                        dims=dims, coords=coords, attrs=attrs
                                        )
    rats_ds = xr.Dataset(rats_arrays)
    return VisualStimData(data=rats_ds)


if __name__ == '__main__':
    stim_data = mock_stim_data()
    stim_data.plot_electrode(3, 7, (0, 1))
    stim_data.experimenter_bias()
