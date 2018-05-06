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
        pass

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
    pass


if __name__ == '__main__':
    stim_data = mock_stim_data()
    stim_data.plot_electrode()  # add necessary vars
    stim_data.experimenter_bias()
