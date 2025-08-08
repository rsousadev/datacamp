client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """
Crie a descrição de um produto chamado SonicPro que é um fone de ouvido com
cancelamento de ruído ativo chamado (ANC), batria que dura até 40 horas e
tem um design elegante e drobável
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Responda sempre em português do Brasil."},
        {"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=30,
    temperature=0
)

print(response.choices[0].message.content)