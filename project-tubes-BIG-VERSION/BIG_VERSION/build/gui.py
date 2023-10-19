from pathlib import Path
from tkinter import *
import requests
from time import strftime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Fungsi Bagian Kiri Kolom Atas
def listWaktu(n):
    list_waktu = []
    for i in range(len(list)):
        list_waktu.append(list[i]['dt_txt'])
    txt = list_waktu[n].split(" ")
    txtWaktu = txt[1]
    txtWaktuFix = txtWaktu[0:5]
    return txtWaktuFix


def listTemperature(n):    
    list_temp = []
    for i in range(len(list)):
        list_temp.append(round(list[i]['main']['temp'] - 273.15))
    print(f"Temperatur : {list_temp[n]} Celcius")
    txt = list_temp[n]
    txtFix = f"{txt}{chr(176)}C"
    return txtFix

def listWeatherIcon(n):
    list_weather_icon = []
    for i in range(len(list)):
        list_weather_icon.append(list[i]['weather'][0]['icon'])
    cuacatxt = list_weather_icon[n]
    return cuacatxt
    #print(list_weather_icon[n])

def kolomatasF():
    canvas.itemconfig(kolomataske1Waktu, text=listWaktu(2))
    canvas.itemconfig(kolomataske1Temp, text=listTemperature(2))
    canvas.itemconfig(kolomataske2Waktu, text=listWaktu(3))
    canvas.itemconfig(kolomataske2Temp, text=listTemperature(3))
    canvas.itemconfig(kolomataske3Waktu, text=listWaktu(4))
    canvas.itemconfig(kolomataske3Temp, text=listTemperature(4))
    canvas.itemconfig(kolomataske4Waktu, text=listWaktu(5))
    canvas.itemconfig(kolomataske4Temp, text=listTemperature(5))
    canvas.itemconfig(kolomataske5Waktu, text=listWaktu(6))
    canvas.itemconfig(kolomataske5Temp, text=listTemperature(6))

def kolomatasF2():
    canvas.itemconfig(kolomataske1Waktu, text=" ")
    canvas.itemconfig(kolomataske1Temp, text=" ")
    canvas.itemconfig(kolomataske2Waktu, text=" ")
    canvas.itemconfig(kolomataske2Temp, text=" ")
    canvas.itemconfig(kolomataske3Waktu, text=" ")
    canvas.itemconfig(kolomataske3Temp, text=" ")
    canvas.itemconfig(kolomataske4Waktu, text=" ")
    canvas.itemconfig(kolomataske4Temp, text=" ")
    canvas.itemconfig(kolomataske5Waktu, text=" ")
    canvas.itemconfig(kolomataske5Temp, text=" ")
    canvas.itemconfig(kolombawahke5Temp, text=" ")

def kolombawahF():
    canvas.itemconfig(kolombawahke1Temp, text=listTemperature(7))
    canvas.itemconfig(kolombawahke2Temp, text=listTemperature(14))
    canvas.itemconfig(kolombawahke3Temp, text=listTemperature(21))
    canvas.itemconfig(kolombawahke4Temp, text=listTemperature(28))
    canvas.itemconfig(kolombawahke5Temp, text=listTemperature(35))
    
    

def kolombawahF2():
    canvas.itemconfig(kolombawahke1Temp, text=" ")
    canvas.itemconfig(kolombawahke2Temp, text=" ")
    canvas.itemconfig(kolombawahke3Temp, text=" ")
    canvas.itemconfig(kolombawahke4Temp, text=" ")
    canvas.itemconfig(kolombawahke5Temp, text=" ")


def on_change_text():
    canvas.itemconfig(cuaca_sekarang, text=(f"{weather}"))
    canvas.itemconfig(temperatur_sekarang, text=(f"{temperature}",chr(176),"C"))
    canvas.itemconfig(tekanan_sekarang, text=(f"{pressure} Pa"))
    canvas.itemconfig(kelembaban_sekarang, text=(f"{humidity}","%"))

def on_change_text2():
    canvas.itemconfig(cuaca_sekarang, text=" ")
    canvas.itemconfig(temperatur_sekarang, text=" ")
    canvas.itemconfig(tekanan_sekarang, text=" ")
    canvas.itemconfig(kelembaban_sekarang, text=" ")

def hpusMarkError():
    canvas.itemconfig(itk, text=" ")
    canvas.itemconfig(copyright, text=" ")
    canvas.itemconfig(notfound0, text =" ")
    canvas.itemconfig(notfound1, text=" ")
    canvas.itemconfig(notfound2, text=" ")
    canvas.itemconfig(notfound3, text=" " )




API_KEY = "d485793245775bad0112e296db963d3a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
BASE_URL2 = "http://api.openweathermap.org/data/2.5/forecast"


# fungsi tombol search
def mintaReq():
    global request_url,response,weather,weatherIcon,temperature,pressure,humidity,cuaca_sekarang, temperatur_sekarang, tekanan_sekarang,kelembaban_sekarang,image_27,copyright,itk,notfound0,notfound1,notfound2,notfound3,kolomataske5Waktu,kolomataske5Temp,kolomataske4Waktu,kolomataske3Temp,kolomataske3Waktu,kolomataske2Waktu,kolomataske1Waktu,kolomataske2Temp,kolomataske1Temp,list,kolomataske4Temp,kolombawahke5Temp,kolombawahke4Temp, kolombawahke3Temp,kolombawahke2Temp,kolombawahke1Temp
    try:
        hpusMarkError()
    except NameError:
        print("Baru Mulai Programnya Gan")
    try:
        on_change_text2()
    except NameError:
        print("Engine Startttt!!!!")

    try:
        canvas.delete(image_27)
    except:
        print("Nanti Pasang Kalau salah")

# TRY UNTUK YANG KOLOM KIRI ATAS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    try:
        canvas.delete(image_image_6)
    except:
        print("Hapus Icon Kolom atas kiri")
    try:
        canvas.delete(image_6)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try:
        canvas.delete(image_image_5)
    except:
        print("Hapus Icon Kolom atas kiri")
    try:
        canvas.delete(image_5)
    except:
        print("Hapus Icon Kolom Atas Kiri")

    try:
        canvas.delete(image_image_3)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_3)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try:
        canvas.delete(image_image_4)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_4)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try:
        canvas.delete(image_image_2)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_2)
    except:
        print("Nanti Pasang Kalau Dimulai")


    try :
        kolomatasF2()
    except:
        print("Program Mulai")

# TRY UNTUK YANG KOLOM KIRI BAWAH
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    try:
        canvas.delete(image_image_8)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_8)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try:
        canvas.delete(image_image_9)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_9)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try:
        canvas.delete(image_image_10)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_10)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try:
        canvas.delete(image_image_11)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_11)
    except:
        print("Nanti Pasang Kalau Dimulai")
    
    try:
        canvas.delete(image_image_12)
    except:
        print("Nanti Pasang Kalau Dimulai")
    try:
        canvas.delete(image_12)
    except:
        print("Nanti Pasang Kalau Dimulai")

    try :
        kolombawahF2()
    except:
        print("Program Mulai")

    print(f"{inputKota()}")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={inputKota()}&lang=en"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].title()
        weatherIcon = data['weather'][0]['icon']
        temperature = round(data["main"]["temp"] - 273.15, 1)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        lon = data['coord']['lon'] #longitude
        lat = data['coord']['lat'] #latitude
        print(lat, lon)
        # bagian cuaca saat ini

        request_url2 = f"{BASE_URL2}?lat={lat}&lon={lon}&appid={API_KEY}&lang=id"
        respon = requests.get(request_url2)
        data2 = respon.json()
        list = data2['list']

        #cuaca hari ini
        cuaca_sekarang = canvas.create_text(
        668,
        133,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 19 * -1)
        )

    #temperatur hari ini
        temperatur_sekarang = canvas.create_text(
        668,
        205,
        anchor="nw",
        fill="#FFFFFF",
        text=" ",
        font=("Questrial Regular", 19 * -1)
        )

    #tekanan hari ini
        tekanan_sekarang = canvas.create_text(
        668,
        287,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 19 * -1)
        )

    #kelembaban hari ini

        kelembaban_sekarang = canvas.create_text(
        668,
        364,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 19 * -1)
        )
        on_change_text()
        #Paling 1 Kiri Kolom Atas
##########################################################
#########################################################
        kolomataske1Waktu = canvas.create_text(
        51,
        75,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("JostRoman Regular", 25 * -1)
    )

        def iconKiriAtas1():
            global image_image_2
            global image_2
            if (listWeatherIcon(2) == "01d"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "01n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "02d"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "02n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "03d" or listWeatherIcon(2) == "03n" or listWeatherIcon(2) == "04d" or listWeatherIcon(2) == "04n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )


            elif (listWeatherIcon(2) == "09d" or listWeatherIcon(2) == "09n" or listWeatherIcon(2) == "10d" or listWeatherIcon(2) == "10n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "11d" or listWeatherIcon(2) == "11n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "13d" or listWeatherIcon(2) == "13n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

            elif (listWeatherIcon(2) == "50d" or listWeatherIcon(2) == "50n"):
                image_image_2= PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_2 = canvas.create_image(
                    78,
                    140,
                    image=image_image_2
                )

        iconKiriAtas1()
        kolomataske1Temp = canvas.create_text(
        82,
        192,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
    )
        #Paling 2 Kiri Kolom Atas
##########################################################
#########################################################
        kolomataske2Waktu = canvas.create_text(
        158,
        75,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("JostRoman Regular", 25 * -1)
    )
        def iconKiriAtas2():
            global image_image_4
            global image_4
            if (listWeatherIcon(3) == "01d"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "01n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "02d"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "02n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "03d" or listWeatherIcon(3) == "03n" or listWeatherIcon(3) == "04d" or listWeatherIcon(3) == "04n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )


            elif (listWeatherIcon(3) == "09d" or listWeatherIcon(3) == "09n" or listWeatherIcon(3) == "10d" or listWeatherIcon(3) == "10n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "11d" or listWeatherIcon(3) == "11n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "13d" or listWeatherIcon(3) == "13n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )

            elif (listWeatherIcon(3) == "50d" or listWeatherIcon(3) == "50n"):
                image_image_4= PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_4 = canvas.create_image(
                    189,
                    140,
                    image=image_image_4
                )
        iconKiriAtas2()

        kolomataske2Temp = canvas.create_text(
        192,
        192,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
    )


        #Bagian Kiri 3 Kolom Atas
##########################################################
#########################################################
        
        kolomataske3Waktu = canvas.create_text(
        262,
        75,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("JostRoman Regular", 25 * -1)
    )
        
        def iconKiriAtas3():
            global image_image_3
            global image_3
            if (listWeatherIcon(4) == "01d"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "01n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "02d"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "02n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "03d" or listWeatherIcon(4) == "03n" or listWeatherIcon(4) == "04d" or listWeatherIcon(4) == "04n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )


            elif (listWeatherIcon(4) == "09d" or listWeatherIcon(4) == "09n" or listWeatherIcon(4) == "10d" or listWeatherIcon(4) == "10n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "11d" or listWeatherIcon(4) == "11n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "13d" or listWeatherIcon(4) == "13n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )

            elif (listWeatherIcon(4) == "50d" or listWeatherIcon(4) == "50n"):
                image_image_3= PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_3 = canvas.create_image(
                    293,
                    141,
                    image=image_image_3
                )
        iconKiriAtas3()
        kolomataske3Temp = canvas.create_text(
            296,
            192,
            anchor="center",
            text=" ",
            fill="#FFFFFF",
            font=("Questrial Regular", 27 * -1)
        )

        #Bagian Kiri 4 Kolom Atas
##########################################################
#########################################################
        kolomataske4Waktu = canvas.create_text(
        369,
        75,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("JostRoman Regular", 25 * -1)
    )

        def iconKiriAtas4():
            global image_image_5
            global image_5
            if (listWeatherIcon(5) == "01d"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "01n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "02d"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "02n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "03d" or listWeatherIcon(5) == "03n" or listWeatherIcon(5) == "04d" or listWeatherIcon(5) == "04n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "09d" or listWeatherIcon(5) == "09n" or listWeatherIcon(5) == "10d" or listWeatherIcon(5) == "10n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "11d" or listWeatherIcon(5) == "11n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "13d" or listWeatherIcon(5) == "13n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )

            elif (listWeatherIcon(5) == "50d" or listWeatherIcon(5) == "50n"):
                image_image_5 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_5 = canvas.create_image(
                    400,
                    139,
                    image=image_image_5
                )
        iconKiriAtas4()

        kolomataske4Temp = canvas.create_text(
        400,
        192,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
    )

        #Bagian Kiri 5 Kolom Atas
##########################################################
#########################################################
        kolomataske5Waktu = canvas.create_text(
        468,
        75,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("JostRoman Regular", 25 * -1)
        )
        
        def iconKiriAtas5():
            global image_image_6
            global image_6
            if (listWeatherIcon(6) == "01d"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "01n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "02d"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "02n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "03d" or listWeatherIcon(6) == "03n" or listWeatherIcon(6) == "04d" or listWeatherIcon(6) == "04n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "09d" or listWeatherIcon(6) == "09n" or listWeatherIcon(6) == "10d" or listWeatherIcon(6) == "10n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "11d" or listWeatherIcon(6) == "11n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "13d" or listWeatherIcon(6) == "13n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )

            elif (listWeatherIcon(6) == "50d" or listWeatherIcon(6) == "50n"):
                image_image_6 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_6 = canvas.create_image(
                    497,
                    139,
                    image=image_image_6
                )
        iconKiriAtas5()

        kolomataske5Temp = canvas.create_text(
        500,
        192,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
        )
        kolomatasF()
#Bagian Kiri 1 Bawah
##########################################################
#########################################################
        def iconKiriBawah1():
            global image_image_8
            global image_8
            if (listWeatherIcon(7) == "01d"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "01n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "02d"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "02n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "03d" or listWeatherIcon(7) == "03n" or listWeatherIcon(7) == "04d" or listWeatherIcon(7) == "04n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "09d" or listWeatherIcon(7) == "09n" or listWeatherIcon(7) == "10d" or listWeatherIcon(7) == "10n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "11d" or listWeatherIcon(7) == "11n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "13d" or listWeatherIcon(7) == "13n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )

            elif (listWeatherIcon(7) == "50d" or listWeatherIcon(7) == "50n"):
                image_image_8 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_8 = canvas.create_image(
                    74,
                    328,
                    image=image_image_8
                )
        iconKiriBawah1()

        kolombawahke1Temp = canvas.create_text(
        76,
        382,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
    )
#Bagian Kiri 2 Bawah
##########################################################
#########################################################

        def iconKiriBawah2():
            global image_image_9
            global image_9
            if (listWeatherIcon(14) == "01d"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "01n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "02d"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "02n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "03d" or listWeatherIcon(14) == "03n" or listWeatherIcon(14) == "04d" or listWeatherIcon(14) == "04n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "09d" or listWeatherIcon(14) == "09n" or listWeatherIcon(14) == "10d" or listWeatherIcon(14) == "10n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "11d" or listWeatherIcon(14) == "11n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "13d" or listWeatherIcon(14) == "13n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )

            elif (listWeatherIcon(14) == "50d" or listWeatherIcon(14) == "50n"):
                image_image_9 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_9 = canvas.create_image(
                    185,
                    328,
                    image=image_image_9
                )
        iconKiriBawah2()

        kolombawahke2Temp = canvas.create_text(
            186,
            382,
            anchor="center",
            text=" ",
            fill="#FFFFFF",
            font=("Questrial Regular", 27 * -1)
        )

#Bagian Kiri 3 Bawah
##########################################################
#########################################################

        def iconKiriBawah3():
            global image_image_11
            global image_11
            if (listWeatherIcon(21) == "01d"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "01n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "02d"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "02n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "03d" or listWeatherIcon(21) == "03n" or listWeatherIcon(21) == "04d" or listWeatherIcon(21) == "04n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "09d" or listWeatherIcon(21) == "09n" or listWeatherIcon(21) == "10d" or listWeatherIcon(21) == "10n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "11d" or listWeatherIcon(21) == "11n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "13d" or listWeatherIcon(21) == "13n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )

            elif (listWeatherIcon(21) == "50d" or listWeatherIcon(21) == "50n"):
                image_image_11 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_11 = canvas.create_image(
                    292,
                    328,
                    image=image_image_11
                )
        iconKiriBawah3()

        kolombawahke3Temp = canvas.create_text(
        295,
        382,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
    )
#Bagian Kiri 4 Bawah
##########################################################
#########################################################

        def iconKiriBawah4():
            global image_image_10
            global image_10
            if (listWeatherIcon(28) == "01d"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "01n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "02d"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "02n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "03d" or listWeatherIcon(28) == "03n" or listWeatherIcon(28) == "04d" or listWeatherIcon(28) == "04n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "09d" or listWeatherIcon(28) == "09n" or listWeatherIcon(28) == "10d" or listWeatherIcon(28) == "10n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "11d" or listWeatherIcon(28) == "11n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "13d" or listWeatherIcon(28) == "13n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )

            elif (listWeatherIcon(28) == "50d" or listWeatherIcon(28) == "50n"):
                image_image_10 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_10 = canvas.create_image(
                    396,
                    328,
                    image=image_image_10
                )
        iconKiriBawah4()
        kolombawahke4Temp = canvas.create_text(
        396,
        382,
        anchor="center",
        text=" ",
        fill="#FFFFFF",
        font=("Questrial Regular", 27 * -1)
    )

#Bagian Kiri 5 Bawah
##########################################################
#########################################################

        def iconKiriBawah5():
            global image_image_12
            global image_12
            if (listWeatherIcon(35) == "01d"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Cerah_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "01n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Bulan_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "02d"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("CerahBerawan_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "02n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("BerawanMalam_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "03d" or listWeatherIcon(35) == "03n" or listWeatherIcon(35) == "04d" or listWeatherIcon(35) == "04n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Berawan_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "09d" or listWeatherIcon(35) == "09n" or listWeatherIcon(35) == "10d" or listWeatherIcon(35) == "10n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Hujan_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "11d" or listWeatherIcon(35) == "11n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Berpetir_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "13d" or listWeatherIcon(35) == "13n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Salju_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )

            elif (listWeatherIcon(35) == "50d" or listWeatherIcon(35) == "50n"):
                image_image_12 = PhotoImage(
                    file=relative_to_assets("Berangin_Putih.png"))
                image_12 = canvas.create_image(
                    493,
                    328,
                    image=image_image_12
                )
        iconKiriBawah5()

        kolombawahke5Temp = canvas.create_text(
            495,
            382,
            anchor="center",
            text=" ",
            fill="#FFFFFF",
            font=("Questrial Regular", 27 * -1)
        )
        kolombawahF()
##########################################################
#########################################################
        def iconUtama():
            global image_image_16
            global image_16
            if (weatherIcon == "01d"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("cerah_banget.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "01n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("bulan.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "02d"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("cerah_berawan.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "02n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("BerawanMalam.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "03d" or weatherIcon == "03n" or weatherIcon == "04d" or weatherIcon == "04n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("mendung.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )


            elif (weatherIcon == "09d" or weatherIcon == "09n" or weatherIcon == "10d" or weatherIcon == "10n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("image_16.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "11d" or weatherIcon == "11n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("bepetir.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "13d" or weatherIcon == "13n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("salju.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )

            elif (weatherIcon == "50d" or weatherIcon == "50n"):
                image_image_16 = PhotoImage(
                    file=relative_to_assets("berangin.png"))
                image_16 = canvas.create_image(
                    629,
                    134,
                    image=image_image_16
                )
        iconUtama()
        #hpusMarkError()

        print("Wheather Icon Right Now : ", weatherIcon)
    if response.status_code == 404:
        print(f"Kota tidak ditemukan")
        image_27 = canvas.create_image(
            729.0,
            214.0,
            image=image_image_27
        )
        itk = canvas.create_text(
        637,
        404,
        anchor="nw",
        text="Institute of Technology Kalimantan, Indonesia",
        fill="#FFFFFF",
        font=("Questrial Regular", 9 * -1)
        )

        copyright = canvas.create_text(
        668,
        417,
        anchor="nw",
        text="©Copyright all rights reserved",
        fill="#FFFFFF",
        font=("Questrial Regular", 9 * -1)
        )

        notfound0 =canvas.create_text(
            733,
            292,
            anchor="center",
            text="Check your",
            fill="#FFFFFF",
            font=("Montserrat", 20 * -1)
        )

        notfound1 =canvas.create_text(
            733,
            310,
            anchor="center",
            text="typing or try again.",
            fill="#FFFFFF",
            font=("Montserrat", 20 * -1)
        )

        notfound2 =canvas.create_text(
            733,
            151,
            #ini center biar relatif sesuai panjang nama kota nya perataannya
            anchor="center",
            text=f"{inputKota()}",
            fill="#FFFFFF",
            font=("Open Sans Extrabold", 20 * -1)
        )

        notfound3 = canvas.create_text(
            733,
            173,
            anchor="center",
            text= "has not found",
            fill="#FFFFFF",
            font=("Montserrat", 20 * -1)
        )


window = Tk()

window.geometry("890x435")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 442,
    width = 890,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    287,
    124,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = None


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = None

image_image_oren = PhotoImage(
    file=relative_to_assets("orenoren.png"))
image_oren = canvas.create_image(
    120,
    226,
    image=image_image_oren
)


image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = None


image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = None

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = None


image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    287,
    345,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = None

canvas.create_text(
    51,
    264,
    anchor="nw",
    text="Sun",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    162.2840576171875,
    264.779296875,
    anchor="nw",
    text="Mon",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    268.19580078125,
    264.779296875,
    anchor="nw",
    text="Tue",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    367.27447509765625,
    264.779296875,
    anchor="nw",
    text="Wed",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

canvas.create_text(
    466.3531799316406,
    264.779296875,
    anchor="nw",
    text="Thur",
    fill="#FFFFFF",
    font=("JostRoman Regular", 30 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = None

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = None


image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = None


image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = None

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    768.7140197753906,
    30.74854278564453,
    image=entry_image_1
)

def inputKota():
    input_kota = var.get()
    return input_kota

def temp_text(e):
   entry_1.delete(0,"end")

var = StringVar()

entry_1 = Entry(
    bd=0,
    bg="#9CBCD0",
    justify="left",
    font=("Questrial", 27 * -1),
    highlightthickness=0,
    textvariable = var
)

entry_1.insert(0, "TYPE YOUR CITY")
entry_1.bind("<FocusIn>", temp_text)

def autoupper(*arg):
    var.set(var.get().upper())

var.trace("w", autoupper)

entry_1.place(
    x=648,
    y=18,
    width=228.90594482421875,
    height=29
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mintaReq(),
    relief="flat"
)
button_1.place(
    x=583,
    y=9,
    width=42,
    height=40,
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    732.681396484375,
    221.0,
    image=image_image_13
)


canvas.create_text(
    71.74665832519531,
    0.0,
    anchor="nw",
    text="WEATHER FORECAST",
    fill="#FF6700",
    font=("Open Sans Bold", 42 * -1)
)


canvas.create_text(
    669.2031860351562,
    182.75608825683594,
    anchor="nw",
    text="TEMPERATURE",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

canvas.create_text(
    669.2031860351562,
    260.02398681640625,
    anchor="nw",
    text="AIR PRESSURE",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    630.2061157226562,
    287.6001281738281,
    image=image_image_14
)

canvas.create_text(
    668.7307739257812,
    107.54867553710938,
    anchor="nw",
    text="WEATHER NOW",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

canvas.create_text(
    669.2031860351562,
    338,
    anchor="nw",
    text="HUMIDITY",
    fill="#FF6700",
    font=("JostRoman Regular", 19 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    630.2569580078125,
    355.6671142578125,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    629.358642578125,
    134.6696319580078,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    629.053466796875,
    209.7366180419922,
    image=image_image_17
)

def hapusWaktu():
    canvas.itemconfig(mesinWaktu, text=" ")
def addWaktu():
    canvas.itemconfig(mesinWaktu, text= string)

def time():
    global mesinWaktu,string
    try :
        hapusWaktu()
    except :
        print("Mesin Waktu Dimulai")

    string = strftime('%A, %D  %r')
    mesinWaktu = canvas.create_text(730, 75, text= string, font=("Open Sans Regular", 16 * -1), fill="#FFFFFF", anchor="center")
    canvas.after(1000, time)
    addWaktu()
time()

canvas.create_text(
    668.5232543945312,
    417.3939514160156,
    anchor="nw",
    text="©Copyright all rights reserved",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

canvas.create_text(
    637.1785888671875,
    404.8560485839844,
    anchor="nw",
    text="Institute of Technology Kalimantan, Indonesia",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

canvas.create_text(
    668.5232543945312,
    417.3939514160156,
    anchor="nw",
    text="©Copyright all rights reserved",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

canvas.create_text(
    637.1785888671875,
    404.8560485839844,
    anchor="nw",
    text="Institute of Technology Kalimantan, Indonesia",
    fill="#FFFFFF",
    font=("Questrial Regular", 9 * -1)
)

image_image_oren2 = PhotoImage(
    file=relative_to_assets("orenoren.png"))
image_oren2 = canvas.create_image(
    120,
    420,
    image=image_image_oren2
)


canvas.create_text(
    25,
    214,
    anchor="nw",
    text="WEATHER TODAY",
    fill="#FFFFFF",
    font=("Open Sans Bold", 18 * -1)
)

canvas.create_text(
    25,
    409,
    anchor="nw",
    text="THE NEXT FEW DAYS",
    fill="#FFFFFF",
    font=("Open Sans Bold", 18 * -1)
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))

window.resizable(False, False)
window.mainloop()
