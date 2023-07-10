# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:07:43 2022

@author: bbaysal
"""

import streamlit as st
import pickle
import pandas as pd

df = pd.DataFrame(columns=['OPERASYON SAYISI','KAMLI DELİK','ZORLUK KATSAYISI','TOPLAM AĞIRLIK',
                    'KALIP TİPİ_0','KALIP TİPİ_1','KALIP TİPİ_2','KALIP TİPİ_3'])

df = df.astype({"OPERASYON SAYISI": int, "KAMLI DELİK": int , 'ZORLUK KATSAYISI':int,
                'TOPLAM AĞIRLIK':int,
                'KALIP TİPİ_0':int,'KALIP TİPİ_1':int,'KALIP TİPİ_2':int,'KALIP TİPİ_3':int})


multiple = 0


from PIL import Image

#opening the image
image = Image.open('coskunoz_metalform.png')

#displaying the image on streamlit app
st.image(image, use_column_width=True)



##93a1a1


st.markdown(
      """
       <style>
     .main {
     background-color:#93a1a1;
    text-align: center;
    font-size: 16px;
     }

     .reportview-container .block-container{
        max-width: 3000px;
        padding-top: 1rem;
        padding-bottom: 3rem;

    }
    .navbar {
    background-color: #333333;
    font-size: 16px;
    color: white
    }

    .result {
    font-size: 20px;
    font-weight: bold;
    }
    footer {
    
    visibility: hidden;
    
    }
    footer:after {
        content:'CMF IT © 2022'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 6px;
        top: 8px;
    }

    </style>
      """, 
    unsafe_allow_html=True
               
)


# ['OPERASYON SAYISI', 'KAMLI DELİK', 'ZORLUK KATSAYISI', 'TOPLAM AĞIRLIK', 'KALIP TİPİ_0', 'KALIP TİPİ_1', 'KALIP TİPİ_2',
#       'KALIP TİPİ_3', 'OEM_0', 'OEM_1', 'OEM_2', 'OEM_3']

siteHeader  = st.container()
footer         = st.container()

with siteHeader:


    st.markdown('<p class="navbar">Dijitalleşme ve IT Projeler </p>', unsafe_allow_html=True)
    
    st.markdown('<p class="navbar">Yapay Zeka ile Kalıp Maliyetlerinin Öngörülmesi </p>', unsafe_allow_html=True)

    with st.form(key='columns_in_form'):

        ######################################## MAIN INPUTS ########################################
        
        
        #FIRMA_ADI            = st.selectbox('Firma Adı', ("FORD","PSA","RENAULT","TOGG"))            # FIRMA ADI ONE HOT ENCODING YAPILACAK
        
        
        
        KALIP_TIPI          = st.selectbox('Kalıp Tipi',("POSTALI","PROGRASİF","TANDEM","TRANSFER"))  # KALIP TIPI DROPDOWN
        
        OPERASYON_SAYISI  = st.number_input('Operasyon/Adım Sayısı', min_value=0, value=0)                 # OPERASYON SAYISI MİN VALUE = 0 MAX = limitless

        KAMLI_DELIK       = st.number_input('Kam Sayısı', min_value=0, value=0)                     # KAMLI DELİK, MİN VALUE =  0, MAX = limitless

        ZORLUK_KATSAYISI  = st.number_input('Zorluk Katsayısı', min_value=0, max_value=5, value=0)    # ZORLUK KATSAYISI, MİN VALUE =  0, MAX = 5

        BIRIM_FIYAT          = st.number_input('Birim Fiyat (FGL215 €)')                # MODELDE YOK SADECE SONUCTA GÖSTER
        
       # KALIP_TIPI          = st.selectbox('Kalıp Tipi',("POSTALI","PROGRASİF","TANDEM","TRANSFER"))  # KALIP TIPI DROPDOWN

        st.write("""
                Yaptırılan Kalıp Adedini Giriniz!
                """)
                
                
        st.write("""

                Kalıp Ekle'ye Basarak Yaptırılan Her Kalıbın YÜKSEKLİK, EN ve BOY Bilgilerini Giriniz!               
                """)
                
        st.write("""
                Request Data'ya Basarak Verilerinizin Doğruluğunu Kontrol Ediniz!
                
                """)






        column1, column2    = st.columns(2)

        kalip_sayisi            = column1.number_input('Yaptırılan Kalıp Adedini Giriniz:',min_value = 0)                    # ARRAY OLUSTURULACAK
        KALIP_EKLE              = st.form_submit_button('Kalıp Ekle')                                # KALIP EKLE BUTTON

        ######################################## MAIN INPUTS ########################################
        
        

        kalip_agirligi = 0
        for i in range(int(kalip_sayisi)):
            [col1, col2, col3] = st.columns(3)
            
            h = col1.number_input("h (Yükseklik mm){}".format(i))
            
            w = col2.number_input("w (En mm){}".format(i))
            
            l = col3.number_input("l (Boy mm){}".format(i))
            
            kalip_agirligi += 0.55*7.85*h*l*w/1000000000
                
     
   
    
        request_datas= st.form_submit_button("request data")    
                                
                                
                                
                                
        
        if request_datas : 
            
            st.write(KALIP_TIPI)
            st.write(OPERASYON_SAYISI)
            st.write(KAMLI_DELIK)
           # st.write(FIRMA_ADI)
            st.write(BIRIM_FIYAT)
            st.write(kalip_agirligi)
            


        submitted           = st.form_submit_button('HESAPLA')
        
        if str(KALIP_TIPI) == "POSTALI":
            kalip_postali,kalip_prograsif,kalip_tandem,kalip_transfer = [1,0,0,0]
        elif str(KALIP_TIPI) == "PROGRASİF":
            kalip_postali,kalip_prograsif,kalip_tandem,kalip_transfer = [0,1,0,0]         
        elif str(KALIP_TIPI) == "TANDEM":
            kalip_postali,kalip_prograsif,kalip_tandem,kalip_transfer = [0,0,1,0]            
        else:
            kalip_postali,kalip_prograsif,kalip_tandem,kalip_transfer = [0,0,0,1]
            
        
       # if str(FIRMA_ADI) == "FORD":
       #     firma_ford , firma_psa , firma_renault , firma_togg = [1,0,0,0]
       # elif str(FIRMA_ADI) == "PSA":
       #     firma_ford , firma_psa , firma_renault , firma_togg = [0,1,0,0]
       # elif str(FIRMA_ADI) == "RENAULT":                                       #reanult yazıldığı için else düşüyor o yüzden fiyatlar tog ile aynı geliyor
       #     firma_ford , firma_psa , firma_renault , firma_togg = [0,0,1,0]
       # else:
       #     firma_ford , firma_psa , firma_renault , firma_togg = [0,0,0,1]
        

   # print(OPERASYON_SAYISI,KAMLI_DELIK,ZORLUK_KATSAYISI,kalip_agirligi,
   #      kalip_postali,kalip_prograsif,kalip_tandem,kalip_transfer,
   #      firma_ford,firma_psa,firma_renault,firma_togg)
   #print(type(OPERASYON_SAYISI),type(KAMLI_DELIK),type(ZORLUK_KATSAYISI),type(kalip_agirligi),
   #      type(kalip_postali),type(kalip_prograsif),type(kalip_tandem),type(kalip_transfer),
   #      type(firma_ford),type(firma_psa),type(firma_renault),type(firma_togg))
    
    
    
    df2 = df.append({'OPERASYON SAYISI' : int(OPERASYON_SAYISI), 'KAMLI DELİK' : int(KAMLI_DELIK),
                     'ZORLUK KATSAYISI' :int(ZORLUK_KATSAYISI), 'TOPLAM AĞIRLIK' : float(kalip_agirligi),'KALIP TİPİ_0' :int(kalip_postali) ,
                     'KALIP TİPİ_1' : int(kalip_prograsif), 'KALIP TİPİ_2' : int(kalip_tandem), 'KALIP TİPİ_3' : int(kalip_transfer)}, ignore_index = True)
    
    

   
    
   
    model_xgb = pickle.load(open("XGB.pkl", 'rb'))
    #model_cat = pickle.load(open("CAT.pkl", 'rb'))

    @st.cache
    def ValuePredictor(to_predict_list):
        #to_predict = np.array(to_predict_list).reshape(1,len(to_predict_list))
        result_xgb = model_xgb.predict(to_predict_list)
        #result_cat = model_cat.predict(to_predict_list)
        return (result_xgb)
    

    if submitted:
        result = ValuePredictor(df2)*float(BIRIM_FIYAT)
        st.markdown('<p class="navbar"> Öngörülen Kalıp Maliyeti (€) </p>', unsafe_allow_html=True)
        st.write(result[0])
        print(result)



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}

            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)       
        
        



    


