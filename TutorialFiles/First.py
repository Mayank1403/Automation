from selenium import webdriver

driver = webdriver.Chrome("C:\chromedriver\chromedriver")
driver.get("https://google.com")

#<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwiq8f3kxrjxAhWRzjgGHZCLA0IQ39UDCAQ">

searchBar = driver.find_element_by_name('q')
searchBar.send_keys('hello world')

#<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwilxLqTx7jxAhVwzTgGHQpjBIwQ4dUDCAs">
button = driver.find_element_by_css_selector('input[type="submit"]')
button.click()