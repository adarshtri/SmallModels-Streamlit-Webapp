from src.web_pages.movie_recommendation_content_based import load_content_based_movie_recommendation_page
from src.web_pages.page_not_found import page_not_found


def load_page_based_on_query_params(params: dict):

    if request_for_movie_recommendation_content_based(params):
        return load_content_based_movie_recommendation_page
    else:
        return page_not_found

def request_for_movie_recommendation_content_based(params: dict) -> bool:

    page = params.get("page", ["home"])

    if page == "movie_recommendation_content_based":
        return True
    return False
