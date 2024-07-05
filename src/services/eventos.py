import traceback
from flask import jsonify
# Database
from src.database.connection import get_connection
# Logger
from src.utils.Logger import Logger
from src.schemas.evento import eventos_schema 

from src.models.eventos import EventoModel

class EventosService():

    @classmethod
    def get_eventos(cls):
        try:
            connection = get_connection()
            eventos = []
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM Eventos WHERE ACTIVO=1;
                ''')
                resultset = cursor.fetchall()
                for row in resultset:
                    evento = EventoModel(row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[0])
                    eventos.append(evento.serializeall())
            connection.close()
            return eventos
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def save_evento(cls, eventos_data):
        try:
            # Deserializar datos
            eventos = eventos_schema.load(eventos_data)

            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
               INSERT INTO ASSEMBLED_DB.Eventos (TIPO, OP, TITULO, DESCRIPCION, FECHA_INICIO, FECHA_FIN, EQUIPOS) 
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                ''', (eventos.tipo, eventos.op, eventos.titulo, eventos.descripcion, eventos.fecha_inicio, eventos.fecha_fin, eventos.equipos))

                if cursor.lastrowid:
                    idEvento = cursor.lastrowid
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False
       
    @classmethod
    def baja_evento(cls, id_evento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                   UPDATE `ASSEMBLED_DB`.`Eventos` SET `ACTIVO` = '0' WHERE (`ID_EVENTO` = '%s'); 
                ''', (id_evento ))
            connection.commit() 
            connection.close()
            return True
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False

    @classmethod
    def update_evento(cls, id_evento, evento_data):
        try:
            # Validar datos
            evento = eventos_schema.load(evento_data)

            connection = get_connection()
            set_clause = []
            values = []

            if evento.tipo is not None:
                set_clause.append("TIPO = %s")
                values.append(evento.tipo)
            if evento.op is not None:
                set_clause.append("OP = %s")
                values.append(evento.op)
            if evento.titulo is not None:
                set_clause.append("TITULO = %s")
                values.append(evento.titulo)
            if evento.descripcion is not None:
                set_clause.append("DESCRIPCION = %s")
                values.append(evento.descripcion)
            if evento.fecha_inicio is not None:
                set_clause.append("FECHA_INICIO = %s")
                values.append(evento.fecha_inicio)
            if evento.fecha_fin is not None:
                set_clause.append("FECHA_FIN = %s")
                values.append(evento.fecha_fin)
            if evento.equipos is not None:
                set_clause.append("EQUIPOS = %s")
                values.append(evento.equipos)

            if not set_clause:
                raise ValueError("nada para actualizar")

            set_clause_str = ", ".join(set_clause)
            values.append(id_evento)

            with connection.cursor() as cursor:
                cursor.execute(f'''
                    UPDATE ASSEMBLED_DB.Eventos
                    SET {set_clause_str}
                    WHERE ID_EVENTO = %s;
                ''', tuple(values))
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False