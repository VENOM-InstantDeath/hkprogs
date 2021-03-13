categs = ["Say", "Chat", "Info", "Utils", "Bot", "Entertainment"]

commands = {
        "/hi": ["Devuelve un saludo.", "Say", """Devuelve un saludo, no recibe ningún argumento."""],

        "/help": ["Muestra este mensaje.", "Say", """Brinda ayuda acerca de un comando o sección.

Sintaxis:
[i]\t\t/help
[i]\t\t/help <sección>
[i]\t\t/help <comando>"""],

        "/version": ["Muestra la versión del bot.", "Say", """Muestra la versión del bot, no recibe ningún argumento."""],

        "/di": ["Repite lo que se le pide.", "Say", """Repite lo que se pasa como argumento.
Sintaxis:
[i]\t\t/di <texto a repetir>"""],

        "/meme": ["Muestra una plantilla, si no se especifican argumentos muestra un meme aleatorio.", "Entertainment", """Muestra un meme aleatorio. Si se especifica una plantilla, el bot la buscará entre las que tiene disponibles.
Sintaxis:
[i]\t\t/meme
[i]\t\t/meme <plantilla>"""],

        "/public_chats": ["Muestra los chats publicos.", "Info", """Muestra los chats públicos de la comunidad, no recibe ningún argumento."""],

        "/info": ["Revela información de un usuario.", "Info", """Muestra información sobre un usuario.
Sintaxis:
[i]\t\t/info <nickname>"""],

        "/goto": ["Envía el bot a otro chat.", "Bot", """Envía el bot a otro chat.
Sintaxis:
[i]\t\t/goto <numero de chat>

Puede buscar los numeros de identificación de los chats usando /public_chats."""],

        "/mv": ["Envía el bot a otra comunidad.", "Bot", """Envía el bot a otra comunidad.
Sintaxis:
[i]\t\t/mv <ID de la comunidad>"""],

        "/guard": ["Repite los mensajes borrados.", "Chat", """Repite los mensajes borrados.
Sintaxis:
[i]\t\t/guard <on | off>"""],

        "/id": ["Revela la Id del chat y de la comunidad.", "Chat", """Revela la ID del chat y la comunidad, no recibe ningún argumento."""],

        "/eval": ["Evalúa una expresión matemática.", "Utils", """Evalúa una expresión matemática.
Sintaxis:
[i]\t\t/eval <expresión>"""],

        "/teach": ["Enseña un comando y su respuesta al bot.", "Entertainment", """Enseña un comando y su respuesta al bot.
Sintaxis:
[i]\t\t/teach <comando> = <respuesta> [opciones]

Los comandos se deben separar de la respuesta usando el símbolo '=', ejemplo de esto sería:

[i]/teach "hello world in python" = "print('hello world')"

Para ejecutar un comando personalizado, se lo escribe tal cual precediéndolo con un '.'"""],

        "/trad": ["Traduce una oración a X idioma.", "Utils", "Traduce una oración a X idioma."],
        "/langdet": ["Detecta el idioma de una oración.", "Utils", "Detecta el idioma de una oración."],
        "/def": ["Busca la definición de un término.", "Utils", """Busca la definición de un término."""],
        "/stop": ["Termina el proceso.", "Bot", "Detiene el bot, no recibe ningún argumento."]
    }
