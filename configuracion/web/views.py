from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formularioPacientes import FormularioPacientes
from web.models import Medicos
from web.models import Pacientes

# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def clientesVista(request):

    formulario=FormularioPacientes()
    diccionario={
        "formulario":formulario
    }

    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioPacientes(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #Llevar mis datos hacia la BD
            pacienteNuevo=Pacientes(
                nombre=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"]
            )
            pacienteNuevo.save()
            print("exito en la operacion")
    return render(request,'registroclientes.html',diccionario)






    return render(request,'registroclientes.html',diccionario)

def MedicosVista(request):

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #Llevar mis datos hacia la BD
            medicoNuevo=Medicos(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"]
            )
            medicoNuevo.save()
            print("exito en la operacion")
    return render(request,'registromedicos.html',diccionario)

