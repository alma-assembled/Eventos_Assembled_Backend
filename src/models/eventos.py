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
            'id':self.id,
            'tipo': self.tipo,
            'op': self.op,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'equipos': self.equipos
        }