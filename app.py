import streamlit as st
import pandas as pd
from constants import *
from  st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode, ColumnsAutoSizeMode

import pickle as pkl

st.set_page_config(layout="wide")


st.header('DHS AI Use Case Ranking', divider='rainbow')
st.write('Powered by LLAMA-2-70B, Mixtral-8X7B, GPT-3.5 and GPT-4.')

@st.cache_data
def load_data():
    df = pd.read_csv("./Data/Streamlit_pass1.csv")
    df.rename(columns= {"gpt-4-turbo-preview_summaries" : "Summaries"}, inplace=True)
    return df

def styler_frame():
    d = {
        "Use Case ID" : "background-color:#E7E8D1",
        "Use Case Name" : "background-color:#E7E8D1"
        # "BIAS_Ranking" : "background-color:#E7E8D1",
        # "COMPLEXITY_Ranking" : "background-color:#FFF2D7",
        # "EFFECTIVENESS_Ranking" : "background-color:#F96167",
        # "EXPENSIVENESS_Ranking" : "background-color:#F9E795",
        # "EXPLAINABLE_Ranking" : "background-color:#D3C5E5",
        # "SAFE_Ranking" : "background-color:#F7C5CC",
        # "TRUSTWORTHY_Ranking" : "background-color:#A7BEAE"
    }

    return d

def background_cell(x):
    d = styler_frame()
    s = pd.DataFrame(d,index=x.index,columns=x.columns)
    return s


#### Main Code #####

main_df = load_data()

st.dataframe(
    # main_df.style.apply(background_cell,axis=None),
    main_df.style.background_gradient(subset=["BIAS_Ranking", "COMPLEXITY_Ranking",
                                              "EFFECTIVENESS_Ranking", "EXPENSIVENESS_Ranking", "EXPLAINABLE_Ranking",
                                               "SAFE_Ranking", "TRUSTWORTHY_Ranking" ],cmap='YlOrRd'),
    use_container_width= True,
    height = 700,
    hide_index=True,
    column_order= ("Use Case ID", "Use Case Name", 'BIAS_Ranking',
                                            'COMPLEXITY_Ranking',
                                        'EFFECTIVENESS_Ranking',
                                        'EXPENSIVENESS_Ranking',
                                        'EXPLAINABLE_Ranking',
                                        'SAFE_Ranking',
                                        'TRUSTWORTHY_Ranking'
                    )
)


