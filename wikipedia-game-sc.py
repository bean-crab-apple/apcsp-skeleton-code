from queue import Queue
import wikipediaapi
import time

user_agent = "hulloits.wikifinder (goofygoff.minecraft@gmail.com)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")

# HELPER FUNCTION: fetch_links(page) passes in a wikipedia page and returns a list of all the pages linked from that page
def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
    #print(links_list)    
    return links_list

#IN CLASS: Finish the definition of the wikipedia_game_solver using a Breadth-First-Search Traversal
def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    # FINISH THE CODE HERE
    visited = []
    queue = Queue()
    path = []
    parent = {}

    queue.put(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_page.title:
            break
        current_page = wiki_wiki.page(current_page_title)
        current_links = fetch_links(current_page)
        visited.append(current_page.title)
        for link in current_links:
            if link not in visited:
                queue.put(link)
                parent[link] = current_page_title
    
    child = target_page.title

    while child != start_page.title:
        path.append(child)
        child = parent[child]
    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
  
    return path

# Example usage:
start_page = wiki_wiki.page('Nina Tandon')
target_page = wiki_wiki.page('Italian Language')
print(str(start_page) + ", " + str(target_page))
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)