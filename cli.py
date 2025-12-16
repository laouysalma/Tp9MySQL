import click
from db import get_conn

@click.group()
def cli():
    pass

@cli.command()
@click.argument("titre")
def add_course(titre):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO COURS (titre, credits) VALUES (%s, %s)", (titre, 3))
    conn.commit()
    click.echo(f"Cours '{titre}' ajouté.")
    conn.close()

@cli.command()
def list_courses():
    """Liste tous les cours"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM COURS")
    rows = cur.fetchall()
    for row in rows:
        click.echo(f"{row[0]} - {row[1]} ({row[2]} crédits)")
    conn.close()

if __name__ == "__main__":
    cli()
