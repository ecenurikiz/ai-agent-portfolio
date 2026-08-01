import os
from dotenv import load_dotenv
from smolagents import CodeAgent, tool, DuckDuckGoSearchTool, InferenceClientModel

load_dotenv()

# --- Kendi tool'larımız ---

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """İki sayı ile matematik işlemi yapar.

    Args:
        a: birinci sayı
        b: ikinci sayı
        operation: yapılacak işlem, 'add', 'subtract', 'multiply' veya 'divide' olmalı
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        raise ValueError("operation 'add', 'subtract', 'multiply' veya 'divide' olmalı")


@tool
def word_counter(text: str) -> int:
    """Bir metindeki kelime sayısını döndürür.

    Args:
        text: kelime sayısı hesaplanacak metin
    """
    return len(text.split())


# --- Model ve Agent Kurulumu ---

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=os.getenv("HF_TOKEN")
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), calculator, word_counter],
    model=model
)

# --- Test Görevi ---

result = agent.run(
    "Şu cümlede kaç kelime var: 'Yapay zeka hayatımızı değiştiriyor'? "
    "Ayrıca 24 çarpı 7 kaç eder?"
)

print("\n=== SONUÇ ===")
print(result)