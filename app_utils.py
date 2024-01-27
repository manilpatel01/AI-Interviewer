def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardizes_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardizes_name(page_name)

    pages = get_pages("Homepage.py") 

    for page_hash, config in pages.items():
        if standardizes_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardizes_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")