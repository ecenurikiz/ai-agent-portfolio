import os
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, tool

load_dotenv()

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=os.getenv("HF_TOKEN")
)

# --- Uzman Agent 1: Sadece web arama yapar ---
web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    name="web_agent",
    description="İnternette arama yaparak güncel bilgi bulur.",
    max_steps=5,
)

# --- Manager'ın kendi tool'u ---
@tool
def calculator(a: float, b: float, operation: str) -> float:
    """İki sayı ile matematik işlemi yapar.

    Args:
        a: birinci sayı
        b: ikinci sayı
        operation: 'add', 'subtract', 'multiply' veya 'divide'
    """
    ops = {"add": a+b, "subtract": a-b, "multiply": a*b, "divide": a/b}
    return ops[operation]

# --- Manager Agent: web_agent'ı yönetir ---
manager_agent = CodeAgent(
    tools=[calculator],
    model=model,
    managed_agents=[web_agent],
)

result = manager_agent.run(
    "Türkiye'nin güncel nüfusunu bul, sonra bu sayıyı 2'ye böl."
)
print(result)