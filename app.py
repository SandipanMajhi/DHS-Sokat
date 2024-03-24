import streamlit as st
import pandas as pd
from constants import *
from  st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode, ColumnsAutoSizeMode

import pickle as pkl


##### This part is the sidebar code #####

st.sidebar.title("DHS AI Inventory Ranker")

ranking_options = [txt.replace("_"," ") for txt in risk_dimensions_classes]

add_ranking = st.sidebar.selectbox(
    "Ranking type",
    ranking_options
)

add_model = st.sidebar.selectbox(
    "Language Model",
    paid_source_models
)

##### Sidebar code ends #####

@st.cache_data
def load_main_frame():
    df = pd.read_excel(r"./Data/output.xlsx", engine='openpyxl')

    return df


@st.cache_data
def load_gpt35_data():
    with open("./gpt35_frames/frames.pkl", "rb") as fp:
        gptframes = pkl.load(fp)

    return gptframes

@st.cache_data
def modify_columns(model_frames, risks):
    risks = [f"{risks[i]}_ranking" for i in range(len(risks))]
    justifications = [f"{risks[i]}_Justifications" for i in range(len(risks))]

    for i in range(len(risks)):
        model_frames[f"df{i}"] = model_frames[f"df{i}"].rename(columns = {"ranks" : risks[i], "Justification" : justifications[i]})


    for i in range(len(risks)):
        stripped_Names = [txt.strip() for txt in model_frames[f"df{i}"]['Use Case Name']]
        model_frames[f"df{i}"]['Use Case Name'] = stripped_Names
    
    return model_frames, risks, justifications

@st.cache_data
def add_Summaries(model_name, main_df, sub_df):
    sum_col = None
    if model_name in paid_source_models:
        sum_col = f"{paid_source_models[0]}_summaries"
    else:
        sum_col = f"{model_name}_summaries"
        
    df_sum = main_df[["Use Case ID", sum_col]]
    df_sum = df_sum.merge(sub_df, on ="Use Case ID", how = "inner")

    df_sum.rename(columns = {sum_col:"summaries"},inplace = True)
    sum_col = "summaries"

    return df_sum, sum_col

def hover_code(tooltipCol):
    return JsCode(f"""
                    class CustomTooltip {{
                                eGui;
                                init(params) {{
                                    const eGui = (this.eGui = document.createElement('div'));
                                    const color = params.color || 'black';
                                    const data = params.api.getDisplayedRowAtIndex(params.rowIndex).data;
                                    eGui.classList.add('custom-tooltip');
                                    //@ts-ignore
                                    eGui.style['background-color'] = color;
                                    eGui.style['color'] = 'white';     
                                    eGui.style['padding'] = "5px 5px 5px 5px";  
                                    eGui.style['font-size'] = "20px";                                         
                                    eGui.style['border-style'] = 'double';                                                             
                                    this.eGui.innerText = data.{tooltipCol};
                                }}
                                getGui() {{
                                    return this.eGui;
                                }}
                                }}
                            """)



#### Main Code #####

main_df = load_main_frame()

if add_model == paid_source_models[1]: #### GPT 3.5 model chosen

    gpt35_frames, risklist, justlist = modify_columns(model_frames=load_gpt35_data(), risks=risk_dimensions_classes)
    choice = ranking_options.index(add_ranking)
    df = gpt35_frames[f"df{choice}"]
    df, sum_col = add_Summaries(model_name=add_model, main_df=main_df, sub_df=df)

    print(df.columns)
    print(sum_col)
    print(df[sum_col][0])

    builder = GridOptionsBuilder.from_dataframe(df)
    builder.configure_column(field=f"{risklist[choice]}", maxWidth = 200, tooltipField = f"{justlist[choice]}", tooltipComponent = hover_code(f"{justlist[choice]}"))
    builder.configure_column(field="Use Case ID", maxWidth = 100)
    builder.configure_column(field="Use Case Name",tooltipField = sum_col, tooltipComponent = hover_code(sum_col))
    options = builder.build()
    

    for col in options["columnDefs"]:
        if col["headerName"] == f"{justlist[choice]}" or col["headerName"] == sum_col:
            col["hide"] = True

    AgGrid(data=df, gridOptions=options, columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW, theme="balham", allow_unsafe_jscode=True)


elif add_model == paid_source_models[0]: #### GPT-4 Chosen
    pass

