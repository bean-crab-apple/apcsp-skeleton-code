# test branch
# queues don't work! when things are alphabetically added to a queue, they work maybe for like the first 20 or so elements(maybe up to "Af..." on large pages)
# however, the last element in the list("Z...") fails to be found when queue.get is being run
# does the queue structure have an inherent size limit?
# btw redirect pages also completely break the API, for example, 'Nina Tandon' links to 'Biomedical engineer' which redirects to 'Biomedical engineering' but
# fetch_links(wiki_wiki.page('Biomedical engineer')) does not return a list containing 'Biomedical engineering'
# update: it's not queues that are broken(although this now uses a standard list) however I did have to add a shortcut break which saves effectively a whole
# level of time and generally makes python behave more nicely because it no longer has this massive queue to manage
# also the links in dropdowns at the bottoms of pages and the links to wiki metapages in the noteboxes are also returned by page.links
from queue import Queue
import wikipediaapi
import time

user_agent = "MsOrret'sWikipediaGame/1.0 (orret.deborah@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")

# HELPER FUNCTION: fetch_links(page) passes in a wikipedia page and returns a list of all the pages linked from that page
def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        
    return links_list

#IN CLASS: Finish the definition of the wikipedia_game_solver using a Breadth-First-Search Traversal
def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    # FINISH THE CODE HERE

    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
  
    return path

# Example usage:
start_page = wiki_wiki.page('Nina Tandon')
target_page = wiki_wiki.page('Italian language')
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)