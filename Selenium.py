from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://www.bauhaus.dk/grouw-robotplaeneklipper-core-600-m-inkl-batteri-og-lader')
elem = browser.find_element('.product-details__content--description > p:nth-child(1)')
elem.text

