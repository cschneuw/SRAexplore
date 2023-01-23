import plotly.express as px

from utils import inverse_mapping


def plot_histograms_categorical(data, category, title):
    """Plot categorical data in histogram of counts.

    Args:
        data (_pandas.DataFrame_): SRA metadata to plot.
        category (_str_): Categorical value to plot in the x axis.
        title (_str_): Title of the histogram.

    Returns:
        _plotly.graph_objects.Figure_: Figure object to plot.
    """
    fig = px.histogram(
        data,
        x=category,
        color="study_accession",
        title=f"{title}",
        hover_name=category,
    )
    fig.update_layout(
        height=600,
    )
    return fig


def plot_boxplots_numerical(data, category, quantity, title):
    """Plot categorical data in boxplot of the quantity in the dataframe to plot.

    Args:
        data (_pandas.DataFrame_): SRA metadata to plot.
        category (_str_): Categorical variable to plot in the x axis.
        quantity (_str_): Quantity to plor in boxplot.
        title (_str_): Title of the boxplot. Categorial variable plotted.

    Returns:
        _plotly.graph_objects.Figure_: Figure object to plot.
    """
    fig = px.box(
        data,
        x=category,
        y=quantity,
        color="study_accession",
        title=title,
        boxmode="group",
    )
    fig.update_layout(boxgap=0, height=500)
    return fig


def plot_strip_numerical(data, category, quantity, title):
    """Plot categorical data in boxplot with only points of the quantity in the dataframe to plot.

    Args:
        data (_pandas.DataFrame_): SRA metadata to plot.
        category (_str_): Categorical value to plot in the x axis.
        quantity (_str_): Quantity to plor in boxplot.
        title (_str_): Title of the boxplot. Categorial variable plotted.

    Returns:
        _plotly.graph_objects.Figure_: Figure object to plot.
    """
    fig = px.strip(
        data,
        x=category,
        y=quantity,
        color="study_accession",
        title=title,
    )
    fig.update_layout(boxgap=0, height=500)
    return fig


def plot_scatter_numerical(data, category, quantity, title):
    """Plot categorical data in scatter plot of the quantity in the dataframe to plot.

    Args:
        data (_pandas.DataFrame_): SRA metadata to plot.
        category (_str_): Categorical value to plot in the x axis.
        quantity (_str_): Quantity to plor in boxplot.
        title (_str_): Title of the histogram.

    Returns:
        _plotly.graph_objects.Figure_: Figure object to plot.
    """
    fig = px.scatter(
        data,
        x=category,
        y=quantity,
        color="study_accession",
        title=title,
        boxmode="group",
    )
    fig.update_layout(boxgap=0, height=500)
    return fig


def plot_study_actgn_content(data_study):
    """Plot stacked barplots of A, C, T, G and N content of each experiment.

    Args:
        data_study (_pandas.DataFrame_): Study of SRA metadata to plot.

    Returns:
        _plotly.graph_objects.Figure_: Figure object to plot.
    """
    nt_labels = inverse_mapping(
        {
            "A count": "run_1_base_A_count",
            "C count": "run_1_base_C_count",
            "G count": "run_1_base_G_count",
            "N count": "run_1_base_N_count",
            "T count": "run_1_base_T_count",
        }
    )
    data_study = data_study.melt(
        id_vars="experiment_accession", value_vars=list(nt_labels.keys())
    )
    fig = px.bar(
        data_study,
        x="experiment_accession",
        y="value",
        color="variable",
        color_discrete_map={
            "run_1_base_A_count": "green",
            "run_1_base_C_count": "blue",
            "run_1_base_G_count": "yellow",
            "run_1_base_N_count": "black",
            "run_1_base_T_count": "red",
        },
        hover_name="experiment_accession",
    )
    fig.for_each_trace(
        lambda t: t.update(
            name=nt_labels[t.name],
            legendgroup=nt_labels[t.name],
            hovertemplate=t.hovertemplate.replace(t.name, nt_labels[t.name]),
        )
    )
    fig.update_layout(hoverlabel=dict(bgcolor="white", font_size=12))

    return fig
