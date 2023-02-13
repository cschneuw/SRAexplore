from utils import human_readable_size
import numpy as np


def data_characteristics(data, query):
    characteristics_str = [
        f"Query : {query}  \n"
        f"Entries : {data.shape[0]}  \n"
        f"Organisms : {'/'.join(data['sample_scientific_name'].unique().tolist())}  \n"
        f"Library strategy : {'/'.join(data['experiment_library_strategy'].unique().tolist())}  \n"
        f"Library source : {'/'.join(data['experiment_library_source'].unique().tolist())}  \n"
        f"Library selection : {'/'.join(data['experiment_library_selection'].unique().tolist())}  \n"
        f"Instrument model : {'/'.join(data['experiment_instrument_model'].unique().tolist())}  \n"
        f"Platform : {'/'.join(data['experiment_platform'].unique().tolist())}  \n"
        f"Platform : {'/'.join(data['library_layout'].unique().tolist())}  \n"
    ]
    return characteristics_str


def simple_statistics(data):

    mean_bases = np.asarray(data["run_set_bases"], dtype=float).mean()
    mean_bytes = np.asarray(data["run_set_bytes"], dtype=float).mean()
    mean_spots = np.asarray(data["run_set_spots"], dtype=float).mean()

    statistics_str = [
        f"Number of unique studies : {data['study_accession'].unique().size}  \n"
        f"Number of unique experiments : {data['experiment_accession'].unique().size}  \n"
        f"Number of unique samples : {data['sample_accession'].unique().size}  \n"
        f"Maximal number of runs per entry : {data['run_set_runs'].max()}  \n"
        f"Mean bases : {human_readable_size(mean_bases)}  \n"
        f"Mean bytes : {human_readable_size(mean_bytes)}  \n"
        f"Mean spots : {human_readable_size(mean_spots)}  \n"
    ]

    return statistics_str
