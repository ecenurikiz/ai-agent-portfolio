import os
from dotenv import load_dotenv
from smolagents import CodeAgent, tool,DuckDuckGoSearchTool, InferenceClientModel, UserInputTool
import json
from tools import LIBRARY_PATH

load_dotenv()

model= InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=os.getenv("HF_TOKEN")
)

@tool
def get_library()-> str:
     """Kullanıcının kütüphanesindeki tüm kayıtları listeler.
     
     """
     with open(LIBRARY_PATH,"r",encoding="utf-8") as f:
       library=json.load(f)

     lines=[
              f"{i+1}.{item.get('baslik','?')}({item.get('tur','?')})-{item.get('aciklama','')}"
              for i,item in enumerate(library)
           ]
     return "\n".join(lines)
     



@tool
def add_item(baslik:str,tur:str,aciklama:str,puan:str)->str:
    """
    Kütüphaneye yeni bir kitap/film kaydı ekler.

    Args:
     baslik: Eklenecek kitap/film adı.
     tur:Eklenecek kaydın türü.
     aciklama:Kaydı tanımlayan kısa açıklama.
     puan:Kayda verilen puan.
    
    """
    with open(LIBRARY_PATH,"r",encoding="utf-8") as f:
        library=json.load(f)

    yeni_kayıt={
        "baslik":baslik,
        "tur":tur,
        "aciklama":aciklama,
        "puan":puan
    }

    library.append(yeni_kayıt)

    with open(LIBRARY_PATH,"w",encoding="utf-8") as f:
        json.dump(library,f,ensure_ascii=False,indent=4)
    return f"'{baslik}' kütüphaneye eklendi."
    
agent= CodeAgent(
    tools=[get_library,add_item,DuckDuckGoSearchTool(),UserInputTool()],
    model=model
)

question=input("Ne önermemi istersin?:")
result=agent.run(question)

