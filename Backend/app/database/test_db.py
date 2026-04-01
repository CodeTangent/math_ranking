from connect import get_connection

def get_ranking():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT 
            u.nick,
            u.curso,
            r.pontuacao
        FROM ranking r
        JOIN usuarios u ON u.usr_id = r.usr_id
        ORDER BY r.pontuacao DESC;
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        cursor.close()
        connection.close()

        return resultados

    except Exception as e:
        print("Erro", e)
        return []


if __name__ == "__main__":
    ranking = get_ranking()

    for posicao, user in enumerate(ranking):
        nick, curso, pontos = user
        print(f"{posicao} Nome: {nick} | Curso: {curso} | Pontos: {pontos}")