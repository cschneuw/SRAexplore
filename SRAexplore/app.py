import streamlit as st
from fetch import fetch
import datetime
from utils import convert_date

from plots import (
    plot_boxplots_numerical,
    plot_histograms_categorical,
    plot_study_actgn_content,
    plot_strip_numerical,
)
from data_simple_stats import data_characteristics, simple_statistics

study_categorical = {
    "study": "study_accession",
    "run publication date": "run_1_published",
    "species": "sample_scientific_name",
    "strategy": "experiment_library_strategy",
    "source": "experiment_library_source",
    "selection": "experiment_library_selection",
    "platform": "experiment_platform",
    "instrument": "experiment_instrument_model",
    "layout": "library_layout",
}

study_numerical = {
    "set bases": "run_set_bases",
    "set bytes": "run_set_bytes",
    "set runs": "run_set_runs",
    "set spots": "run_set_spots",
}

## INTRODUCTION ##
st.set_page_config(layout="wide")
st.title("SRA database explorer")
st.markdown(
    "Welcome to the SRA study explorer! Choose some filters to apply and fetch the metadata:"
)
# Prepare the columns to input the access to the data
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
# Maybe add somethign to download directly the data.
query = col1.text_input("Query ", "Melanoma")
return_max = col2.text_input("Maximum number of entries ", 100)
organism = col3.text_input("Organism ", "")
mbases = col4.text_input("Minimum number of bases ", "")
source = col5.text_input("Sequencing source (eg. TRANSCRIPTOMIC, GENOMIC)  ", "")
strategy = col6.text_input("Sequencing strategy (eg. RNA-seq, miRNA-seq)  ", "")
selection = col7.text_input("Sequencing selection (eg. RNA-seq, miRNA-seq)  ", "")
layout = col8.text_input("Library layout (paired or single) ", "")
start_date = col9.date_input(
    "Start date interval ",
    datetime.date(2018, 1, 1),
)
end_date = col10.date_input(
    "End date interval ",
    datetime.date.today(),
)
data_load_state = st.text("Loading data...")
data = fetch(
    query,
    return_max,
    organism,
    layout,
    mbases,
    selection,
    source,
    strategy,
    publication_date=convert_date(start_date, end_date),
)
data_load_state.text("Done! (using st.cache)")
st.markdown("The metadata loaded has the following characteristics: ")
st.write(data_characteristics(data, query)[0])
st.markdown(f"Statistics :")
st.write(simple_statistics(data)[0])

## OVERVIEW OF SRA STUDIES METADATA ###

st.header("Overview of all the studies")
st.subheader("Histogram of SRA metadata categories")
row1_1, row1_2 = st.columns(2)
with row1_1:
    plot_category = st.selectbox(
        "Select study categories",
        study_categorical,
    )
st.plotly_chart(
    plot_histograms_categorical(
        data,
        study_categorical[plot_category],
        plot_category,
    ),
    use_container_width=True,
)

st.subheader("Boxplots of SRA metadata quantities")
row2_1, row2_2 = st.columns(2)
with row2_1:
    plot_quantity = st.selectbox(
        "Select study quantities",
        study_numerical,
    )
with row2_2:
    plot_category = st.selectbox(
        "Select study quantities",
        study_categorical,
    )

tab1, tab2 = st.tabs(["Boxplot", "Strip plot"])
with tab1:
    st.plotly_chart(
        plot_boxplots_numerical(
            data,
            study_categorical[plot_category],
            study_numerical[plot_quantity],
            plot_quantity,
        ),
        use_container_width=True,
    )
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(
        plot_strip_numerical(
            data,
            study_categorical[plot_category],
            study_numerical[plot_quantity],
            plot_quantity,
        ),
        use_container_width=True,
    )

## FOCUS ON EXPERIMENTS ###

row3_spacer1, row3_1, row3_spacer2 = st.columns((0.2, 7.1, 0.2))
with row3_1:
    st.subheader("Nucleotide content of a study")
row4_spacer1, row4_1, row4_spacer2, row4_2, row4_spacer3 = st.columns(
    (0.2, 2.3, 0.4, 4.4, 0.2)
)
with row4_1:
    selected_study = st.selectbox(
        "Select a study of interest",
        data["study_accession"].unique().tolist(),
    )
    data_study = data[data["study_accession"] == selected_study]
    st.write(data_characteristics(data_study, query)[0])
with row4_2:
    st.plotly_chart(plot_study_actgn_content(data_study))

# RAW DATA

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)
