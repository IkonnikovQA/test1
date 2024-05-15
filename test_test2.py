from selene import browser,be, have

def test_test2():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))