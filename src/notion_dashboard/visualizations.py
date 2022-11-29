import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def visualize_volume_across_hue_column(
    ex_df: pd.DataFrame,
    hue_column_name: str = "type",
    volume_column_name: str = "volume",
    aggregation_column_name: str = "date",
):
    plt.figure(figsize=(12, 8))
    # Get all unique values in hue column
    unique_values_in_hue_column = ex_df[hue_column_name].unique()
    hue_dfs = []
    # For each hue value get the aggregated volume
    for value in unique_values_in_hue_column:
        # Get only rows of hue value
        current_hue_df = ex_df[ex_df[hue_column_name] == value]
        # Aggregate for rows with hue value
        current_hue_df = (
            current_hue_df[[aggregation_column_name, volume_column_name]]
            .groupby([aggregation_column_name])
            .sum()
        )
        # Re-attach hue column
        current_hue_df[hue_column_name] = value
        hue_dfs += [current_hue_df]

    comb_df = pd.concat(hue_dfs)
    ax = sns.lineplot(
        data=comb_df,
        x=aggregation_column_name,
        y=volume_column_name,
        hue=hue_column_name,
    )
    ax.set_title("Week over Week Exercise Volume")


def visualize_exercise_volume_over_time(
    ex_df: pd.DataFrame,
    exercise_column_name: str = "name",
    aggregation_column_name: str = "date",
    volume_column_name: str = "volume",
    n_cols: int = 3,
):
    plt.figure(figsize=(12, 8))
    # Get list of exercises
    exercises_list = ex_df[exercise_column_name].unique().tolist()
    n = len(exercises_list)
    # Setup subplots
    fig, axes = plt.subplots(
        nrows=math.ceil(n / n_cols), ncols=n_cols, figsize=(30, 30)
    )
    # For each exercise
    for exercise, ax in zip(exercises_list, axes.flatten()):
        # Aggregate volume and plot lineplot
        sns.lineplot(
            data=ex_df[ex_df[exercise_column_name] == exercise][
                [aggregation_column_name, volume_column_name]
            ]
            .groupby([aggregation_column_name])
            .sum(),
            x=aggregation_column_name,
            y=volume_column_name,
            ax=ax,
        )
        ax.set_title(f"{exercise} Volume over Time")
    plt.tight_layout()


def visualize_week_on_week_volume(
    ex_df: pd.DataFrame,
    date_column_name: str = "date",
    volume_column_name: str = "volume",
):
    plt.figure(figsize=(12, 8))
    week_column_name = "week"
    ex_df[week_column_name] = ex_df[date_column_name].apply(
        lambda x: x.isocalendar().week
    )

    sns.lineplot(
        data=ex_df[[week_column_name, volume_column_name]]
        .groupby(week_column_name)
        .sum(),
        x=week_column_name,
        y=volume_column_name,
    )
