class IRecordatorio: #interfaz
    def update(self): 
        pass

class Tareas(IRecordatorio):
    def __init__(self,id,titulo,descripcion,fecha_ven=None):
        self.id=id
        self.titulo=titulo
        self.descripcion=descripcion
        self.fecha_ven=fecha_ven
    
    def update(self):
        print(f"¡Tiene esta tarea próxima a vencer: {self.titulo}, no lo olvide!")

class GestorTareas:
    def __init__(self):
        self._tareas=[]
        self._completada=[]

    def agregar_tarea(self,id,titulo,descripcion,fecha=None):
        tarea=Tareas(id,titulo,descripcion,fecha)
        self._tareas.append(tarea)
    
    # def estado_tarea(self,estado):
    #     self.estado=estado

    def completadas(self):
        num_tarea=int(input('Digite el número de tarea que acaba de completar: '))
        tarea=self._tareas[num_tarea-1]
        self._tareas.remove(tarea)
        self._completada.append(tarea)
        for i in self._completada:
            print(f"Tarea completada: {i.id}-{i.titulo}")

    def pendientes(self):
        for tarea in self._tareas:
            print(f"Tiene pendiente: {tarea.id}-{tarea.titulo}")

    def notificar(self):
        for tarea in self._tareas:
            tarea.update()
    
if __name__ == '__main__':
    gestor=GestorTareas()
  
    gestor.agregar_tarea(1,"Tarea 1","lavar loza")
    gestor.agregar_tarea(2,"Tarea 2","proyecto")
    gestor.completadas()
    gestor.pendientes() 
    gestor.notificar()   
    
    
    
