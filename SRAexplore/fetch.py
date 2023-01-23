from pysradb.search import SraSearch
import streamlit as st

from utils import none_string


@st.cache
def fetch(
    query,
    return_max,
    organism,
    layout,
    mbases,
    selection,
    source,
    strategy,
    publication_date,
):
    """Simple fetch function to call in the app with subselection of parameters
    of interest. Calls pysradb python API with the parameters passed in argument
    and returns a dataframe with a selection of SRA metadata.

    Args:
        query (_str_): Query to submit to pysradb.
        return_max (_int_): Maximal number of entries returned by pysradb.
        organism (_str_): Name of the organism of interest.
        layout (_str_): Library layout. Can take two values paired or single.
        mbases (_int_): Minimum of number of bases in the studies.
        selection (_str_): Library selection.
        source (_str_): Library source.
        strategy (_str_): Library sequencing strategy.
        publication_date (__str__): Publication date interval int the format dd-mm-YY:dd-mm-YY.

    Returns:
        _pandas.DataFrame_: Dataframe to plot.
    """

    instance = SraSearch(
        verbosity=3,
        return_max=none_string(return_max),
        query=none_string(query),
        organism=none_string(organism),
        layout=none_string(layout),
        mbases=none_string(mbases),
        selection=none_string(selection),
        source=none_string(source),
        strategy=none_string(strategy),
        publication_date=none_string(publication_date),
    )
    instance.search()
    data = instance.get_df()

    return data
