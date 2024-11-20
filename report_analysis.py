# report_generator.py

import os

def generate_summary(emotion_counts, total_frames, output_path):
    # Exibir Relatório no Console
    print("RELATÓRIO:")

    # Exibir o total de frames analisados
    print(f"\nTotal de frames analisados: {total_frames}")

    # Exibir o resumo das emoções detectadas
    print("\nResumo das emoções detectadas:")
    for emotion, count in emotion_counts.items():
        print(f"{emotion}: {count} ocorrências")

    # Exibir o número de anomalias detectadas (categorias 'Unknown')
    anomalies = emotion_counts.get("Unknown", 0)
    print(f"\nNúmero de anomalias detectadas: {anomalies}")

    # Criar o arquivo de relatório
    report_path = os.path.join(os.path.dirname(output_path), 'relatorio_analise.txt')
    
    with open(report_path, 'w') as report_file:
        # Escrever o total de frames analisados
        report_file.write(f"Total de frames analisados: {total_frames}\n")
        
        # Escrever o resumo das emoções detectadas
        report_file.write("\nResumo das emoções detectadas:\n")
        for emotion, count in emotion_counts.items():
            report_file.write(f"{emotion}: {count} ocorrências)\n")
        
        # Escrever o número de anomalias detectadas
        report_file.write(f"\nNúmero de anomalias detectadas: {anomalies}\n")

    print(f"\nRelatório salvo em: {report_path}")