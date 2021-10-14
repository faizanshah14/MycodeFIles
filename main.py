import selenium # Using Chrome to access web
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options();
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.get('https://nims.nadra.gov.pk/nims/certificate')

scriptString = """
$('input[name="checkEligibilityForm:issueDate_input"]').removeAttr('readonly');
$("input[name='checkEligibilityForm:j_idt90']").removeAttr('disabled');
$('.submit__generated').addClass("valid");
$('.submit__generated').removeClass("invalid");
$('input[name="checkEligibilityForm:issueDate_input"]').remove();
$('.ui-calendar.placeholder-no-fix.background-white').append('<input id="checkEligibilityForm:issueDate_input" name="checkEligibilityForm:issueDate_input" type="text" value="04-12-2014">')
/*
let firstVal = $('.submit__generated').children()[0].children[0].innerHTML
let secondVal = $('.submit__generated').children()[0].children[1].innerHTML
let sum = parseInt(firstVal) + parseInt(secondVal);
$('.submit__input').val(sum);*/
$('.submit__generated').remove();
$('#checkEligibilityForm').submit();

"""
cnicBox = driver.find_element_by_name('checkEligibilityForm:cnic')
cnicBox.send_keys('3710459870825')
driver.execute_script(scriptString)
#driver.refresh()
driver.execute_script('''$("input[name='checkEligibilityForm:j_idt90']").removeAttr('disabled');
$('.submit__generated').addClass("valid");
$('.submit__generated').removeClass("invalid");
let firstVal = $('.submit__generated').children()[0].children[0].innerHTML
let secondVal = $('.submit__generated').children()[0].children[1].innerHTML
let sum = parseInt(firstVal) + parseInt(secondVal);
$('.submit__input').val(sum);
''')

driver.find_element_by_name('checkEligibilityForm:j_idt90').click()
print(driver.current_url);
if driver.current_url == 'https://nims.nadra.gov.pk/nims/certificateVaccinationInfo':
    numberOfDoses = driver.execute_script("return $('.table.table-bordered.text-center').children()[1].children.length")
    if numberOfDoses > 1:
        print('both doses found')
    else:
        print('one dose found')
else:
    print('no doses found')
