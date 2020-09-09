from selenium import webdriver

try:
  fireFoxOptions = webdriver.FirefoxOptions()
  fireFoxOptions.set_headless()
  browser = webdriver.Firefox(firefox_options=fireFoxOptions)

  browser.get('https://pythonbasics.org')
  print(browser.page_source)
finally:
  try:
    brower.close()
  except:
    pass

