import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
from datetime import datetime
import clipboard
from branca.element import Template, MacroElement
import process as pr

class ClickForLatLng(MacroElement):
    _template = Template(u"""
                {% macro script(this, kwargs) %}
                    var marker = new Array();
                    function getLatLng(e){  
                        if (marker.length >0) {
                            for(i=0;i<marker.length;i++){
                                {{this._parent.get_name()}}.removeLayer(marker[i])
                            }
                        }
                        var new_mark = L.marker().setLatLng(e.latlng).addTo({{this._parent.get_name()}});
                        marker.push(new_mark);
                        new_mark.dragging.enable();
                        new_mark.on('dblclick', function(e){ {{this._parent.get_name()}}.removeLayer(e.target)})
                        var lat = e.latlng.lat.toFixed(6),
                        lng = e.latlng.lng.toFixed(6);
                        var txt = {{this.format_str}};
                        navigator.clipboard.writeText(txt);
                        new_mark.bindPopup({{ this.popup }});
                        };
                    {{this._parent.get_name()}}.on('click', getLatLng);
                    
                {% endmacro %}
                """)

    def __init__(self,popup=None):
        super(ClickForLatLng, self).__init__()
        self._name = 'ClickForLatLng'
        self.format_str = 'lat + "," + lng'
        self.alert = True
        self.lat_long = clipboard.paste().split(',')
        if popup:
            self.popup = ''.join(['"', popup, '"'])
        else:
            self.popup = '"Latitude: " + lat + "<br>Longitude: " + lng '


def generateBaseMap(default_location=[40.704467, -73.892246], default_zoom_start=11,min_zoom=11,max_zoom=15,):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start, min_zoom=min_zoom, max_zoom=max_zoom,max_bounds=True, min_lat= 40.47739894 , min_lon= -74.25909008, max_lat= 40.91617849,max_lon=-73.70018092)
    return base_map


def init():
    with st.sidebar:
        st.header("Enter your information", )
        gender = st.radio("Gender:", ["Male","Female"],key="vic1")
        race = st.selectbox("Race:",['WHITE', 'WHITE HISPANIC', 'BLACK', 'ASIAN / PACIFIC ISLANDER', 'BLACK HISPANIC', 'AMERICAN INDIAN/ALASKAN NATIVE', 'OTHER'],key="vic2")
        age = st.slider("Age:",0,120,key="vic3")
        date = st.date_input("Date:",datetime.now())
        hour = st.slider("Hour:",min_value=0,max_value=24)
        place = st.radio("Place:",("In park","In public housing","In station"))
        _,col,_ = st.sidebar.columns(3)   
        with  col:
            predict = st.button("predict")
        
    return gender, race, age, predict, date, hour, place

st.set_page_config(
    page_title="NYC Crime Prediction",
    page_icon="🌍",  # You can use any emoji or a URL to an image
    layout="wide",  # or "centered" or "wide"
    initial_sidebar_state="expanded",  # or "collapsed"
)

# Custom CSS style for the red box
red_box_style = """
    <style>
        .red-box {
            background-color:tomato;
            padding: 10px;
            border-radius: 5px;
            margin-bottom:10px;
            color: white;
            text-align: center;
        }
    </style>
"""

# Display the custom style
st.markdown(red_box_style, unsafe_allow_html=True)

# Create the red box around the title
st.markdown('<div class="red-box"><h1>New York Crime Prediction</h1></div>', unsafe_allow_html=True)
st.markdown("### Select your location on the map by clicking.")

gender, race, age, predict, date, hour, place= init()
base_map = generateBaseMap()
click = ClickForLatLng()
base_map.add_child(click)

lat_long = click.lat_long
if len(lat_long) == 2:
    lat = lat_long[0]
    long = lat_long[1]

else :
    lat = ""
    long = ""
# try:
    # print(float(lat),float(long))
    # folium.Marker([float(lat),float(long)]).add_to(base_map)
# except:
#     print("no marker")

x = folium_static(base_map)

if predict:
    if lat=='' or long == '':
        st.error("Please make sure that you selected a location on the map")    
        if st.button("Okay"):
            pass
    else:
        X = pr.create_df(hour,date.month,date.day,lat,long,place,age,race,gender)
        pred, crimes = pr.predict(X)
        st.markdown(f"You are likely to be a victim of: **{pred}**")
        st.markdown(f"#### Some of the crimes types are the following: ")
        st.markdown(crimes)