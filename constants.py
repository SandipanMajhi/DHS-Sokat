groq_api_key = "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"
openai_api_key = "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"

open_source_models = ["llama2-70b-4096", "gemma-7b-it", "mixtral-8x7b-32768"]
paid_source_models = ["gpt-4-turbo-preview", "gpt-3.5-turbo"]

summary_prompt_template = """Write a concise summary of the following text.
"{text}"
CONCISE SUMMARY:"""


risk_dimensions = ["most complex", "most expensive", "most trustworthy and dependable by the public and Department of Homeland Security", 
                   "most effective by the public and Department of Homeland Security", "most safe",
                   "most unbiased", "most explainable"]

risk_dimensions_classes = ["Complexity", 
                           "Expensiveness", 
                           "Trustworthy", 
                           "Effectiveness", 
                           "Privacy", "Inappropriate_Biases", "Explainability"]


sys_msg = "You are a smart Executive at the Department of Homeland Security. You are given a list of 58 use cases.\n"
user_msg = [f"""
For each one of the 58 use cases rank them from 1 to 58. Rank them from {risk_dimensions[i]} to least {risk_dimensions[i][5:]}. Ensure that each case is used and ranked to your best abilities. Do not exclude any cases.
Here is sample output: 
DHS-728 : 23
DHS-98 : 46""" for i in range(len(risk_dimensions))] 


# user_msg = f"""
# For each one of the 58 use cases rank them from 1 to 58. Rank them from {risk_dimensions[0]} to least {risk_dimensions[0][5:]}. Ensure that each case is used and ranked to your best abilities. Do not exclude any cases.
# Here is sample output: 
# DHS-728 : 23
# DHS-98 : 46"""

# ranking_prompt_with_tasks = [f"""You are a smart Executive at the Department of Homeland Security. You are given a list of 58 use cases.
# For each one of the 58 use cases rank them from 1 to 58. Rank them from {risk_dimensions[i]} to least {risk_dimensions[i][5:]}. Ensure that each case is used and ranked to your best abilities. Do not exclude any cases.""" for i in range(len(risk_dimensions))] 

# ranking_prompt_with_tasks = [f"""You are an extremely intelligent and thoughtful Executive at the Department of Homeland Security. You will review each of these use cases along the following dimension.
# Rank order and sort -- which {risk_dimensions[i]}. Give {risk_dimensions[i][3:]} a score 58 and least 1. Also provide justification for scores given to each use case.""" for i in range(len(risk_dimensions))] 


#### Got good answers in gpt3.5 turbo with temperature 0.5 ####
# ranking_prompt_with_tasks = [f"""You are an extremely intelligent and thoughtful Executive at the Department of Homeland Security. You will review each of these use cases along the following dimension.
# Relatively Rank order every one of them with careful justification on each rank from 1 to 58 where {risk_dimensions[i][3:]} is ranked 58 and least {risk_dimensions[i][12:]} 1.""" for i in range(len(risk_dimensions))] 


# ranking_prompt_with_tasks = [f"""You are an extremely intelligent and thoughtful Executive at the Department of Homeland Security. You will review each of these use cases along the following dimension.
# Rank order -- which {risk_dimensions[i]}. Assign each text a score where {risk_dimensions[i][3:]} a score 58 and least 1.""" for i in range(len(risk_dimensions))] 

# rest = """
# "{texts}"
# RANKING:
# """

# rest = """
# """

# ranking_prompt_with_tasks = [task+rest  for task in user_msg]



##### Lets revisit this again #####

# Rank the 100 financial project summaries from 1 to 100 based on the estimated project costs in US Dollars. Consider the complexity of the project and time required for delivery as secondary factors that might influence costs. Pay particular attention to projects utilizing AI, as they could potentially offer cost-effective solutions. Additionally, be mindful of any potential cost-saving measures mentioned in the summaries. Cost is the most significant criterion for ranking these projects.