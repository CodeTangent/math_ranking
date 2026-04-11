from app.database.connect import get_connection


def get_ranking():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT 
                u.nick,
                u.curso,
                r.pontuacao,
                ROW_NUMBER() OVER (
                    ORDER BY r.pontuacao DESC, r.ultima_atualizacao ASC
                ) AS posicao
            FROM ranking r
            JOIN usuarios u ON u.usr_id = r.usr_id;
        """

        cursor.execute(query)

        ranking = []

        if resultados := cursor.fetchall():
            for i in resultados:
                ranking.append(
                    {"nick": i[0], "curso": i[1], "pontos": i[2], "posicao": i[3]}
                )
        return ranking

    except Exception as e:
        return {"Error": str(e)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#ajuda a debugar o codigo aparecendo tudo no terminal
if __name__ == "__main__":
    resultado = get_ranking()
    print(resultado)