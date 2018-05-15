import numpy as np
# from connector import connector

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
           new_score = alpha*engine_score + (1-alpha)*cat_cosine_score
    '''
    def __init__(self, alpha):
        self.alpha = alpha

    '''
    param: results is a list of json objects returned from the engine
    return: array of all categories in results
    '''
    def collect_categories(self, results):
        c_all = []
        for k, v in results.items():
            c = results[k]['categories']
            c_all.extend(c)
        return np.unique(c_all)

    '''
    param: user object
    param: list of result categories
    return: normalized category vector for the user (in same order as categoreis)
    '''
    def create_user_cv(self, user, categories):
        '''
        What is the User object structure?
        '''
        u_cv = np.zeros(len(categories))
        cat = list(user.keys())  # THIS NEED FIXING
        # print(cat)
        for c in cat:
            i = np.where(categories == c)[0]
            if len(i) == 0: #i[0].shape[0]==0:
                continue
            u_cv[i] = user[c]
        return u_cv/np.sum(u_cv)


    '''
    See create_user_cv()
    '''
    def create_article_cv(self, article, categories):
        a_cv = np.zeros(len(categories))
        art_cat = article['categories']
        for a in art_cat:
            i = np.where(categories == a)[0]
            if len(i) == 0:
                continue
            a_cv[i] = 1/len(art_cat)
        return a_cv


    '''
    param: results object from engine
    param: list of categories
    return: all article normalized category vectors
    {
        "article_id":np.array([]),
    }
    '''
    def create_all_article_cvs(self, results, categories):
        a_cvs = {}
        for k, v in results.items():
            a_cv = self.create_article_cv(results[k], categories)
            a_cvs[k] = a_cv
        return a_cvs


    '''
    param: category vectors for user and article
    return: cosine similarity
    '''
    def cosine_sim(self, u_cv, a_cvs):
        for k, v in a_cvs.items():
            a_cvs[k] = u_cv@v
        return a_cvs


    '''
    param: results object
    param: user object
    return: new_results where the objects have been re-ranked using category similarity scores as well.
    '''
    def rerank(self, results, user):
        cat = self.collect_categories(results)
        u_cv = self.create_user_cv(user, cat)
        a_cvs = self.create_all_article_cvs(results, cat)
        cosine_scores = self.cosine_sim(u_cv, a_cvs)
        for k, v in results.items():
            # print("%f, %f\n" % (results[k]['score'], cosine_scores[k]))
            results[k]['score'] = self.alpha*results[k]['score'] + (1-self.alpha)*cosine_scores[k]
        return results

    '''
    param: top N results from the search engine
    param: the original query
    param: user_sh is the user search history
    return: boosted results, sorted
    '''
    def LucBoost(self, results, query, user_sh, rho=100):
        if query in user_sh:
            res = user_sh[query]
        else:
            return results.items()
        for k,v in results.items():
            ctQD = np.sum(np.where(np.array(res)==k, 1, 0))
            ctQ = len(res)
            gamma = ctQ / (ctQ+rho)
            results[k]['score'] = gamma*ctQD/ctQ + (1-gamma)*results[k]['score']
        return sorted(results.items(), key=lambda x: x[1]['score'], reverse=True)

'''
if __name__ == '__main__':
    user = {'categories':['Auto racing']}
    comp = Comparator(0.6)
    conn = connector(hostname='http://localhost:9200', index_name='articles')
    results = conn.search('australia')
    for d in results:
        del d['_source']['text']
    print('Original:')
    for d in results:
        print(d['_source']['title'],d['_score'])
    new_results = comp.rerank(results,user)
    new_results.sort(key=lambda x: x['_score'], reverse=True)
    print('New:')
    for d in new_results:
        print(d['_source']['title'],d['_score'])
'''