from .models import Tarea, SubTarea

def show_task_subtask():
    tareas = Tarea.objects.prefetch_related('subtareas').all()
    return [(tarea, list(tarea.subtareas.all())) for tarea in tareas]

def new_task(descripcion, estado=False):
    tarea = Tarea.objects.create(descripcion=descripcion, estado=estado)
    return show_task_subtask()

def new_subtask(tarea_id, descripcion, estado=False):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion, estado=estado)
    return show_task_subtask()

def delete_task(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return show_task_subtask()

def delete_subtask(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return show_task_subtask()

def show_tasks(tareas_y_subtareas):
    for tarea, subtareas in tareas_y_subtareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
