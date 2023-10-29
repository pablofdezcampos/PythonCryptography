from PIL import Image

def ocultar_mensaje(imagen_path, mensaje, imagen_de_salida_path):
    imagen = Image.open(imagen_path)
    
    #Convierte cada carácter del mensaje en su representación binaria de 8 bits
    mensaje_binario = ''.join(format(ord(caracter), '08b') for caracter in mensaje)
    
    #Construye el mensaje oculto concatenando el mensaje binario con delimitadores '1111111111111110'.
    #Estos delimitadores se utilizan para indicar el inicio y el final del mensaje oculto en la imagen.
    mensaje_oculto = '1111111111111110' + mensaje_binario + '1111111111111110'
    
    #Comprueba si el mensaje es demasiado largo para ser ocultado en la imagen.
    #Cada píxel tiene tres canales(RGB), por lo tanto, se multiplica la longitud de la lista de píxeles por 3.
    if len(mensaje_oculto) > imagen.width * imagen.height * 3:
        raise ValueError("El mensaje es demasiado largo para ser ocultado en la imagen.")
    
    imagen_encriptada_pixeles = []
    mensaje_index = 0
    
    for pixel in imagen.getdata():
        
        #Comprueba si todavía hay bits del mensaje oculto para ocultar en la imagen.
        if mensaje_index < len(mensaje_oculto):
            
            #Convierte el píxel en una lista para poder modificar sus valores RGB.
            pixel_modificado = list(pixel)
            
            for i in range(0, 3):
                
                if mensaje_index < len(mensaje_oculto):
                    
                    #Esta operación & (AND a nivel de bits) con 254 asegura que el último bit del canal de color se establezca en 0. 
                    #En binario, 254 se representa como 11111110. Al hacer un AND con 254, todos los bits del número original se mantienen igual, excepto el último, que se convierte en 0.
                    pixel_modificado[i] = pixel[i] & 254 | int(mensaje_oculto[mensaje_index])
                    mensaje_index += 1
                    
             #Convierte la lista de píxeles nuevamente en una tupla y la agrega a la lista        
            imagen_encriptada_pixeles.append(tuple(pixel_modificado))
        else:
            imagen_encriptada_pixeles.append(pixel)
    
    imagen_encriptada = Image.new(imagen.mode, imagen.size)
    
    #Establece los píxeles de la nueva imagen
    imagen_encriptada.putdata(imagen_encriptada_pixeles)
    
    imagen_encriptada.save(imagen_de_salida_path)
    
    print("Mensaje oculto correctamente en la imagen.")

def extraer_mensaje(imagen_path):
    imagen = Image.open(imagen_path)
    mensaje_oculto = ''
    
    for pixel in imagen.getdata():
        for bit in pixel:
            #Para cada componente de color (R,G,B) del píxel, se aplica la operación bit & 1, que realiza una AND bit a bit con 1. 
            #Esto básicamente retiene solo el último bit de cada componente de color. 
            #El mensaje se oculta en los bits menos significativos, esta operación extrae los bits del mensaje de los píxeles de la imagen.
            mensaje_oculto += str(bit & 1)
    
    delimitador = '1111111111111110'
    mensaje_binario = mensaje_oculto.split(delimitador)[1]
    
    #El código int(mensaje_binario[i:i+8], 2) convierte cada conjunto de 8 bits en un número entero, y chr(...) convierte ese número entero en un carácter ASCII. 
    # Estos caracteres se combinan para formar el mensaje original.
    mensaje = ''.join(chr(int(mensaje_binario[i:i+8], 2)) for i in range(0, len(mensaje_binario), 8))
    
    return mensaje

#Main - Ejemplo de uso
imagen_original_path = './img/image.jpeg'
mensaje_a_ocultar = 'Hola, este es un mensaje oculto en una imagen.'
imagen_con_mensaje_path = './img/imagen_con_mensaje.png'

ocultar_mensaje(imagen_original_path, mensaje_a_ocultar, imagen_con_mensaje_path)

mensaje_extraido = extraer_mensaje(imagen_con_mensaje_path)
print("Mensaje extraído de la imagen:", mensaje_extraido)
