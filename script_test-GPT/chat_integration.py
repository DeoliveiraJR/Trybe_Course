import openai
import openpyxl

# Configurar a chave de API do OpenAI
secret_key = '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'
openai.api_key = secret_key

# Carregar a planilha
workbook = openpyxl.load_workbook('Plano_Sobre_Objetivos_e_Metas-v2.xlsm')
sheet_name = 'Bd_Dados'  # Nome da sua planilha
sheet = workbook[sheet_name]  # Selecionar a planilha pelo nome

# Loop para interação contínua
while True:
    usuario_input = input("Digite sua pergunta ou comando (ou pressione Enter para sair): ")
    
    if not usuario_input:
        break
    
    # Enviar o input para o ChatGPT
    resposta_chat = openai.Completion.create(
        engine="davinci",  # Escolher o motor do ChatGPT
        prompt=usuario_input,  # Usar o input como prompt
        max_tokens=50  # Limitar o tamanho da resposta
    )
    
    # Processar a resposta do ChatGPT
    resposta_texto = resposta_chat.choices[0].text.strip()
    
    # Atualizar a planilha com a resposta do ChatGPT (escolha a linha que deseja atualizar)
    linha_atualizar = 2  # Altere para a linha que deseja atualizar
    sheet.cell(row=linha_atualizar, column=22, value=resposta_texto)  # Coluna V
    
    # Salvar a planilha com as atualizações
    workbook.save('sua_planilha_atualizada.xlsx')
