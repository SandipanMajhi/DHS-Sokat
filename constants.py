groq_api_key = "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"
openai_api_key = "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"

open_source_models = ["llama2-70b-4096", "gemma-7b-it", "mixtral-8x7b-32768"]
paid_source_models = ["gpt-4-turbo-preview", "gpt-3.5-turbo"]

summary_prompt_template = """Write a concise summary of the following text.
"{text}"
CONCISE SUMMARY:"""


risk_dimensions = ["is the most complex, complexity", "is the most expensive", "is the most responsible and trustworthy", 
                   "is the most rigorously tested to be effective", "is the safest for privacy, civil rights, and civil liberties",
                   "is the most likely to avoid inappropriate biases", "is the most transparent and explainable"]

# ranking_prompt_with_tasks = [f"""You are an extremely intelligent and thoughtful Executive at the Department of Homeland Security. You will review each of these use cases along the following dimension.
# Rank order and sort -- which {risk_dimensions[i]}. Give {risk_dimensions[i][3:]} a score 58 and least 1.""" for i in range(len(risk_dimensions))] 

ranking_prompt_with_tasks = [f"""You are an extremely intelligent and thoughtful Executive at the Department of Homeland Security. You will review each of these use cases along the following dimension.
Relatively Rank order every one of them with careful justification on each rank from 1 to 58 where {risk_dimensions[i][3:]} is ranked 58 and least {risk_dimensions[i][12:]} 1.""" for i in range(len(risk_dimensions))] 


# ranking_prompt_with_tasks = [f"""You are an extremely intelligent and thoughtful Executive at the Department of Homeland Security. You will review each of these use cases along the following dimension.
# Rank order -- which {risk_dimensions[i]}. Assign each text a score where {risk_dimensions[i][3:]} a score 58 and least 1.""" for i in range(len(risk_dimensions))] 

rest = """
"{texts}"
RANKING:
"""


ranking_prompt_with_tasks = [task+rest  for task in ranking_prompt_with_tasks]