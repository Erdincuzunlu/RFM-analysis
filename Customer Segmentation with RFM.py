### Business problem
### Data understanding
### Data Preparation
### Calculating RFM Metrics
### Calculating RFM scores
### Creating analysing And RFM Segments



##### 1 . Business Problem...

### Bir e-Ticaret şirketi müşterinlerini segmentlere ayırıp
### Pazarlama stratejilerini istiyor..

### Veri Seti hikayesi

### online Retail ll isimli veri seti ingiltere merkezli online satış mağazasının
### 01/12/2009 - 09/ 12 / 2011 Tarihleri arsaında ki satışları içeriyor

### Değişkenler

## İnvoice NO :
## StockCode :
## Description :
## Quantity :
## InvoiceDate :
## unit Price :
### Costumer ID :
## Country :

###############################################
## 2. Veriyi anlama ( Data Understanding )
################################################

import pandas as pd
import datetime as dt

from RMF.rfm import today_date

pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows" , None)
pd.set_option("display.float_format", lambda x: "%.3f" %  x)


df_ = pd.read_excel("/Users/erdinc/PycharmProjects/pythonProject4/RMF/online_retail_II.xlsx", sheet_name="Year 2009-2010")

df = df_.copy()
df.head()
df.shape
### (525461, 8) 8 değişken 524461 satır bulunur..
df.isnull().sum()

#### essiz urun sayisi nedir ?

df["Description"].nunique()

### 4681 tane eksik değer bulunmaktadır.

df["Description"].value_counts().head()

df.groupby("Description").agg({"Quantity": "sum"}).head()
 #### quantity - çıkamaz.. kesinlikle burada bir hata var...


df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()

df["Description"].nunique()

df["TotalPrice"] = df["Quantity"] * df["Price"]

df.head()

df.groupby("Invoice").agg({"TotalPrice": "sum"}).head()

##### Data preparation
df.shape

df.isnull().sum()

df.dropna(inplace=True)

df.describe().T


#### iade edilen faturaları toplamdan çıkarma
### ( bunun dışındakileri getir ifadesini yazacağız burada )) ****

df = df[~df["Invoice"].str.contains("C", na=False)]

#### seçmek isteseydik peki....
#### ~ kaldırmamız yeterli....
df[df["Invoice"].str.contains("C", na=False)]

## Bu durumda quantity'ler - geliyor böyle bir durum beklemiyoruz biz..


#### 4... Calculating RFM Metrics...

### Recency, Frequency, Monetary...

df.head()
df["InvoiceDate"].max()

today_date = dt.datetime(2010,12,11)
type(today_date)

#### pandas operasyonu....


rfm = df.groupby("Customer ID").agg({"InvoiceDate": lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                               "Invoice":lambda Invoice: Invoice.nunique(),
                               "TotalPrice": lambda TotalPrice: TotalPrice.sum()})

df.columns

### Birinci işlem.... Her bir müşterinin recency'sini bulmak için... Bugünün tarihinden son yaptığı işlem tarihinden çıkar
#### ikinci işlem Frequency bulmak için.  İnvoicelara gidiyoruz ve orada ki eşşsiz değerlere bakacağız ve bak bakalım kaç fatura var...
#### Monetary .... Total Pricelar'ın sum'ını al sadece bu kadar...

rfm.head()

rfm.columns = ["recency", "frequency", "Monetary"]

rfm.describe().T


#### Monetary  4314.000 2047.289 8912.523 0.000 307.950 705.
### burada monetary değerinde 0.000 var ve bu istenilen bir durum değil o yüzden drop kullanacağız.

rfm = rfm[rfm["Monetary"] > 0]
rfm.head()
rfm.describe().T

rfm.shape

#RFM skolarının hesaplanması ( calculating RFM Scores)

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])

#### 0- 100 , 5 parçaya böl dersek qcut ile ... 0-20, 20-40, 40-60, 60-80, 80-100

rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["Monetary_score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])


#### bu değerlerin üzerinden score değişkeni oluşturmamız gerekiyor...

###  r ve f değerlerini bir araya getirerek yazmak...


rfm["RFM_SCORE"] =(rfm["recency_score"].astype(str) +
                   rfm["frequency_score"].astype(str))

rfm.describe().T

#### özetle elimizde rfm skorları var.... Şimdi ??? bizim için şampiyon grubu neydi??

#### frequency 5 olacak recency 5 olanlardır....4000 bin müşteri için hepsi için hesaplandı...

rfm[rfm["RFM_SCORE"] == "55"]
#### bunlar bizim için değerli müşterilerdir....

rfm[rfm["RFM_SCORE"] == "11"]
### bu da sondan şampiyon müşteriler anlamı var :D


##### Creating and analysing RFM segments

##### regex...
### RFM ismlendirilmesiii...

seg_map = {
    r'[1-2][1-2]': "hibernating",
    r'[1-2][3-4]':  "at_Risk",
    r'[1-2]5' :     "can't_loose",
    r'3[1-2]' :     "about_to_sleep",
    r'33':          "Need_attention",
    r'[3-4][4-5]':  "loya_customers",
    r'41':          "promosing",
    r'51':          "new_customers",
    r'[4-5][2-3]':  "potantinal_loyalist",
    r'5[4-5]':      "champions"
}

rfm["segment"] = rfm["RFM_SCORE"].replace(seg_map, regex=True)


rfm[["segment", "recency", "frequency", "Monetary"]].groupby("segment").agg(["mean", "count"])

rfm[rfm["segment"] == "Need_attention"].head()
rfm[rfm["segment"] == "Need_attention"].index


##### ilgili departmana göndermek gerekiyor... yapılan ID'leri


new_df = pd.DataFrame()

new_df["new_customer_id"] = rfm[rfm["segment"] == "new_customers"].index

new_df["new_customer_id"] = new_df["new_customer_id"].astype((int))

new_df.to_csv("new_customers.csv")


#### Last Step.... Functionalization...








