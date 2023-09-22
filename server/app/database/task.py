from server.app.database import get_db

def output_formatted(results):
    out = []

    for result in results:
        task = {
            "id" : result[0],
            "summary" : result[1],
            "description" : result[2],
            "is_active" : result[3]
        }
        out.append(task)

    return out

def scan():
    conn = get_db()

    cursor = conn.execute(
        "SELECT * FROM task", ()
    )

    results = cursor.fetchall()
    cursor.close()
    return output_formatted(results)

def select_by_id(task_id):
    conn = get_db()

    cursor = conn.execute(
        "SELECT * FROM task where id=?", (task_id,)
    )

    results = cursor.fetchall()
    cursor.close()

    if results:
        return output_formatted(results)[0]
    
    return {}

def insert(task_data):
    value_tuple = (
        task_data.get("summary"),
        task_data.get("description"),
    )

    statement = """
        INSERT INTO task (
            summary,
            description
        ) VALUES (
            ?, ?
        )
    """

    conn = get_db()
    conn.execute(statement, value_tuple)
    conn.commit()

def update(task_data, task_id):
    value_tuple = (
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_active"),
        task_id
    )

    statement = """
        UPDATE task SET
            summary=?,
            description=?,
            is_active=?
        WHERE id = ?
    """

    conn = get_db()
    conn.execute(statement, value_tuple)
    conn.commit()

def delete(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (task_id,))
    conn.commit()