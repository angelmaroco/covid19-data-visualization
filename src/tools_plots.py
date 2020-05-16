import folium
import folium.plugins

STATE_COLOR = {'infected': 'red', 'suspect': 'orange', 'negative': 'green'}


def build_map_cluster(title, data, geojson, central_position=[40.4169749, -3.7031846]):
    map = folium.Map(central_position, zoom_start=9, tiles='cartodbpositron')
    folium.GeoJson(geojson).add_to(map)

    infected = data.query("state == 'infected'")['state'].count()
    suspect = data.query("state == 'suspected'")['state'].count()
    negative = data.query("state == 'negative'")['state'].count()
    recovered = data.query("state == 'recovered'")['state'].count()

    marker_cluster = folium.plugins.MarkerCluster().add_to(map)

    for index, row in data.iterrows():
        color_state = STATE_COLOR.get(row['state'], 'orange')

        folium.Marker(
            [row['lon'], row['lat']],
            popup=f"Age: {row['age']}",
            icon=folium.Icon(color=color_state, icon='icon-circle'),
        ).add_to(marker_cluster)

    legend_html = """
    <div style="position: absolute;right: 0.5%;top: 5%;z-index:9999;width: 170px;">
        <ul class="list-group">
            <li class="list-group-item" style="height: 38px;">
                <i class="fa fa-map-marker" aria-hidden="true" style="color:blue; font-size: 20px;"></i>&nbsp;&nbsp;
                <span>Negative</span>&nbsp;<span class="badge">{}</span>
            </li>
            <li class="list-group-item " style="height: 38px;">
                <i class="fa fa-map-marker" aria-hidden="true" style="color:orange; font-size: 20px;"></i>&nbsp;&nbsp;
                <span>Suspected</span>&nbsp;<span class="badge">{}</span>
            </li>
            <li class="list-group-item " style="height: 38px;">
                <i class="fa fa-map-marker" aria-hidden="true" style="color:red; font-size: 20px;"></i>&nbsp;&nbsp;
                <span>Infected</span>&nbsp;<span style="text-align=right;" class="badge">{}</span>
            </li>
            <li class="list-group-item " style="height: 38px;">
                <i class="fa fa-map-marker" aria-hidden="true" style="color:green; font-size: 20px;"></i>&nbsp;&nbsp;
                <span>Recovered</span>&nbsp;<span style="text-align=right;" class="badge">{}</span>
            </li>
        </ul>
    </div>
    """.format(
        negative, suspect, infected, recovered
    )

    map.get_root().html.add_child(folium.Element(legend_html))
    print(title)

    title_html = """
    <div class="leaflet-top leaflet-right" style="z-index: 2000;font-size: 16px;font-weight: bold; top: 0.5%;">
          <div class="leaflet-control-attribution">{}</div>
    </div>
    """.format(
        str(title)
    )

    map.get_root().html.add_child(folium.Element(title_html))
    return map
