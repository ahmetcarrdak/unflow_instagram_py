from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from users import usernames

# Chrome tarayıcı ayarları (opsiyonel)
chrome_options = webdriver.ChromeOptions()

# WebDriverManager ile ChromeDriver'ı indir ve kullan
service = Service(ChromeDriverManager().install())

# WebDriver'ı başlat
driver = webdriver.Chrome(service=service, options=chrome_options)

# Instagram giriş sayfasını aç
driver.get("https://www.instagram.com/accounts/login/")

# Giriş formu yüklenene kadar bekle
sleep(3)

# Instagram'a giriş yap
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys("")  # Buraya kendi kullanıcı adını yaz
password_input.send_keys("")  # Buraya kendi şifreni yaz

password_input.send_keys(Keys.RETURN)

# Giriş yaptıktan sonra sayfanın yüklenmesi için bekleme süresi
sleep(5)

# İki faktörlü kimlik doğrulama bekleme
input("İki faktörlü doğrulama kodunu girin ve Enter'a basın...")

# Takip isteği geri çekilecek kullanıcı adlarından oluşan array
#usernames = ['celinegzl', 'ez0gelin', 'berfdilan']  # Buraya kullanıcı adlarını ekleyin

for username in usernames:
    # Kullanıcı sayfasına git
    driver.get(f"https://www.instagram.com/{username}/")
    sleep(3)  # Sayfanın yüklenmesini bekle

    try:
        # Takip etme durumunu kontrol et ve butona tıkla
        follow_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acat')]"))
        )
        follow_button.click()

        # Onay butonuna tıkla (Unfollow)
        unfollow_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Takibi Bırak')]"))
        )
        unfollow_button.click()

        print(f"{username} için takip isteği geri çekildi.")
    except Exception as e:
        print(f"{username} için takip isteği geri çekilemedi veya zaten takip edilmiyor. Hata: {e}")

    # Bir sonraki kullanıcıya geçmeden önce bekle
    sleep(2)

# Tüm işlemler bittikten sonra tarayıcıyı kapat
driver.quit()