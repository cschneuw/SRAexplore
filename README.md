# SRAexplore

This package aims at fetching with some filtering criteria and analyzing sequencing metadata from the Sequence Read Archive (SRA) database and explore the available studies. It will generate some statistics of interest and vizualisations.

## Description

This package makes use of the pysradb package to fetch study metadata from SRA. It allows the exploration of a selection of studies and experiments by imputing a simple query with keywords on studies of interest. 

It uses streamlit to produce a GUI in html that allows the user add some filters and launch a new query. Plots were generated with plotly and are all interactive. Meaning that we can unselect some studies for example, the data can be viausalized by just hovering with the mouse on the data points and by double clicking on a specific study or data point, it will be automatically zoomed in. Fetched raw data can be visualized by just clicking on a select box at the end of the html page. 

## Installation for end-user

1) Clone the repository

```bash
git clone https://github.com/cschneuw/SRAexplore.git
```

2) Create a conda environment with python 3.10 and activate it.

```bash
conda create -n sra_explore python=3.10
conda activate sra_explore
```

3) Install the package

```bash
pip install .
```

## Installation for developers

1) Clone the repository

```bash
git clone 
```

2) Create a conda environment with python 3.10 and activate it.

```bash
conda create -n sra_explore python=3.10
conda activate sra_explore
```

3) Install the package

```bash
pip install poetry
poetry install
```

4) Test if the package was successfuly installed

```bash
poetry run pytest
```

## Use

Go in the main directory of this package and run in a terminal : 

```bash
streamlit run SRAexplore/app.py
```

To close just type <kbd>Ctrl</kbd> + <kbd>c</kbd>.


## Improvements

The metadata downloadable from SRA in its detailed version is complex and a lot more values can help us guide users in their choices of study. The number of runs is variable and we focused on values available for the full sets. We should have re-worked the dataframes to keep the last or make run-wise plots. This means that some data will be missing from the dataframes for example the date since the value used here was taken from the first run. 

An extensive error handling would be great to implement, Streamlit has it's own syntax to handle errors and more time spent on this would have been of great use to be able to redirect the user's entries if these would be faulty or if metadata would be missing. Instead we have to rely for now on the built-in error handlings of our tools, which might not be sufficiently explicit for novices in Python. 

Streamlit provides a nice and quick way to create GUIs for users, however we only used half of the functionalities and the aspect of the figures could be improved. Boxplots in particular are particularly tricky to set to the right size when too much data is inputed. The data displayed in the hover are defined by default, it would have been of use to add more labels and values displayed. The user then would have a better idea of the subjects of the study and goals.

With more time and more diving into the data and studies available, it would have been nice to list and verify all available entries to SRA, to make the selection of studies easier for the user by making multiple choices selection. Also an additonal scraping of the inputs to detect words of interest. This would have been implemented as an additonal function or as unitary tests. Since currently, we only have a simple pass test that just allowed us to know if the installation was correct. 

Pysradb allows some additional filtering on the data, that we left out to still keep a rather simple interface for the user. However in future verisons, these additonal filters could be explored and hidden in an optional widget. 