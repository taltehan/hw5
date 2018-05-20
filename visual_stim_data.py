import numpy as np
import xarray as xr


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
        pass

    def experimenter_bias(self):
        """ Shows the statistics of the average recording across all experimenters """
        pass


def mock_stim_data() -> VisualStimData:
    """ Creates a new VisualStimData instance with mock data """
    num_of_rats = np.random.randint(10,21)
    dims = ('electrode', 'time', 'repetition')
    coords = {'electrode': np.arange(10), 'time': np.linspace(0, 2, num=10000), 'repetition': np.arange(4)}
    rat_ids = list(range(num_of_rats))
    experimenter_name = ['Leonardo', 'Donatello', 'Michelangelo', 'Raphael']
    genders = ['F', 'M']
    rats_arrays = {}
    for rat in rat_ids:
        attrs = {'Rat ID': rat,
                 'Room temp': np.random.randint(20, 30),
                 'Room humidity': np.random.randint(30, 70),
                 'Experimenter name': np.random.choice(experimenter_name),
                 'Rat gender': np.random.choice(genders)
                 }
        rats_arrays[rat] = xr.DataArray(np.random.random((len(coords['electrode']),
                                                          len(coords['time']),
                                                          len(coords['repetition']))),
                                        dims=dims, coords=coords, attrs=attrs
                                        )
    rats_ds = VisualStimData(data=rats_arrays)
    return rats_ds


if __name__ == '__main__':
    # stim_data = mock_stim_data()
    # stim_data.plot_electrode()  # add necessary vars
    # stim_data.experimenter_bias()
    # ToDo: remove comments above
    print(mock_stim_data().data)
