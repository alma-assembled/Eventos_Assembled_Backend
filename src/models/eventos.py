from datetime import datetime

class EventoModel:
    def __init__(self, tipo=None, op=None, titulo=None, descripcion=None, fecha_inicio=None, fecha_fin=None,equipos= None, id=None):
        self.id = id
        self.tipo = tipo
        self.op = op
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.equipos  = equipos

    def serialize(self):
        from src.schemas.evento import eventos_schema  
        return eventos_schema.dump(self)
    
    def serializeall(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'op': self.op,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'fecha_inicio': self.format_date(self.fecha_inicio),
            'fecha_fin': self.format_date(self.fecha_fin),
            'equipos': self.equipos
        }
    
    def format_date(self, date_obj):
        # Verifica si es un objeto datetime y formatea directamente
        if isinstance(date_obj, datetime):
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")
        # Si es una cadena, intenta convertirla usando strptime
        try:
            return datetime.strptime(date_obj, "%a, %d %b %Y %H:%M:%S GMT").strftime("%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            # Devuelve la fecha sin modificar si no es una cadena válida o None
            return date_obj