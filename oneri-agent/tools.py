import os #dosya yolu işlemleri için
from smolagents import Tool #smolagents kütüphanesinden kendi Tool'umuz için
import json # json dosyasını python nesnesine (list/dict) çevirmek için


# __file__, bu tools.y dosyasının kendi konumu
# os.path.dirname(__file__) (oneri-agent/) dizinini verir
# buna "data/library.json" eklenerek agent nereden çalışırsa çalışsın her zaman doğru dosyayı bulan bir yol oluşturulur
LIBRARY_PATH = os.path.join(os.path.dirname(__file__),"data","library.json")



class OneriRetrieverTool(Tool):

    name= "oneri_retriever"  #LLM'in bu Tool'u çağırırken kullanacağı isim
    description= "Kullanıcın kitap/film kütüphanesinde arama yapar."  #LLM'e bu Toolun ne işe yaradığını anlatır
    inputs={ #toolun aldığı parametreleri ve tiplerini tanımlar

       "query":{"type":"string","description":"Aranacak konu veya tür"}
    }
    output_type="string"

    def __init__(self,path=LIBRARY_PATH,**kwargs):
        super().__init__(**kwargs)

        with open(path,"r",encoding="utf-8") as f:
          self.library=json.load(f)  # json içeriğini python listesine çevirip nesneye(self) kaydeder, böylece forward her çağrıldığında dosya tekrar okunmaz


    #asıl arama mantığı
    def forward(self, query: str) -> str:
       words = query.lower().split()  #LLMden gelen query'i küçük harfe çevirip boşluklardan böler


       #sonuçları biriktirecek boş liste
       #kütüphanedeki her kayıt gözden geçiriliyor
       scored = []
       for item in self.library:
          baslik= item.get("baslik","")
          tur=item.get("tur","")
          aciklama=item.get("aciklama","")
          puan=item.get("puan","")
          text =f"{baslik} {tur} {aciklama} {puan}".lower()

          score =sum(1 for w in words if w in text)
          if score ==len(words):
             scored.append((score,item))

       scored.sort(key=lambda x: x[0],reverse=True)
       top= [item for _, item in scored[:5]]
 
       if not top:
          return "Aramanizla eşleşen kayıt bulunmadı."

       lines=[
          f"{i+1}.{item.get('baslik','?')}({item.get('tur','?')})-{item.get('aciklama','')}"
          for i,item in enumerate(top)
       ]
       return "\n".join(lines)
      