import wikipedia

page_name = 'kamal haasan'  # Specify the Wikipedia page title

try:
    page = wikipedia.page(page_name)  # Get the Wikipedia page
    summary = page.summary  # Get the summary of the page
    print(summary)
except wikipedia.exceptions.PageError:
    print("Page does not exist.")
except wikipedia.exceptions.DisambiguationError as e:
    print("Page title is ambiguous. Suggestions:", e.options)