import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
from streamlit_tree_select import tree_select
from coder import coder
from use_case import use_case as uc
from io import BytesIO
from PIL import Image
st.set_page_config(
    page_title="UML generator",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="⚙️",
)
if 'node' not in st.session_state:
    st.session_state.node = []
if "len_node" not in st.session_state:
    st.session_state.len_node = 0
if "len_actor" not in st.session_state:
    st.session_state.len_actor = 0
if "checked" not in st.session_state:
    st.session_state.checked = []
if "expanded" not in st.session_state:
    st.session_state.expanded = []
if "selected" not in st.session_state:
    st.session_state.selected = {"checked":[],"expanded":[]}
if "image" not in st.session_state:
    st.session_state.image = ""
st.title("UML generator")

button_style = """
.css-b3z5c9    {
    width: 100%;
}
"""
st.markdown(f"<style>{button_style}</style>",unsafe_allow_html=True)

left,right = st.columns(2)
with left:
    use_cases = st_tags(
        label='type your use cases here',
        text='Press enter to add more',
        maxtags=50,
        key='1')
with right:
    actors = st_tags(
        label='type your actors here',
        text='Press enter to add more',
        maxtags=50,
        key='2')

if st.session_state.len_node != len(use_cases) or st.session_state.len_actor != len(actors):
    st.session_state.node = []
    st.session_state.len_node = len(use_cases)
    st.session_state.len_actor = len(actors)
    st.session_state.checked = st.session_state.selected["checked"]
    st.session_state.expanded = st.session_state.selected["expanded"]
    for uc in use_cases:
        element = {"label":uc,"value":uc,
            "children":[
                    {"label":"actor(s)","value":f"{uc}_actor",
                        "children":[{"label": actor, "value": f"{uc}_actor_{actor}"} for actor in actors]},
                    {"label":"extends","value":f"{uc}_extends",
                        "children":[{"label":extends,"value":f"{uc}_extends_{extends}"} for extends in use_cases]},
                    {"label":"includes","value":f"{uc}_includes",
                        "children":[{"label":includes,"value":f"{uc}_includes_{includes}"} for includes in use_cases]},
                    {"label":"inheritance","value":f"{uc}_inheritance",
                        "children":[{"label":inherit,"value":f"{uc}_inheritance_{inherit}"} for inherit in use_cases]},
            ]}
        st.session_state.node.append(element)
with left:
    generate,add = st.columns(2)
    with generate:
        generateButton = st.button("generate")
    st.session_state.selected = tree_select(st.session_state.node,only_leaf_checkboxes=True,checked= st.session_state.checked ,expanded=st.session_state.expanded,expand_on_click=True)
    

if generateButton:
    plantuml = "@startuml\n left to right direction\n " 
    for actor in actors:
        plantuml += "  actor " + actor + "\n"
    plantuml += "rectangle {\n"
    for use_case in use_cases:
        plantuml += "  usecase " + '('+use_case+')' + "\n"
    plantuml += "}\n"
    for element in st.session_state.selected["checked"]:
        if element.count("_") == 2:
            split = element.split("_")
            if split[1] == "actor":
                plantuml += "  "+split[2] + " -- " +"("+ split[0] +")"+ "\n"
            elif split[1] == "extends":
                plantuml += "  "+"("+split[0]+")" + " <.. " +"("+ split[2]+")"+":<<extends>>" + "\n"
            elif split[1] == "includes":
                plantuml += "  "+"("+split[0]+")" + " ..> " + "("+split[2] + ")"+":<<includes>>" +"\n"
            elif split[1] == "inheritance":
                plantuml += "  "+"("+split[0]+")" + " <|-l--- " +"("+ split[2] +")"+ "\n"

    plantuml += "@enduml"
    code = coder(plantuml)
    response = uc(code,"png")
    image_data = BytesIO(response)              

    st.session_state.image = Image.open(image_data)
with right:
    if st.session_state.image == "":
        st.write("No image to display")
    else:
        st.image(st.session_state.image, caption='Use case diagram', use_column_width=True)