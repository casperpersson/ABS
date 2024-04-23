import bs4, requests


def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()  # tjekker for fejl når man henter fra siden
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # soup.select henter en css selecter fra hjemmesiden
    elems = soup.select(
        'html body#html-body.catalog-product-view.product-grouw-robotplaeneklipper-core-600-m-inkl-batteri-og-lader.categorypath-maskiner-havemaskiner-robotplaeneklippere.category-robotplaeneklippere.page-layout-1column main#maincontent.category-content.page-main div.columns div.column.main div.product-info-container div.product-info-container--main div.product-info.product-info--main div div.product-add-form form#product_addtocart_form.product-sku-1428776 div.price-wrapper div.price-box.price-final_price span.price-block__price span.price-container.amount-default.price-final_price.tax.weee span#product-price-670885.price-wrapper')
    return elems[0].text.strip()


price = getPrice('https://www.bauhaus.dk/grouw-robotplaeneklipper-core-600-m-inkl-batteri-og-lader')
print('the price is ' + price)
