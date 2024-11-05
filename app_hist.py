import pandas as pd
import plotly.express as px
from requests import session
from shiny.express import input, render, ui
from shiny import reactive
from shinywidgets import render_widget # type: ignore
from matplotlib import pyplot as plt

ui.page_opts(title="Histogram", fillable=True)

with ui.sidebar():
    ui.input_file("file_upload", "Choose CSV File", accept=[".csv"], multiple=False)
    ui.input_select("target_column", "Data", choices=[])
    ui.input_select("bins", "Bins", choices=[5,10,12,15,18])
    
with ui.navset_card_underline(title="Result"):
    with ui.nav_panel("Table"):
        @render.data_frame
        def show_table():
            file = input.file_upload()
            if file:
                df = pd.DataFrame(file)
                df = pd.read_csv(df.iloc[0,3])
                return df

    with ui.nav_panel("Plot"):
        @render.plot(alt="A histogram")
        def plot():
            file = input.file_upload()
            if file:
                df = pd.DataFrame(file)
                df = pd.read_csv(df.iloc[0,3])
                fig, ax = plt.subplots()
                ax.hist(df[input.target_column()], int(input.bins()), density=True)
                
        @reactive.effect
        def _():
            file = input.file_upload()
            if file:
                df = pd.DataFrame(file)
                df = pd.read_csv(df.iloc[0,3])
                ui.update_select("target_column",choices=df.columns.tolist())
        
                
