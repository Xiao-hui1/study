from selenium import webdriver
from selenium.webdriver.edge.service import Service
import requests
import pytesseract
from PIL import Image

import time
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "_xsrf=ct67JsLVezrvGxTXSeTp7nuMzz6d9A3j; _zap=349ee25d-0369-4c32-ba27-1737f25bd000; d_c0=-vCXQe_oRxyPTvzKybBqYP3cYIWz5AX4g58=|1778642128; __zse_ck=005_YvC4Dd0Fv/D5rKd1i75Ml/FjjXCzXklJpTulDVkVrlpsuPRwnBnUQrXQ8qKRJ1dK9uWfmA2P6o4PJ7zN3iVJ=M9wJGIrb=YjO46Aqg9KF55OS9DftJGa75j4krm6voqA-qPudEfg77HTq1jSYWsKyit7kAu1t4VlCYDIJXR4AzY+0TJHG5Rh6935O+8gWKJWgCvZz5/7i39KN+5omoqPoe3ojbsXFR9L/o4LP0OfI0Axi7DpeSyAx4Xg4XcDLhrWm; __snaker__id=7i80u5zqDbwZ0hdM; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1786176363,1786534574; HMACCOUNT=747E6C262F7535FB; SESSIONID=RaZTJgAHGA5UPwAAgFVO924JKwzGJD14ctUAuW53pAv; JOID=UF4UAkoT7KGmGjUyQsFdu8PVG41dRYr78lNWdApXqZPzSkF3BL6x3c8dNjVCj2tpNOXjw1_4ohSXDNHMbIaHVl0=; osd=U18WBU0Q7aOhHTYzQMZauMLXHIpeRIj89VBXdg1QqpLxTUZ0Bby22swcNDJFjGprM-Lgwl3_pReWDtbLb4eFUVo=; DATE=1786176376976; crystal=U2FsdGVkX19pR7ARRcnSUQTym/5QmR9xzAJVdBhb3DE82M077/ckT7z7R/kXkKqsvekYkWOX7uXaIy4UvMPLYQYPgGgKePkKmT3E/VkWKw8eELF5DJ2j/cWUkRu6cmKBhmxPCJjBOJTjcTMoTEIKcQvPhgbMwOg/265kVfTkgkbWf8aY0jwn/71yiBCCOYcyDoeNNTufUVYvQHcZ/nE2muJPn9UOzoDASSkg+O+qCCFqlL9AWEB/PdZDgaPMyYG8; gdxidpyhxdE=Q%5Cj%2FGvxPkXY1ib4SowLJdICKG1NXHEaX2foUdelUak48MUf%2FHRSA8CUSg3i6Rcc18qNe9tr9hT%2F9LV87ZLKWZgalGnQK0QBT8rJ73eEWVSVa3PIQ9eYOrKn0pQkoeSG4XURSjQDW9M%5CWcHx%2B%2FpD3CK5PLrz%5C8eRlHlCu03tsMDU%2F%5CUPq%3A1786535475872; cmci9xde=U2FsdGVkX19auMyHmpRL6nXigG+DHiR/KUr7QTlvwP1wK+vPxL+mrsV53qa++YmVa2hGbk/nMV1phFBQ+lwKlA==; pmck9xge=U2FsdGVkX18yD+DCl89AFCfQxyJX6CwyZC0JwU/inn8=; assva6=U2FsdGVkX187IADVmntfmxX7oVSl1ufNSEaEyDgYENs=; assva5=U2FsdGVkX18svSAXNS+x8LtotGv8GrqpH8Wz1NMo5s6yIsiBf5VUR2I0kgU+N8yIy6oLvnBvNukxLHFmEPpU/Q==; vmce9xdq=U2FsdGVkX19kOf4uwJonOc4LLmvVR07qsN2H9PgBmUWkek6jBVgCzeb3cAC7WCxuzkb9l2T0eerfCSjZBNbDCMO2NON8SbBIB0wA5BtmQuG+N4PcRLR7xXk/9KrQYeBYhvGSQ1c1QNJMJSenbnqunyD7hpaStBjsx2s10Ditjl8=; captcha_session_v2=2|1:0|10:1786534831|18:captcha_session_v2|88:Qmx5WXkvcGtsVTJ6b0FNamh5WUFSOWxwckFGNmN4Y0xSK2dsb2Q1U1pXZXpoY3B0YmFEM2tKS1h2djJwQXdQbQ==|8d5d246fc0857bb88cb66f29a3ac1da7aa99b1eb06bc662074646ebf31320f47; o_act=login; ref_source=otherhttps://www.zhihu.com/signin; expire_in=15552000; q_c1=f5464c04b8794b25a46183e1ad898b43|1786534873000|1786534873000; z_c0=2|1:0|10:1786534875|4:z_c0|92:Mi4xNnZ4VFV3QUFBQUQ2OEpkQjZoSEhCQ0FBQkdnQWxWTjJhbHBhd0M2V1k4U1V5cWN3YnNFclh2Qmw1Vk91X215WXc=|6bb8545cfc63817bcf4fb11f6df521500a30b131b692d775109fc11ec8cd1542; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1786598303; BEC=92a0fca0e2e4d1109c446d0a990ad863; unlock_ticket=ANDQ2AMxyBgXAAAAYAJVTadafWo_I4emofuqVGnD82ED_HPzEdeGNw==",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.zhihu.com/signin?next=%2F",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Microsoft Edge\";v=\"151\", \"Chromium\";v=\"151\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

# session = requests.Session()
# html = session.get('https://www.zhihu.com/',headers=headers).content.decode('utf-8')
# print(html)
driver = webdriver.Edge()
driver.get('https://weread.qq.com/web/reader/e30323f0716ac22fe3092b2k16732dc0161679091c5aeb1')
time.sleep(10)
html = driver.page_source
print(html)

#
# image = Image.open('test.jpg')
# code = pytesseract.image_to_string(image)
# print(code)
