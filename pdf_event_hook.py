"""PDF rendering hooks for mkdocs-to-pdf."""


def pre_pdf_render(soup, logger):
    """Add a repeated PDF footer link back to the table of contents."""
    toc = soup.find("article", id="doc-toc")
    if not toc:
        logger.warning("PDF ToC anchor not found; footer ToC link not added")
        return soup

    link = soup.new_tag("a", href="#doc-toc", **{"class": "pdf-toc-footer-link"})
    link.string = "[ToC]"
    toc.insert_after(link)
    return soup
