from marshmallow import Schema, fields, post_load
from enum import Enum

class TipoEvento(Enum):
    S = 'S'
    E = 'E'
    F = 'F'
    M = 'M'
    H = 'H'
    RM = 'RM'

class EventoSchema(Schema):
    tipo = fields.Str(validate=lambda t: t in [e.value for e in TipoEvento], required=True)
    op = fields.Int(required=False,  allow_none=True)
    titulo = fields.Str(required=True)
    descripcion = fields.Str(required=False,  allow_none=True)
    fecha_inicio = fields.Str(required=False , allow_none=True)
    fecha_fin = fields.Str(required=False,  allow_none=True)
    equipos = fields.Str(required=False, allow_none=True)
    id = fields.Int(required=False, allow_none=True)

    @post_load
    def make_evento(self, data, **kwargs):
        from src.models.eventos import EventoModel  # Asegúrate de importar correctamente tu modelo de evento
        return EventoModel(**data)

# Ejemplo de uso
eventos_schema = EventoSchema()
eventos_schema_many = EventoSchema(many=True)