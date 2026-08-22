# 🌐 Traductor Simple en Python

Un script de consola interactivo y minimalista desarrollado en Python que traduce texto del **Español al Inglés** en tiempo real utilizando la librería externa `translate`.

## 🚀 Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado Python en tu sistema y la librería necesaria.

Instala la dependencia ejecutando el siguiente comando en tu terminal:

```bash
pip install translate
```

## 🛠️ Ejecución y Uso

1. Descarga o copia el archivo del script (por ejemplo, `traductor.py`).
2. Abre tu terminal y navega hasta la carpeta donde guardaste el archivo.
3. Ejecuta el programa con el comando:

```bash
python traductor.py
```

4. El sistema te solicitará el texto en consola:
   ```text
   Que deseas traducir? Hola mundo, este es mi script de Python.
   ```
5. El programa devolverá la traducción automática de inmediato:
   ```text
   Hello world, this is my Python script.
   ```

## 📝 El Código

```python
from translate import Translator

# Configuración del traductor: Idioma origen -> Idioma destino
translator = Translator(from_lang='spanish', to_lang='english')

# Captura de datos del usuario
txt = input('Que deseas traducir? ')

# Proceso de traducción
res = translator.translate(txt)

# Salida del resultado en consola
print(res)
```

> *Nota de desarrollo:* Se corrigió el nombre de la variable `Translator` en minúscula (`translator`) para seguir las buenas prácticas de nombrado en Python (**PEP 8**), evitando confundir la instancia con la clase original.
