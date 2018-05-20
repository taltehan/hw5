import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


class VisualStimData:
    """
    Data and methods for the visual stimulus ePhys experiment.
    The data table itself is held in self.data, an `xarray` object.
    Inputs:
        data: xr.DataArray or xr.Dataset
        ...
    Methods:
         ...
    """
    def __init__(self, data, ):
        self.data = data
        # experimenters, how many rats, some means
        # ToDo: pre/during/post

    def plot_electrode(self, rep_number: int, rat_id: int, elec_number: tuple=(0,)):
        """
        Plots the voltage of the electrodes in "elec_number" for the rat "rat_id" in the repetition
        "rep_number". Shows a single figure with subplots.
        """
        rat_data = self.data[rat_id].sel(repetition=[rep_number])
        fig = plt.figure()
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



def mock_stim_data() -> VisualStimData:
    """ Creates a new VisualStimData instance with mock data """
    num_of_rats = np.random.randint(10,21)
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
    # stim_data.plot_electrode(3, 7, (0, 1))
    # stim_data.experimenter_bias()
    # ToDo: remove comments above
    # X = mock_stim_data().data[2].sel(repetition=[0])
    # print(X.sel(electrode=[0]).values.size)
    # print(X.time.values)
    # print(X.coords['time'])
    # plt.scatter(X.coords['time'].values, X.isel(electrode=0).values, s=0.05)
    # plt.show()
    # print(stim_data.data)
    # filtered = stim_data.data.filter_by_attrs(experimenter_name='Donatello')
    # print(type(stim_data))
    # filtered = stim_data.data.where(stim_data.data.time<1, drop=True)
    # print(stim_data.data.data_vars[0])
    print(stim_data.data.data_vars.items())
