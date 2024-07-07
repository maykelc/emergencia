from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, AlertaForm
from .models import Usuario, Alerta,ubicacion
import requests
from django.http import JsonResponse

# Create your views here.


def base(request):
    return render(request, 'base.html')


def inicio(request):
    return render(request, 'inicio.html')


def login_view(request):
    if request.method == 'POST':
        # Si se está enviando el formulario (POST request)

        # Crear una instancia del formulario LoginForm con los datos recibidos
        form = LoginForm(request.POST)

        if form.is_valid():  # Verificar si el formulario es válido
            # Obtener el correo electrónico limpio
            correo = form.cleaned_data['correo']
            # Obtener la contraseña limpias
            contrasena = form.cleaned_data['contrasena']

            # Autenticar al usuario
            user = authenticate(request, email=correo, password=contrasena)

            if user is not None:  # Si el usuario es autenticado correctamente
                # Iniciar sesión para el usuario en Django
                login(request, user)

                # Redirigir a la página de inicio después de iniciar sesión
                # Reemplaza 'inicio' con la ruta a la que quieres redirigir después del login
                return redirect('inicio')
            else:
                # Si las credenciales no son válidas, mostrar un mensaje de error
                error_login = "Credenciales incorrectas. Inténtelo de nuevo."
                return render(request, 'login.html', {'form': form, 'error_login': error_login})

    else:
        # Si es una solicitud GET (primera carga de la página o falla de validación)
        form = LoginForm()  # Crear una instancia vacía del formulario LoginForm

    # Renderizar la página de inicio de sesión con el formulario
    return render(request, 'login.html', {'form': form})


def newalert(request, pk=None):
    modificar_alerta = False
    alerta = None

    if pk:
        alerta = get_object_or_404(Alerta, pk=pk)
        modificar_alerta = True

    if request.method == 'POST':
        if modificar_alerta:
            form = AlertaForm(request.POST, instance=alerta)
        else:
            form = AlertaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('newalert')
    else:
        if modificar_alerta:
            form = AlertaForm(instance=alerta)
        else:
            form = AlertaForm()

    alertas = Alerta.objects.all()

    context = {
        'form': form,
        'alertas': alertas,
        'modificar_alerta': modificar_alerta,
    }
    return render(request, 'newalert.html', context)


def eliminar_alerta(request, pk):
    alerta = get_object_or_404(Alerta, pk=pk)

    if request.method == 'POST':
        alerta.delete()
        return redirect('newalert')

    context = {
        'alerta': alerta,
    }
    return render(request, 'newalert.html', context)


def contacto(request):
    return render(request, 'contacto.html')


def servicioalerta(request):
    return render(request, 'servicios.html')


def quienessomos(request):
    return render(request, 'quienesomos.html')


def nosotros(request):
    return render(request, 'sobremi.html')



# APIS DE SISMOS 

def sismos(request):
    api_sismos = 'https://api.gael.cloud/general/public/sismos'
    try:
        response = requests.get(api_sismos)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = []
        print(f"error al recuperar datos desde la api: {e}")
    return render(request, 'sismos.html', {'sismos': data})



# APIS DE CLIMA

# OBTENER KEY DE LA CIUDAD
def get_city_key(city):
    api_key = '5YhZPwbIOaXEDSuBJjSbpG5q7yZtWnhY'
    api_clima = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    query = f'?apikey={api_key}&q={city}'
    response = requests.get(api_clima + query)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['Key']
        else:
            return None
    else:
        return None

# OBTENER CONDICIONES CLIMATTICAS ACTUALES
def get_climate(id):
    api_key = '5YhZPwbIOaXEDSuBJjSbpG5q7yZtWnhY'
    obt_ubi_clima = 'http://dataservice.accuweather.com/currentconditions/v1/'
    query = f'{id}?apikey={api_key}'
    response = requests.get(obt_ubi_clima + query)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]
        else:
            return None
    else:
        return None


# MOSTRAR CONDICIONES ACTUALES EN EL CLIMA.HTML
def clima(request):
    city = 'Santiago'  # Puedes obtener esta ciudad de una solicitud GET o POST en tu vista
    city_key = get_city_key(city)
    if city_key:
        clima_actual = get_climate(city_key)
        return render(request, 'clima.html', {'clima_actual': clima_actual})
    else:
        return render(request, 'clima.html', {'error': 'No se pudo obtener la clave de ubicación.'})

# OBTENER KEY POR  GEOLOCALIZACION CON JAVASCRIPT, USANDO MODELS.PY, FORMS.PY , URL

def geoclima(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if latitude and longitude:
            ubicacion.objects.create(latitude=latitude, longitude= longitude)
            apikey= '5YhZPwbIOaXEDSuBJjSbpG5q7yZtWnhY'
            api_url= 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
            query= {'apikey': apikey, 'q': f'{latitude},{longitude}'}
            response = requests.get(api_url, params = query)
            if response.status_code == 200:
                data= response.json()
                location_key = data.get('key')
                return JsonResponse({'status': 'succes', 'location_key': location_key})
            else:
                return JsonResponse({'status': 'error', 'message': 'No se pudo obtener la clave desde AccuWeather'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid coordinates'})
    return render(request, 'clima.html')




def noticias(request):
    return render(request, 'noticias.html')


def emergencias(request):
    return render(request, 'emergencias.html')
