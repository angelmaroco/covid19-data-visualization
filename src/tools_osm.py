import glob
import os
import random

import pkg_resources

import geopandas as gpd
import matplotlib.pyplot as plt
import osmnx as ox
import pandas as pd
from shapely.geometry import Point

ox.config(log_console=True, use_cache=True)
ox.__version__

BASE = pkg_resources.resource_filename(__name__, '')

PATH_GDF = f'{BASE}/../data/osm/gdf/'
PATH_GRAPHML = f'{BASE}/../data/osm/graphml/'
PATH_GRAPHML_IMAGES = f'{BASE}/../data/images/graphml/'


def build_gdf(places, gdf_name, location=PATH_GDF, save_gdf=True):

    places = [places] if isinstance(places, list) else places
    state = False

    print(f'Building GDF for {places}')

    try:
        gdf = ox.gdf_from_place(places, gdf_name=gdf_name)
        ox.save_gdf_shapefile(gdf, gdf_name, location) if save_gdf else None
        state = True
    except Exception as exc:
        print(exc)

    return state


def build_network(
    places, network_type, file_name, save_graphml=True, location=PATH_GRAPHML
):

    places = [places] if isinstance(places, list) else places
    state = False

    print(f'Building network for {places}')

    try:
        G = ox.graph_from_place(places, network_type=network_type)
        G = ox.project_graph(G)
        ox.save_graphml(G, file_name, location) if save_graphml else None
        state = True
    except Exception as exc:
        print(exc)

    return state


def load_graphml(filename, folder=PATH_GRAPHML):
    G = ox.load_graphml(filename, folder)
    G = ox.project_graph(G)

    return G


def load_geopandas_file(filename, folder, location=PATH_GDF):
    return gpd.read_file(f'{location}/{folder}/{filename}.shp')


def save_graphml_image(filename, location=PATH_GRAPHML_IMAGES):

    state = False
    try:
        graphml = load_graphml(filename)
        fig, ax = ox.plot_graph(
            graphml,
            fig_height=10,
            show=False,
            close=False,
            edge_color='#777777',
            node_size=1,
        )
        plt.savefig(f'{location}/{filename}.png')
        state = True
    except Exception as exc:
        print(exc)

    return state


def random_points_in_polygon(number, polygon):

    points = []

    minx, miny, maxx, maxy = polygon.bounds

    i = 0
    while i < number:
        point = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(point):
            points.append(point)
            i += 1
    return points


def build_geojson_population():

    gpd_list = []

    for filename in glob.iglob(f'{PATH_GDF}**', recursive=True):
        if os.path.isfile(filename) and filename.endswith('.shp'):
            # print(f"Loading geodataframe file {os.path.basename(filename)}")
            gpd_list.append(gpd.GeoDataFrame.from_file(filename))

    return pd.concat(gpd_list)
