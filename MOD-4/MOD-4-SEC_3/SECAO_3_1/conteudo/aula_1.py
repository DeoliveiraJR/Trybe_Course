import requests
from parsel import Selector


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text  # <hmtml5!>


def extract_quotes(content: str) -> list[dict]:
    selector = Selector(content)
    quotes = []
    for quote in selector.css("div.quote"):
        text = quote.css("span.text::text").get()
        author = quote.css("small.author::text").get()
        tags = quote.css("a.tag::text").getall()
        quotes.append(
            {
                "text": text,
                "author": author,
                "tags": tags,
            }
        )
    return quotes  # return {text: text, author: author, tags: tags}


def get_next_page(content: str) -> str | None:
    selector = Selector(content)
    next_page = selector.css("li.next > a::attr(href)").get()
    return next_page  # return /page/2/


def get_all_quotes() -> list[dict]:
    base_url = "https://quotes.toscrape.com"
    next_page = "/"
    quotes = []

    while next_page:
        url = base_url + next_page
        # print('url ====', url)

        page_content = fetch_content(url)
        # print('page_content ====', page_content)

        quotes.extend(extract_quotes(page_content))
        next_page = get_next_page(page_content)
        # print('next_page ====', url)

    return quotes


if __name__ == "__main__":
    # url = "https://quotes.toscrape.com"
    # page_content = fetch_content(url)
    # quotes = extract_quotes(page_content)
    quotes = get_all_quotes()
    # print(quotes)
