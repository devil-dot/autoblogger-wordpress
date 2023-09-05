template_test_2 = """
Use the real article summaries under "Context" to generate the blog section. Nothing is fabricated.
Answer the question below in 250 to 400 words. Your answer should be at least 5 paragraphs long. 
Each paragraph should be 50 to 80 words long. Separate each paragraph with "\\n\n".
Make sure there are no cutoff sentences. Make sure to include the closing clurly brackets in the JSON.
Also make sure there is a closing quotation mark for the JSON string.


{format_instructions}

{chat_history}
Question: {input}
AI:
"""
template_test_3 = """
Use the real article summaries under "Context" to generate the blog section. Nothing is fabricated.
Answer the question below in 250 to 400 words. Your answer should be at least 5 paragraphs long. 
Each paragraph should be 50 to 80 words long. Separate each paragraph with "\\n\n".
Make sure there are no cutoff sentences. Make sure to include the closing clurly brackets in the JSON.
Also make sure there is a closing quotation mark for the JSON string.


{format_instructions}

Question: {input}
AI:
"""
template_test_5 = """



{input}
{chat_history}
AI Response:
"""

template_test_6="""
    {chat_history}
    {format_instructions}
    {input}
"""
template_test_4 = """
Use the section passed in under 'Question'-> 'Section' and rewrite it using the instructions below.

{format_instructions}

Section to rewrite (rewrite the whole thing): {input}
"""

llm_chain_prompt_template = f"""
    Answer the question based on the information below and output in JSON format with the keys specified below.
    Your response will be no longer than 300 words.
    If the question cannot be answered using the information provided answer with an empty string.

    Use these format instructions to format the output:
    {{format_instructions}}

    Question:{{question}}
    Answer:"""