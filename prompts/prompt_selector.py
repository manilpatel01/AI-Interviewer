from langchain.prompts import PromptTemplate
def prompt_sector(position: str, prompts: classmethod) -> dict:

    """ Select the prompt template based on the position """

    if position == 'Data Analyst':
        PROMPT = PromptTemplate(
            template= prompts.da_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Software Engineer':
        PROMPT = PromptTemplate(
            template= prompts.swe_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Data Scientist':
        PROMPT = PromptTemplate(
            template= prompts.ds_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Data Engineer':
        PROMPT = PromptTemplate(
            template= prompts.de_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}
    
    if position == 'Frontend Developer':
        PROMPT = PromptTemplate(
            template= prompts.ft_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Backend Developer':
        PROMPT = PromptTemplate(
            template= prompts.bk_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Cloud Engineer':
        PROMPT = PromptTemplate(
            template= prompts.cd_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}
    
    if position == 'DevOps Engineer':
        PROMPT = PromptTemplate(
            template= prompts.do_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Database Administrator':
        PROMPT = PromptTemplate(
            template= prompts.db_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Application Developer':
        PROMPT = PromptTemplate(
            template= prompts.ad_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Quality Assurance Engineer':
        PROMPT = PromptTemplate(
            template= prompts.qa_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    if position == 'Full Stack Developer':
        PROMPT = PromptTemplate(
            template= prompts.fs_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

    return chain_type_kwargs

