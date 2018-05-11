import numpy as np

class Comparator:
    '''
    - Take top N results.
    - Collect categories of results.
    - Make user category vector and article category vectors
    - Calculate similarity
    - Rerank with a weighting scheme (linear)

    TODO as well:
    - Use user previous searches
    '''

    '''
    param: alpha is the weighing factor used in the linear weighing scheme
    '''
    def __init__(self, alpha):
        self.alpha = alpha

    '''
    param: results is a list of json objects returned from the engine

    return: array of all categories in results
    '''
    def collect_categories(self, results):

    '''
    param: user object
    param: list of result categories

    return: normalized category vector for the user (in same order as categoreis)
    '''
    def create_user_cv(self, user, categories):

    '''
    See create_user_cv()
    '''
    def create_article_cv(self, article, categories):

    '''
    param: results object from engine
    param: list of categories

    return: all article normalized category vectors
    '''
    def create_all_article_cvs(self, results, categories):

    '''
    param: category vectors for user and article

    return: cosine similarity
    '''
    def cosine_sim(self, u_cv, a_cv):

    '''
    param: results object
    param: user object

    return: new_results where the objects have been re-ranked using category similarity scores as well.
    '''
    def rerank(self, results, user):
