import os, sys, string
try:
    import random, warnings
    import time, requests
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from colorama import Back, Fore
    from os import path
except:
    os.system('pip uninstall -r requirements.txt -y')
    os.system('pip install -r requirements.txt')
    os.system('cls')
    import random, warnings
    import time, requests
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from colorama import Back, Fore
    from os import path

print(f'''
▀█▀ █▀█ █▄▀ █▀▀ █▄░█   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
░█░ █▄█ █░█ ██▄ █░▀█   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄   Made By Leluka11

''')
print("Please note that sometimes the hCaptcha solver may need to have the 'auto open' feature enabled.")
print("To fix this issue, click on the extension, and click 'auto open'.")
print(' ')


warnings.filterwarnings("ignore", category=DeprecationWarning) 

file = open("users.txt", "a")
file1 = open("tokens.txt", "a")

if path.exists('solver.crx'):
    pass
else:
    print(f'{Back.RED}  ERROR!  {Back.RESET} Solver Extension Not Downloaded! Download at: {Fore.LIGHTGREEN_EX}https://drive.google.com/file/d/1EFnjfkfzkDXshRSG9KdjIARwoH0J-EpW/view?usp=sharing{Fore.RESET} , then put in this directory!')
    quit()


def start():
    def get_random_email(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(result_str + '@wp2.pl')
        file.write("\n email: " + result_str +"@wp2.pl\n")
        


    def get_random_username(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(result_str)
        file.write("username: " + result_str + "\n")


    def get_random_password(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("!" + result_str)
        file.write("password: " + "!" + result_str)
        


    def get_date():
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[1]").click()
        driver.find_element(By.ID, "react-select-2-option-0").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[2]/div/div/div/div/div[1]/div[1]").click()
        driver.find_element(By.ID, "react-select-3-option-0").click()
        
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[3]/div/div/div/div/div[1]").click()
        driver.find_element(By.ID, "react-select-4-option-17").click()


    def get_checkbox():
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/label/input").click()


    def get_button():
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def quit():
        driver.quit()




    option = webdriver.ChromeOptions()
    option.add_argument("--mute-audio")
    option.add_extension(os.getcwd() + '\solver.crx')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1")



    driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
    driver.get('https://discord.com/register')

    time.sleep(2)
    print(f'{Back.GREEN}  INFO  {Back.RESET} Generating Token.')
    get_random_email(8)
    get_random_username(8)
    get_random_password(8)
    get_date()
    get_checkbox()
    get_button()

    token = None
    while token is None:
        token = driver.execute_script("""return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()""")
        if token is None:
            pass
        else:
            print(f'{Back.GREEN}  INFO  {Back.RESET} Token Generated! {token}')
            with open('tokens.txt', 'w') as tokens:
                tokens.write('\n')
                tokens.write(token)
                tokens.close()




amount = int(input('How Many Tokens Would you like to generate: '))

for run in range(amount):
    start()