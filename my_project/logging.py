import logging

# Crear un logger
logger = logging.getLogger(__name__)

# Definir un handler para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Crear un formatter para los logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Agregar el handler al logger
logger.addHandler(console_handler)

# Otras configuraciones pueden ir aquí, como el logging en archivos si se necesita

